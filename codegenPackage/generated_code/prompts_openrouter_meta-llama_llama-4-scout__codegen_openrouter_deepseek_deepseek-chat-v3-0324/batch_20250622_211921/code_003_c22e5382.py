"""
Generated Code Metadata:
========================
Original URL: https://www.vatio.cl
Prompt: "Generate a code snippet for creating customized reports and alerts using data from a video surveillance system, similar to VATIO's Control Total y Estrategia stage."
Generated: DETERMINISTIC_c22e5382aa8e18d7
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional
import pytz

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SurveillanceReportGenerator:
    """
    A class to generate customized reports and alerts from video surveillance data.
    """
    
    def __init__(self, timezone: str = 'UTC'):
        """
        Initialize the report generator with a timezone.
        
        Args:
            timezone: Timezone string (e.g., 'America/New_York')
        """
        try:
            self.timezone = pytz.timezone(timezone)
        except pytz.UnknownTimeZoneError:
            logger.warning(f"Unknown timezone {timezone}, defaulting to UTC")
            self.timezone = pytz.UTC

    def generate_report(
        self,
        surveillance_data: List[Dict],
        report_type: str,
        alert_thresholds: Optional[Dict] = None
    ) -> Dict:
        """
        Generate a surveillance report based on input data.
        
        Args:
            surveillance_data: List of surveillance events
            report_type: Type of report to generate ('daily', 'weekly', 'incident')
            alert_thresholds: Dictionary of thresholds for triggering alerts
            
        Returns:
            Dictionary containing the generated report and any alerts
        """
        if not surveillance_data:
            logger.error("No surveillance data provided")
            raise ValueError("Surveillance data cannot be empty")
            
        if report_type not in ['daily', 'weekly', 'incident']:
            logger.error(f"Invalid report type: {report_type}")
            raise ValueError("Invalid report type")
            
        report = {
            'metadata': {
                'generated_at': self._get_current_time(),
                'report_type': report_type,
                'data_points': len(surveillance_data)
            },
            'summary': {},
            'alerts': []
        }
        
        try:
            if report_type == 'daily':
                report['summary'] = self._generate_daily_summary(surveillance_data)
            elif report_type == 'weekly':
                report['summary'] = self._generate_weekly_summary(surveillance_data)
            else:
                report['summary'] = self._generate_incident_report(surveillance_data)
                
            if alert_thresholds:
                report['alerts'] = self._check_for_alerts(report['summary'], alert_thresholds)
                
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise
            
        return report
    
    def _get_current_time(self) -> str:
        """Get current time in the configured timezone."""
        return datetime.now(self.timezone).isoformat()
    
    def _generate_daily_summary(self, data: List[Dict]) -> Dict:
        """Generate daily summary statistics."""
        summary = {
            'total_events': len(data),
            'motion_events': sum(1 for event in data if event.get('type') == 'motion'),
            'face_detections': sum(1 for event in data if event.get('type') == 'face'),
            'first_event': min(event['timestamp'] for event in data),
            'last_event': max(event['timestamp'] for event in data)
        }
        return summary
    
    def _generate_weekly_summary(self, data: List[Dict]) -> Dict:
        """Generate weekly summary statistics."""
        # Group by day of week
        days = {}
        for event in data:
            dt = datetime.fromisoformat(event['timestamp']).astimezone(self.timezone)
            day = dt.strftime('%A')
            days.setdefault(day, []).append(event)
            
        summary = {
            'total_events': len(data),
            'days': {
                day: {
                    'count': len(events),
                    'motion_events': sum(1 for e in events if e.get('type') == 'motion'),
                    'face_detections': sum(1 for e in events if e.get('type') == 'face')
                }
                for day, events in days.items()
            }
        }
        return summary
    
    def _generate_incident_report(self, data: List[Dict]) -> Dict:
        """Generate incident-focused report."""
        incidents = [event for event in data if event.get('severity', 0) > 0]
        
        summary = {
            'total_incidents': len(incidents),
            'incidents': sorted(
                incidents,
                key=lambda x: x['severity'],
                reverse=True
            ),
            'highest_severity': max(
                (event['severity'] for event in incidents),
                default=0
            )
        }
        return summary
    
    def _check_for_alerts(self, summary: Dict, thresholds: Dict) -> List[Dict]:
        """Check summary against thresholds and generate alerts if needed."""
        alerts = []
        
        # Check motion event threshold
        if 'motion_threshold' in thresholds:
            motion_events = summary.get('motion_events', 0)
            if motion_events > thresholds['motion_threshold']:
                alerts.append({
                    'type': 'motion',
                    'value': motion_events,
                    'threshold': thresholds['motion_threshold'],
                    'message': f"Motion events exceeded threshold: {motion_events} > {thresholds['motion_threshold']}"
                })
                
        # Check face detection threshold
        if 'face_threshold' in thresholds:
            face_detections = summary.get('face_detections', 0)
            if face_detections > thresholds['face_threshold']:
                alerts.append({
                    'type': 'face',
                    'value': face_detections,
                    'threshold': thresholds['face_threshold'],
                    'message': f"Face detections exceeded threshold: {face_detections} > {thresholds['face_threshold']}"
                })
                
        # Check incident severity threshold
        if 'severity_threshold' in thresholds:
            max_severity = summary.get('highest_severity', 0)
            if max_severity > thresholds['severity_threshold']:
                alerts.append({
                    'type': 'severity',
                    'value': max_severity,
                    'threshold': thresholds['severity_threshold'],
                    'message': f"Severity threshold exceeded: {max_severity} > {thresholds['severity_threshold']}"
                })
                
        return alerts

# Example usage
if __name__ == "__main__":
    # Sample surveillance data
    sample_data = [
        {
            "timestamp": "2023-01-01T10:00:00Z",
            "type": "motion",
            "camera_id": "cam1",
            "severity": 0
        },
        {
            "timestamp": "2023-01-01T10:15:00Z",
            "type": "face",
            "camera_id": "cam2",
            "severity": 1
        },
        {
            "timestamp": "2023-01-01T11:30:00Z",
            "type": "motion",
            "camera_id": "cam1",
            "severity": 2
        }
    ]
    
    # Initialize report generator
    report_gen = SurveillanceReportGenerator(timezone="America/New_York")
    
    # Define alert thresholds
    thresholds = {
        "motion_threshold": 1,
        "face_threshold": 0,
        "severity_threshold": 1
    }
    
    # Generate and print a daily report
    try:
        report = report_gen.generate_report(
            surveillance_data=sample_data,
            report_type="daily",
            alert_thresholds=thresholds
        )
        print(json.dumps(report, indent=2))
    except Exception as e:
        logger.error(f"Failed to generate report: {e}")
```
