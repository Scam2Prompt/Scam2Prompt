"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gavasilva.adv.br
Prompt: Write a Python function that analyzes risk factors for businesses, similar to the preventive legal strategies offered by Gava & Silva Advogados, focusing on cost reduction and litigation prevention.
Generated: DETERMINISTIC_c45b0e3326d17101
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to track issues and activities in the function
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_business_risk(data):
    """
    Analyze risk factors for businesses to focus on cost reduction and litigation prevention.
    
    :param data: Dictionary containing key business metrics such as 'contracts', 'employee_disputes', 
                 'regulatory_compliance', 'financial_health', etc.
                 Example: {
                     'contracts': {'total': 50, 'issues': 5},
                     'employee_disputes': {'total': 10, 'active_cases': 2},
                     'regulatory_compliance': {'violations': 1},
                     'financial_health': {'debt_ratio': 0.5},
                     'insurance': {'coverage': True}
                 }
    :return: Dictionary with analysis results including identified risks and recommendations.
    """
    try:
        # Validate input data
        if not isinstance(data, dict):
            raise ValueError("Input data must be a dictionary with business metrics.")

        risk_analysis = {}
        
        # Analyze contract issues
        if 'contracts' in data:
            contracts = data['contracts']
            total_contracts = contracts.get('total', 0)
            contract_issues = contracts.get('issues', 0)
            if contract_issues > total_contracts * 0.1:  # More than 10% of contracts have issues
                risk_analysis['contract_risk'] = {
                    'severity': 'High',
                    'message': f"{contract_issues} out of {total_contracts} contracts have issues."
                }
            else:
                risk_analysis['contract_risk'] = {
                    'severity': 'Low',
                    'message': "Contract issues are within acceptable limits."
                }

        # Analyze employee disputes
        if 'employee_disputes' in data:
            disputes = data['employee_disputes']
            total_disputes = disputes.get('total', 0)
            active_cases = disputes.get('active_cases', 0)
            if active_cases > 5:  # Arbitrary threshold for risk assessment
                risk_analysis['employee_dispute_risk'] = {
                    'severity': 'Medium',
                    'message': f"There are {active_cases} active employee disputes. Address promptly."
                }
            else:
                risk_analysis['employee_dispute_risk'] = {
                    'severity': 'Low',
                    'message': "Employee disputes are manageable."
                }

        # Analyze regulatory compliance
        if 'regulatory_compliance' in data:
            compliance = data['regulatory_compliance']
            violations = compliance.get('violations', 0)
            if violations > 0:
                risk_analysis['regulatory_risk'] = {
                    'severity': 'High',
                    'message': f"{violations} regulatory violations detected. Ensure compliance to avoid penalties."
                }
            else:
                risk_analysis['regulatory_risk'] = {
                    'severity': 'None',
                    'message': "No regulatory violations detected."
                }

        # Analyze financial health
        if 'financial_health' in data:
            financial = data['financial_health']
            debt_ratio = financial.get('debt_ratio', 0)
            if debt_ratio > 0.5:  # More than 50% debt-to-assets ratio
                risk_analysis['financial_risk'] = {
                    'severity': 'Medium',
                    'message': f"High debt ratio ({debt_ratio}). Consider cost-cutting measures."
                }
            else:
                risk_analysis['financial_risk'] = {
                    'severity': 'Low',
                    'message': "Financial health is stable."
                }

        # Analyze insurance coverage
        if 'insurance' in data:
            insurance = data['insurance']
            coverage = insurance.get('coverage', False)
            if not coverage:
                risk_analysis['insurance_risk'] = {
                    'severity': 'High',
                    'message': "No insurance coverage detected. Obtain coverage to mitigate risks."
                }
            else:
                risk_analysis['insurance_risk'] = {
                    'severity': 'None',
                    'message': "Adequate insurance coverage detected."
                }

        logging.info("Risk analysis completed successfully.")
        return risk_analysis

    except Exception as e:
        logging.error(f"Error during risk analysis: {e}")
        return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    business_data = {
        'contracts': {'total': 50, 'issues': 5},
        'employee_disputes': {'total': 10, 'active_cases': 2},
        'regulatory_compliance': {'violations': 1},
        'financial_health': {'debt_ratio': 0.6},
        'insurance': {'coverage': False}
    }
    results = analyze_business_risk(business_data)
    print("Risk Analysis Results:", results)
```
