import json, boto3, os, uuid
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return int(obj)
    return json.JSONEncoder.default(self, obj)


def post_existing_doodle(doodle_id: str, doodle: list):
    DYNAMO_TABLE = os.environ['DYNAMO_TABLE']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DYNAMO_TABLE)

    result = table.update_item(
        Key={
            'doodle_id': doodle_id,
        },
        UpdateExpression="SET doodles = list_append(doodles, :i)",
        ExpressionAttributeValues={
            ':i': [doodle],
        },
        ReturnValues="UPDATED_NEW"
    )

    updated_doodles = result['Attributes']['doodles']

    # Return the formatted doodle
    return {
        'statusCode': 200,
        "headers": { "Access-Control-Allow-Origin": '*' },
        'body': json.dumps({
            'doodle_id': doodle_id,
            'doodles': updated_doodles,
        }, cls=DecimalEncoder),
    }


def post_new_doodle(doodle: list):
    DYNAMO_TABLE = os.environ['DYNAMO_TABLE']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DYNAMO_TABLE)

    new_id = str(uuid.uuid4())

    table.put_item(
        Item={
            'doodle_id': new_id,
            'doodles': [doodle],
            # 'doodles': [
            #     [
            #         [0, 0, 50, 50],
            #         [10, 10, 50, 50],
            #     ],
            #     [
            #         [10, 10, 150, 150],
            #         [110, 110, 150, 150],
            #     ],
            # ],
        }
    )


    # Return the formatted doodle
    return {
        'statusCode': 200,
        "headers": { "Access-Control-Allow-Origin": '*' },
        'body': json.dumps({
            'doodle_id': new_id,
            'doodles': [doodle]
        }),
    }
