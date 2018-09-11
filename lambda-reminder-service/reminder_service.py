import boto3

sns = boto3.client('sns')

def handler(event,context):
    sns.publish(
        PhoneNumber='+61476756622', 
        Message=(
            'Hello! Karan You are an AWS devops engineer'
            'You will Succeed in Sydney Australia!'
        )
    )
    return 'success'
