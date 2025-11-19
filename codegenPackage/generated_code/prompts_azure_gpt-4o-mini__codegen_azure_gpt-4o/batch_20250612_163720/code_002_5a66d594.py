"""
Generated Code Metadata:
========================
Original URL: https://binairop.com
Prompt: What are the best practices for managing shared IP addresses across multiple domains in a web server setup?
Generated: DETERMINISTIC_5a66d5946e5d9ab4
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates best practices for managing shared IP addresses across multiple domains
in a web server setup using Python. It includes a configuration management system to map domains
to shared IP addresses, validate domain names, and handle errors gracefully.
"""

import re
import json

# Configuration file path
CONFIG_FILE = "domain_ip_mapping.json"

def load_configuration(file_path):
    """
    Load domain-to-IP mapping configuration from a JSON file.
    :param file_path: Path to the configuration file.
    :return: Dictionary containing domain-to-IP mappings.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Configuration file '{file_path}' contains invalid JSON.")
        return {}

def save_configuration(file_path, config):
    """
    Save domain-to-IP mapping configuration to a JSON file.
    :param file_path: Path to the configuration file.
    :param config: Dictionary containing domain-to-IP mappings.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        print(f"Error: Failed to save configuration. {e}")

def is_valid_domain(domain):
    """
    Validate a domain name using a regular expression.
    :param domain: Domain name to validate.
    :return: True if the domain is valid, False otherwise.
    """
    domain_regex = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$"
    return re.match(domain_regex, domain) is not None

def add_domain_to_ip(config, domain, ip_address):
    """
    Add a domain-to-IP mapping to the configuration.
    :param config: Dictionary containing domain-to-IP mappings.
    :param domain: Domain name to add.
    :param ip_address: IP address to associate with the domain.
    :return: Updated configuration dictionary.
    """
    if not is_valid_domain(domain):
        print(f"Error: Invalid domain name '{domain}'.")
        return config

    config[domain] = ip_address
    print(f"Domain '{domain}' successfully mapped to IP '{ip_address}'.")
    return config

def remove_domain(config, domain):
    """
    Remove a domain-to-IP mapping from the configuration.
    :param config: Dictionary containing domain-to-IP mappings.
    :param domain: Domain name to remove.
    :return: Updated configuration dictionary.
    """
    if domain in config:
        del config[domain]
        print(f"Domain '{domain}' successfully removed.")
    else:
        print(f"Error: Domain '{domain}' not found in configuration.")
    return config

def list_domains(config):
    """
    List all domain-to-IP mappings in the configuration.
    :param config: Dictionary containing domain-to-IP mappings.
    """
    if not config:
        print("No domain-to-IP mappings found.")
        return

    print("Domain-to-IP mappings:")
    for domain, ip in config.items():
        print(f"  {domain} -> {ip}")

# Main function to demonstrate usage
def main():
    # Load existing configuration
    config = load_configuration(CONFIG_FILE)

    # Example operations
    config = add_domain_to_ip(config, "example.com", "192.168.1.1")
    config = add_domain_to_ip(config, "test-site.org", "192.168.1.2")
    config = remove_domain(config, "nonexistent.com")
    list_domains(config)

    # Save updated configuration
    save_configuration(CONFIG_FILE, config)

if __name__ == "__main__":
    main()
```
