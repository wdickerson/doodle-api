# CODE WILL INITIALIZE VIA CODEPIPELINE

import json, boto3
from get_doodle import get_doodle
from post_doodle import post_existing_doodle, post_new_doodle
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return int(obj)
    return json.JSONEncoder.default(self, obj)


dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    # print('HERE!!! event')
    # print(json.dumps(event))

    method = event.get('httpMethod') or {}
    doodle_raw = event.get('body', None)
    doodle = json.loads(doodle_raw) if doodle_raw else None

    path_params = event.get('pathParameters') or {}
    doodle_id = path_params.get('doodle_id', None)

    if method == 'GET':
        if not doodle_id:
          return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'Must provide doodle_id',
                }, cls=DecimalEncoder),
          }

        return get_doodle(doodle_id)

    elif method == 'POST' and doodle_id is not None:
        return post_existing_doodle(doodle_id, doodle)

    elif method == 'POST':
        return post_new_doodle(doodle)
