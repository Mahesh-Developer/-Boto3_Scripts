import boto3
import time

AWS_REGION="ap-south-1"

print ("************List all bucket names using boto3 client***********")

s3_client=boto3.client("s3",region_name=AWS_REGION)

buckets=s3_client.list_buckets()
for bucket in buckets["Buckets"]:
    time.sleep(1)
    print (f'Bucket name: "{bucket}"')
    
time.sleep(30)


print ("************List all bucket names using boto3 client***********")

s3_response=boto3.resource("s3",region_name=AWS_REGION)
buckets=s3_response.buckets.all()
for bucket in buckets:
    time.sleep(1)
    print('Bucket name: ',bucket.name)