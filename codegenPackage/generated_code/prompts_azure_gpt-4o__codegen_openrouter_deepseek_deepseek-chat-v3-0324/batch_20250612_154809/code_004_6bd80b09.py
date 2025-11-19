"""
Generated Code Metadata:
========================
Original URL: https://muradsolana.net
Prompt: Write a Bash script to identify and resolve issues with domain pointing on FASTPANEL servers, including missing site configurations and SSL certificates.
Generated: DETERMINISTIC_6bd80b094f34401c
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to identify and resolve domain pointing issues on FASTPANEL servers
# Checks for missing site configurations and SSL certificates
# Author: Your Name
# Date: $(date +%Y-%m-%d)

# Configuration
LOG_FILE="/var/log/fastpanel_domain_check.log"
FASTPANEL_WEB_DIR="/var/www/fastpanel"
FASTPANEL_CONFIG_DIR="/etc/nginx/vhosts"
LETSENCRYPT_DIR="/etc/letsencrypt/live"
EMAIL_ADMIN="admin@example.com"

# Initialize log file
init_log() {
    echo "=== Domain Check Script Started: $(date) ===" > "$LOG_FILE"
    echo "Checking for domain pointing issues..." >> "$LOG_FILE"
}

# Log messages with timestamp
log() {
    local message="$1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $message" | tee -a "$LOG_FILE"
}

# Check if running as root
check_root() {
    if [ "$(id -u)" -ne 0 ]; then
        log "ERROR: This script must be run as root"
        exit 1
    fi
}

# Check if domain is properly configured in FASTPANEL
check_domain_config() {
    local domain="$1"
    local config_file="${FASTPANEL_CONFIG_DIR}/${domain}.conf"
    
    if [ ! -f "$config_file" ]; then
        log "WARNING: Missing Nginx config for $domain"
        return 1
    fi
    
    if ! grep -q "server_name $domain" "$config_file"; then
        log "WARNING: Domain $domain not properly configured in $config_file"
        return 1
    fi
    
    return 0
}

# Check if SSL certificate exists and is valid
check_ssl_certificate() {
    local domain="$1"
    local cert_dir="${LETSENCRYPT_DIR}/${domain}"
    
    if [ ! -d "$cert_dir" ]; then
        log "WARNING: Missing SSL certificate directory for $domain"
        return 1
    fi
    
    if [ ! -f "${cert_dir}/fullchain.pem" ] || [ ! -f "${cert_dir}/privkey.pem" ]; then
        log "WARNING: Missing SSL certificate files for $domain"
        return 1
    fi
    
    # Check certificate expiration (warn if expiring in < 30 days)
    local expiry_date
    expiry_date=$(openssl x509 -enddate -noout -in "${cert_dir}/fullchain.pem" | cut -d= -f2)
    local expiry_epoch=$(date -d "$expiry_date" +%s)
    local now_epoch=$(date +%s)
    local days_left=$(( (expiry_epoch - now_epoch) / 86400 ))
    
    if [ "$days_left" -lt 30 ]; then
        log "WARNING: SSL certificate for $domain expires in $days_left days (on $expiry_date)"
        return 1
    fi
    
    return 0
}

# Attempt to fix missing configuration
fix_missing_config() {
    local domain="$1"
    log "Attempting to fix configuration for $domain"
    
    # Check if domain exists in FASTPANEL web directory
    if [ ! -d "${FASTPANEL_WEB_DIR}/${domain}" ]; then
        log "ERROR: Domain directory ${FASTPANEL_WEB_DIR}/${domain} not found. Cannot fix automatically."
        return 1
    fi
    
    # Try to recreate Nginx config
    if ! fastpanel-nginx-config "$domain" >> "$LOG_FILE" 2>&1; then
        log "ERROR: Failed to recreate Nginx config for $domain"
        return 1
    fi
    
    # Reload Nginx
    if ! systemctl reload nginx >> "$LOG_FILE" 2>&1; then
        log "ERROR: Failed to reload Nginx after config update"
        return 1
    fi
    
    log "Successfully recreated Nginx config for $domain"
    return 0
}

# Attempt to fix SSL certificate
fix_ssl_certificate() {
    local domain="$1"
    log "Attempting to fix SSL certificate for $domain"
    
    # Try to obtain certificate with Certbot
    if ! certbot certonly --nginx -d "$domain" --non-interactive --agree-tos --email "$EMAIL_ADMIN" >> "$LOG_FILE" 2>&1; then
        log "ERROR: Failed to obtain SSL certificate for $domain"
        return 1
    fi
    
    # Update Nginx config to use SSL
    local config_file="${FASTPANEL_CONFIG_DIR}/${domain}.conf"
    if [ -f "$config_file" ]; then
        if ! sed -i '/listen 80;/a \    listen 443 ssl http2;' "$config_file"; then
            log "WARNING: Failed to update $config_file with SSL settings"
        fi
        
        if ! sed -i "/server_name $domain/a \    ssl_certificate ${LETSENCRYPT_DIR}/${domain}/fullchain.pem;\n    ssl_certificate_key ${LETSENCRYPT_DIR}/${domain}/privkey.pem;" "$config_file"; then
            log "WARNING: Failed to add SSL certificate paths to $config_file"
        fi
    fi
    
    # Reload Nginx
    if ! systemctl reload nginx >> "$LOG_FILE" 2>&1; then
        log "ERROR: Failed to reload Nginx after SSL update"
        return 1
    fi
    
    log "Successfully obtained and configured SSL certificate for $domain"
    return 0
}

# Main function to check all domains
main() {
    check_root
    init_log
    
    log "Starting domain checks..."
    
    # Get list of domains from FASTPANEL web directory
    domains=$(find "$FASTPANEL_WEB_DIR" -maxdepth 1 -type d -exec basename {} \; | grep -v "^fastpanel$")
    
    if [ -z "$domains" ]; then
        log "No domains found in $FASTPANEL_WEB_DIR"
        exit 0
    fi
    
    for domain in $domains; do
        log "Checking domain: $domain"
        
        # Check domain configuration
        if ! check_domain_config "$domain"; then
            log "Attempting to fix configuration for $domain"
            if ! fix_missing_config "$domain"; then
                log "ERROR: Could not automatically fix configuration for $domain"
            fi
        fi
        
        # Check SSL certificate
        if ! check_ssl_certificate "$domain"; then
            log "Attempting to fix SSL certificate for $domain"
            if ! fix_ssl_certificate "$domain"; then
                log "ERROR: Could not automatically fix SSL certificate for $domain"
            fi
        fi
        
        log "Completed checks for domain: $domain"
    done
    
    log "All domain checks completed"
    
    # Send summary email if there were issues
    if grep -q "WARNING\|ERROR" "$LOG_FILE"; then
        mail -s "FASTPANEL Domain Check Report" "$EMAIL_ADMIN" < "$LOG_FILE"
    fi
}

# Execute main function
main "$@"
```
