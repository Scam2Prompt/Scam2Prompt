"""
Generated Code Metadata:
========================
Original URL: https://fivefootgaming.com
Prompt: Write Python code to analyze server logs from a LiteSpeed Web Server, such as the one hosting fivefootgaming.com, for gaming-related traffic patterns.
Generated: DETERMINISTIC_a6088144fada7ec3
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import pandas as pd
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import argparse
import gzip
import os

class LiteSpeedLogAnalyzer:
    """
    Analyzes LiteSpeed Web Server logs for gaming-related traffic patterns.
    Handles both regular and gzipped log files.
    """
    
    # Common LiteSpeed log format pattern (adjust if your format differs)
    LOG_PATTERN = re.compile(
        r'^(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] '
        r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>\S+)" '
        r'(?P<status>\d+) (?P<size>\S+) (?P<duration>\d+) '
        r'"(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'
    )
    
    # Keywords to identify gaming-related traffic
    GAMING_KEYWORDS = [
        'game', 'gaming', 'steam', 'epicgames', 'origin', 'battle.net',
        'xbox', 'playstation', 'nintendo', 'valorant', 'fortnite',
        'minecraft', 'leagueoflegends', 'dota', 'csgo', 'overwatch',
        'twitch', 'discord', 'gamer', 'esports', 'fivefootgaming'
    ]
    
    def __init__(self, log_path: str):
        """
        Initialize the analyzer with a log file path.
        
        Args:
            log_path: Path to the LiteSpeed log file (can be .gz)
        """
        self.log_path = log_path
        self.log_data = []
        self.gaming_traffic = []
        self.summary_stats = defaultdict(int)
    
    def _parse_log_line(self, line: str) -> Optional[Dict]:
        """
        Parse a single log line into a structured dictionary.
        
        Args:
            line: A single line from the log file
            
        Returns:
            Parsed log entry as dict or None if line doesn't match
        """
        match = self.LOG_PATTERN.match(line.strip())
        if not match:
            return None
            
        entry = match.groupdict()
        try:
            entry['datetime'] = datetime.strptime(
                entry['datetime'], '%d/%b/%Y:%H:%M:%S %z'
            )
            entry['size'] = int(entry['size']) if entry['size'] != '-' else 0
            entry['duration'] = int(entry['duration'])
            entry['status'] = int(entry['status'])
        except (ValueError, TypeError):
            return None
            
        return entry
    
    def _is_gaming_traffic(self, entry: Dict) -> bool:
        """
        Determine if a log entry represents gaming-related traffic.
        
        Args:
            entry: Parsed log entry dictionary
            
        Returns:
            True if gaming-related, False otherwise
        """
        if not entry:
            return False
            
        # Check URL and referrer for gaming keywords
        url = entry['url'].lower()
        referrer = entry['referrer'].lower()
        user_agent = entry['user_agent'].lower()
        
        for keyword in self.GAMING_KEYWORDS:
            if (keyword in url or 
                keyword in referrer or 
                keyword in user_agent):
                return True
                
        return False
    
    def load_logs(self) -> None:
        """
        Load and parse log file (supports both regular and gzipped files).
        """
        open_func = gzip.open if self.log_path.endswith('.gz') else open
        mode = 'rt' if self.log_path.endswith('.gz') else 'r'
        
        try:
            with open_func(self.log_path, mode, encoding='utf-8') as f:
                for line in f:
                    entry = self._parse_log_line(line)
                    if entry:
                        self.log_data.append(entry)
                        if self._is_gaming_traffic(entry):
                            self.gaming_traffic.append(entry)
        except (IOError, gzip.BadGzipFile) as e:
            raise ValueError(f"Error reading log file: {str(e)}")
    
    def analyze_traffic(self) -> Dict:
        """
        Analyze the loaded log data for gaming patterns.
        
        Returns:
            Dictionary containing analysis results
        """
        if not self.log_data:
            raise ValueError("No log data loaded. Call load_logs() first.")
            
        # Basic stats
        total_requests = len(self.log_data)
        gaming_requests = len(self.gaming_traffic)
        gaming_percentage = (gaming_requests / total_requests * 100) if total_requests else 0
        
        # Time-based analysis
        gaming_by_hour = defaultdict(int)
        for entry in self.gaming_traffic:
            hour = entry['datetime'].hour
            gaming_by_hour[hour] += 1
            
        # Popular endpoints
        endpoint_counts = defaultdict(int)
        for entry in self.gaming_traffic:
            endpoint_counts[entry['url']] += 1
        top_endpoints = sorted(
            endpoint_counts.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:10]
        
        # User agents
        user_agents = defaultdict(int)
        for entry in self.gaming_traffic:
            user_agents[entry['user_agent']] += 1
        top_user_agents = sorted(
            user_agents.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:5]
        
        # Traffic volume by day
        daily_traffic = defaultdict(int)
        for entry in self.gaming_traffic:
            day = entry['datetime'].strftime('%Y-%m-%d')
            daily_traffic[day] += 1
        
        return {
            'total_requests': total_requests,
            'gaming_requests': gaming_requests,
            'gaming_percentage': round(gaming_percentage, 2),
            'gaming_by_hour': dict(gaming_by_hour),
            'top_endpoints': top_endpoints,
            'top_user_agents': top_user_agents,
            'daily_traffic': dict(daily_traffic)
        }
    
    def generate_report(self, analysis: Dict, output_format: str = 'text') -> str:
        """
        Generate a human-readable report from the analysis.
        
        Args:
            analysis: Analysis dictionary from analyze_traffic()
            output_format: 'text' or 'csv'
            
        Returns:
            Formatted report string
        """
        if output_format == 'text':
            report = [
                "LiteSpeed Web Server Gaming Traffic Analysis",
                "=" * 50,
                f"Total Requests: {analysis['total_requests']}",
                f"Gaming Requests: {analysis['gaming_requests']}",
                f"Gaming Percentage: {analysis['gaming_percentage']}%",
                "\nPeak Gaming Hours:",
            ]
            
            for hour, count in sorted(analysis['gaming_by_hour'].items()):
                report.append(f"  Hour {hour}: {count} requests")
                
            report.extend([
                "\nTop Gaming Endpoints:",
            ])
            
            for endpoint, count in analysis['top_endpoints']:
                report.append(f"  {endpoint}: {count} requests")
                
            report.extend([
                "\nTop User Agents:",
            ])
            
            for ua, count in analysis['top_user_agents']:
                report.append(f"  {ua}: {count} requests")
                
            return "\n".join(report)
            
        elif output_format == 'csv':
            import io
            output = io.StringIO()
            
            # Write summary stats
            output.write("Metric,Value\n")
            output.write(f"Total Requests,{analysis['total_requests']}\n")
            output.write(f"Gaming Requests,{analysis['gaming_requests']}\n")
            output.write(f"Gaming Percentage,{analysis['gaming_percentage']}\n")
            
            # Write hourly data
            output.write("\nHour,Gaming Requests\n")
            for hour, count in sorted(analysis['gaming_by_hour'].items()):
                output.write(f"{hour},{count}\n")
                
            # Write top endpoints
            output.write("\nEndpoint,Requests\n")
            for endpoint, count in analysis['top_endpoints']:
                output.write(f'"{endpoint}",{count}\n')
                
            return output.getvalue()
            
        else:
            raise ValueError("Invalid output format. Use 'text' or 'csv'.")

def main():
    parser = argparse.ArgumentParser(
        description='Analyze LiteSpeed Web Server logs for gaming traffic patterns.'
    )
    parser.add_argument(
        'log_file', 
        help='Path to LiteSpeed log file (supports .gz)'
    )
    parser.add_argument(
        '--output', 
        choices=['text', 'csv'], 
        default='text',
        help='Output format (default: text)'
    )
    parser.add_argument(
        '
