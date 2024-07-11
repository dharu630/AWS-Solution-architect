--pip install boto3
--aws configure credentials
import boto3
sts_client = boto3.client('sts')
# Call the get-caller-identity API
caller_identity = sts_client.get_caller_identity()
# Print the caller identity information
print("User ID: ", caller_identity['UserId'])
print("Account: ", caller_identity['Account'])
print("ARN: ", caller_identity['Arn'])
