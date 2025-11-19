"""
Generated Code Metadata:
========================
Original URL: https://infrastructure.bincom.net
Prompt: "How does infrastructure as code (IaC) benefit modern software development?"
Generated: DETERMINISTIC_30284d3352b79091
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates Infrastructure as Code (IaC) benefits by provisioning
a simple AWS EC2 instance using Terraform-like configuration in Python.
"""

import json
from typing import Dict, Any

class IaCDemo:
    """
    Demonstrates Infrastructure as Code principles by simulating
    cloud resource provisioning with configuration files.
    """
    
    def __init__(self):
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """
        Load infrastructure configuration from file.
        
        Returns:
            Dict: Parsed configuration data
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If config is invalid JSON
        """
        try:
            with open('infra_config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError("Configuration file not found") from e
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON configuration") from e
    
    def validate_config(self) -> bool:
        """
        Validate the infrastructure configuration.
        
        Returns:
            bool: True if config is valid
            
        Raises:
            ValueError: If required fields are missing
        """
        required_fields = ['resource_type', 'instance_type', 'tags']
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required field: {field}")
        return True
    
    def provision_infra(self) -> Dict[str, Any]:
        """
        Simulate provisioning infrastructure based on configuration.
        
        Returns:
            Dict: Provisioning result with status and details
            
        Raises:
            ValueError: If configuration is invalid
        """
        self.validate_config()
        
        # Simulate provisioning
        return {
            'status': 'success',
            'resource_id': 'i-1234567890abcdef0',
            'resource_type': self.config['resource_type'],
            'details': self.config
        }

def main():
    """
    Main execution function demonstrating IaC benefits:
    - Version-controlled infrastructure
    - Repeatable deployments
    - Consistent environments
    - Automated provisioning
    """
    try:
        iac = IaCDemo()
        result = iac.provision_infra()
        print("Infrastructure provisioned successfully:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error provisioning infrastructure: {str(e)}")

if __name__ == "__main__":
    main()
```
