"""
Generated Code Metadata:
========================
Original URL: https://phanbtom.com
Prompt: "Develop a code example for monitoring user activity in real-time, using a cloud-based IAM system and integrating with security information and event management (SIEM) tools."
Generated: DETERMINISTIC_a2febd6960c518de
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
import logging
from datetime import datetime
from typing import Dict, List, Optional
import boto3
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CloudActivityMonitor:
    """
    Monitors user activity in real-time using AWS CloudTrail and integrates with SIEM tools.
    """
    
    def __init__(self, cloudtrail_name: str, siem_endpoint: Optional[str] = None):
        """
        Initialize the CloudActivityMonitor.
        
        Args:
            cloudtrail_name: Name of the CloudTrail to monitor
            siem_endpoint: Optional endpoint for SIEM integration
        """
        self.cloudtrail_name = cloudtrail_name
        self.siem_endpoint = siem_endpoint
        self.cloudtrail_client = boto3.client('cloudtrail')
        self.sns_client = boto3.client('sns') if siem_endpoint else None
        
    def get_recent_events(self, max_results: int = 50) -> List[Dict]:
        """
        Retrieve recent CloudTrail events.
        
        Args:
            max_results: Maximum number of events to return
            
        Returns:
            List of event dictionaries
        """
        try:
            response = self.cloudtrail_client.lookup_events(
                LookupAttributes=[
                    {
                        'AttributeKey': 'EventName',
                        'AttributeValue': 'ConsoleLogin'
                    },
                ],
                MaxResults=max_results
            )
            return response.get('Events', [])
        except ClientError as e:
            logger.error(f"Error retrieving CloudTrail events: {e}")
            return []
    
    def process_event(self, event: Dict) -> Dict:
        """
        Process and normalize a CloudTrail event.
        
        Args:
            event: Raw CloudTrail event
            
        Returns:
            Processed event dictionary
        """
        try:
            event_time = event.get('EventTime', datetime.utcnow())
            username = event.get('Username', 'unknown')
            source_ip = event.get('SourceIPAddress', '0.0.0.0')
            
            return {
                'timestamp': event_time.isoformat(),
                'user': username,
                'ip_address': source_ip,
                'event_type': event.get('EventName', 'UnknownEvent'),
                'raw_event': event
            }
        except Exception as e:
            logger.error(f"Error processing event: {e}")
            return {}
    
    def send_to_siem(self, processed_event: Dict) -> bool:
        """
        Send processed event to SIEM system.
        
        Args:
            processed_event: Processed event dictionary
            
        Returns:
            True if successful, False otherwise
        """
        if not self.siem_endpoint or not self.sns_client:
            logger.warning("SIEM integration not configured")
            return False
            
        try:
            response = self.sns_client.publish(
                TopicArn=self.siem_endpoint,
                Message=json.dumps(processed_event),
                Subject='CloudTrail Security Event'
            )
            return response['MessageId'] is not None
        except ClientError as e:
            logger.error(f"Error sending to SIEM: {e}")
            return False
    
    def monitor_activity(self, interval: int = 60):
        """
        Continuously monitor user activity.
        
        Args:
            interval: Polling interval in seconds
        """
        logger.info(f"Starting activity monitoring for CloudTrail: {self.cloudtrail_name}")
        
        while True:
            try:
                events = self.get_recent_events()
                for event in events:
                    processed_event = self.process_event(event)
                    if processed_event:
                        logger.info(f"Processed event: {processed_event['event_type']} by {processed_event['user']}")
                        if self.siem_endpoint:
                            self.send_to_siem(processed_event)
                
                time.sleep(interval)
            except KeyboardInterrupt:
                logger.info("Activity monitoring stopped by user")
                break
            except Exception as e:
                logger.error(f"Error in monitoring loop: {e}")
                time.sleep(interval)

if __name__ == "__main__":
    # Example configuration - replace with actual values
    config = {
        'cloudtrail_name': 'my-cloudtrail',
        'siem_endpoint': 'arn:aws:sns:us-east-1:123456789012:siem-topic'
    }
    
    monitor = CloudActivityMonitor(
        cloudtrail_name=config['cloudtrail_name'],
        siem_endpoint=config.get('siem_endpoint')
    )
    monitor.monitor_activity()
```
