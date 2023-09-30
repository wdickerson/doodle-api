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
                    'message': 'Must provide doodle ID',
                }),
            }

        return get_doodle(doodle_id)

    elif method == 'POST' and doodle_id is not None:
        if not doodle:
            return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'Must include a doodle',
                }),
            }

        error_response = validate_doodle(doodle)
        if error_response:
            return error_response

        return post_existing_doodle(doodle_id, doodle)

    elif method == 'POST':
        if not doodle:
            return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'Must include a doodle',
                }),
            }

        error_response = validate_doodle(doodle)
        if error_response:
            return error_response

        return post_new_doodle(doodle)


def validate_doodle(doodle):
    if not isinstance(doodle, list):
       return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'body must be a list',
                }),
            }

    if len(doodle) > 750:
       return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'That doodle is too big!',
                }),
            }

    for stroke in doodle:
        if not isinstance(stroke, list):
            return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'every item in the body should be a list',
                }),
            }

        if len(stroke) != 5:
            return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'every item in the body should have 5 elements',
                }),
            }

        if (
            not isinstance(stroke[0], int)
            or not isinstance(stroke[1], int)
            or not isinstance(stroke[2], int)
            or not isinstance(stroke[3], int)
        ):
            return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'first four items of each stroke should be an int',
                }),
            }

        if (
            stroke[0] < 0
            or stroke[1] < 0
            or stroke[2] < 0
            or stroke[3] < 0
        ):
            return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'first four items of each stroke should be non-negative',
                }),
            }

        if (
            stroke[0] > 2000
            or stroke[1] > 2000
            or stroke[2] > 2000
            or stroke[3] > 2000
        ):
            return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'first four items of each stroke should be non-negative',
                }),
            }

        if not isinstance(stroke[4], str):
            return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'fifth item of each stroke should be a string',
                }),
            }

        if len(stroke[4]) != 7:
            return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'fifth item should be a six digit hex color code',
                }),
            }

        if stroke[4][0] != '#':
            return {
                'statusCode': 400,
                "headers": { "Access-Control-Allow-Origin": '*' },
                'body': json.dumps({
                    'message': 'fifth item should be a hex color code starting with #',
                }),
            }

    return None
