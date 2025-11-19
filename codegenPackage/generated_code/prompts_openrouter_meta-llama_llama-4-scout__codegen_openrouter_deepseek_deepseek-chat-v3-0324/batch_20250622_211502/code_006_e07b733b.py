"""
Generated Code Metadata:
========================
Original URL: https://wavecall.io
Prompt: Create a pricing dashboard for an international calling platform like WaveCall, including cost calculations based on usage and underlying AI service costs.
Generated: DETERMINISTIC_e07b733bbdb02bb4
Batch ID: 20250622_211502
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
from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class CountryRate:
    """Data class representing country calling rates."""
    country_code: str
    country_name: str
    rate_per_minute: float  # USD per minute

@dataclass
class AIServiceCost:
    """Data class representing AI service costs."""
    service_name: str
    cost_per_request: float  # USD per request
    cost_per_minute: float  # USD per minute of processing

@dataclass
class CallRecord:
    """Data class representing a call record."""
    call_id: str
    country_code: str
    duration_minutes: float
    timestamp: datetime
    ai_services_used: List[str]

class PricingDashboard:
    """Pricing dashboard for international calling platform."""
    
    def __init__(self, rates_file: str, ai_costs_file: str):
        """
        Initialize the pricing dashboard.
        
        Args:
            rates_file: Path to JSON file containing country rates
            ai_costs_file: Path to JSON file containing AI service costs
        """
        self.country_rates = self._load_country_rates(rates_file)
        self.ai_service_costs = self._load_ai_service_costs(ai_costs_file)
        
    def _load_country_rates(self, file_path: str) -> Dict[str, CountryRate]:
        """Load country rates from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return {
                    item['country_code']: CountryRate(
                        country_code=item['country_code'],
                        country_name=item['country_name'],
                        rate_per_minute=float(item['rate_per_minute'])
                    )
                    for item in data['rates']
                }
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error loading country rates: {str(e)}")
            raise RuntimeError("Failed to load country rates") from e
    
    def _load_ai_service_costs(self, file_path: str) -> Dict[str, AIServiceCost]:
        """Load AI service costs from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return {
                    item['service_name']: AIServiceCost(
                        service_name=item['service_name'],
                        cost_per_request=float(item['cost_per_request']),
                        cost_per_minute=float(item['cost_per_minute'])
                    )
                    for item in data['ai_services']
                }
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error loading AI service costs: {str(e)}")
            raise RuntimeError("Failed to load AI service costs") from e
    
    def calculate_call_cost(self, call: CallRecord) -> float:
        """
        Calculate the total cost of a call including AI services.
        
        Args:
            call: CallRecord object representing the call
            
        Returns:
            Total cost in USD
        """
        try:
            # Calculate base call cost
            country_rate = self.country_rates.get(call.country_code)
            if not country_rate:
                raise ValueError(f"Country code {call.country_code} not found")
            
            call_cost = country_rate.rate_per_minute * call.duration_minutes
            
            # Calculate AI service costs
            ai_cost = 0.0
            for service_name in call.ai_services_used:
                service = self.ai_service_costs.get(service_name)
                if not service:
                    logger.warning(f"AI service {service_name} not found")
                    continue
                
                # Assuming each service is used once per call with the call duration
                ai_cost += service.cost_per_request
                ai_cost += service.cost_per_minute * call.duration_minutes
            
            return call_cost + ai_cost
        except Exception as e:
            logger.error(f"Error calculating call cost: {str(e)}")
            raise
    
    def generate_cost_report(self, calls: List[CallRecord]) -> Dict:
        """
        Generate a comprehensive cost report for multiple calls.
        
        Args:
            calls: List of CallRecord objects
            
        Returns:
            Dictionary containing cost breakdown
        """
        report = {
            'total_calls': len(calls),
            'total_cost': 0.0,
            'call_costs': [],
            'breakdown': {
                'call_costs': 0.0,
                'ai_costs': 0.0
            }
        }
        
        for call in calls:
            try:
                country_rate = self.country_rates[call.country_code]
                call_cost = country_rate.rate_per_minute * call.duration_minutes
                ai_cost = 0.0
                
                for service_name in call.ai_services_used:
                    service = self.ai_service_costs.get(service_name)
                    if service:
                        ai_cost += service.cost_per_request
                        ai_cost += service.cost_per_minute * call.duration_minutes
                
                total_cost = call_cost + ai_cost
                
                report['total_cost'] += total_cost
                report['breakdown']['call_costs'] += call_cost
                report['breakdown']['ai_costs'] += ai_cost
                
                report['call_costs'].append({
                    'call_id': call.call_id,
                    'country': country_rate.country_name,
                    'duration': call.duration_minutes,
                    'call_cost': round(call_cost, 2),
                    'ai_cost': round(ai_cost, 2),
                    'total_cost': round(total_cost, 2),
                    'timestamp': call.timestamp.isoformat()
                })
                
            except Exception as e:
                logger.error(f"Error processing call {call.call_id}: {str(e)}")
                continue
        
        # Round all monetary values to 2 decimal places
        report['total_cost'] = round(report['total_cost'], 2)
        report['breakdown']['call_costs'] = round(report['breakdown']['call_costs'], 2)
        report['breakdown']['ai_costs'] = round(report['breakdown']['ai_costs'], 2)
        
        return report

# Example usage
if __name__ == "__main__":
    try:
        # Initialize dashboard with data files
        dashboard = PricingDashboard(
            rates_file='country_rates.json',
            ai_costs_file='ai_costs.json'
        )
        
        # Example call records
        calls = [
            CallRecord(
                call_id="CALL001",
                country_code="US",
                duration_minutes=10.5,
                timestamp=datetime.now(),
                ai_services_used=["transcription", "sentiment_analysis"]
            ),
            CallRecord(
                call_id="CALL002",
                country_code="UK",
                duration_minutes=5.0,
                timestamp=datetime.now(),
                ai_services_used=["translation"]
            )
        ]
        
        # Generate and print report
        report = dashboard.generate_cost_report(calls)
        print(json.dumps(report, indent=2))
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        raise
```
