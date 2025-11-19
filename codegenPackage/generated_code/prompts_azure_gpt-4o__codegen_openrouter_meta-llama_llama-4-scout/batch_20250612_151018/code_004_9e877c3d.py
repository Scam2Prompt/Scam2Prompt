"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a Terraform configuration file to provision a GPU Linode instance for machine learning workloads and configure it with Linode's Block Storage.
Generated: DETERMINISTIC_9e877c3d5e9d459e
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```terraform
# Configure the Linode Provider
provider "linode" {
  token = var.linode_token
}

# Create a Linode GPU instance
resource "linode_instance" "gpu_instance" {
  image      = "linode/debian11"
  label      = "ml-gpu-instance"
  region     = "us-west"
  type       = "g6-highmem-2g"
  root_pass  = var.root_password

  # Configure GPU
  gpu = true

  # Block Storage for additional storage
  block_storage {
    target  = "/dev/sdb"
    size    = 100
    label   = "ml-block-storage"
  }
}

# Create a Linode Block Storage volume
resource "linode_block_storage_volume" "ml_storage" {
  label  = "ml-storage-volume"
  region = "us-west"
  size   = 500
}

# Attach Block Storage volume to instance
resource "linode_instance_disk" "attach_storage" {
  instance_id = linode_instance.gpu_instance.id
  disk_id     = linode_block_storage_volume.ml_storage.id
  target      = "/dev/sdc"
}

# Configure Linode instance networking
resource "linode_instance_ip" "gpu_instance_ip" {
  instance_id = linode_instance.gpu_instance.id
  type        = "ipv4"
}

# Output instance details
output "instance_ip" {
  value = linode_instance_ip.gpu_instance_ip.address
}

output "instance_label" {
  value = linode_instance.gpu_instance.label
}

variable "linode_token" {
  type        = string
  description = "Linode API token"
  sensitive   = true
}

variable "root_password" {
  type        = string
  description = "Root password for Linode instance"
  sensitive   = true
}
```
