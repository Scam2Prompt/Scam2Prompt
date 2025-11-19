"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.metis-labs.com
Prompt: Generate a cloud architecture design for a startup looking to implement a scalable data and AI stack, referencing Metis Labs' tailored solutions.
Generated: DETERMINISTIC_cc6f42c8de74edd2
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a template code that represents a cloud architecture design for a scalable data and AI stack using AWS as the cloud provider. The solution incorporates infrastructure as code (IaC) using Terraform, which is widely used for deploying cloud infrastructure in a reproducible and scalable manner.

```hcl
# Terraform configuration for a scalable data and AI architecture

# Specify Terraform version and provider
terraform {
  required_version = ">= 1.3.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1" # Specify your preferred region
}

# Define variables for flexibility
variable "project_name" {
  default = "metis-ai-stack"
}

variable "environment" {
  default = "prod"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "subnet_cidrs" {
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

# Create a VPC
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "${var.project_name}-vpc"
  }
}

# Create subnets
resource "aws_subnet" "subnets" {
  count             = length(var.subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.subnet_cidrs[count.index]
  map_public_ip_on_launch = true
  tags = {
    Name = "${var.project_name}-subnet-${count.index + 1}"
  }
}

# Create an S3 bucket for data storage
resource "aws_s3_bucket" "data_bucket" {
  bucket = "${var.project_name}-data-${var.environment}"
  acl    = "private"

  tags = {
    Name        = "${var.project_name}-data-bucket"
    Environment = var.environment
  }
}

# Enable versioning for the S3 bucket
resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.data_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Create an EKS cluster for scalable AI workloads
module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "${var.project_name}-eks-${var.environment}"
  cluster_version = "1.27"
  subnets         = aws_subnet.subnets[*].id
  vpc_id          = aws_vpc.main.id

  tags = {
    Environment = var.environment
  }
}

# Create an RDS instance for structured data storage
resource "aws_db_instance" "rds_instance" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "14.4"
  instance_class       = "db.t3.medium"
  name                 = "${var.project_name}_db"
  username             = "admin"
  password             = "securepassword123" # Replace with secure secrets management in production
  publicly_accessible  = false
  skip_final_snapshot  = true

  tags = {
    Name        = "${var.project_name}-rds-instance"
    Environment = var.environment
  }
}

# Create IAM roles for AI/ML workloads
resource "aws_iam_role" "ai_role" {
  name = "${var.project_name}-ai-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = "sts:AssumeRole"
        Effect    = "Allow"
        Principal = {
          Service = "eks.amazonaws.com"
        }
      }
    ]
  })

  tags = {
    Environment = var.environment
  }
}

# Attach policies to the IAM role
resource "aws_iam_policy_attachment" "ai_policy_attachment" {
  name       = "${var.project_name}-ai-policy-attachment"
  roles      = [aws_iam_role.ai_role.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess" # Example policy, adjust as needed
}

# Outputs for reference
output "vpc_id" {
  value = aws_vpc.main.id
}

output "s3_bucket_name" {
  value = aws_s3_bucket.data_bucket.bucket
}

output "eks_cluster_name" {
  value = module.eks.cluster_name
}

output "rds_endpoint" {
  value = aws_db_instance.rds_instance.endpoint
}

output "ai_role_arn" {
  value = aws_iam_role.ai_role.arn
}
```

### Notes:
1. This script sets up a Virtual Private Cloud (VPC), subnets, an S3 bucket for data storage, an EKS cluster for AI workloads, an RDS instance for structured data, and IAM roles for AI/ML operations.
2. Replace placeholder values (e.g., `securepassword123`) with secrets retrieved from a secure secrets manager.
3. Use Terraform modules (like `eks/aws`) for reusable components.
4. Ensure proper security practices, such as encryption for S3 buckets and RDS instances, before deployment into production.
