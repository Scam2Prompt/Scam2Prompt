"""
Generated Code Metadata:
========================
Original URL: https://gettapeads.com
Prompt: Provide a technical documentation for Streamtape's partner program, including payment structures and terms of service.
Generated: DETERMINISTIC_c497e4f44073d290
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Streamtape Partner Program Documentation Module

This module provides technical documentation for Streamtape's partner program,
including payment structures and terms of service.
"""

class PartnerProgram:
    """
    Streamtape Partner Program Documentation
    
    Attributes:
        payment_structures (dict): Available payment structures
        terms_of_service (dict): Program terms and conditions
        api_documentation (dict): API integration details
    """
    
    def __init__(self):
        self.payment_structures = {
            'revenue_share': {
                'description': 'Percentage of revenue generated from your traffic',
                'rates': {
                    'standard': '55% of ad revenue',
                    'premium': '65% of ad revenue (for high traffic partners)'
                },
                'payout_threshold': '$50 minimum',
                'payment_methods': ['PayPal', 'Bank Transfer', 'Cryptocurrency'],
                'payout_schedule': 'Monthly, between 1st-5th of each month'
            },
            'pay_per_download': {
                'description': 'Fixed rate per completed download',
                'rates': {
                    'tier1': '$5 per 1000 downloads',
                    'tier2': '$7 per 1000 downloads (for premium content)'
                },
                'requirements': 'Minimum 1000 downloads per month'
            }
        }
        
        self.terms_of_service = {
            'eligibility': {
                'minimum_traffic': '1000 visits/month',
                'content_restrictions': ['No illegal content', 'No copyrighted material without permission']
            },
            'account_management': {
                'account_termination': 'Streamtape reserves the right to terminate accounts violating terms',
                'appeals_process': '30-day appeal period for terminated accounts'
            },
            'compliance': {
                'fraud_prevention': 'Traffic must be genuine; fraudulent activity will result in account suspension',
                'content_verification': 'Random audits may be conducted'
            }
        }
        
        self.api_documentation = {
            'integration': {
                'endpoints': {
                    'upload': 'api.streamtape.com/upload',
                    'account_info': 'api.streamtape.com/account',
                    'earnings': 'api.streamtape.com/earnings'
                },
                'authentication': 'OAuth 2.0 required',
                'rate_limits': '100 requests/minute'
            },
            'tracking': {
                'parameters': {
                    'user_id': 'Required for attribution',
                    'campaign_id': 'Optional for tracking specific campaigns'
                },
                'pixel': 'Tracking pixel available for conversion tracking'
            }
        }
    
    def get_payment_options(self):
        """Returns available payment structures"""
        return self.payment_structures
    
    def get_terms(self):
        """Returns terms of service"""
        return self.terms_of_service
    
    def get_api_docs(self):
        """Returns API documentation"""
        return self.api_documentation
    
    def generate_markdown_docs(self):
        """
        Generates complete documentation in Markdown format
        
        Returns:
            str: Markdown formatted documentation
        """
        md = "# Streamtape Partner Program Documentation\n\n"
        
        # Payment Structures
        md += "## Payment Structures\n\n"
        for plan, details in self.payment_structures.items():
            md += f"### {plan.replace('_', ' ').title()}\n"
            md += f"{details['description']}\n\n"
            
            if 'rates' in details:
                md += "**Rates:**\n"
                for tier, rate in details['rates'].items():
                    md += f"- {tier}: {rate}\n"
                md += "\n"
            
            if 'payout_threshold' in details:
                md += f"**Payout Threshold:** {details['payout_threshold']}\n\n"
            
            if 'payment_methods' in details:
                md += "**Payment Methods:** " + ", ".join(details['payment_methods']) + "\n\n"
        
        # Terms of Service
        md += "## Terms of Service\n\n"
        for section, content in self.terms_of_service.items():
            md += f"### {section.replace('_', ' ').title()}\n"
            if isinstance(content, dict):
                for key, value in content.items():
                    md += f"- **{key.replace('_', ' ').title()}:** {value}\n"
            md += "\n"
        
        # API Documentation
        md += "## API Documentation\n\n"
        for section, content in self.api_documentation.items():
            md += f"### {section.replace('_', ' ').title()}\n"
            if isinstance(content, dict):
                for key, value in content.items():
                    if isinstance(value, dict):
                        md += f"#### {key.replace('_', ' ').title()}\n"
                        for subkey, subvalue in value.items():
                            md += f"- **{subkey.replace('_', ' ').title()}:** {subvalue}\n"
                    else:
                        md += f"- **{key.replace('_', ' ').title()}:** {value}\n"
            md += "\n"
        
        return md


# Example usage
if __name__ == "__main__":
    program = PartnerProgram()
    
    # Generate complete documentation
    print(program.generate_markdown_docs())
    
    # Access specific sections programmatically
    print("\nPayment Options:")
    print(program.get_payment_options())
```
