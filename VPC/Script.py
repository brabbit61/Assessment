import boto3
import time

region = 'us-east-1'
instance_id = "i-067948446631b1473"
ec21 = boto3.resource('ec2',region_name = region)
ec2 = boto3.client('ec2',region_name = region)

vpc = ec21.create_vpc(CidrBlock='172.16.0.0/16')
print("VPC id: " + vpc.id)

subnet1 = ec21.create_subnet(CidrBlock = '172.16.1.0/24', VpcId= vpc.id)
subnet2 = ec21.create_subnet(CidrBlock = '172.16.2.0/24', VpcId= vpc.id)
subnet3 = ec21.create_subnet(CidrBlock = '172.16.3.0/24', VpcId= vpc.id)
subnet4 = ec21.create_subnet(CidrBlock = '172.16.4.0/24', VpcId= vpc.id)
print("Subnet1 id: "+ subnet1.id)
print("Subnet2 id: "+ subnet2.id)
print("Subnet3 id: "+ subnet3.id)
print("Subnet4 id: "+ subnet4.id)

internet_gateway = ec2.create_internet_gateway()
ig_id = internet_gateway['InternetGateway']['InternetGatewayId']
vpc.attach_internet_gateway(InternetGatewayId = ig_id)
print("Internet Gateway id: "+ig_id)

route_table1 = vpc.create_route_table()
route = route_table1.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=ig_id)
print("Route Table 1 id: "+route_table1.id)

route_table1.associate_with_subnet(SubnetId=subnet1.id)
route_table1.associate_with_subnet(SubnetId=subnet2.id)

address = ec2.allocate_address(Domain='vpc')
allocation_id = address['AllocationId']
nat_gateway = ec2.create_nat_gateway(SubnetId=subnet1.id, AllocationId=allocation_id)
print("NAT Gateway id: "+nat_gateway['NatGateway']['NatGatewayId'])

route_table2 = vpc.create_route_table()
route = route_table2.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=nat_gateway['NatGateway']['NatGatewayId'])
print("Route Table 2 id: "+route_table2.id)
route_table2.associate_with_subnet(SubnetId=subnet3.id)
route_table2.associate_with_subnet(SubnetId=subnet4.id)


