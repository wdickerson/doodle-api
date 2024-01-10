## doodle-api

This is a serverless backend for a doodling game, which is to be deployed to AWS Lambda. 

A CloudFormation templete defines AWS API Gateway endpoints which route to the Lambda function.

### Data model

The data structures are `strokes` and `doodles`.

#### `stroke`

A `stroke` represents one "stroke" that can be drawn on an HTML canvas: a line from (x0, y0) to (x1, y1) in the specified color. We save the required data in a 5-element array:

```
[x0, y0, x1, y1, color]
```
where `color` is a hexadecimal representation, ie `#f3f3f3`.

#### `doodle`

A `doodle` is a collection of strokes that represent a user's small drawing:

```
[
    <stroke 0>,
    <stroke 1>,
    <stroke 2>,
    ...
]
```

### API methods

Two methods are provided:

#### GET doodles/:doodle_id

Returns `doodle_id` and `doodles` as JSON:

```json
{
    "doodle_id": <id>,
    "doodles": [
        [
            <stroke>,
            <stroke>,
            ...
        ],
        [
            <stroke>,
            <stroke>,
            ...
        ],
        ...
    ]
}
```

Responds `404` if `doodle_id` is not found.


#### POST doodles/:doodle_id(optional)

Accepts a `doodle` in the post body:

```
[
    <stroke 0>,
    <stroke 1>,
    <stroke 2>,
    ...
]
```

If a `doodle_id` is provided in the path, then the `doodle` is appended to the end of `doodles` on the corresponding database object.

If a `doodle_id` is not provided, a database object is created with one doodle.

Returns the same format as `GET`.

Responds `404` if `doodle_id` is not found.

Responds `400` for various malformed inputs:
+ Malformed post body
+ Non-integer coordinates
+ Malformed color code
+ Doodle too big
+ Too many doodles
+ Coordinates out of range
