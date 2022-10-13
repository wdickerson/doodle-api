from index import lambda_handler


# my_event = {
#     "Records": [
#         {
#             "s3": {
#                 "bucket": {
#                     "name": "cfy-wad-csgy-9223-photobot-store",
#                 },
#                 "object": {
#                     "key": "b1849bac-fdbb-4c6b-af1b-1b808226b365",
#                 }
#             }
#         }
#     ]
# }

my_event = {
    'httpMethod': 'GET',
    'pathParameters': {
        'doodle_id': 'taco0',
    },
}


print('Should get a doodle')
print(lambda_handler(my_event, {}))

my_event = {
    'httpMethod': 'GET',
    'pathParameters': {
        'doodle_id': None,
    },
}

print('Should return error with no doodle_id')
print(lambda_handler(my_event, {}))

my_event = {
    'httpMethod': 'GET',
    'pathParameters': {
        'doodle_id': 'nonexistent_id',
    },
}

print('Should return error with nonexistent doodle_id')
print(lambda_handler(my_event, {}))
