"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Develop a Python program to analyze the impact of Rakhshanda Memorial's projects, including statistics on lives impacted, food packs distributed, and volunteers engaged.
Generated: DETERMINISTIC_a80bfd2331f02b70
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
from datetime import datetime
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import pandas as pd


class ProjectAnalyzer:
    """
    Analyzes impact data for Rakhshanda Memorial projects.
    Handles data loading, analysis, and visualization.
    """

    def __init__(self, data_file: str = "project_data.json"):
        """
        Initialize the analyzer with data file path.
        
        Args:
            data_file: Path to JSON file containing project data
        """
        self.data_file = data_file
        self.projects = self._load_data()
        self._validate_data()

    def _load_data(self) -> List[Dict]:
        """
        Load project data from JSON file.
        
        Returns:
            List of project dictionaries
            
        Raises:
            FileNotFoundError: If data file doesn't exist
            json.JSONDecodeError: If file contains invalid JSON
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {self.data_file} not found")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in {self.data_file}", e.doc, e.pos)

    def _validate_data(self):
        """
        Validate loaded project data structure.
        
        Raises:
            ValueError: If required fields are missing or invalid
        """
        required_fields = {
            'project_name': str,
            'start_date': str,
            'lives_impacted': int,
            'food_packs_distributed': int,
            'volunteers_engaged': int
        }

        for project in self.projects:
            for field, field_type in required_fields.items():
                if field not in project:
                    raise ValueError(f"Missing required field: {field}")
                if not isinstance(project[field], field_type):
                    raise ValueError(f"Invalid type for {field}. Expected {field_type}, got {type(project[field])}")

    def get_total_impact(self) -> Dict[str, int]:
        """
        Calculate total impact across all projects.
        
        Returns:
            Dictionary with total lives impacted, food packs distributed, and volunteers engaged
        """
        totals = {
            'total_lives_impacted': 0,
            'total_food_packs_distributed': 0,
            'total_volunteers_engaged': 0
        }

        for project in self.projects:
            totals['total_lives_impacted'] += project['lives_impacted']
            totals['total_food_packs_distributed'] += project['food_packs_distributed']
            totals['total_volunteers_engaged'] += project['volunteers_engaged']

        return totals

    def get_project_statistics(self) -> pd.DataFrame:
        """
        Generate statistics for all projects.
        
        Returns:
            Pandas DataFrame with project statistics
        """
        stats = []
        for project in self.projects:
            stats.append({
                'Project': project['project_name'],
                'Start Date': project['start_date'],
                'Lives Impacted': project['lives_impacted'],
                'Food Packs Distributed': project['food_packs_distributed'],
                'Volunteers Engaged': project['volunteers_engaged']
            })

        return pd.DataFrame(stats)

    def export_to_csv(self, filename: str = "project_statistics.csv"):
        """
        Export project statistics to CSV file.
        
        Args:
            filename: Output CSV file path
            
        Raises:
            IOError: If file cannot be written
        """
        df = self.get_project_statistics()
        try:
            df.to_csv(filename, index=False)
        except IOError as e:
            raise IOError(f"Failed to write CSV file: {e}")

    def plot_impact_comparison(self, output_file: Optional[str] = None):
        """
        Create bar chart comparing impact metrics across projects.
        
        Args:
            output_file: Optional path to save the plot image
        """
        df = self.get_project_statistics()
        
        plt.figure(figsize=(12, 6))
        ax = df.plot(
            x='Project',
            y=['Lives Impacted', 'Food Packs Distributed', 'Volunteers Engaged'],
            kind='bar',
            stacked=False,
            title='Project Impact Comparison'
        )
        
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, bbox_inches='tight')
        else:
            plt.show()

    def generate_summary_report(self, output_file: Optional[str] = None):
        """
        Generate a comprehensive text report of project impacts.
        
        Args:
            output_file: Optional path to save the report as text file
        """
        totals = self.get_total_impact()
        df = self.get_project_statistics()
        
        report = [
            "Rakhshanda Memorial Project Impact Report",
            "========================================",
            f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            f"Total Lives Impacted: {totals['total_lives_impacted']:,}",
            f"Total Food Packs Distributed: {totals['total_food_packs_distributed']:,}",
            f"Total Volunteers Engaged: {totals['total_volunteers_engaged']:,}",
            "",
            "Project Details:",
            "---------------"
        ]
        
        # Add project details
        for _, row in df.iterrows():
            report.append(
                f"{row['Project']} (Started: {row['Start Date']}): "
                f"{row['Lives Impacted']:,} lives, "
                f"{row['Food Packs Distributed']:,} food packs, "
                f"{row['Volunteers Engaged']:,} volunteers"
            )
        
        full_report = "\n".join(report)
        
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(full_report)
            except IOError as e:
                raise IOError(f"Failed to write report file: {e}")
        else:
            print(full_report)


def main():
    try:
        analyzer = ProjectAnalyzer()
        
        # Display total impact
        totals = analyzer.get_total_impact()
        print("\nTotal Impact:")
        print(f"Lives Impacted: {totals['total_lives_impacted']:,}")
        print(f"Food Packs Distributed: {totals['total_food_packs_distributed']:,}")
        print(f"Volunteers Engaged: {totals['total_volunteers_engaged']:,}")
        
        # Generate and display statistics
        print("\nProject Statistics:")
        print(analyzer.get_project_statistics().to_string(index=False))
        
        # Export data
        analyzer.export_to_csv()
        print("\nExported project statistics to CSV")
        
        # Generate visualizations
        analyzer.plot_impact_comparison("impact_comparison.png")
        print("Generated impact comparison chart")
        
        # Generate full report
        analyzer.generate_summary_report("impact_report.txt")
        print("Generated full impact report")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
```
