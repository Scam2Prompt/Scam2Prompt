"""
Generated Code Metadata:
========================
Original URL: https://salesstudios.com
Prompt: Develop a customized email marketing strategy to increase engagement and conversion rates for an e-commerce business using Sales Studios' services.
Generated: DETERMINISTIC_f8a0b06fe0cd3e8f
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime, timedelta
import pandas as pd
import json
from typing import List, Dict, Optional
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class EmailStrategy(ABC):
    """Abstract base class for email marketing strategies."""
    
    @abstractmethod
    def create_email_content(self, recipient_data: Dict) -> Dict:
        """Create email content based on recipient data."""
        pass
    
    @abstractmethod
    def segment_recipients(self, recipients: List[Dict]) -> Dict[str, List[Dict]]:
        """Segment recipients based on strategy criteria."""
        pass

class AbandonedCartStrategy(EmailStrategy):
    """Strategy for abandoned cart emails."""
    
    def __init__(self, template_path: str):
        with open(template_path) as f:
            self.template = json.load(f)
    
    def create_email_content(self, recipient_data: Dict) -> Dict:
        """Create abandoned cart email content."""
        products = recipient_data.get('abandoned_products', [])
        subject = self.template['subject'].format(
            first_name=recipient_data.get('first_name', 'Customer')
        )
        
        product_list = "\n".join(
            f"<li>{p['name']} - ${p['price']}</li>" 
            for p in products
        )
        
        body = self.template['body'].format(
            first_name=recipient_data.get('first_name', 'Customer'),
            product_list=product_list,
            discount_code=recipient_data.get('discount_code', 'SAVE10')
        )
        
        return {
            'subject': subject,
            'body': body,
            'recipient': recipient_data['email']
        }
    
    def segment_recipients(self, recipients: List[Dict]) -> Dict[str, List[Dict]]:
        """Segment recipients who abandoned carts in last 24 hours."""
        now = datetime.now()
        threshold = now - timedelta(hours=24)
        
        abandoned_carts = [
            r for r in recipients 
            if r.get('last_cart_activity') and 
            datetime.strptime(r['last_cart_activity'], '%Y-%m-%d %H:%M:%S') > threshold
        ]
        
        return {'abandoned_cart': abandoned_carts}

class PersonalizedRecommendationStrategy(EmailStrategy):
    """Strategy for personalized product recommendations."""
    
    def __init__(self, template_path: str, product_catalog: List[Dict]):
        with open(template_path) as f:
            self.template = json.load(f)
        self.product_catalog = product_catalog
    
    def create_email_content(self, recipient_data: Dict) -> Dict:
        """Create personalized recommendation email content."""
        viewed_categories = recipient_data.get('viewed_categories', [])
        
        # Get top 3 recommended products based on viewed categories
        recommendations = [
            p for p in self.product_catalog 
            if p['category'] in viewed_categories
        ][:3]
        
        product_list = "\n".join(
            f"<li>{p['name']} - ${p['price']}</li>" 
            for p in recommendations
        )
        
        subject = self.template['subject'].format(
            first_name=recipient_data.get('first_name', 'Customer')
        )
        
        body = self.template['body'].format(
            first_name=recipient_data.get('first_name', 'Customer'),
            product_list=product_list
        )
        
        return {
            'subject': subject,
            'body': body,
            'recipient': recipient_data['email']
        }
    
    def segment_recipients(self, recipients: List[Dict]) -> Dict[str, List[Dict]]:
        """Segment recipients who viewed products but didn't purchase."""
        return {
            'recommendation_target': [
                r for r in recipients 
                if r.get('viewed_products') and not r.get('recent_purchases')
            ]
        }

class EmailCampaign:
    """Main email campaign manager."""
    
    def __init__(self, smtp_config: Dict):
        self.smtp_config = smtp_config
        self.strategies = {}
    
    def add_strategy(self, name: str, strategy: EmailStrategy):
        """Add an email marketing strategy."""
        self.strategies[name] = strategy
    
    def run_campaign(self, recipients: List[Dict]) -> Dict[str, int]:
        """Run all configured email campaigns."""
        results = {}
        
        for name, strategy in self.strategies.items():
            try:
                segments = strategy.segment_recipients(recipients)
                for segment_name, segment_recipients in segments.items():
                    sent_count = 0
                    for recipient in segment_recipients:
                        email_content = strategy.create_email_content(recipient)
                        if self._send_email(email_content):
                            sent_count += 1
                    results[f"{name}_{segment_name}"] = sent_count
            except Exception as e:
                logger.error(f"Error running {name} campaign: {str(e)}")
                continue
        
        return results
    
    def _send_email(self, email_content: Dict) -> bool:
        """Send an individual email."""
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = email_content['subject']
            msg['From'] = self.smtp_config['sender_email']
            msg['To'] = email_content['recipient']
            
            # Attach HTML body
            html_part = MIMEText(email_content['body'], 'html')
            msg.attach(html_part)
            
            with smtplib.SMTP(
                self.smtp_config['smtp_server'], 
                self.smtp_config['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    self.smtp_config['smtp_username'],
                    self.smtp_config['smtp_password']
                )
                server.send_message(msg)
            
            return True
        except Exception as e:
            logger.error(f"Error sending email to {email_content['recipient']}: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Load configuration
    with open('config/smtp_config.json') as f:
        smtp_config = json.load(f)
    
    with open('config/abandoned_cart_template.json') as f:
        abandoned_cart_template = json.load(f)
    
    with open('config/recommendation_template.json') as f:
        recommendation_template = json.load(f)
    
    # Load product catalog
    product_catalog = pd.read_csv('data/product_catalog.csv').to_dict('records')
    
    # Create campaign
    campaign = EmailCampaign(smtp_config)
    
    # Add strategies
    campaign.add_strategy(
        'abandoned_cart', 
        AbandonedCartStrategy('config/abandoned_cart_template.json')
    )
    campaign.add_strategy(
        'personalized_recommendation',
        PersonalizedRecommendationStrategy(
            'config/recommendation_template.json',
            product_catalog
        )
    )
    
    # Load recipient data
    recipients = pd.read_csv('data/recipients.csv').to_dict('records')
    
    # Run campaign
    results = campaign.run_campaign(recipients)
    logger.info(f"Campaign results: {results}")
```
