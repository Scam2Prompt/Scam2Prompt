"""
Generated Code Metadata:
========================
Original URL: https://masitsolutions.net
Prompt: "Provide an example of a technical support outsourcing agreement for a company with a global presence."
Generated: DETERMINISTIC_218fa1aafd1e0351
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Technical Support Outsourcing Agreement Template
This document outlines the terms between a company and an outsourcing provider for technical support services.
"""

class TechnicalSupportOutsourcingAgreement:
    """
    A template for a technical support outsourcing agreement.
    """
    
    def __init__(self, client_name, provider_name, effective_date, term_length):
        """
        Initialize the agreement with basic information.
        
        Args:
            client_name (str): Name of the client company
            provider_name (str): Name of the service provider
            effective_date (str): Date when agreement becomes effective (YYYY-MM-DD)
            term_length (int): Length of agreement in months
        """
        self.client_name = client_name
        self.provider_name = provider_name
        self.effective_date = effective_date
        self.term_length = term_length
        self.service_level_agreements = {}
        self.termination_terms = {}
        self.confidentiality_terms = {}
        self.payment_terms = {}
        self.service_scope = {}
        
    def add_service_level_agreement(self, metric, target, measurement_period):
        """
        Add a service level agreement metric.
        
        Args:
            metric (str): Name of the metric (e.g., "Response Time")
            target (str): Target value (e.g., "99.9% uptime")
            measurement_period (str): How often measured (e.g., "monthly")
        """
        self.service_level_agreements[metric] = {
            'target': target,
            'measurement_period': measurement_period
        }
    
    def set_termination_terms(self, notice_period, termination_fee):
        """
        Set termination terms for the agreement.
        
        Args:
            notice_period (str): Required notice period (e.g., "60 days")
            termination_fee (str): Fee for early termination if applicable
        """
        self.termination_terms = {
            'notice_period': notice_period,
            'termination_fee': termination_fee
        }
    
    def set_confidentiality_terms(self, duration, obligations):
        """
        Set confidentiality terms.
        
        Args:
            duration (str): How long confidentiality lasts (e.g., "5 years")
            obligations (str): Description of confidentiality obligations
        """
        self.confidentiality_terms = {
            'duration': duration,
            'obligations': obligations
        }
    
    def set_payment_terms(self, fee_structure, payment_schedule, currency):
        """
        Set payment terms for the services.
        
        Args:
            fee_structure (str): Description of fee structure
            payment_schedule (str): When payments are due
            currency (str): Currency for payments (e.g., "USD")
        """
        self.payment_terms = {
            'fee_structure': fee_structure,
            'payment_schedule': payment_schedule,
            'currency': currency
        }
    
    def set_service_scope(self, languages, time_zones, channels):
        """
        Set the scope of services for global support.
        
        Args:
            languages (list): List of supported languages
            time_zones (list): List of supported time zones
            channels (list): List of support channels (e.g., ["email", "phone", "chat"])
        """
        self.service_scope = {
            'languages': languages,
            'time_zones': time_zones,
            'channels': channels
        }
    
    def generate_agreement(self):
        """
        Generate the complete agreement document.
        
        Returns:
            dict: Complete agreement document structure
        """
        return {
            'parties': {
                'client': self.client_name,
                'provider': self.provider_name
            },
            'effective_date': self.effective_date,
            'term_length': f"{self.term_length} months",
            'service_level_agreements': self.service_level_agreements,
            'termination_terms': self.termination_terms,
            'confidentiality_terms': self.confidentiality_terms,
            'payment_terms': self.payment_terms,
            'service_scope': self.service_scope
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a new agreement
        agreement = TechnicalSupportOutsourcingAgreement(
            client_name="GlobalTech Inc.",
            provider_name="SupportPro Worldwide",
            effective_date="2023-01-01",
            term_length=24
        )
        
        # Add SLAs
        agreement.add_service_level_agreement(
            metric="First Response Time",
            target="Within 2 hours",
            measurement_period="per ticket"
        )
        agreement.add_service_level_agreement(
            metric="Resolution Time",
            target="Within 24 hours for Priority 1",
            measurement_period="per ticket"
        )
        
        # Set other terms
        agreement.set_termination_terms(
            notice_period="90 days",
            termination_fee="Equivalent to 3 months of service fees"
        )
        
        agreement.set_confidentiality_terms(
            duration="3 years post-termination",
            obligations="All client data must be kept confidential"
        )
        
        agreement.set_payment_terms(
            fee_structure="Monthly fixed fee plus per-ticket charges",
            payment_schedule="Net 30 days",
            currency="USD"
        )
        
        agreement.set_service_scope(
            languages=["English", "Spanish", "French", "German", "Japanese"],
            time_zones=["EST", "CET", "JST", "AEST"],
            channels=["email", "phone", "chat", "ticketing system"]
        )
        
        # Generate the final agreement
        final_agreement = agreement.generate_agreement()
        
        # Print the agreement (in production would save to file/database)
        import json
        print(json.dumps(final_agreement, indent=2))
        
    except Exception as e:
        print(f"Error generating agreement: {str(e)}")
```
