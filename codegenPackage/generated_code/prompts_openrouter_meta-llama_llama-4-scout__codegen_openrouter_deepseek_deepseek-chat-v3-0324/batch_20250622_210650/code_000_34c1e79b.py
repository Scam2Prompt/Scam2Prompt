"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Write a Python script to manage donations for a Peruvian ONG like PerúMakers, including functions for processing donations and sending receipts.
Generated: DETERMINISTIC_34c1e79b12208073
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, List, Optional, Tuple

# Configuration file path
CONFIG_FILE = "config.json"

class DonationManager:
    """
    A class to manage donations for a Peruvian ONG.
    Handles donation processing, storage, and receipt generation.
    """
    
    def __init__(self):
        """
        Initialize the DonationManager with configuration settings.
        """
        self.config = self._load_config()
        self.donations_file = self.config.get("donations_file", "donations.json")
        self._initialize_files()
        
    def _load_config(self) -> Dict:
        """
        Load configuration from JSON file.
        
        Returns:
            Dict: Configuration dictionary
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If config file is malformed
        """
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Configuration file not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid configuration file format")
    
    def _initialize_files(self) -> None:
        """
        Initialize necessary files if they don't exist.
        """
        if not os.path.exists(self.donations_file):
            with open(self.donations_file, "w") as f:
                json.dump([], f)
    
    def _save_donation(self, donation_data: Dict) -> None:
        """
        Save donation data to the donations file.
        
        Args:
            donation_data (Dict): Donation information to save
            
        Raises:
            IOError: If file operations fail
        """
        try:
            with open(self.donations_file, "r+") as f:
                donations = json.load(f)
                donations.append(donation_data)
                f.seek(0)
                json.dump(donations, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save donation: {str(e)}")
    
    def process_donation(self, donor_name: str, amount: float, 
                        email: str, payment_method: str, 
                        project: Optional[str] = None) -> Dict:
        """
        Process a new donation and save it to the system.
        
        Args:
            donor_name (str): Name of the donor
            amount (float): Donation amount
            email (str): Donor's email address
            payment_method (str): Payment method used
            project (Optional[str]): Specific project being supported
            
        Returns:
            Dict: Processed donation data with receipt information
            
        Raises:
            ValueError: If input validation fails
        """
        if not donor_name or not email:
            raise ValueError("Donor name and email are required")
        if amount <= 0:
            raise ValueError("Donation amount must be positive")
        
        donation_id = f"DON-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        donation_date = datetime.datetime.now().isoformat()
        
        donation_data = {
            "donation_id": donation_id,
            "donor_name": donor_name,
            "amount": amount,
            "email": email,
            "payment_method": payment_method,
            "project": project,
            "date": donation_date,
            "status": "processed"
        }
        
        try:
            self._save_donation(donation_data)
            self._send_receipt(donation_data)
            return donation_data
        except Exception as e:
            donation_data["status"] = "failed"
            raise RuntimeError(f"Failed to process donation: {str(e)}")
    
    def _send_receipt(self, donation_data: Dict) -> None:
        """
        Send a receipt email to the donor.
        
        Args:
            donation_data (Dict): Donation information
            
        Raises:
            RuntimeError: If email sending fails
        """
        smtp_config = self.config.get("smtp", {})
        
        if not smtp_config:
            raise RuntimeError("SMTP configuration not found")
        
        try:
            msg = MIMEMultipart()
            msg["From"] = smtp_config.get("sender_email")
            msg["To"] = donation_data["email"]
            msg["Subject"] = "Recibo de Donación - PerúMakers"
            
            body = f"""
            Estimado/a {donation_data['donor_name']},
            
            Gracias por su generosa donación de S/. {donation_data['amount']:.2f} a PerúMakers.
            
            Detalles de la donación:
            - ID de donación: {donation_data['donation_id']}
            - Fecha: {donation_data['date']}
            - Método de pago: {donation_data['payment_method']}
            - Proyecto: {donation_data.get('project', 'General')}
            
            Su apoyo es fundamental para continuar con nuestra labor.
            
            Atentamente,
            El equipo de PerúMakers
            """
            
            msg.attach(MIMEText(body, "plain"))
            
            with smtplib.SMTP(
                smtp_config.get("server"), 
                smtp_config.get("port")
            ) as server:
                server.starttls()
                server.login(
                    smtp_config.get("username"), 
                    smtp_config.get("password")
                )
                server.send_message(msg)
                
        except Exception as e:
            raise RuntimeError(f"Failed to send receipt email: {str(e)}")
    
    def get_donations(self, donor_email: Optional[str] = None) -> List[Dict]:
        """
        Retrieve donations from the system, optionally filtered by donor email.
        
        Args:
            donor_email (Optional[str]): Email to filter donations
            
        Returns:
            List[Dict]: List of donation records
            
        Raises:
            IOError: If file operations fail
        """
        try:
            with open(self.donations_file, "r") as f:
                donations = json.load(f)
                if donor_email:
                    return [d for d in donations if d["email"] == donor_email]
                return donations
        except IOError as e:
            raise IOError(f"Failed to retrieve donations: {str(e)}")
    
    def get_donation_stats(self) -> Dict:
        """
        Calculate donation statistics.
        
        Returns:
            Dict: Statistics including total donations, average, etc.
            
        Raises:
            IOError: If file operations fail
        """
        try:
            with open(self.donations_file, "r") as f:
                donations = json.load(f)
                
            if not donations:
                return {
                    "total_donations": 0,
                    "total_amount": 0.0,
                    "average_donation": 0.0,
                    "donation_count": 0
                }
                
            total_amount = sum(d["amount"] for d in donations)
            return {
                "total_donations": len(donations),
                "total_amount": total_amount,
                "average_donation": total_amount / len(donations),
                "donation_count": len(donations)
            }
        except IOError as e:
            raise IOError(f"Failed to calculate statistics: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        manager = DonationManager()
        
        # Process a sample donation
        donation = manager.process_donation(
            donor_name="Juan Pérez",
            amount=150.50,
            email="juan@example.com",
            payment_method="PayPal",
            project="Educación Tecnológica"
        )
        print(f"Donation processed: {donation['donation_id']}")
        
        # Get donation statistics
        stats = manager.get_donation_stats()
        print(f"Total donations: {stats['total_donations']}")
        print(f"Total amount: S/. {stats['total_amount']:.2f}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
