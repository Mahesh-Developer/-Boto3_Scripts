import boto3
import time

aws_region="ap-south-1"

#Deleting S3 bucket using Boto3 client

s3_client=boto3.client("s3",region_name=aws_region)
bucket_name="mahesh-bucket-using-resource"
s3_client.delete_bucket(Bucket=bucket_name)

print ("bucket deleted..........")

print ("*"*20)

#Deleting S3 bucket using Boto3 resource

s3_resource=boto3.resource("s3",region_name=aws_region)
bucket_name="mahesh-bucket-using-client"
s3_object=s3_resource.Bucket(bucket_name)
s3_object.delete()

print ("bucket deleted..........")