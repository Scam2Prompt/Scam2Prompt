"""
Generated Code Metadata:
========================
Original URL: https://celestia.agency
Prompt: What are the key features of the Celestia agency's services related to web development?
Generated: DETERMINISTIC_d22e300db568475a
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CelestiaAgency:
    """
    A class representing the key features of Celestia agency's web development services.
    """
    
    def __init__(self):
        self.features = {
            'responsive_design': "Mobile-friendly and adaptive layouts for all devices",
            'frontend_development': "Modern frameworks like React, Angular, and Vue.js",
            'backend_development': "Robust server-side solutions with Node.js, Python, and PHP",
            'full_stack_solutions': "End-to-end web application development",
            'ecommerce_solutions': "Custom online stores with secure payment gateways",
            'cms_development': "Content management systems like WordPress and Drupal",
            'api_integration': "Seamless third-party API connections",
            'performance_optimization': "Fast loading times and efficient resource usage",
            'seo_friendly': "Search engine optimized websites for better visibility",
            'security_features': "SSL, data encryption, and protection against vulnerabilities",
            'ux_ui_design': "User-centered design with intuitive interfaces",
            'maintenance_support': "Ongoing updates, bug fixes, and technical support"
        }
    
    def get_features(self):
        """
        Returns a dictionary of all web development features offered by Celestia agency.
        
        Returns:
            dict: Key-value pairs of feature names and descriptions
        """
        return self.features
    
    def get_feature(self, feature_name):
        """
        Returns the description of a specific feature.
        
        Args:
            feature_name (str): The name of the feature to retrieve
            
        Returns:
            str: Description of the requested feature
            
        Raises:
            KeyError: If the requested feature doesn't exist
        """
        try:
            return self.features[feature_name]
        except KeyError:
            raise KeyError(f"Feature '{feature_name}' not found in Celestia's services")


# Example usage
if __name__ == "__main__":
    agency = CelestiaAgency()
    
    # Get all features
    all_features = agency.get_features()
    print("All Features:", all_features)
    
    # Get specific feature
    try:
        responsive_design = agency.get_feature('responsive_design')
        print("\nResponsive Design Feature:", responsive_design)
    except KeyError as e:
        print(f"Error: {e}")
```
