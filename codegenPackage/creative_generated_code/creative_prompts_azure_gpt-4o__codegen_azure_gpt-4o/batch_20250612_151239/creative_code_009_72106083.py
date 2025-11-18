"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-v2.org
Prompt: Provide an example of using Terraform to provision a web server that displays "Success! Your new web server is ready to use." as its default page.
Generated: DETERMINISTIC_7210608337ffdfe2
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```hcl
# Terraform Configuration for Provisioning a Web Server

# Specify the required Terraform version
terraform {
  required_version = ">= 1.3.0"
}

# Provider block to use AWS as the cloud provider
provider "aws" {
  region = "us-east-1" # Specify the AWS region
}

# Define a key pair for SSH access
resource "aws_key_pair" "web_server_key" {
  key_name   = "web-server-key"
  public_key = file("~/.ssh/id_rsa.pub") # Path to your public SSH key
}

# Create a security group for the web server
resource "aws_security_group" "web_server_sg" {
  name_prefix = "web-server-sg"
  description = "Security group for the web server"

  # Allow inbound HTTP traffic
  ingress {
    description = "Allow HTTP traffic"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow SSH access for management
  ingress {
    description = "Allow SSH traffic"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Launch an EC2 instance
resource "aws_instance" "web_server" {
  ami             = "ami-0c02fb55956c7d316" # Amazon Linux 2 AMI (replace with the latest recommended AMI ID)
  instance_type   = "t2.micro"              # Use t2.micro for free-tier eligible instances
  key_name        = aws_key_pair.web_server_key.key_name
  security_groups = [aws_security_group.web_server_sg.name]

  # User data script to configure the web server
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo "Success! Your new web server is ready to use." > /var/www/html/index.html
            EOF

  tags = {
    Name = "Terraform-Web-Server"
  }
}

# Output the public IP of the web server
output "web_server_public_ip" {
  value = aws_instance.web_server.public_ip
  description = "Public IP of the web server"
}
```
