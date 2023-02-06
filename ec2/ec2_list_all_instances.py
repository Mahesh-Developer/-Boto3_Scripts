import boto3
import time

AWS_REGION='us-east-1'
ec2_resource=boto3.resource("ec2",region_name=AWS_REGION)

response=ec2_resource.instances.all()

for instance in response:
    time.sleep(2)
    print ("Instance id is: ",instance.id)