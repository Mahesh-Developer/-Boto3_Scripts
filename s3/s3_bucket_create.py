import boto3
import time

AWS_REGION="ap-south-1"

print ("**************Creating Bucket using Client Object*****************")

s3_client=boto3.client("s3",region_name=AWS_REGION)
bucket_name="mahesh-bucket-using-client"
location={"LocationConstraint":AWS_REGION}
client_response=s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'})

print (f'Amazon "{bucket_name}" bucket has been created.....')


time.sleep(60)

print ("**************Creating Bucket using Response Object*****************")

s3_response=boto3.resource("s3",region_name=AWS_REGION)
bucket_name="mahesh-bucket-using-resource"
location={"LocationConstraint":AWS_REGION}

resource_response=s3_response.create_bucket(Bucket=bucket_name,
                                            CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'})

print (f'Amazon "{bucket_name}" bucket has been created....')