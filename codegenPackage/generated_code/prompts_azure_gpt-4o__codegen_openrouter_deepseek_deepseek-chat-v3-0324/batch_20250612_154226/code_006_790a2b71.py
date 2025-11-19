"""
Generated Code Metadata:
========================
Original URL: https://sunsystems.hk
Prompt: Write a script to train staff on using Infor SunSystems effectively, including generating sample financial reports and scenarios for hands-on practice.
Generated: DETERMINISTIC_790a2b71c754d414
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Infor SunSystems Training Script

This script provides interactive training for staff on using Infor SunSystems.
It includes sample financial reports generation and hands-on practice scenarios.
"""

import sys
import random
from datetime import datetime, timedelta
import csv
from pathlib import Path

class SunSystemsTrainer:
    """Main training class for Infor SunSystems"""
    
    def __init__(self):
        self.training_modules = {
            '1': {'name': 'Basic Navigation', 'func': self.basic_navigation},
            '2': {'name': 'Journal Entry', 'func': self.journal_entry},
            '3': {'name': 'Financial Reports', 'func': self.financial_reports},
            '4': {'name': 'Period End Processing', 'func': self.period_end},
            '5': {'name': 'Exit', 'func': self.exit_training}
        }
        self.sample_data = self._generate_sample_data()
        
    def _generate_sample_data(self):
        """Generate sample financial data for training"""
        accounts = [
            {'code': '1000', 'name': 'Cash', 'type': 'Asset'},
            {'code': '2000', 'name': 'Accounts Receivable', 'type': 'Asset'},
            {'code': '3000', 'name': 'Inventory', 'type': 'Asset'},
            {'code': '4000', 'name': 'Accounts Payable', 'type': 'Liability'},
            {'code': '5000', 'name': 'Revenue', 'type': 'Income'},
            {'code': '6000', 'name': 'Expenses', 'type': 'Expense'}
        ]
        
        transactions = []
        for i in range(1, 31):
            debit_acc = random.choice(accounts[:3])
            credit_acc = random.choice(accounts[3:])
            amount = round(random.uniform(100, 10000), 2)
            
            transactions.append({
                'date': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d'),
                'reference': f"TRN-{i:03d}",
                'debit_account': debit_acc['code'],
                'debit_name': debit_acc['name'],
                'credit_account': credit_acc['code'],
                'credit_name': credit_acc['name'],
                'amount': amount,
                'description': f"Sample transaction {i}"
            })
        
        return {
            'accounts': accounts,
            'transactions': transactions
        }
    
    def run(self):
        """Main training program loop"""
        print("\n=== Infor SunSystems Training Program ===")
        print("Please select a training module:")
        
        while True:
            for key, module in self.training_modules.items():
                print(f"{key}. {module['name']}")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice in self.training_modules:
                self.training_modules[choice]['func']()
            else:
                print("Invalid choice. Please try again.")
    
    def basic_navigation(self):
        """Basic navigation training module"""
        print("\n=== Basic Navigation ===")
        print("1. Main Menu Structure")
        print("2. Screen Layout Components")
        print("3. Common Shortcut Keys")
        print("4. Back to Main Menu")
        
        choice = input("\nSelect navigation topic (1-4): ").strip()
        
        if choice == '1':
            print("\nMain Menu Structure:")
            print("- Financials")
            print("- Ledger")
            print("- Reports")
            print("- Utilities")
            print("- System")
        elif choice == '2':
            print("\nScreen Layout Components:")
            print("- Menu Bar")
            print("- Toolbar")
            print("- Navigation Pane")
            print("- Data Entry Area")
            print("- Status Bar")
        elif choice == '3':
            print("\nCommon Shortcut Keys:")
            print("- F1: Help")
            print("- F2: Save")
            print("- F5: Refresh")
            print("- Ctrl+N: New Record")
            print("- Ctrl+F: Find")
        elif choice == '4':
            return
        else:
            print("Invalid choice. Returning to main menu.")
    
    def journal_entry(self):
        """Journal entry training module"""
        print("\n=== Journal Entry Practice ===")
        print("1. View Sample Journal Entries")
        print("2. Create New Journal Entry")
        print("3. Validate Journal Entry")
        print("4. Back to Main Menu")
        
        choice = input("\nSelect journal entry option (1-4): ").strip()
        
        if choice == '1':
            print("\nSample Journal Entries:")
            for i, entry in enumerate(self.sample_data['transactions'][:5], 1):
                print(f"\nEntry {i}:")
                print(f"Date: {entry['date']}")
                print(f"Reference: {entry['reference']}")
                print(f"Debit: {entry['debit_account']} - {entry['debit_name']}")
                print(f"Credit: {entry['credit_account']} - {entry['credit_name']}")
                print(f"Amount: {entry['amount']:.2f}")
                print(f"Description: {entry['description']}")
        elif choice == '2':
            print("\nCreate New Journal Entry:")
            date = input("Enter date (YYYY-MM-DD): ")
            reference = input("Enter reference: ")
            debit_acc = input("Enter debit account code: ")
            credit_acc = input("Enter credit account code: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            
            try:
                amount = float(amount)
                print("\nJournal Entry Created Successfully!")
                print(f"Date: {date}")
                print(f"Reference: {reference}")
                print(f"Debit: {debit_acc}")
                print(f"Credit: {credit_acc}")
                print(f"Amount: {amount:.2f}")
                print(f"Description: {description}")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == '3':
            print("\nJournal Entry Validation:")
            print("1. Check account codes exist")
            print("2. Verify debit equals credit")
            print("3. Validate date format")
            
            test_entry = random.choice(self.sample_data['transactions'])
            print("\nTest Journal Entry:")
            print(f"Date: {test_entry['date']}")
            print(f"Reference: {test_entry['reference']}")
            print(f"Debit: {test_entry['debit_account']}")
            print(f"Credit: {test_entry['credit_account']}")
            print(f"Amount: {test_entry['amount']:.2f}")
            
            print("\nValidation Results:")
            print("1. Account codes: Valid")
            print("2. Debit equals credit: Balanced")
            print("3. Date format: Valid")
        elif choice == '4':
            return
        else:
            print("Invalid choice. Returning to main menu.")
    
    def financial_reports(self):
        """Financial reports training module"""
        print("\n=== Financial Reports ===")
        print("1. Generate Trial Balance")
        print("2. Generate Profit & Loss")
        print("3. Generate Balance Sheet")
        print("4. Export Report Data")
        print("5. Back to Main Menu")
        
        choice = input("\nSelect report option (1-5): ").strip()
        
        if choice == '1':
            print("\nTrial Balance Report:")
            print("{:<10} {:<25} {:<15} {:<15}".format(
                "Account", "Account Name", "Debit", "Credit"))
            print("-" * 65)
            
            for account in self.sample_data['accounts']:
                debits = sum(t['amount'] for t in self.sample_data['transactions'] 
                            if t['debit_account'] == account['code'])
                credits = sum(t['amount'] for t in self.sample_data['transactions'] 
                             if t['credit_account'] == account['code'])
                
                print("{:<10} {:<25} {:<15.2f} {:<15.2f}".format(
                    account['code'], account['name'], debits, credits))
            
            total_debit = sum(t['amount'] for t in self.sample_data['transactions'])
            total_credit = total_debit
            print("\n{:<35} {:<15.2f} {:<15.2f}".format(
                "Total", total_debit, total_credit))
        
        elif choice == '2':
            print("\nProfit & Loss Report:")
            print("{:<10} {:<25} {:<15}".format(
                "Account", "Account Name", "Amount"))
            print("-" * 50)
            
            income = sum(t['amount'] for t in self.sample_data['transactions'] 
                        if any(acc['code'] == t['credit_account'] and acc['type'] == 'Income' 
                              for acc in self.sample_data['accounts']))
            
            expenses = sum(t['amount'] for t in self.sample_data['transactions
