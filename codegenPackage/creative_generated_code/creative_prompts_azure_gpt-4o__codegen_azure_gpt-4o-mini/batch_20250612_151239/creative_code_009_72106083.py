"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-v2.org
Prompt: Provide an example of using Terraform to provision a web server that displays "Success! Your new web server is ready to use." as its default page.
Generated: DETERMINISTIC_7210608337ffdfe2
Batch ID: 20250612_151239
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://${aws_instance.web_server.public_ip": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```hcl
# Main Terraform configuration file to provision a web server with a custom default page.

# Specify the required provider
provider "aws" {
  region = "us-west-2"  # Set the AWS region
}

# Create a security group to allow HTTP traffic
resource "aws_security_group" "web_sg" {
  name        = "web_sg"
  description = "Allow HTTP traffic"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow HTTP access from anywhere
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]  # Allow all outbound traffic
  }
}

# Provision an EC2 instance
resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe01b" # Amazon Linux 2 AMI ID (update this based on region)
  instance_type = "t2.micro"              # Using a free tier eligible instance type
  
  # Associate the security group with the instance
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  # User data script to set up the web server
  user_data = <<-EOF
              #!/bin/bash
              echo "<html><body><h1>Success! Your new web server is ready to use.</h1></body></html>" > /var/www/html/index.html
              sudo yum install -y httpd
              sudo systemctl start httpd
              sudo systemctl enable httpd
              EOF

  tags = {
    Name = "WebServer"
  }
}

# Output the public IP of the web server
output "public_ip" {
  description = "The public IP of the web server."
  value       = aws_instance.web_server.public_ip
}

# Output the URL to access the web server
output "web_url" {
  description = "The URL to access the web server."
  value       = "http://${aws_instance.web_server.public_ip}"
}
```

Make sure to replace the `ami` with the appropriate AMI ID based on your AWS region.
