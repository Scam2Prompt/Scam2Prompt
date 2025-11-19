"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Develop a script to automate property management tasks, including tenant communication and financial reporting, using the streamlined and results-driven approach mentioned by Bebold Properties.
Generated: DETERMINISTIC_e964359f07b280f0
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import csv
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json
from typing import Dict, List, Optional

# Configuration file path
CONFIG_FILE = "config.json"

class PropertyManagementAutomation:
    """
    A class to automate property management tasks including tenant communication and financial reporting.
    """
    
    def __init__(self):
        """
        Initialize the PropertyManagementAutomation with configuration.
        """
        self.config = self._load_config()
        self.smtp_server = self.config.get("smtp_server")
        self.smtp_port = self.config.get("smtp_port")
        self.email = self.config.get("email")
        self.password = self.config.get("password")
        self.tenant_file = self.config.get("tenant_file", "tenants.csv")
        self.transaction_file = self.config.get("transaction_file", "transactions.csv")
        
    def _load_config(self) -> Dict:
        """
        Load configuration from JSON file.
        
        Returns:
            Dict: Configuration dictionary
            
        Raises:
            FileNotFoundError: If config file is not found
            json.JSONDecodeError: If config file is not valid JSON
        """
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {CONFIG_FILE} not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Configuration file {CONFIG_FILE} is not valid JSON.")
    
    def send_email(self, to_email: str, subject: str, body: str) -> bool:
        """
        Send an email to a tenant.
        
        Args:
            to_email (str): Recipient email address
            subject (str): Email subject
            body (str): Email body
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            msg = MIMEMultipart()
            msg["From"] = self.email
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def get_tenants(self) -> List[Dict]:
        """
        Get list of tenants from CSV file.
        
        Returns:
            List[Dict]: List of tenant dictionaries
            
        Raises:
            FileNotFoundError: If tenant file is not found
        """
        tenants = []
        try:
            with open(self.tenant_file, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tenants.append(row)
            return tenants
        except FileNotFoundError:
            raise FileNotFoundError(f"Tenant file {self.tenant_file} not found.")
    
    def get_transactions(self) -> List[Dict]:
        """
        Get list of transactions from CSV file.
        
        Returns:
            List[Dict]: List of transaction dictionaries
            
        Raises:
            FileNotFoundError: If transaction file is not found
        """
        transactions = []
        try:
            with open(self.transaction_file, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transactions.append(row)
            return transactions
        except FileNotFoundError:
            raise FileNotFoundError(f"Transaction file {self.transaction_file} not found.")
    
    def send_rent_reminders(self) -> Dict[str, bool]:
        """
        Send rent payment reminders to all tenants.
        
        Returns:
            Dict[str, bool]: Dictionary mapping tenant emails to success status
        """
        tenants = self.get_tenants()
        results = {}
        
        for tenant in tenants:
            subject = "Rent Payment Reminder"
            body = f"Dear {tenant['name']},\n\nThis is a reminder that your rent of ${tenant['rent']} is due on {tenant['due_date']}.\n\nThank you,\nProperty Management"
            success = self.send_email(tenant["email"], subject, body)
            results[tenant["email"]] = success
        
        return results
    
    def generate_financial_report(self, month: Optional[str] = None, year: Optional[str] = None) -> Dict:
        """
        Generate a financial report for the specified month and year.
        
        Args:
            month (str, optional): Month to filter by (MM format). Defaults to current month.
            year (str, optional): Year to filter by (YYYY format). Defaults to current year.
            
        Returns:
            Dict: Financial report containing total income, expenses, and net profit
        """
        now = datetime.now()
        month = month or now.strftime("%m")
        year = year or now.strftime("%Y")
        
        transactions = self.get_transactions()
        filtered_transactions = [
            t for t in transactions 
            if t["date"].split("-")[0] == year and t["date"].split("-")[1] == month
        ]
        
        report = {
            "month": month,
            "year": year,
            "total_income": 0,
            "total_expenses": 0,
            "net_profit": 0
        }
        
        for t in filtered_transactions:
            amount = float(t["amount"])
            if t["type"] == "income":
                report["total_income"] += amount
            else:
                report["total_expenses"] += amount
        
        report["net_profit"] = report["total_income"] - report["total_expenses"]
        
        return report
    
    def save_report_to_csv(self, report: Dict, filename: str = None) -> bool:
        """
        Save financial report to CSV file.
        
        Args:
            report (Dict): Financial report dictionary
            filename (str, optional): Output filename. Defaults to "financial_report_YYYY-MM.csv"
            
        Returns:
            bool: True if file was saved successfully, False otherwise
        """
        if not filename:
            filename = f"financial_report_{report['year']}-{report['month']}.csv"
        
        try:
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Metric", "Amount"])
                writer.writerow(["Total Income", report["total_income"]])
                writer.writerow(["Total Expenses", report["total_expenses"]])
                writer.writerow(["Net Profit", report["net_profit"]])
            return True
        except Exception as e:
            print(f"Error saving report: {e}")
            return False

def main():
    """
    Main function to demonstrate property management automation.
    """
    try:
        pma = PropertyManagementAutomation()
        
        # Example: Send rent reminders
        print("Sending rent reminders...")
        reminder_results = pma.send_rent_reminders()
        print(f"Reminders sent: {sum(1 for success in reminder_results.values() if success)}/{len(reminder_results)}")
        
        # Example: Generate and save financial report
        print("Generating financial report...")
        report = pma.generate_financial_report()
        print(f"Report for {report['month']}/{report['year']}:")
        print(f"Income: ${report['total_income']:.2f}")
        print(f"Expenses: ${report['total_expenses']:.2f}")
        print(f"Net Profit: ${report['net_profit']:.2f}")
        
        if pma.save_report_to_csv(report):
            print("Report saved successfully.")
        
    except Exception as e:
        print(f"Error in property management automation: {e}")

if __name__ == "__main__":
    main()
```
