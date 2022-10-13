from index import lambda_handler
import json


my_event = {
    'httpMethod': 'POST',
    'pathParameters': None,
}

new_doodle = lambda_handler(my_event, {})

print('HERE!!! should require a body for a new doodle')
print(new_doodle)


my_event = {
    'httpMethod': 'POST',
    'pathParameters': None,
    'body': json.dumps([
        [0, 0, 5, 5, '#000000'],
        [0, 0, 15, 15, '#000000'],
        [0, 0, 25, 25, '#000000'],
    ])
}

new_doodle = lambda_handler(my_event, {})

print('HERE!!! should post new doodle')
print(new_doodle)
new_doodle_id = json.loads(new_doodle['body'])['doodle_id']


my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    }
}

print('HERE!!! should require a body for an existing doodle')
print(lambda_handler(my_event, {}))


my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        [0, 0, 5, 5, '#000000'],
        [0, 0, 15, 15, '#000000'],
        [0, 0, 25, 25, '#000000']
    ])
}

print('HERE!!! should post to existing doodle')
print(lambda_handler(my_event, {}))



my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps('taco')
}

print('HERE!!! should require body to be a list')
print(lambda_handler(my_event, {}))


big_body = []
for i in range(1002):
    big_body.append([0, 0, 15, 15, '#000000'])

my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps(big_body)
}

print('HERE!!! should require the doodle to have 1000 or fewer strokes')
print(lambda_handler(my_event, {}))


my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        'apple',
        [0, 0, 15, 15, '#000000'],
        [0, 0, 25, 25, '#000000']
    ])
}

print('HERE!!! should require every item of body to be a list')
print(lambda_handler(my_event, {}))


my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        [0, 0, 15, 15],
        [0, 0, 15, 15, '#000000'],
        [0, 0, 25, 25, '#000000']
    ])
}

print('HERE!!! should require every item of body to have 5 items')
print(lambda_handler(my_event, {}))


my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        ['apple', 0, 15, 15, '#000000'],
        [0, 0, 15, 15, '#000000'],
        [0, 0, 25, 25, '#000000']
    ])
}

print('HERE!!! should require first four elements of strokes to be ints')
print(lambda_handler(my_event, {}))



my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        [0, 0, 15, 15, '#000000'],
        [0, 0, 15, 15, '#000000'],
        [0, 0, 'apple', 25, '#000000']
    ])
}

print('HERE!!! should require first four elements of strokes to be ints')
print(lambda_handler(my_event, {}))


my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        [-5, 0, 15, 15, '#000000'],
        [0, 0, 15, 15, '#000000'],
        [0, 0, 25, 25, '#000000']
    ])
}

print('HERE!!! should require first four elements of strokes to be non-negative')
print(lambda_handler(my_event, {}))

my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        [5, 0, 15, 15, '#000000'],
        [0, 0, 15, 15, '#000000'],
        [0, 0, 25, -25, '#000000']
    ])
}

print('HERE!!! should require first four elements of strokes to be non-negative')
print(lambda_handler(my_event, {}))


my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        [5000, 0, 15, 15, '#000000'],
        [0, 0, 15, 15, '#000000'],
        [0, 0, 25, 25, '#000000']
    ])
}

print('HERE!!! should require first four elements of strokes to be less than 2000')
print(lambda_handler(my_event, {}))

my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        [5, 0, 15, 15, '#000000'],
        [0, 0, 15, 15, '#000000'],
        [0, 0, 25, 5000, '#000000']
    ])
}

print('HERE!!! should require first four elements of strokes to be less than 2000')
print(lambda_handler(my_event, {}))


my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        [0, 0, 15, 15, 0],
        [0, 0, 15, 15, '#000000'],
        [0, 0, 25, 25, '#000000']
    ])
}

print('HERE!!! should require fifth element to be a string')
print(lambda_handler(my_event, {}))



my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        [0, 0, 15, 15, '#000000'],
        [0, 0, 15, 15, '#abc'],
        [0, 0, 25, 25, '#000000']
    ])
}

print('HERE!!! should require fifth element to be seven characters')
print(lambda_handler(my_event, {}))



my_event = {
    'httpMethod': 'POST',
    'pathParameters': {
        'doodle_id': new_doodle_id,
    },
    'body': json.dumps([
        [0, 0, 15, 15, '#000000'],
        [0, 0, 15, 15, '#ffaa00'],
        [0, 0, 25, 25, '@000000']
    ])
}

print('HERE!!! should require fifth element to start with #')
print(lambda_handler(my_event, {}))
