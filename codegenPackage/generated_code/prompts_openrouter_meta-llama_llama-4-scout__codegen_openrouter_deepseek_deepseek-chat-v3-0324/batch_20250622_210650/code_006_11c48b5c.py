"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: "Suggest a suitable programming approach for building a brand protection tool that monitors and responds to online threats, considering the multidisciplinary team's expertise at Garud Associates."
Generated: DETERMINISTIC_11c48b5c91ae186c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Brand Protection Tool for Garud Associates

This tool monitors online threats and responds to them using a multi-disciplinary approach.
It integrates web scraping, threat analysis, automated response, and reporting capabilities.
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime
import json
import logging
from typing import List, Dict, Optional
from dataclasses import dataclass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('brand_protection.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class Threat:
    """Data class representing a detected threat"""
    source: str
    url: str
    threat_type: str
    severity: int
    timestamp: str
    content: Optional[str] = None

class BrandMonitor:
    """Main class for brand protection monitoring"""
    
    def __init__(self, config_file: str = 'config.json'):
        """
        Initialize the brand monitor with configuration
        
        Args:
            config_file: Path to JSON configuration file
        """
        self.config = self._load_config(config_file)
        self.blacklist = self._load_blacklist()
        self.keywords = self.config.get('keywords', [])
        self.brand_names = self.config.get('brand_names', [])
        self.thresholds = self.config.get('thresholds', {})
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'GarudBrandProtection/1.0'})
        
    def _load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file {config_file} not found")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in config file {config_file}")
            raise
            
    def _load_blacklist(self) -> List[str]:
        """Load blacklisted domains/URLs"""
        try:
            with open('blacklist.txt', 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            logger.warning("Blacklist file not found, using empty list")
            return []
            
    def monitor_social_media(self) -> List[Threat]:
        """Monitor social media platforms for brand mentions"""
        threats = []
        for platform in self.config.get('social_media', []):
            try:
                threats.extend(self._check_platform(platform))
            except Exception as e:
                logger.error(f"Error monitoring {platform}: {str(e)}")
        return threats
        
    def _check_platform(self, platform: Dict) -> List[Threat]:
        """Check a specific social media platform"""
        threats = []
        # Implementation would vary by platform API
        # This is a placeholder for actual API calls
        logger.info(f"Checking {platform['name']} for brand mentions")
        return threats
        
    def scan_websites(self) -> List[Threat]:
        """Scan websites for brand infringement"""
        threats = []
        for site in self.config.get('target_sites', []):
            try:
                threats.extend(self._scan_site(site))
            except Exception as e:
                logger.error(f"Error scanning {site}: {str(e)}")
        return threats
        
    def _scan_site(self, url: str) -> List[Threat]:
        """Scan a single website for infringements"""
        threats = []
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text().lower()
            
            for keyword in self.keywords:
                if keyword.lower() in text:
                    threat = Threat(
                        source=url,
                        url=url,
                        threat_type="keyword_match",
                        severity=self._assess_severity(keyword),
                        timestamp=datetime.now().isoformat(),
                        content=self._extract_context(text, keyword)
                    )
                    threats.append(threat)
                    
        except requests.RequestException as e:
            logger.warning(f"Failed to scan {url}: {str(e)}")
            
        return threats
        
    def _assess_severity(self, keyword: str) -> int:
        """Assess threat severity based on keyword"""
        return self.thresholds.get(keyword, 1)
        
    def _extract_context(self, text: str, keyword: str, window=50) -> str:
        """Extract context around the keyword match"""
        index = text.find(keyword.lower())
        if index == -1:
            return ""
        start = max(0, index - window)
        end = min(len(text), index + len(keyword) + window)
        return text[start:end]
        
    def check_domain_squatting(self) -> List[Threat]:
        """Check for domain squatting attempts"""
        threats = []
        # Implementation would use domain registration APIs
        logger.info("Checking for domain squatting")
        return threats
        
    def analyze_threats(self, threats: List[Threat]) -> List[Threat]:
        """Analyze and prioritize detected threats"""
        return sorted(
            [t for t in threats if t.severity >= self.config.get('min_severity', 1)],
            key=lambda x: x.severity,
            reverse=True
        )
        
    def generate_report(self, threats: List[Threat]) -> str:
        """Generate a report of detected threats"""
        report = f"Brand Protection Report - {datetime.now().date()}\n\n"
        report += f"Total threats detected: {len(threats)}\n\n"
        
        for threat in threats:
            report += (
                f"Source: {threat.source}\n"
                f"URL: {threat.url}\n"
                f"Type: {threat.threat_type}\n"
                f"Severity: {threat.severity}\n"
                f"Timestamp: {threat.timestamp}\n"
                f"Context: {threat.content[:200] if threat.content else 'N/A'}\n\n"
            )
            
        return report
        
    def send_alert(self, threats: List[Threat]) -> bool:
        """Send email alert for high-priority threats"""
        if not threats:
            return False
            
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config['email']['sender']
            msg['To'] = ', '.join(self.config['email']['recipients'])
            msg['Subject'] = f"Brand Protection Alert - {len(threats)} High Priority Threat(s)"
            
            body = self.generate_report(threats)
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(
                self.config['email']['smtp_server'],
                self.config['email']['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    self.config['email']['username'],
                    self.config['email']['password']
                )
                server.send_message(msg)
                
            logger.info("Alert email sent successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send alert email: {str(e)}")
            return False
            
    def take_action(self, threat: Threat) -> bool:
        """Take appropriate action based on threat type"""
        # Implementation would vary based on response protocols
        logger.info(f"Taking action on threat: {threat.url}")
        return True
        
    def run_monitoring_cycle(self):
        """Run complete monitoring cycle"""
        logger.info("Starting brand protection monitoring cycle")
        
        # Detect threats from various sources
        threats = []
        threats.extend(self.monitor_social_media())
        threats.extend(self.scan_websites())
        threats.extend(self.check_domain_squatting())
        
        # Analyze and prioritize
        prioritized_threats = self.analyze_threats(threats)
        
        # Generate report
        report = self.generate_report(prioritized_threats)
        logger.info(report)
        
        # Send alerts for high priority threats
        high_priority = [t for t in prioritized_threats if t.severity >= 3]
        if high_priority:
            self.send_alert(high_priority)
            
        # Take automated actions
        for threat in prioritized_threats:
            if threat.severity >= self.config.get('action_threshold', 4):
                self.take_action(threat)
                
        logger.info("Monitoring cycle completed")

def main():
    """Main entry point for the brand protection tool"""
    try:
        monitor = BrandMonitor()
        while True:
            monitor.run_monitoring_cycle()
            time.sleep(3600)  # Run hourly
    except KeyboardInterrupt:
        logger.info("Brand protection monitoring stopped by user")
    except Exception as e:
        logger.error(f"
