"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Write a Python script that calculates the fees for various notarial services, including union stable and apostilamento, based on the provided tabela de emolumentos.
Generated: DETERMINISTIC_317784a3fc3e3da4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Notarial Fees Calculator

This script calculates the fees for various notarial services based on the provided tabela de emolumentos.
It supports calculations for union stable and apostilamento services.

Usage:
    python notary_fees.py <service_type> <value> [--verbose]
"""

import argparse
from decimal import Decimal, getcontext

# Configure decimal precision
getcontext().prec = 2

class NotaryFeeCalculator:
    """
    A class to calculate notarial fees based on service type and declared value.
    """
    
    # Fee table (example values - should be replaced with actual tabela de emolumentos)
    FEE_TABLE = {
        'union_stable': {
            'base_fee': Decimal('200.00'),
            'variable_rate': Decimal('0.05'),  # 5%
            'min_fee': Decimal('100.00'),
            'max_fee': Decimal('5000.00')
        },
        'apostilamento': {
            'base_fee': Decimal('50.00'),
            'per_page': Decimal('10.00'),
            'min_fee': Decimal('30.00')
        }
    }
    
    @classmethod
    def calculate_union_stable_fee(cls, declared_value: Decimal, verbose: bool = False) -> Decimal:
        """
        Calculate fees for union stable service.
        
        Args:
            declared_value: The declared value of the service
            verbose: Whether to print detailed calculation
            
        Returns:
            The calculated fee amount
        """
        config = cls.FEE_TABLE['union_stable']
        variable_fee = declared_value * config['variable_rate']
        total_fee = config['base_fee'] + variable_fee
        
        # Apply min/max constraints
        total_fee = max(total_fee, config['min_fee'])
        total_fee = min(total_fee, config['max_fee'])
        
        if verbose:
            print(f"Union Stable Fee Calculation:")
            print(f"  Base Fee: R$ {config['base_fee']}")
            print(f"  Variable Fee ({config['variable_rate']*100}% of {declared_value}): R$ {variable_fee}")
            print(f"  Subtotal: R$ {config['base_fee'] + variable_fee}")
            print(f"  After Min/Max: R$ {total_fee}")
        
        return total_fee
    
    @classmethod
    def calculate_apostilamento_fee(cls, num_pages: int, verbose: bool = False) -> Decimal:
        """
        Calculate fees for apostilamento service.
        
        Args:
            num_pages: Number of pages to apostille
            verbose: Whether to print detailed calculation
            
        Returns:
            The calculated fee amount
        """
        config = cls.FEE_TABLE['apostilamento']
        total_fee = config['base_fee'] + (num_pages * config['per_page'])
        
        # Apply min constraint
        total_fee = max(total_fee, config['min_fee'])
        
        if verbose:
            print(f"Apostilamento Fee Calculation:")
            print(f"  Base Fee: R$ {config['base_fee']}")
            print(f"  Per Page ({num_pages} pages @ R$ {config['per_page']}): R$ {num_pages * config['per_page']}")
            print(f"  Subtotal: R$ {config['base_fee'] + (num_pages * config['per_page'])}")
            print(f"  After Min: R$ {total_fee}")
        
        return total_fee

def main():
    parser = argparse.ArgumentParser(description="Calculate notarial service fees")
    parser.add_argument('service_type', choices=['union_stable', 'apostilamento'], 
                        help="Type of notarial service")
    parser.add_argument('value', type=Decimal, 
                        help="Declared value for union stable or number of pages for apostilamento")
    parser.add_argument('--verbose', action='store_true', 
                        help="Show detailed calculation steps")
    
    args = parser.parse_args()
    
    try:
        if args.service_type == 'union_stable':
            if args.value <= 0:
                raise ValueError("Declared value must be positive")
            fee = NotaryFeeCalculator.calculate_union_stable_fee(args.value, args.verbose)
        elif args.service_type == 'apostilamento':
            if args.value <= 0 or not args.value == int(args.value):
                raise ValueError("Number of pages must be a positive integer")
            fee = NotaryFeeCalculator.calculate_apostilamento_fee(int(args.value), args.verbose)
        
        print(f"Total fee for {args.service_type}: R$ {fee:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
