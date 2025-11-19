"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Bash script to automate the creation of a Linode instance with a Dedicated CPU, set up DNS using Linode's DNS Manager, and configure backups.
Generated: DETERMINISTIC_a16e9182220b5bfd
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Linode Instance Creator with DNS and Backup Configuration
# Requires linode-cli to be installed and configured with API token

# Configuration variables
LINODE_TYPE="g6-dedicated-2"
LINODE_REGION="us-east"
LINODE_IMAGE="linode/ubuntu22.04"
LINODE_ROOT_PASS=$(openssl rand -base64 32)
LINODE_LABEL="prod-instance-$(date +%s)"
SSH_PUBLIC_KEY="$HOME/.ssh/id_rsa.pub"
DOMAIN="example.com"
SUBDOMAIN="www"
EMAIL="admin@example.com"
BACKUP_ENABLED="true"

# Check if linode-cli is installed
if ! command -v linode-cli &> /dev/null; then
    echo "Error: linode-cli is not installed. Please install it first."
    exit 1
fi

# Validate SSH key exists
if [ ! -f "$SSH_PUBLIC_KEY" ]; then
    echo "Error: SSH public key not found at $SSH_PUBLIC_KEY"
    exit 1
fi

# Create Linode instance
echo "Creating Linode instance..."
INSTANCE_RESPONSE=$(linode-cli linodes create \
    --type "$LINODE_TYPE" \
    --region "$LINODE_REGION" \
    --image "$LINODE_IMAGE" \
    --root_pass "$LINODE_ROOT_PASS" \
    --label "$LINODE_LABEL" \
    --authorized_keys "$(cat $SSH_PUBLIC_KEY)" \
    --backups_enabled "$BACKUP_ENABLED" \
    --json)

# Check if instance creation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to create Linode instance"
    exit 1
fi

INSTANCE_ID=$(echo "$INSTANCE_RESPONSE" | jq -r '.[0].id')
INSTANCE_IP=$(echo "$INSTANCE_RESPONSE" | jq -r '.[0].ipv4[0]')

if [ -z "$INSTANCE_ID" ] || [ -z "$INSTANCE_IP" ]; then
    echo "Error: Failed to parse instance information"
    exit 1
fi

echo "Instance created successfully. ID: $INSTANCE_ID, IP: $INSTANCE_IP"

# Wait for instance to be running
echo "Waiting for instance to be ready..."
while true; do
    STATUS=$(linode-cli linodes view "$INSTANCE_ID" --format "status" --text)
    if [ "$STATUS" == "running" ]; then
        break
    fi
    sleep 10
done

# Configure DNS
echo "Configuring DNS..."
DOMAIN_ID=$(linode-cli domains list --format "id,domain" | grep "$DOMAIN" | awk '{print $1}')

if [ -z "$DOMAIN_ID" ]; then
    echo "Domain not found. Creating domain..."
    DOMAIN_RESPONSE=$(linode-cli domains create \
        --type master \
        --domain "$DOMAIN" \
        --soa_email "$EMAIL" \
        --json)
    
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create domain"
        exit 1
    fi
    
    DOMAIN_ID=$(echo "$DOMAIN_RESPONSE" | jq -r '.id')
fi

# Create DNS record
echo "Creating DNS record..."
linode-cli domains records-create "$DOMAIN_ID" \
    --name "$SUBDOMAIN" \
    --type A \
    --target "$INSTANCE_IP" \
    --ttl_sec 300

if [ $? -ne 0 ]; then
    echo "Error: Failed to create DNS record"
    exit 1
fi

echo "DNS configured successfully. $SUBDOMAIN.$DOMAIN points to $INSTANCE_IP"

# Enable backups if not already enabled
CURRENT_BACKUP_STATUS=$(linode-cli linodes view "$INSTANCE_ID" --format "backups.enabled" --text)
if [ "$CURRENT_BACKUP_STATUS" != "True" ]; then
    echo "Enabling backups..."
    linode-cli linodes backups-enable "$INSTANCE_ID"
    
    if [ $? -ne 0 ]; then
        echo "Warning: Failed to enable backups"
    else
        echo "Backups enabled successfully"
    fi
else
    echo "Backups are already enabled for this instance"
fi

# Output summary
echo ""
echo "=== Deployment Summary ==="
echo "Instance ID: $INSTANCE_ID"
echo "Label: $LINODE_LABEL"
echo "IP Address: $INSTANCE_IP"
echo "Root Password: $LINODE_ROOT_PASS"
echo "SSH Access: ssh root@$INSTANCE_IP"
echo "Domain: $SUBDOMAIN.$DOMAIN"
echo "Backups: $BACKUP_ENABLED"
echo "========================="

exit 0
```
