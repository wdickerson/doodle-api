import json, boto3, os
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return int(obj)
    return json.JSONEncoder.default(self, obj)


dynamodb = boto3.resource('dynamodb')


def get_doodle(doodle_id: str):
    DYNAMO_TABLE = os.environ['DYNAMO_TABLE']
    table = dynamodb.Table(DYNAMO_TABLE)

    response = table.get_item(
        Key={
            'doodle_id': doodle_id,
        }
    )
    item = response['Item']

    # Return the formatted doodle
    return {
        'statusCode': 200,
        "headers": { "Access-Control-Allow-Origin": '*' },
        'body': json.dumps({
            'doodle_id': doodle_id,
            'doodles': item['doodles'],
        }, cls=DecimalEncoder),
    }
