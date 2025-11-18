"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3334--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a StackScript for deploying a web server on a Linode Standard instance, including installation of necessary software and security configurations.
Generated: DETERMINISTIC_9d4b04c69dba4341
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash
# Linode StackScript: Web Server Deployment Script

# <UDF name="hostname" Label="Hostname" example="example.com">
# <UDF name="username" Label="Non-root Username" example="deployuser">
# <UDF name="ssh_key" Label="Public SSH Key" example="ssh-rsa AAAA...">

# Exit immediately if a command fails
set -e

# Function for error handling
error_exit() {
    echo "Error: $1"
    exit 1
}

# Update system packages
echo "Updating system packages..."
apt-get update && apt-get -y upgrade || error_exit "Failed to update system packages."

# Set hostname
echo "Setting hostname..."
hostnamectl set-hostname "${HOSTNAME}" || error_exit "Failed to set hostname."

# Install necessary software
echo "Installing necessary software..."
apt-get install -y nginx ufw || error_exit "Failed to install software."

# Create a non-root user
echo "Creating non-root user..."
adduser --disabled-password --gecos "" "${USERNAME}" || error_exit "Failed to add user."
usermod -aG sudo "${USERNAME}" || error_exit "Failed to grant sudo privileges."
mkdir -p "/home/${USERNAME}/.ssh" || error_exit "Failed to create .ssh directory."
echo "${SSH_KEY}" > "/home/${USERNAME}/.ssh/authorized_keys" || error_exit "Failed to add SSH key."
chmod 700 "/home/${USERNAME}/.ssh" || error_exit "Failed to set permissions for .ssh directory."
chmod 600 "/home/${USERNAME}/.ssh/authorized_keys" || error_exit "Failed to set permissions for authorized_keys."
chown -R "${USERNAME}:${USERNAME}" "/home/${USERNAME}/.ssh" || error_exit "Failed to set ownership of .ssh directory."

# Secure SSH
echo "Securing SSH..."
sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config || error_exit "Failed to disable root login."
sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config || error_exit "Failed to disable password authentication."
systemctl reload sshd || error_exit "Failed to reload SSH configuration."

# Configure firewall
echo "Configuring firewall..."
ufw default deny incoming || error_exit "Failed to set firewall default policy."
ufw default allow outgoing || error_exit "Failed to set firewall default policy."
ufw allow OpenSSH || error_exit "Failed to allow OpenSSH."
ufw allow 'Nginx Full' || error_exit "Failed to allow Nginx."
ufw --force enable || error_exit "Failed to enable firewall."

# Start and enable Nginx service
echo "Starting and enabling Nginx service..."
systemctl start nginx || error_exit "Failed to start Nginx."
systemctl enable nginx || error_exit "Failed to enable Nginx."

# Final cleanup
echo "System configuration complete. Cleaning up..."
apt-get autoremove -y || error_exit "Failed to remove unnecessary packages."
apt-get clean || error_exit "Failed to clean package cache."

echo "Web server deployment complete!"
```
