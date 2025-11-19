"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunsystems.hk
Prompt: What security features does Infor SunSystems provide to protect financial data from unauthorized access?
Generated: DETERMINISTIC_83af12f83d732e69
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InforSunSystemsSecurity:
    """
    A class to represent the security features of Infor SunSystems
    aimed at protecting financial data from unauthorized access.
    """

    def __init__(self):
        self.features = {
            "User Authentication": "Supports multi-factor authentication to verify user identity.",
            "Role-Based Access Control": "Allows access permissions based on user roles and responsibilities.",
            "Data Encryption": "Encrypts sensitive financial data both in transit and at rest.",
            "Audit Trails": "Maintains logs of user activities for accountability and traceability.",
            "Data Masking": "Obscures sensitive information in non-production environments.",
            "Network Security": "Utilizes firewalls and intrusion detection systems to protect against external threats.",
            "Regular Security Updates": "Ensures that the system is updated with the latest security patches."
        }

    def get_security_features(self):
        """
        Returns a list of security features implemented in Infor SunSystems.

        :return: A dictionary containing security features and their descriptions.
        """
        return self.features

    def check_feature_availability(self, feature_name):
        """
        Checks if a specific security feature is available.

        :param feature_name: Name of the security feature to check.
        :return: A message indicating whether the feature is available or not.
        """
        if feature_name in self.features:
            return f"Feature '{feature_name}' is available: {self.features[feature_name]}"
        else:
            return f"Feature '{feature_name}' is not available."

if __name__ == "__main__":
    # Create an instance of InforSunSystemsSecurity
    security_system = InforSunSystemsSecurity()

    # Get and display all security features
    print("Infor SunSystems Security Features:")
    for feature, description in security_system.get_security_features().items():
        print(f"- {feature}: {description}")

    # Example feature check
    feature_name = "Data Encryption"
    result = security_system.check_feature_availability(feature_name)
    print(result)
```
