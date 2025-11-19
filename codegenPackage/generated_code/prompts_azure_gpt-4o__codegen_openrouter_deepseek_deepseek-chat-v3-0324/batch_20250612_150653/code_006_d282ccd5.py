"""
Generated Code Metadata:
========================
Original URL: https://reckonmexico.com
Prompt: Create a script to automate the preparation of tax declarations, leveraging the compliance guidelines from Reckon Business Consulting's fiscal consulting services.
Generated: DETERMINISTIC_d282ccd506b98c85
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

# Constants
CONFIG_FILE = "tax_config.json"
OUTPUT_DIR = "tax_declarations"
SUPPORTED_TAX_TYPES = ["income", "gst", "payroll", "capital_gains"]
DEFAULT_CURRENCY = "USD"

class TaxAutomationError(Exception):
    """Custom exception for tax automation errors."""
    pass

def load_config(config_path: str) -> Dict:
    """Load configuration from JSON file.
    
    Args:
        config_path: Path to the configuration file.
    
    Returns:
        Dictionary containing configuration data.
    
    Raises:
        TaxAutomationError: If config file is invalid or missing.
    """
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Validate config
        if not all(key in config for key in ["fiscal_year", "tax_types", "client_info"]):
            raise TaxAutomationError("Invalid configuration: Missing required fields")
        
        return config
    except FileNotFoundError:
        raise TaxAutomationError(f"Config file not found at {config_path}")
    except json.JSONDecodeError:
        raise TaxAutomationError(f"Invalid JSON in config file {config_path}")

def validate_tax_data(tax_data: Dict, tax_type: str) -> bool:
    """Validate tax data against required fields for the tax type.
    
    Args:
        tax_data: Dictionary containing tax data.
        tax_type: Type of tax being processed.
    
    Returns:
        True if data is valid, False otherwise.
    """
    required_fields = {
        "income": ["gross_income", "deductions", "tax_paid"],
        "gst": ["gst_collected", "gst_paid", "gst_credits"],
        "payroll": ["wages", "tax_withheld", "superannuation"],
        "capital_gains": ["asset_name", "purchase_price", "sale_price", "holding_period"]
    }
    
    if tax_type not in required_fields:
        return False
    
    return all(field in tax_data for field in required_fields[tax_type])

def calculate_tax(tax_type: str, tax_data: Dict) -> Dict:
    """Calculate tax based on tax type and data.
    
    Args:
        tax_type: Type of tax being calculated.
        tax_data: Dictionary containing tax data.
    
    Returns:
        Dictionary with calculated tax values.
    
    Raises:
        TaxAutomationError: If tax type is unsupported or data is invalid.
    """
    if not validate_tax_data(tax_data, tax_type):
        raise TaxAutomationError(f"Invalid data for tax type {tax_type}")
    
    calculations = {}
    
    if tax_type == "income":
        taxable_income = tax_data["gross_income"] - tax_data["deductions"]
        calculations = {
            "taxable_income": taxable_income,
            "tax_liability": taxable_income * 0.3,  # Simplified flat rate
            "tax_refund": max(0, tax_data["tax_paid"] - (taxable_income * 0.3))
        }
    elif tax_type == "gst":
        net_gst = tax_data["gst_collected"] - tax_data["gst_paid"]
        calculations = {
            "gst_net": net_gst,
            "gst_credits": tax_data["gst_credits"],
            "gst_payable": max(0, net_gst - tax_data["gst_credits"])
        }
    elif tax_type == "payroll":
        calculations = {
            "net_pay": tax_data["wages"] - tax_data["tax_withheld"],
            "super_liability": tax_data["wages"] * 0.095,  # 9.5% super rate
            "tax_withheld": tax_data["tax_withheld"]
        }
    elif tax_type == "capital_gains":
        gain = tax_data["sale_price"] - tax_data["purchase_price"]
        discount = 0.5 if tax_data["holding_period"] > 365 else 0
        calculations = {
            "capital_gain": gain,
            "discounted_gain": gain * (1 - discount),
            "taxable_amount": gain * (1 - discount)
        }
    
    return calculations

def generate_declaration(
    client_info: Dict,
    tax_type: str,
    tax_data: Dict,
    calculations: Dict,
    fiscal_year: str
) -> Dict:
    """Generate a tax declaration document.
    
    Args:
        client_info: Dictionary containing client information.
        tax_type: Type of tax declaration.
        tax_data: Original tax data.
        calculations: Calculated tax values.
        fiscal_year: Fiscal year for declaration.
    
    Returns:
        Dictionary representing the tax declaration.
    """
    declaration = {
        "declaration_id": f"{client_info['client_id']}-{tax_type}-{datetime.now().strftime('%Y%m%d')}",
        "client_info": client_info,
        "tax_type": tax_type,
        "fiscal_year": fiscal_year,
        "submission_date": datetime.now().isoformat(),
        "currency": DEFAULT_CURRENCY,
        "input_data": tax_data,
        "calculations": calculations,
        "compliance_notes": "Prepared in accordance with Reckon Business Consulting guidelines"
    }
    
    return declaration

def save_declaration(declaration: Dict, output_dir: str) -> str:
    """Save declaration to file.
    
    Args:
        declaration: Dictionary containing declaration data.
        output_dir: Directory to save declaration file.
    
    Returns:
        Path to the saved file.
    
    Raises:
        TaxAutomationError: If output directory cannot be created.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        filename = f"{declaration['declaration_id']}.json"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(declaration, f, indent=2)
        
        return filepath
    except OSError as e:
        raise TaxAutomationError(f"Failed to save declaration: {str(e)}")

def process_tax_declaration(
    config_path: str,
    tax_type: str,
    tax_data: Dict,
    output_dir: Optional[str] = None
) -> str:
    """Main function to process a tax declaration.
    
    Args:
        config_path: Path to configuration file.
        tax_type: Type of tax to process.
        tax_data: Dictionary containing tax data.
        output_dir: Optional custom output directory.
    
    Returns:
        Path to the generated declaration file.
    
    Raises:
        TaxAutomationError: For any processing errors.
    """
    if tax_type not in SUPPORTED_TAX_TYPES:
        raise TaxAutomationError(f"Unsupported tax type: {tax_type}")
    
    try:
        # Load configuration
        config = load_config(config_path)
        
        # Validate tax type is enabled in config
        if tax_type not in config["tax_types"]:
            raise TaxAutomationError(f"Tax type {tax_type} not enabled in configuration")
        
        # Calculate tax
        calculations = calculate_tax(tax_type, tax_data)
        
        # Generate declaration
        declaration = generate_declaration(
            client_info=config["client_info"],
            tax_type=tax_type,
            tax_data=tax_data,
            calculations=calculations,
            fiscal_year=config["fiscal_year"]
        )
        
        # Save declaration
        output_path = output_dir if output_dir else OUTPUT_DIR
        filepath = save_declaration(declaration, output_path)
        
        return filepath
    except Exception as e:
        raise TaxAutomationError(f"Failed to process tax declaration: {str(e)}")

def main():
    """Example usage of the tax automation script."""
    try:
        # Example tax data (in a real scenario, this would come from external source)
        example_tax_data = {
            "gross_income": 100000,
            "deductions": 20000,
            "tax_paid": 25000
        }
        
        # Process income tax declaration
        declaration_path = process_tax_declaration(
            config_path=CONFIG_FILE,
            tax_type="income",
            tax_data=example_tax_data
        )
        
        print(f"Successfully generated tax declaration at: {declaration_path}")
    except TaxAutomationError as e:
        print(f"Error processing tax declaration: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
```
