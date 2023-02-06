import boto3
import time

AWS_REGION="ap-south-1"
bucket="mahesh-bucket-using-resource"
s3_resource=boto3.resource("s3",region_name=AWS_REGION)
s3_object=s3_resource.Bucket(bucket)
# s3_object=s3_resource.Object(Bucket,"test12345.py")
s3_object.download_file(r"C:\Users\s4489mah\Desktop\GangiReddy\Boto_Scripts\s3\s3_bucket_create.py","test12345.py")
print ("Download is done.....")