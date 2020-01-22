import boto3

v=raw_input("Enter instance Id : ")
ec2=boto3.client("ec2",region_name='us-east-1')
start=ec2.start_instances(InstanceIds=[v])
stop=ec2.stop_instances(InstanceIds=[v])
ec2_1=boto3.resource('ec2',region_name='us-east-1')
inst=ec2_1.Instance(v)
vol=inst.volumes.all()
l=[v.id for v in vol]
vol_snap=ec2.create_snapshot(Decription='Vol1',VolumeId=l[0])
print(vol_snap)
trmt=ec2.terminate_instances(InstanceIds=[v])
