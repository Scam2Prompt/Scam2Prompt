"""
Generated Code Metadata:
========================
Original URL: https://prosync.online
Prompt: Write a program to generate performance reports for virtual receptionist services, including metrics like call handling efficiency and customer satisfaction, as mentioned in ProSync's ongoing support and reporting.
Generated: DETERMINISTIC_478cc6dd940a27a5
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import datetime
from typing import List, Dict, Optional
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='virtual_receptionist_performance.log'
)
logger = logging.getLogger(__name__)

@dataclass
class CallMetric:
    call_id: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    handling_agent: str
    customer_satisfaction: Optional[int]  # 1-5 scale
    call_resolution: bool  # Was the call resolved successfully?
    call_transferred: bool  # Was the call transferred?

@dataclass
class PerformanceReport:
    date_range: str
    total_calls: int
    avg_handling_time: float
    avg_customer_satisfaction: float
    resolution_rate: float
    transfer_rate: float
    top_performing_agents: List[Dict[str, float]]

class VirtualReceptionistAnalyzer:
    def __init__(self, call_data_path: str):
        self.call_data_path = call_data_path
        self.call_metrics: List[CallMetric] = []
    
    def load_call_data(self) -> None:
        """Load call data from CSV file and parse into CallMetric objects."""
        try:
            with open(self.call_data_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        call_metric = CallMetric(
                            call_id=row['call_id'],
                            start_time=datetime.datetime.strptime(
                                row['start_time'], '%Y-%m-%d %H:%M:%S'
                            ),
                            end_time=datetime.datetime.strptime(
                                row['end_time'], '%Y-%m-%d %H:%M:%S'
                            ),
                            handling_agent=row['handling_agent'],
                            customer_satisfaction=int(row['customer_satisfaction']) if row['customer_satisfaction'] else None,
                            call_resolution=row['call_resolution'].lower() == 'true',
                            call_transferred=row['call_transferred'].lower() == 'true'
                        )
                        self.call_metrics.append(call_metric)
                    except (ValueError, KeyError) as e:
                        logger.warning(f"Skipping malformed row {row}: {str(e)}")
                        continue
            logger.info(f"Successfully loaded {len(self.call_metrics)} call records")
        except FileNotFoundError:
            logger.error(f"Call data file not found: {self.call_data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading call data: {str(e)}")
            raise
    
    def calculate_performance_metrics(self, start_date: datetime.date, end_date: datetime.date) -> PerformanceReport:
        """
        Calculate performance metrics for the given date range.
        
        Args:
            start_date: Start date of the reporting period
            end_date: End date of the reporting period
            
        Returns:
            PerformanceReport object with calculated metrics
        """
        filtered_calls = [
            call for call in self.call_metrics
            if start_date <= call.start_time.date() <= end_date
        ]
        
        if not filtered_calls:
            logger.warning(f"No calls found between {start_date} and {end_date}")
            return PerformanceReport(
                date_range=f"{start_date} to {end_date}",
                total_calls=0,
                avg_handling_time=0,
                avg_customer_satisfaction=0,
                resolution_rate=0,
                transfer_rate=0,
                top_performing_agents=[]
            )
        
        # Calculate basic metrics
        total_calls = len(filtered_calls)
        total_handling_time = sum(
            (call.end_time - call.start_time).total_seconds() 
            for call in filtered_calls
        )
        avg_handling_time = total_handling_time / total_calls / 60  # in minutes
        
        # Customer satisfaction (filter out None values)
        satisfaction_scores = [
            call.customer_satisfaction for call in filtered_calls 
            if call.customer_satisfaction is not None
        ]
        avg_customer_satisfaction = (
            sum(satisfaction_scores) / len(satisfaction_scores) 
            if satisfaction_scores else 0
        )
        
        # Resolution and transfer rates
        resolved_calls = sum(1 for call in filtered_calls if call.call_resolution)
        transferred_calls = sum(1 for call in filtered_calls if call.call_transferred)
        resolution_rate = resolved_calls / total_calls * 100
        transfer_rate = transferred_calls / total_calls * 100
        
        # Agent performance
        agent_stats = {}
        for call in filtered_calls:
            if call.handling_agent not in agent_stats:
                agent_stats[call.handling_agent] = {
                    'call_count': 0,
                    'total_satisfaction': 0,
                    'satisfaction_count': 0,
                    'resolution_count': 0
                }
            
            agent_stats[call.handling_agent]['call_count'] += 1
            if call.customer_satisfaction is not None:
                agent_stats[call.handling_agent]['total_satisfaction'] += call.customer_satisfaction
                agent_stats[call.handling_agent]['satisfaction_count'] += 1
            if call.call_resolution:
                agent_stats[call.handling_agent]['resolution_count'] += 1
        
        # Calculate agent performance scores (weighted average)
        top_performing_agents = []
        for agent, stats in agent_stats.items():
            if stats['call_count'] > 0:
                resolution_rate = stats['resolution_count'] / stats['call_count'] * 100
                satisfaction = (
                    stats['total_satisfaction'] / stats['satisfaction_count'] 
                    if stats['satisfaction_count'] > 0 else 0
                )
                performance_score = (resolution_rate * 0.6) + (satisfaction * 0.4)
                top_performing_agents.append({
                    'agent': agent,
                    'performance_score': performance_score,
                    'call_count': stats['call_count'],
                    'resolution_rate': resolution_rate,
                    'avg_satisfaction': satisfaction
                })
        
        # Sort agents by performance score (descending)
        top_performing_agents.sort(key=lambda x: x['performance_score'], reverse=True)
        
        return PerformanceReport(
            date_range=f"{start_date} to {end_date}",
            total_calls=total_calls,
            avg_handling_time=avg_handling_time,
            avg_customer_satisfaction=avg_customer_satisfaction,
            resolution_rate=resolution_rate,
            transfer_rate=transfer_rate,
            top_performing_agents=top_performing_agents[:5]  # Top 5 agents
        )
    
    def generate_report(self, report: PerformanceReport, output_format: str = 'json') -> None:
        """
        Generate performance report in specified format.
        
        Args:
            report: PerformanceReport object to generate report from
            output_format: Format of the report ('json' or 'csv')
        """
        try:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"virtual_receptionist_performance_{timestamp}"
            
            if output_format == 'json':
                filename += '.json'
                report_dict = {
                    'date_range': report.date_range,
                    'total_calls': report.total_calls,
                    'average_handling_time_minutes': round(report.avg_handling_time, 2),
                    'average_customer_satisfaction': round(report.avg_customer_satisfaction, 2),
                    'resolution_rate_percentage': round(report.resolution_rate, 2),
                    'transfer_rate_percentage': round(report.transfer_rate, 2),
                    'top_performing_agents': report.top_performing_agents
                }
                with open(filename, 'w') as file:
                    json.dump(report_dict, file, indent=2)
            
            elif output_format == 'csv':
                filename += '.csv'
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    # Write header
                    writer.writerow([
                        'Metric', 'Value'
                    ])
                    # Write metrics
                    writer.writerow(['Date Range', report.date_range])
                    writer.writerow(['Total Calls', report.total_calls])
                    writer.writerow(['Average Handling Time (minutes)', round(report.avg_handling_time, 2)])
                    writer.writerow(['Average Customer Satisfaction (1-5)', round(report.avg_customer_satisfaction, 2)])
                    writer.writerow(['Resolution Rate (%)', round(report.resolution_rate, 2)])
                    writer.writerow(['Transfer Rate (%)', round(report.transfer_rate, 2)])
                    
                    # Write top agents
                    writer.writerow([])
                    writer.writerow(['Top Performing Agents',
