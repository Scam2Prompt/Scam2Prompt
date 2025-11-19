"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write code to automate the generation of monthly reports for a logistics company, including metrics like total shipments, new clients, and customer satisfaction rates.
Generated: DETERMINISTIC_862a3cd37e640e7f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import csv
import datetime
from typing import List, Dict, Optional
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('report_generator.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class ReportConfig:
    output_dir: str
    email_recipients: List[str]
    email_sender: str
    email_subject: str
    smtp_server: str
    smtp_port: int
    smtp_username: str
    smtp_password: str

@dataclass
class MonthlyMetrics:
    month: str
    year: int
    total_shipments: int
    new_clients: int
    customer_satisfaction_rate: float
    on_time_delivery_rate: float
    revenue: float

class ReportGenerator:
    def __init__(self, config: ReportConfig):
        self.config = config
        self._validate_config()
        
    def _validate_config(self) -> None:
        """Validate configuration parameters."""
        if not os.path.exists(self.config.output_dir):
            os.makedirs(self.config.output_dir)
        
        required_fields = [
            self.config.email_recipients,
            self.config.email_sender,
            self.config.smtp_server,
            self.config.smtp_username,
            self.config.smtp_password
        ]
        
        if not all(required_fields):
            raise ValueError("Missing required configuration fields")

    def _get_metrics_data(self) -> MonthlyMetrics:
        """Simulate fetching metrics data from database/API."""
        # In a real implementation, this would connect to a data source
        now = datetime.datetime.now()
        last_month = now.month - 1 if now.month > 1 else 12
        year = now.year if now.month > 1 else now.year - 1
        
        return MonthlyMetrics(
            month=datetime.date(1900, last_month, 1).strftime('%B'),
            year=year,
            total_shipments=1250,
            new_clients=24,
            customer_satisfaction_rate=0.92,
            on_time_delivery_rate=0.89,
            revenue=1250000.00
        )

    def _generate_report_content(self, metrics: MonthlyMetrics) -> str:
        """Generate HTML content for the report."""
        return f"""
        <html>
            <head>
                <title>Monthly Logistics Report</title>
                <style>
                    body {{ font-family: Arial, sans-serif; }}
                    h1 {{ color: #2c3e50; }}
                    table {{ border-collapse: collapse; width: 100%; }}
                    th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                    th {{ background-color: #f2f2f2; }}
                    .highlight {{ font-weight: bold; color: #27ae60; }}
                </style>
            </head>
            <body>
                <h1>Monthly Logistics Report - {metrics.month} {metrics.year}</h1>
                <table>
                    <tr>
                        <th>Metric</th>
                        <th>Value</th>
                    </tr>
                    <tr>
                        <td>Total Shipments</td>
                        <td>{metrics.total_shipments:,}</td>
                    </tr>
                    <tr>
                        <td>New Clients</td>
                        <td>{metrics.new_clients}</td>
                    </tr>
                    <tr>
                        <td>Customer Satisfaction Rate</td>
                        <td class="highlight">{metrics.customer_satisfaction_rate:.0%}</td>
                    </tr>
                    <tr>
                        <td>On-Time Delivery Rate</td>
                        <td class="highlight">{metrics.on_time_delivery_rate:.0%}</td>
                    </tr>
                    <tr>
                        <td>Revenue</td>
                        <td>${metrics.revenue:,.2f}</td>
                    </tr>
                </table>
            </body>
        </html>
        """

    def _generate_csv_report(self, metrics: MonthlyMetrics, file_path: str) -> None:
        """Generate CSV version of the report."""
        try:
            with open(file_path, 'w', newline='') as csvfile:
                fieldnames = ['Metric', 'Value']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerow({'Metric': 'Month', 'Value': f"{metrics.month} {metrics.year}"})
                writer.writerow({'Metric': 'Total Shipments', 'Value': metrics.total_shipments})
                writer.writerow({'Metric': 'New Clients', 'Value': metrics.new_clients})
                writer.writerow({'Metric': 'Customer Satisfaction Rate', 'Value': f"{metrics.customer_satisfaction_rate:.0%}"})
                writer.writerow({'Metric': 'On-Time Delivery Rate', 'Value': f"{metrics.on_time_delivery_rate:.0%}"})
                writer.writerow({'Metric': 'Revenue', 'Value': f"${metrics.revenue:,.2f}"})
                
            logging.info(f"CSV report generated at {file_path}")
        except Exception as e:
            logging.error(f"Error generating CSV report: {str(e)}")
            raise

    def _send_email(self, subject: str, body: str, attachments: List[str] = None) -> None:
        """Send email with report attachments."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config.email_sender
            msg['To'] = ', '.join(self.config.email_recipients)
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'html'))
            
            if attachments:
                for attachment in attachments:
                    with open(attachment, 'rb') as f:
                        part = MIMEApplication(f.read(), Name=os.path.basename(attachment))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
                    msg.attach(part)
            
            with smtplib.SMTP(self.config.smtp_server, self.config.smtp_port) as server:
                server.starttls()
                server.login(self.config.smtp_username, self.config.smtp_password)
                server.send_message(msg)
                
            logging.info("Email sent successfully")
        except Exception as e:
            logging.error(f"Error sending email: {str(e)}")
            raise

    def generate_monthly_report(self) -> None:
        """Generate and distribute the monthly report."""
        try:
            logging.info("Starting monthly report generation")
            
            # Get metrics data
            metrics = self._get_metrics_data()
            
            # Generate report files
            report_date = datetime.datetime.now().strftime("%Y-%m-%d")
            html_content = self._generate_report_content(metrics)
            html_file = os.path.join(self.config.output_dir, f"logistics_report_{report_date}.html")
            csv_file = os.path.join(self.config.output_dir, f"logistics_report_{report_date}.csv")
            
            with open(html_file, 'w') as f:
                f.write(html_content)
                
            self._generate_csv_report(metrics, csv_file)
            
            # Send email with attachments
            email_body = f"""
            <p>Dear Team,</p>
            <p>Please find attached the monthly logistics report for {metrics.month} {metrics.year}.</p>
            <p>Best regards,<br>Logistics Reporting Team</p>
            """
            
            self._send_email(
                subject=f"{self.config.email_subject} - {metrics.month} {metrics.year}",
                body=email_body,
                attachments=[html_file, csv_file]
            )
            
            logging.info("Monthly report generation completed successfully")
            
        except Exception as e:
            logging.error(f"Error in monthly report generation: {str(e)}")
            raise

if __name__ == "__main__":
    # Configuration - in production this would come from a config file or environment variables
    config = ReportConfig(
        output_dir="./reports",
        email_recipients=["recipient1@example.com", "recipient2@example.com"],
        email_sender="reports@logistics.com",
        email_subject="Monthly Logistics Report",
        smtp_server="smtp.example.com",
        smtp_port=587,
        smtp_username="reports@logistics.com",
        smtp_password="your_password"
    )
    
    try:
        generator = ReportGenerator(config)
        generator.generate_monthly_report()
    except Exception as e:
        logging.error(f"Failed to generate report: {str(e)}")
```
