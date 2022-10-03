from index import lambda_handler


my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': 'taco1',
    },
}


# print('HERE!!! my_event')
# print(my_event)

test_response = lambda_handler(my_event, {})

print('HERE!!! test response')
print(test_response)


