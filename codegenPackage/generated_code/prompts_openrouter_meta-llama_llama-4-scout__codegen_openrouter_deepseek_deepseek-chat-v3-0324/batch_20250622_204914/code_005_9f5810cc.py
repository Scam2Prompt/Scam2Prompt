"""
Generated Code Metadata:
========================
Original URL: https://clientfuel.digital
Prompt: "Develop a client re-engagement strategy using email follow-ups and tailored deals for a pet grooming business."
Generated: DETERMINISTIC_9f5810cc721eeb9f
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import json
import random
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Customer:
    def __init__(self, customer_id: str, name: str, email: str, last_visit: str, 
                 pet_type: str, services_used: List[str], frequency: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.last_visit = datetime.strptime(last_visit, "%Y-%m-%d")
        self.pet_type = pet_type
        self.services_used = services_used
        self.frequency = frequency

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        try:
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = recipient
            message["Subject"] = subject
            message.attach(MIMEText(body, "html"))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logger.info(f"Email sent to {recipient}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {str(e)}")
            return False

class DealGenerator:
    def __init__(self, deals_config: Dict):
        self.deals_config = deals_config

    def generate_deal(self, customer: Customer) -> str:
        pet_type = customer.pet_type.lower()
        services = customer.services_used
        
        # Base discount
        discount = random.randint(10, 25)
        
        # Add extra discount for preferred services
        preferred_services = self.deals_config.get("preferred_services", {}).get(pet_type, [])
        if any(service in services for service in preferred_services):
            discount += 5
        
        # Special deal for infrequent customers
        if customer.frequency.lower() == "infrequent":
            discount += 5
        
        # Cap discount at 30%
        discount = min(discount, 30)
        
        return f"{discount}% off your next grooming service!"

class ReEngagementStrategy:
    def __init__(self, email_sender: EmailSender, deal_generator: DealGenerator):
        self.email_sender = email_sender
        self.deal_generator = deal_generator

    def _get_email_template(self, customer: Customer, deal: str) -> str:
        return f"""
        <html>
            <body>
                <h2>Hi {customer.name}, we miss you and your {customer.pet_type}!</h2>
                <p>It's been a while since your last visit on {customer.last_visit.strftime('%B %d, %Y')}.</p>
                <p>As a special treat, here's an exclusive offer just for you:</p>
                <h3>{deal}</h3>
                <p>Book your appointment today to take advantage of this limited-time offer!</p>
                <p>Best regards,<br>The Pet Grooming Team</p>
            </body>
        </html>
        """

    def execute_strategy(self, customers: List[Customer]) -> Dict[str, bool]:
        results = {}
        for customer in customers:
            days_since_last_visit = (datetime.now() - customer.last_visit).days
            
            # Only engage customers who haven't visited in over 60 days
            if days_since_last_visit > 60:
                deal = self.deal_generator.generate_deal(customer)
                email_body = self._get_email_template(customer, deal)
                subject = f"Special Offer for {customer.name} and Their {customer.pet_type}"
                
                success = self.email_sender.send_email(
                    customer.email,
                    subject,
                    email_body
                )
                results[customer.customer_id] = success
        
        return results

def load_customers_from_json(file_path: str) -> List[Customer]:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [
                Customer(
                    customer_id=c["id"],
                    name=c["name"],
                    email=c["email"],
                    last_visit=c["last_visit"],
                    pet_type=c["pet_type"],
                    services_used=c["services_used"],
                    frequency=c["frequency"]
                ) for c in data["customers"]
            ]
    except Exception as e:
        logger.error(f"Error loading customer data: {str(e)}")
        return []

def main():
    # Configuration
    config = {
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "sender_email": "your_email@example.com",
        "sender_password": "your_password",
        "deals_config": {
            "preferred_services": {
                "dog": ["full grooming", "nail trimming"],
                "cat": ["bath", "brushing"]
            }
        },
        "customers_file": "customers.json"
    }

    # Initialize components
    email_sender = EmailSender(
        config["smtp_server"],
        config["smtp_port"],
        config["sender_email"],
        config["sender_password"]
    )
    
    deal_generator = DealGenerator(config["deals_config"])
    strategy = ReEngagementStrategy(email_sender, deal_generator)
    
    # Load customers and execute strategy
    customers = load_customers_from_json(config["customers_file"])
    if customers:
        results = strategy.execute_strategy(customers)
        logger.info(f"Re-engagement campaign completed. Results: {results}")
    else:
        logger.error("No customers loaded. Campaign aborted.")

if __name__ == "__main__":
    main()
```
