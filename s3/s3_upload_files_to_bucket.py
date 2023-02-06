import boto3
import pathlib
import os

BASEDIR=pathlib.Path(__file__).parent.resolve()
print (BASEDIR)

AWS_REGION="ap-south-1"

s3_client=boto3.client("s3",region_name=AWS_REGION)
print ("****************Uploading files to s3**************")
def upload_files(filename, bucket,object_name=None):
    if object_name==None:
        object_name=filename
    
    s3_client.upload_file(filename,bucket,object_name)
    print ("{0} has been uploaded to {1}".format(filename,bucket))
    
    
file_name=os.path.join(BASEDIR,'s3_bucket_create.py')
upload_files(file_name,"mahesh-bucket-using-resource")
print ("Done")