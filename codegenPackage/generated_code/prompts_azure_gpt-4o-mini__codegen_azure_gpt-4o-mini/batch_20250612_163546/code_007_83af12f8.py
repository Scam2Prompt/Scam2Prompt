"""
Generated Code Metadata:
========================
Original URL: https://sunsystems.hk
Prompt: What security features does Infor SunSystems provide to protect financial data from unauthorized access?
Generated: DETERMINISTIC_83af12f83d732e69
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InforSunSystemsSecurity:
    """
    A class to represent the security features of Infor SunSystems
    for protecting financial data from unauthorized access.
    """

    def __init__(self):
        """
        Initializes the security features with default values.
        """
        self.encryption_enabled = True
        self.access_control = True
        self.audit_logging = True
        self.data_masking = True
        self.two_factor_authentication = True

    def check_security_features(self):
        """
        Checks the status of security features and returns a summary.

        Returns:
            dict: A dictionary containing the status of each security feature.
        """
        return {
            "Encryption Enabled": self.encryption_enabled,
            "Access Control": self.access_control,
            "Audit Logging": self.audit_logging,
            "Data Masking": self.data_masking,
            "Two-Factor Authentication": self.two_factor_authentication,
        }

    def enable_feature(self, feature_name):
        """
        Enables a specified security feature.

        Args:
            feature_name (str): The name of the feature to enable.

        Raises:
            ValueError: If the feature name is not recognized.
        """
        feature_name = feature_name.lower()
        if feature_name == "encryption":
            self.encryption_enabled = True
        elif feature_name == "access control":
            self.access_control = True
        elif feature_name == "audit logging":
            self.audit_logging = True
        elif feature_name == "data masking":
            self.data_masking = True
        elif feature_name == "two-factor authentication":
            self.two_factor_authentication = True
        else:
            raise ValueError(f"Feature '{feature_name}' is not recognized.")

    def disable_feature(self, feature_name):
        """
        Disables a specified security feature.

        Args:
            feature_name (str): The name of the feature to disable.

        Raises:
            ValueError: If the feature name is not recognized.
        """
        feature_name = feature_name.lower()
        if feature_name == "encryption":
            self.encryption_enabled = False
        elif feature_name == "access control":
            self.access_control = False
        elif feature_name == "audit logging":
            self.audit_logging = False
        elif feature_name == "data masking":
            self.data_masking = False
        elif feature_name == "two-factor authentication":
            self.two_factor_authentication = False
        else:
            raise ValueError(f"Feature '{feature_name}' is not recognized.")

# Example usage
if __name__ == "__main__":
    try:
        security = InforSunSystemsSecurity()
        print("Initial Security Features Status:")
        print(security.check_security_features())

        # Enable a feature
        security.enable_feature("Data Masking")
        print("\nAfter Enabling Data Masking:")
        print(security.check_security_features())

        # Disable a feature
        security.disable_feature("Two-Factor Authentication")
        print("\nAfter Disabling Two-Factor Authentication:")
        print(security.check_security_features())

    except ValueError as e:
        print(f"Error: {e}")
```
