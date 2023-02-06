import boto3

AWS_REGION="us-east-1"

ec2_resource=boto3.resource("ec2",region_name=AWS_REGION)
instance_id="i-08ac6aebb3dabfa4f"
instance=ec2_resource.Instance(instance_id)
instance.reboot()

print(f'Ec2 instance"{instance.id}"has been rebooted......')