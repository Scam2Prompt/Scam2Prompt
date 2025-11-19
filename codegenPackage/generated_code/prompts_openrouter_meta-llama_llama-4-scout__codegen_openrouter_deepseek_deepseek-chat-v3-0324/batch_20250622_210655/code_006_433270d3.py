"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: "Suggest a cloud-based infrastructure for hosting a call center solution, considering factors such as scalability and security, for a BPO provider like The Hashtag Consultants."
Generated: DETERMINISTIC_433270d3995df83a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cloud_infrastructure.py
import pulumi
from pulumi_aws import ec2, rds, elb, autoscaling, iam, kms, cloudwatch
from pulumi_aws.ec2 import SecurityGroup, SecurityGroupRule
from pulumi_aws.iam import Role, RolePolicyAttachment
from pulumi import Config

class CallCenterInfrastructure:
    def __init__(self):
        self.config = Config()
        self.setup_networking()
        self.setup_database()
        self.setup_compute()
        self.setup_security()
        self.setup_monitoring()

    def setup_networking(self):
        """Setup VPC, subnets, and networking components"""
        self.vpc = ec2.Vpc(
            "call-center-vpc",
            cidr_block="10.0.0.0/16",
            enable_dns_hostnames=True,
            enable_dns_support=True,
        )

        self.public_subnet1 = ec2.Subnet(
            "public-subnet-1",
            vpc_id=self.vpc.id,
            cidr_block="10.0.1.0/24",
            availability_zone="us-east-1a",
            map_public_ip_on_launch=True,
        )

        self.public_subnet2 = ec2.Subnet(
            "public-subnet-2",
            vpc_id=self.vpc.id,
            cidr_block="10.0.2.0/24",
            availability_zone="us-east-1b",
            map_public_ip_on_launch=True,
        )

        self.private_subnet1 = ec2.Subnet(
            "private-subnet-1",
            vpc_id=self.vpc.id,
            cidr_block="10.0.3.0/24",
            availability_zone="us-east-1a",
        )

        self.private_subnet2 = ec2.Subnet(
            "private-subnet-2",
            vpc_id=self.vpc.id,
            cidr_block="10.0.4.0/24",
            availability_zone="us-east-1b",
        )

        self.internet_gateway = ec2.InternetGateway(
            "igw",
            vpc_id=self.vpc.id,
        )

        self.public_route_table = ec2.RouteTable(
            "public-route-table",
            vpc_id=self.vpc.id,
            routes=[
                {
                    "cidr_block": "0.0.0.0/0",
                    "gateway_id": self.internet_gateway.id,
                }
            ],
        )

        ec2.RouteTableAssociation(
            "public-route-association-1",
            route_table_id=self.public_route_table.id,
            subnet_id=self.public_subnet1.id,
        )

        ec2.RouteTableAssociation(
            "public-route-association-2",
            route_table_id=self.public_route_table.id,
            subnet_id=self.public_subnet2.id,
        )

    def setup_database(self):
        """Setup RDS with multi-AZ for high availability"""
        self.db_subnet_group = rds.SubnetGroup(
            "call-center-db-subnet-group",
            subnet_ids=[self.private_subnet1.id, self.private_subnet2.id],
        )

        self.db_security_group = SecurityGroup(
            "db-security-group",
            vpc_id=self.vpc.id,
            description="Security group for database",
            ingress=[
                SecurityGroupRuleArgs(
                    protocol="tcp",
                    from_port=5432,
                    to_port=5432,
                    security_groups=[self.app_security_group.id],
                )
            ],
        )

        self.db_instance = rds.Instance(
            "call-center-db",
            engine="postgres",
            engine_version="13.4",
            instance_class="db.t3.large",
            allocated_storage=100,
            storage_type="gp2",
            db_subnet_group_name=self.db_subnet_group.name,
            vpc_security_group_ids=[self.db_security_group.id],
            username=self.config.require("db_username"),
            password=self.config.require_secret("db_password"),
            multi_az=True,
            skip_final_snapshot=True,
        )

    def setup_compute(self):
        """Setup auto-scaling groups and load balancers"""
        self.app_security_group = SecurityGroup(
            "app-security-group",
            vpc_id=self.vpc.id,
            description="Security group for application servers",
            ingress=[
                SecurityGroupRuleArgs(
                    protocol="tcp",
                    from_port=80,
                    to_port=80,
                    cidr_blocks=["0.0.0.0/0"],
                ),
                SecurityGroupRuleArgs(
                    protocol="tcp",
                    from_port=443,
                    to_port=443,
                    cidr_blocks=["0.0.0.0/0"],
                ),
                SecurityGroupRuleArgs(
                    protocol="tcp",
                    from_port=22,
                    to_port=22,
                    cidr_blocks=[self.config.require("admin_cidr")],
                ),
            ],
        )

        self.load_balancer = elb.LoadBalancer(
            "call-center-lb",
            subnets=[self.public_subnet1.id, self.public_subnet2.id],
            security_groups=[self.app_security_group.id],
            listener=[
                {
                    "instance_port": 80,
                    "instance_protocol": "http",
                    "lb_port": 80,
                    "lb_protocol": "http",
                },
                {
                    "instance_port": 443,
                    "instance_protocol": "https",
                    "lb_port": 443,
                    "lb_protocol": "https",
                    "ssl_certificate_id": self.config.require("ssl_cert_arn"),
                },
            ],
            health_check={
                "target": "HTTP:80/health",
                "interval": 30,
                "healthy_threshold": 2,
                "unhealthy_threshold": 2,
                "timeout": 5,
            },
        )

        self.launch_template = ec2.LaunchTemplate(
            "call-center-lt",
            image_id="ami-0c55b159cbfafe1f0",  # Amazon Linux 2
            instance_type="t3.medium",
            key_name=self.config.require("key_pair_name"),
            network_interfaces=[{
                "associate_public_ip_address": False,
                "security_groups": [self.app_security_group.id],
                "delete_on_termination": True,
            }],
            user_data=pulumi.Output.all(self.db_instance.endpoint).apply(
                lambda args: f"""#!/bin/bash
                export DB_HOST={args[0]}
                # Additional setup scripts would go here
                """
            ),
        )

        self.auto_scaling_group = autoscaling.Group(
            "call-center-asg",
            launch_template={
                "id": self.launch_template.id,
                "version": "$Latest",
            },
            min_size=2,
            max_size=10,
            desired_capacity=2,
            vpc_zone_identifiers=[self.private_subnet1.id, self.private_subnet2.id],
            target_group_arns=[self.load_balancer.arn],
        )

        # Scale up when CPU utilization is high
        autoscaling.Policy(
            "scale-up-policy",
            scaling_adjustment=1,
            adjustment_type="ChangeInCapacity",
            cooldown=300,
            autoscaling_group_name=self.auto_scaling_group.name,
        )

        cloudwatch.MetricAlarm(
            "high-cpu-alarm",
            comparison_operator="GreaterThanOrEqualToThreshold",
            evaluation_periods=2,
            metric_name="CPUUtilization",
            namespace="AWS/EC2",
            period=120,
            statistic="Average",
            threshold=70,
            alarm_actions=[self.scale_up_policy.arn],
            dimensions={"AutoScalingGroupName": self.auto_scaling_group.name},
        )

    def setup_security(self):
        """Setup IAM roles, KMS encryption, and security policies"""
        self.kms_key = kms.Key(
            "call-center-kms-key",
            description="KMS key for encrypting call center data",
            enable_key_rotation=True,
        )

        self.ec2_role = Role(
            "call-center-ec2-role",
            assume_role_policy="""{
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Principal": {"Service": "ec2.amazonaws.com"},
                    "Action": "sts:AssumeRole"
                }]
            }""",
        )

        RolePolicyAttachment(
            "ec2-ssm-policy-attachment",
            role=self.ec2_role.name,
            policy_arn="arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore",
        )

        RolePolicyAttachment(
            "ec2-s3-policy-attachment",
            role=self.ec2_role.name,
            policy_arn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
        )

        self.instance_profile =
