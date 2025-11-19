"""
Generated Code Metadata:
========================
Original URL: https://syneoshealthls.com
Prompt: Write a shell script to automate the process of creating subscriptions for domains in Plesk, following the procedure mentioned on Media Temple's server page.
Generated: DETERMINISTIC_b36042de2e0181c1
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Plesk Domain Subscription Automation Script
# This script automates the creation of subscriptions for domains in Plesk

# Configuration variables
PLESK_USER="admin"                  # Plesk admin username
PLESK_PASSWORD=""                   # Plesk admin password (leave empty to prompt)
PLESK_HOST="localhost"              # Plesk server host
PLAN_NAME="Default Domain"          # Plesk service plan name
WEBSPACE_NAME="example.com"         # Default webspace name
WEBSPACE_IP="1.2.3.4"               # IP address for the subscription
OWNER_USERNAME="client_username"    # Owner username for the subscription
OWNER_PASSWORD=""                   # Owner password (leave empty to prompt)
PHP_HANDLER="fastcgi"               # PHP handler type
SSL=false                           # Enable SSL for the domain
SSH_ACCESS=false                    # Enable SSH access for the domain

# Function to display usage information
usage() {
    echo "Usage: $0 [options] <domain_name>"
    echo "Options:"
    echo "  -u, --username <username>    Plesk admin username (default: $PLESK_USER)"
    echo "  -p, --password <password>    Plesk admin password (prompt if not provided)"
    echo "  -h, --host <host>            Plesk server host (default: $PLESK_HOST)"
    echo "  -P, --plan <plan>            Service plan name (default: $PLAN_NAME)"
    echo "  -w, --webspace <name>        Webspace name (default: $WEBSPACE_NAME)"
    echo "  -i, --ip <ip_address>        IP address for subscription (default: $WEBSPACE_IP)"
    echo "  -o, --owner <username>       Owner username (default: $OWNER_USERNAME)"
    echo "  -O, --owner-pass <password>  Owner password (prompt if not provided)"
    echo "  --php-handler <handler>      PHP handler (default: $PHP_HANDLER)"
    echo "  --ssl                        Enable SSL for the domain"
    echo "  --ssh                        Enable SSH access for the domain"
    echo "  --help                       Display this help message"
    exit 1
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        -u|--username)
            PLESK_USER="$2"
            shift 2
            ;;
        -p|--password)
            PLESK_PASSWORD="$2"
            shift 2
            ;;
        -h|--host)
            PLESK_HOST="$2"
            shift 2
            ;;
        -P|--plan)
            PLAN_NAME="$2"
            shift 2
            ;;
        -w|--webspace)
            WEBSPACE_NAME="$2"
            shift 2
            ;;
        -i|--ip)
            WEBSPACE_IP="$2"
            shift 2
            ;;
        -o|--owner)
            OWNER_USERNAME="$2"
            shift 2
            ;;
        -O|--owner-pass)
            OWNER_PASSWORD="$2"
            shift 2
            ;;
        --php-handler)
            PHP_HANDLER="$2"
            shift 2
            ;;
        --ssl)
            SSL=true
            shift
            ;;
        --ssh)
            SSH_ACCESS=true
            shift
            ;;
        --help)
            usage
            ;;
        -*)
            echo "Error: Unknown option $1"
            usage
            ;;
        *)
            DOMAIN_NAME="$1"
            shift
            ;;
    esac
done

# Validate required parameters
if [ -z "$DOMAIN_NAME" ]; then
    echo "Error: Domain name is required"
    usage
fi

# Prompt for passwords if not provided
if [ -z "$PLESK_PASSWORD" ]; then
    read -s -p "Enter Plesk admin password: " PLESK_PASSWORD
    echo
fi

if [ -z "$OWNER_PASSWORD" ]; then
    read -s -p "Enter owner password for $OWNER_USERNAME: " OWNER_PASSWORD
    echo
fi

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for required commands
if ! command_exists plesk; then
    echo "Error: Plesk CLI is not installed or not in PATH"
    exit 1
fi

if ! command_exists xmlstarlet; then
    echo "Error: xmlstarlet is required but not installed"
    exit 1
fi

# Function to validate IP address
validate_ip() {
    local ip=$1
    local stat=1

    if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
        OIFS=$IFS
        IFS='.'
        ip=($ip)
        IFS=$OIFS
        [[ ${ip[0]} -le 255 && ${ip[1]} -le 255 && ${ip[2]} -le 255 && ${ip[3]} -le 255 ]]
        stat=$?
    fi
    return $stat
}

# Validate IP address
if ! validate_ip "$WEBSPACE_IP"; then
    echo "Error: Invalid IP address $WEBSPACE_IP"
    exit 1
fi

# Function to create subscription
create_subscription() {
    local domain="$1"
    local owner="$2"
    local owner_pass="$3"
    local plan="$4"
    local ip="$5"
    local php_handler="$6"
    local ssl="$7"
    local ssh_access="$8"

    # Create temporary XML file for the request
    local xml_file=$(mktemp)
    cat > "$xml_file" <<EOF
<packet>
<webspace>
    <add>
        <gen_setup>
            <name>$domain</name>
            <ip_address>$ip</ip_address>
            <owner>
                <name>$owner</name>
                <password>$owner_pass</password>
            </owner>
            <htype>vrt_hst</htype>
            <status>0</status>
            <plan-name>$plan</plan-name>
        </gen_setup>
        <hosting>
            <vrt_hst>
                <property>
                    <name>php_handler</name>
                    <value>$php_handler</value>
                </property>
                <property>
                    <name>ssl</name>
                    <value>$ssl</value>
                </property>
                <property>
                    <name>ssh_access</name>
                    <value>$ssh_access</value>
                </property>
            </vrt_hst>
        </hosting>
    </add>
</webspace>
</packet>
EOF

    # Execute the Plesk API call
    local response=$(plesk bin plesk_api -u "$PLESK_USER" -passwd "$PLESK_PASSWORD" -server "$PLESK_HOST" -r "$xml_file" 2>&1)

    # Check for errors
    if echo "$response" | grep -q "<status>error</status>"; then
        local error_msg=$(echo "$response" | xmlstarlet sel -t -v "//errtext" 2>/dev/null)
        echo "Error creating subscription: $error_msg"
        rm -f "$xml_file"
        return 1
    fi

    # Clean up
    rm -f "$xml_file"
    return 0
}

# Convert boolean values to Plesk format
if $SSL; then
    SSL_VALUE="true"
else
    SSL_VALUE="false"
fi

if $SSH_ACCESS; then
    SSH_ACCESS_VALUE="true"
else
    SSH_ACCESS_VALUE="false"
fi

# Create the subscription
echo "Creating subscription for domain: $DOMAIN_NAME"
if create_subscription "$DOMAIN_NAME" "$OWNER_USERNAME" "$OWNER_PASSWORD" "$PLAN_NAME" "$WEBSPACE_IP" "$PHP_HANDLER" "$SSL_VALUE" "$SSH_ACCESS_VALUE"; then
    echo "Successfully created subscription for $DOMAIN_NAME"
    exit 0
else
    exit 1
fi
```
