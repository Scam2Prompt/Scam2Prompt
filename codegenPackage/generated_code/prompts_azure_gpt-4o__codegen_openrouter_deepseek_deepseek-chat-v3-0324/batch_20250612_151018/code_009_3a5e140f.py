"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3346--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a StackScript for deploying a custom application on Linode, utilizing Linode's developer tools and integrations.
Generated: DETERMINISTIC_3a5e140faad0dbca
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

# StackScript for deploying a custom application on Linode
# Description: This script automates the deployment of a custom application on a Linode instance.
# It includes system updates, dependency installation, application setup, and security configurations.

# <UDF name="APP_NAME" label="Application Name" default="myapp">
# <UDF name="APP_REPO" label="Git Repository URL" default="">
# <UDF name="APP_PORT" label="Application Port" default="3000">
# <UDF name="SSH_USER" label="SSH Username" default="deploy">
# <UDF name="SSH_PUBKEY" label="SSH Public Key" default="">
# <UDF name="ENV_VARS" label="Environment Variables (KEY=VALUE, separated by commas)" default="">

# Ensure the script fails on any error
set -euo pipefail

# Logging function
log() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $*"
}

# Update system and install dependencies
system_setup() {
    log "Updating system packages..."
    apt-get update -y
    apt-get upgrade -y

    log "Installing required dependencies..."
    apt-get install -y \
        git \
        curl \
        wget \
        build-essential \
        ufw \
        python3 \
        python3-pip \
        python3-venv \
        software-properties-common
}

# Configure firewall
configure_firewall() {
    log "Configuring firewall..."
    ufw allow ssh
    ufw allow "${APP_PORT}/tcp"
    ufw --force enable
}

# Setup SSH access
setup_ssh() {
    if [ -n "${SSH_PUBKEY}" ]; then
        log "Setting up SSH access..."
        local ssh_dir="/home/${SSH_USER}/.ssh"
        mkdir -p "${ssh_dir}"
        echo "${SSH_PUBKEY}" > "${ssh_dir}/authorized_keys"
        chown -R "${SSH_USER}:${SSH_USER}" "${ssh_dir}"
        chmod 700 "${ssh_dir}"
        chmod 600 "${ssh_dir}/authorized_keys"
    fi
}

# Clone and setup application
setup_application() {
    if [ -z "${APP_REPO}" ]; then
        log "No repository URL provided, skipping application setup."
        return
    fi

    log "Cloning application repository..."
    local app_dir="/opt/${APP_NAME}"
    git clone "${APP_REPO}" "${app_dir}"
    cd "${app_dir}"

    log "Setting up application environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    # Set environment variables
    if [ -n "${ENV_VARS}" ]; then
        log "Setting environment variables..."
        IFS=',' read -ra vars <<< "${ENV_VARS}"
        for var in "${vars[@]}"; do
            echo "export ${var}" >> /etc/environment
        done
    fi
}

# Setup systemd service
setup_service() {
    log "Creating systemd service..."
    local service_file="/etc/systemd/system/${APP_NAME}.service"
    cat > "${service_file}" << EOF
[Unit]
Description=${APP_NAME} Service
After=network.target

[Service]
User=${SSH_USER}
WorkingDirectory=/opt/${APP_NAME}
EnvironmentFile=/etc/environment
ExecStart=/opt/${APP_NAME}/venv/bin/python /opt/${APP_NAME}/app.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

    systemctl daemon-reload
    systemctl enable "${APP_NAME}"
    systemctl start "${APP_NAME}"
}

# Main execution
main() {
    log "Starting deployment..."

    # Create deploy user
    if ! id "${SSH_USER}" &>/dev/null; then
        log "Creating user ${SSH_USER}..."
        useradd -m -s /bin/bash "${SSH_USER}"
        usermod -aG sudo "${SSH_USER}"
        echo "${SSH_USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
    fi

    system_setup
    configure_firewall
    setup_ssh
    setup_application
    setup_service

    log "Deployment completed successfully!"
    log "Application is running on port ${APP_PORT}"
    log "SSH access is available for user ${SSH_USER}"
}

main "$@"
```
