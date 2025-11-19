"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write a code to generate a report on research activities and innovation metrics for ORIC, including number of publications, presentations, and patent filings.
Generated: DETERMINISTIC_905494d404a749fb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
from typing import List, Dict, Optional
import json
import os

class ResearchActivityReport:
    """
    A class to generate reports on research activities and innovation metrics.
    """
    
    def __init__(self, data_file: str = "research_data.json"):
        """
        Initialize the report generator with data file.
        
        Args:
            data_file: Path to JSON file containing research data
        """
        self.data_file = data_file
        self.research_data = self._load_data()
        
    def _load_data(self) -> Dict:
        """
        Load research data from JSON file.
        
        Returns:
            Dictionary containing research data
            
        Raises:
            FileNotFoundError: If data file doesn't exist
            json.JSONDecodeError: If data file is malformed
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {self.data_file} not found")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in data file: {e.msg}", e.doc, e.pos)
    
    def _validate_data(self, data: Dict) -> bool:
        """
        Validate the structure of research data.
        
        Args:
            data: Research data to validate
            
        Returns:
            bool: True if data is valid
            
        Raises:
            ValueError: If data structure is invalid
        """
        required_fields = {
            'publications': ['journal', 'year', 'authors'],
            'presentations': ['title', 'conference', 'year', 'presenters'],
            'patents': ['title', 'filing_date', 'status', 'inventors']
        }
        
        for category, fields in required_fields.items():
            if category not in data:
                raise ValueError(f"Missing category: {category}")
            for item in data[category]:
                for field in fields:
                    if field not in item:
                        raise ValueError(f"Missing field {field} in {category}")
        
        return True
    
    def generate_report(self, output_format: str = "csv", output_file: Optional[str] = None) -> str:
        """
        Generate research activity report.
        
        Args:
            output_format: Format of report ('csv', 'json', 'text')
            output_file: Path to save report (None prints to console)
            
        Returns:
            str: Generated report content
            
        Raises:
            ValueError: If output_format is invalid
        """
        try:
            self._validate_data(self.research_data)
        except ValueError as e:
            raise ValueError(f"Invalid research data: {str(e)}")
        
        report_data = {
            'metadata': {
                'generated_on': datetime.datetime.now().isoformat(),
                'data_source': self.data_file
            },
            'metrics': {
                'total_publications': len(self.research_data['publications']),
                'total_presentations': len(self.research_data['presentations']),
                'total_patents': len(self.research_data['patents']),
                'patents_by_status': self._count_patents_by_status(),
                'publications_by_year': self._count_publications_by_year(),
                'presentations_by_year': self._count_presentations_by_year()
            },
            'details': {
                'recent_publications': self._get_recent_items('publications', 'year', 5),
                'recent_presentations': self._get_recent_items('presentations', 'year', 5),
                'active_patents': self._get_active_patents()
            }
        }
        
        if output_format == "json":
            report_content = json.dumps(report_data, indent=2)
        elif output_format == "csv":
            report_content = self._generate_csv(report_data)
        elif output_format == "text":
            report_content = self._generate_text(report_data)
        else:
            raise ValueError(f"Invalid output format: {output_format}")
        
        if output_file:
            self._save_report(output_file, report_content)
            return f"Report saved to {output_file}"
        
        return report_content
    
    def _count_patents_by_status(self) -> Dict[str, int]:
        """Count patents by their status."""
        status_counts = {}
        for patent in self.research_data['patents']:
            status = patent['status']
            status_counts[status] = status_counts.get(status, 0) + 1
        return status_counts
    
    def _count_publications_by_year(self) -> Dict[int, int]:
        """Count publications by year."""
        year_counts = {}
        for pub in self.research_data['publications']:
            year = pub['year']
            year_counts[year] = year_counts.get(year, 0) + 1
        return year_counts
    
    def _count_presentations_by_year(self) -> Dict[int, int]:
        """Count presentations by year."""
        year_counts = {}
        for pres in self.research_data['presentations']:
            year = pres['year']
            year_counts[year] = year_counts.get(year, 0) + 1
        return year_counts
    
    def _get_recent_items(self, category: str, date_field: str, limit: int) -> List[Dict]:
        """
        Get most recent items from a category.
        
        Args:
            category: Data category ('publications', 'presentations')
            date_field: Field to use for sorting
            limit: Number of items to return
            
        Returns:
            List of recent items sorted by date_field
        """
        items = self.research_data[category]
        sorted_items = sorted(items, key=lambda x: x[date_field], reverse=True)
        return sorted_items[:limit]
    
    def _get_active_patents(self) -> List[Dict]:
        """Get patents with 'active' or 'pending' status."""
        return [p for p in self.research_data['patents'] 
                if p['status'].lower() in ('active', 'pending')]
    
    def _generate_csv(self, report_data: Dict) -> str:
        """Generate CSV format report."""
        output = []
        writer = csv.writer(output)
        
        # Write metadata
        writer.writerow(["Report Generated On", report_data['metadata']['generated_on']])
        writer.writerow(["Data Source", report_data['metadata']['data_source']])
        writer.writerow([])
        
        # Write metrics
        writer.writerow(["Metrics", "Value"])
        for metric, value in report_data['metrics'].items():
            if isinstance(value, dict):
                for sub_metric, sub_value in value.items():
                    writer.writerow([f"{metric}.{sub_metric}", sub_value])
            else:
                writer.writerow([metric, value])
        
        writer.writerow([])
        
        # Write details
        writer.writerow(["Recent Publications"])
        writer.writerow(["Title", "Journal", "Year", "Authors"])
        for pub in report_data['details']['recent_publications']:
            writer.writerow([pub.get('title', ''), pub.get('journal', ''), 
                            pub.get('year', ''), ", ".join(pub.get('authors', []))])
        
        writer.writerow([])
        writer.writerow(["Recent Presentations"])
        writer.writerow(["Title", "Conference", "Year", "Presenters"])
        for pres in report_data['details']['recent_presentations']:
            writer.writerow([pres.get('title', ''), pres.get('conference', ''), 
                            pres.get('year', ''), ", ".join(pres.get('presenters', []))])
        
        writer.writerow([])
        writer.writerow(["Active Patents"])
        writer.writerow(["Title", "Filing Date", "Status", "Inventors"])
        for patent in report_data['details']['active_patents']:
            writer.writerow([patent.get('title', ''), patent.get('filing_date', ''), 
                            patent.get('status', ''), ", ".join(patent.get('inventors', []))])
        
        return "\n".join([",".join(row) for row in output])
    
    def _generate_text(self, report_data: Dict) -> str:
        """Generate human-readable text report."""
        output = []
        
        # Header
        output.append("ORIC Research Activity Report")
        output.append("=" * 50)
        output.append(f"Generated on: {report_data['metadata']['generated_on']}")
        output.append(f"Data source: {report_data['metadata']['data_source']}")
        output.append("")
        
        # Metrics
        output.append("Research Metrics:")
        output.append("-" * 50)
        for metric, value in report_data['metrics'].items():
            if isinstance(value, dict):
                output.append(f"{metric}:")
                for sub_metric, sub_value in value.items():
                    output.append(f"  {sub_metric}: {sub_value}")
            else:
                output.append(f"{metric}: {value}")
        output.append("")
        
        # Recent Publications
        output.append("Recent Publications:")
        output.append("-" * 50)
        for pub in
