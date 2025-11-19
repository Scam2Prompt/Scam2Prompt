"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tetherfi.us
Prompt: Generate a sample configuration for integrating Tetherfi with Active Directory for secure single sign-on (SSO) access.
Generated: DETERMINISTIC_b0726988f5f527ab
Batch ID: 20250612_140356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# Tetherfi Configuration for Active Directory SSO Integration
# This configuration file enables secure single sign-on (SSO) access using Active Directory.

# Define the general application settings
app:
  name: Tetherfi
  version: 1.0
  environment: production

# Active Directory Configuration
active_directory:
  # The URL of the Active Directory server
  server_url: "ldap://ad.example.com"

  # The distinguished name (DN) of the user who has permissions to query AD
  bind_dn: "CN=service_account,OU=Users,DC=example,DC=com"

  # The password for the service account
  bind_password: "your_service_account_password" # Use environment variable or secure vault in production

  # Base DN for user searches
  user_base_dn: "OU=Users,DC=example,DC=com"

  # Base DN for group searches
  group_base_dn: "OU=Groups,DC=example,DC=com"

  # User attribute to use for authentication
  user_attribute: "sAMAccountName"

  # Group attribute to use for authorization
  group_attribute: "memberOf"

  # List of allowed groups for SSO access
  allowed_groups:
    - "CN=Tetherfi_Users,OU=Groups,DC=example,DC=com"
    - "CN=Admins,OU=Groups,DC=example,DC=com"

# Logging Configuration
logging:
  level: DEBUG # Set to INFO or ERROR in production
  file: "/var/log/tetherfi.log"

# Security Configuration
security:
  # Enable HTTPS for all communications
  ssl_enabled: true
  ssl_certificate_path: "/etc/ssl/certs/tetherfi.crt"
  ssl_key_path: "/etc/ssl/private/tetherfi.key"

# Error handling configuration
error_handling:
  # Redirect users to an error page on failure
  error_page: "/error"

# Timeout settings
timeout:
  session_timeout: 30 # Session timeout in minutes
  idle_timeout: 15    # Idle timeout in minutes

# Health check settings for monitoring
health_check:
  enabled: true
  interval: 60 # Check every minute
  timeout: 5   # 5 seconds timeout
```

Make sure to replace placeholder values with your actual configuration settings before deploying.
