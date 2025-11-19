"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://event-clink.org
Prompt: How do I troubleshoot common issues when accessing the Nginx Proxy Manager admin panel?
Generated: DETERMINISTIC_683634223e4ebbf7
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Troubleshoot common issues when accessing the Nginx Proxy Manager admin panel

# Define helper functions for logging and error handling
log_info() {
    echo "[INFO] $(date +'%Y-%m-%d %H:%M:%S') - $1"
}

log_error() {
    echo "[ERROR] $(date +'%Y-%m-%d %H:%M:%S') - $1" >&2
}

# Check if Docker is running
check_docker() {
    if ! systemctl is-active --quiet docker; then
        log_error "Docker is not running. Please start Docker."
        exit 1
    fi
    log_info "Docker is running."
}

# Check if Nginx Proxy Manager container is running
check_container() {
    local container_name="nginx-proxy-manager"
    if ! docker ps -q --filter "name=${container_name}" | grep -q .; then
        log_error "Nginx Proxy Manager container is not running. Please check with 'docker-compose up'."
        exit 1
    fi
    log_info "Nginx Proxy Manager container is running."
}

# Check Nginx Proxy Manager logs for errors
check_logs() {
    local container_name="nginx-proxy-manager"
    log_info "Checking logs for container: ${container_name}"
    docker logs "${container_name}" --tail 50 | grep -i "error"
}

# Check if the correct ports are open
check_ports() {
    local admin_port=81
    local ssl_port=443

    # Check if the admin port is listening
    if ! ss -tuln | grep -q ":${admin_port}"; then
        log_error "Admin port ${admin_port} is not listening. Please check your Nginx Proxy Manager configuration."
    else
        log_info "Admin port ${admin_port} is listening."
    fi

    # Check if the SSL port is listening
    if ! ss -tuln | grep -q ":${ssl_port}"; then
        log_error "SSL port ${ssl_port} is not listening. Please check your Nginx Proxy Manager configuration."
    else
        log_info "SSL port ${ssl_port} is listening."
    fi
}

# Main troubleshooting function
troubleshoot_nginx_proxy_manager() {
    log_info "Starting troubleshooting for Nginx Proxy Manager..."

    check_docker
    check_container
    check_logs
    check_ports

    log_info "Troubleshooting completed."
}

# Run the troubleshooting function
troubleshoot_nginx_proxy_manager
```
