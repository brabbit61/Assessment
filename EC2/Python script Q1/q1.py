import boto3

instance=['i-0c60f9b341e2d0249']
ec2=boto3.client("ec2",region_name='us-east-1')
start=ec2.start_instances(InstanceIds=instance)
stop=ec2.stop_instances(InstanceIds=instance)
ec2_1=boto3.resource('ec2',region_name='us-east-1')
inst=ec2_1.Instance(instance[0])
vol=inst.volumes.all()
l=[v.id for v in vol]
vol_snap=ec2.create_snapshot(Decription='Vol1',VolumeId=l[0])
print(vol_snap)
trmt=ec2.terminate_instances(InstanceIds=instance)
