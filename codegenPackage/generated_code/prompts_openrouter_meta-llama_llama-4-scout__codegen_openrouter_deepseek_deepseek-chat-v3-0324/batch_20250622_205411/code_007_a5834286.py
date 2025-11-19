"""
Generated Code Metadata:
========================
Original URL: https://best-crypto-wallet.yivesites.com
Prompt: "Generate a technical documentation section for Apelbet's use of cookies, explaining the types of cookies used, their purposes, and how users can manage their cookie preferences."
Generated: DETERMINISTIC_a58342867ad55098
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cookie Policy Documentation for Apelbet

This module provides technical documentation about Apelbet's cookie usage,
including types of cookies, their purposes, and management options.
"""

class CookiePolicy:
    """
    A class to represent and document Apelbet's cookie policy.
    
    Attributes:
        essential_cookies (dict): Essential cookies required for site functionality
        analytics_cookies (dict): Cookies used for analytics and performance
        marketing_cookies (dict): Cookies used for marketing and personalization
    """
    
    def __init__(self):
        """Initialize cookie categories with their descriptions and purposes."""
        self.essential_cookies = {
            'session_id': {
                'purpose': 'Maintain user session state',
                'duration': 'Session',
                'mandatory': True
            },
            'csrf_token': {
                'purpose': 'Security against CSRF attacks',
                'duration': 'Session',
                'mandatory': True
            }
        }
        
        self.analytics_cookies = {
            '_ga': {
                'purpose': 'Google Analytics - distinguishes users',
                'duration': '2 years',
                'mandatory': False
            },
            '_gid': {
                'purpose': 'Google Analytics - distinguishes users',
                'duration': '24 hours',
                'mandatory': False
            }
        }
        
        self.marketing_cookies = {
            '_fbp': {
                'purpose': 'Facebook Pixel - tracks conversions',
                'duration': '3 months',
                'mandatory': False
            },
            'ads_prefs': {
                'purpose': 'Stores advertising preferences',
                'duration': '1 year',
                'mandatory': False
            }
        }
    
    def get_cookie_categories(self):
        """
        Returns all cookie categories with their details.
        
        Returns:
            dict: Dictionary containing all cookie categories and their details
        """
        return {
            'essential': self.essential_cookies,
            'analytics': self.analytics_cookies,
            'marketing': self.marketing_cookies
        }
    
    def get_cookie_management_options(self):
        """
        Returns information about how users can manage their cookie preferences.
        
        Returns:
            dict: Dictionary containing management options
        """
        return {
            'browser_settings': {
                'description': 'Users can manage cookies through browser settings',
                'instructions': 'Browser settings > Privacy > Cookie settings'
            },
            'consent_banner': {
                'description': 'Initial consent banner allows preference selection',
                'instructions': 'Click "Cookie Preferences" in footer to change'
            },
            'api_endpoint': {
                'description': 'Programmatic preference management via API',
                'endpoint': '/api/cookie-preferences',
                'methods': ['GET', 'POST']
            }
        }
    
    def generate_documentation(self):
        """
        Generates complete cookie policy documentation in markdown format.
        
        Returns:
            str: Markdown formatted documentation
        """
        doc = "# Apelbet Cookie Policy\n\n"
        doc += "## Types of Cookies Used\n\n"
        
        for category, cookies in self.get_cookie_categories().items():
            doc += f"### {category.capitalize()} Cookies\n\n"
            doc += "| Cookie Name | Purpose | Duration | Mandatory |\n"
            doc += "|-------------|---------|----------|-----------|\n"
            for name, details in cookies.items():
                doc += f"| {name} | {details['purpose']} | {details['duration']} | {'Yes' if details['mandatory'] else 'No'} |\n"
            doc += "\n"
        
        doc += "## Managing Cookie Preferences\n\n"
        for option, details in self.get_cookie_management_options().items():
            doc += f"### {option.replace('_', ' ').title()}\n"
            doc += f"{details['description']}\n\n"
            if 'instructions' in details:
                doc += f"**How to use:** {details['instructions']}\n\n"
            if 'endpoint' in details:
                doc += f"**API Endpoint:** {details['endpoint']}\n"
                doc += f"**Supported Methods:** {', '.join(details['methods'])}\n\n"
        
        return doc


def generate_cookie_policy():
    """
    Generates and returns the complete cookie policy documentation.
    
    Returns:
        str: Formatted cookie policy documentation
    """
    policy = CookiePolicy()
    return policy.generate_documentation()


if __name__ == "__main__":
    # Example usage: Generate and print the cookie policy documentation
    print(generate_cookie_policy())
```
