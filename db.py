import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.create_table(
    TableName = 'users',
    KeySchema = [
        {
            'AttributeName' : 'id',
            'KeyType' : 'HASH'
        },
        {
            'AttributeName' : 'rng',
            'KeyType' : 'RANGE'
        }
    ],
    AttributeDefinations = [
        {
            'AttributeName' : 'id',
            'AttributeType' : 's'
        },
        {
            'AttributeName' : 'rng',
            'AttributeType' : 's'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits' : 5,
        'WriteCapacityUnits' : 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)
