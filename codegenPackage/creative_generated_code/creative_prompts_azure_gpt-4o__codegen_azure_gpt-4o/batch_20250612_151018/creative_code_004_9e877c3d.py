"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a Terraform configuration file to provision a GPU Linode instance for machine learning workloads and configure it with Linode's Block Storage.
Generated: DETERMINISTIC_9e877c3d5e9d459e
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```hcl
# Terraform configuration for provisioning a GPU Linode instance with attached Block Storage

terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = ">=1.28.0"
    }
  }
  required_version = ">= 0.12"
}

provider "linode" {
  token = var.linode_api_token # Linode API Token (stored securely in variables or environment variables)
}

variable "linode_api_token" {
  description = "Linode API Token"
  type        = string
}

variable "region" {
  description = "Region where the Linode instance will be created"
  type        = string
  default     = "us-east" # Default region (can be changed)
}

variable "gpu_instance_type" {
  description = "Instance type for GPU workloads"
  type        = string
  default     = "g1-gpu-1" # GPU instance type
}

variable "block_storage_size" {
  description = "Size of the Block Storage volume in GB"
  type        = number
  default     = 100 # Default block storage size in GB
}

resource "linode_instance" "gpu_instance" {
  label      = "gpu-instance"                  # Human-readable label for the instance
  region     = var.region                      # Select the region
  type       = var.gpu_instance_type           # Select the GPU instance type
  image      = "linode/ubuntu22.04"            # Operating system image
  root_pass  = var.root_password               # Root password for the server
  authorized_keys = [var.ssh_public_key]       # Public key for SSH access
  tags       = ["gpu", "machine_learning"]     # Tags for categorization

  # Enable backups for production workloads (optional)
  backups {
    enabled = true
  }
}

resource "linode_volume" "block_storage" {
  label       = "gpu-storage"                 # Label for the Block Storage
  region      = var.region                    # Same region as the instance
  size        = var.block_storage_size        # Size of the Block Storage in GB
  linode_id   = linode_instance.gpu_instance.id # Attach to GPU instance
}

output "instance_ip" {
  description = "Public IPv4 address of the GPU instance"
  value       = linode_instance.gpu_instance.ip_address
}

output "storage_label" {
  description = "Label of the Block Storage volume"
  value       = linode_volume.block_storage.label
}

# Sensitive information like SSH keys and root password should be securely passed via Terraform variables or environment variables
variable "root_password" {
  description = "Root password for the instance"
  type        = string
  sensitive   = true
}

variable "ssh_public_key" {
  description = "SSH public key for accessing the instance"
  type        = string
}
```
