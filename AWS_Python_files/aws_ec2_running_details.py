#Adrian Guillory (Dack Dissident)
#06-02-2023

#Python Program for viewing details of running instances

import boto3

#Copy + paste AWS Access Key from AWS > IAM > User Account name > Security Credentials
AWS_KEY="<AWS_KEY HERE>"
#Copy + paste AWS Secret Access Key from AWS > IAM > User Account name > Security Credentials
AWS_SECRET="<AWS_SECRET HERE>"
#Copy + paste AWS Region
REGION="<REGION HERE>"

print("Connecting to EC2")
ec2 = boto3.client('ec2', aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET, region_name=REGION)

response = ec2.describe_instances()
for instance in response['Reservations'][0]['Instances']:
    print("Instance Type: " + str(instance['InstanceType']))
    print("Instance State:" + str(instance['State']['Name']))
    print("Instance Launch Time: " + str(instance['LaunchTime']))
    print("Instance Public DNS: " + str(instance['PublicDnsName']))
    print("Instance Private DNS: " + str(instance['PrivateDnsName']))
    print("Instance IP: " + str(instance['PublicIpAddress']))
    print("Instance Private IP: " + str(instance['PrivateIpAddress']))
