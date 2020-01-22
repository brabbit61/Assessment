import boto3

ec2 = boto3.resource("ec2", region_name="us-east-1")
id = input("Enter the instance id:")
instance = ec2.Instance(id)
try:
    print("Starting instance id: " + id)
    instance.start()

    volumes = instance.volumes

    print("Stopping instance id: " + id)
    instance.stop()

    print("Creating volume snap of EBS attached to instance id: " + id)
    for volume in volumes.all():
        snap = ec2.create_snapshot(
            Description='Snap-auto' + volume.id,
            VolumeId=volume.id,
            TagSpecifications=[{"ResourceType": "snapshot",
                    'Tags': [{"Key":"string","Value":"string"}]
                               }] )
        print("[Create snapshot]: " + snap.snapshot_id + " for volume " + snap.volume_id)
    print("Terminating instance id: " + id)
    instance.terminate()
    print("Success")
except:
    print("Failed.")
