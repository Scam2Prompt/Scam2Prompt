"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: Generate a script to analyze migration testing results for food contact materials, including plastics and ceramics, as described by Northern Testhouse's testing services.
Generated: DETERMINISTIC_857e31a1b2e19d4a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Migration Testing Results Analyzer for Food Contact Materials (FCM)

This script analyzes migration testing results for food contact materials,
including plastics and ceramics, based on Northern Testhouse's testing services.

Key Features:
- Parses test results from CSV files
- Validates data against regulatory limits
- Generates summary reports
- Provides visualization of results
"""

import csv
import json
import argparse
from datetime import datetime
from typing import List, Dict, Tuple, Optional
import matplotlib.pyplot as plt
import numpy as np
from enum import Enum, auto


class MaterialType(Enum):
    """Enumeration of food contact material types."""
    PLASTIC = auto()
    CERAMIC = auto()
    METAL = auto()
    PAPER = auto()
    OTHER = auto()


class MigrationResult:
    """Class representing a single migration test result."""
    
    def __init__(self, sample_id: str, material: MaterialType, 
                 substance: str, concentration: float, 
                 test_date: str, limit: Optional[float] = None):
        """
        Initialize a migration test result.
        
        Args:
            sample_id: Unique identifier for the sample
            material: Material type (from MaterialType enum)
            substance: Name of the migrated substance
            concentration: Measured concentration (mg/kg)
            test_date: Date of testing (YYYY-MM-DD)
            limit: Regulatory limit (mg/kg), optional
        """
        self.sample_id = sample_id
        self.material = material
        self.substance = substance
        self.concentration = concentration
        self.test_date = datetime.strptime(test_date, "%Y-%m-%d").date()
        self.limit = limit
        
    def is_compliant(self) -> bool:
        """Check if the result is within regulatory limits."""
        if self.limit is None:
            return True
        return self.concentration <= self.limit
    
    def to_dict(self) -> Dict:
        """Convert result to dictionary for serialization."""
        return {
            "sample_id": self.sample_id,
            "material": self.material.name,
            "substance": self.substance,
            "concentration": self.concentration,
            "test_date": self.test_date.strftime("%Y-%m-%d"),
            "limit": self.limit,
            "is_compliant": self.is_compliant()
        }


class MigrationAnalyzer:
    """Main class for analyzing migration test results."""
    
    def __init__(self):
        self.results: List[MigrationResult] = []
        self.substance_limits: Dict[str, float] = {}
        
    def load_limits(self, limits_file: str) -> None:
        """
        Load regulatory limits from a JSON file.
        
        Args:
            limits_file: Path to JSON file containing substance limits
        """
        try:
            with open(limits_file, 'r') as f:
                self.substance_limits = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading limits file: {str(e)}")
    
    def load_results(self, results_file: str) -> None:
        """
        Load test results from a CSV file.
        
        Args:
            results_file: Path to CSV file containing test results
        """
        try:
            with open(results_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        material = MaterialType[row['material'].upper()]
                        substance = row['substance']
                        limit = self.substance_limits.get(substance)
                        
                        result = MigrationResult(
                            sample_id=row['sample_id'],
                            material=material,
                            substance=substance,
                            concentration=float(row['concentration']),
                            test_date=row['test_date'],
                            limit=limit
                        )
                        self.results.append(result)
                    except (KeyError, ValueError) as e:
                        print(f"Skipping invalid row: {row}. Error: {str(e)}")
        except FileNotFoundError as e:
            raise ValueError(f"Error loading results file: {str(e)}")
    
    def get_compliance_rate(self) -> float:
        """Calculate overall compliance rate (0-1)."""
        if not self.results:
            return 0.0
            
        compliant = sum(1 for r in self.results if r.is_compliant())
        return compliant / len(self.results)
    
    def get_material_compliance(self) -> Dict[MaterialType, float]:
        """Calculate compliance rates by material type."""
        material_counts: Dict[MaterialType, int] = {}
        material_compliant: Dict[MaterialType, int] = {}
        
        for result in self.results:
            material_counts[result.material] = material_counts.get(result.material, 0) + 1
            if result.is_compliant():
                material_compliant[result.material] = material_compliant.get(result.material, 0) + 1
        
        return {
            mat: (material_compliant.get(mat, 0) / count if count > 0 else 0)
            for mat, count in material_counts.items()
        }
    
    def get_substance_violations(self) -> Dict[str, int]:
        """Count violations by substance."""
        violations: Dict[str, int] = {}
        
        for result in self.results:
            if not result.is_compliant():
                violations[result.substance] = violations.get(result.substance, 0) + 1
        
        return violations
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive report of analysis results."""
        return {
            "total_samples": len(self.results),
            "compliance_rate": self.get_compliance_rate(),
            "material_compliance": {
                mat.name: rate 
                for mat, rate in self.get_material_compliance().items()
            },
            "substance_violations": self.get_substance_violations(),
            "non_compliant_samples": [
                r.to_dict() 
                for r in self.results 
                if not r.is_compliant()
            ]
        }
    
    def plot_compliance_by_material(self, output_file: str) -> None:
        """Generate a bar plot of compliance rates by material type."""
        compliance = self.get_material_compliance()
        materials = [mat.name for mat in compliance.keys()]
        rates = list(compliance.values())
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(materials, rates, color=['green' if r > 0.9 else 'orange' if r > 0.7 else 'red' for r in rates])
        plt.ylabel('Compliance Rate')
        plt.title('Compliance Rates by Material Type')
        plt.ylim(0, 1.1)
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1%}',
                    ha='center', va='bottom')
        
        plt.savefig(output_file)
        plt.close()
    
    def plot_violations_by_substance(self, output_file: str, top_n: int = 10) -> None:
        """Generate a bar plot of top violating substances."""
        violations = self.get_substance_violations()
        sorted_violations = sorted(violations.items(), key=lambda x: x[1], reverse=True)[:top_n]
        
        if not sorted_violations:
            return
            
        substances, counts = zip(*sorted_violations)
        
        plt.figure(figsize=(12, 6))
        bars = plt.bar(substances, counts, color='red')
        plt.ylabel('Number of Violations')
        plt.title(f'Top {top_n} Substances with Regulatory Violations')
        plt.xticks(rotation=45, ha='right')
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    str(int(height)),
                    ha='center', va='bottom')
        
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()


def main():
    """Main function for command-line execution."""
    parser = argparse.ArgumentParser(
        description='Analyze migration testing results for food contact materials.'
    )
    parser.add_argument('results_file', help='CSV file containing test results')
    parser.add_argument('limits_file', help='JSON file containing regulatory limits')
    parser.add_argument('--report', help='Output JSON report file', default='report.json')
    parser.add_argument('--material-plot', help='Output material compliance plot file', 
                        default='material_compliance.png')
    parser.add_argument('--substance-plot', help='Output substance violations plot file', 
                        default='substance_violations.png')
    
    args = parser.parse_args()
    
    try:
        analyzer = MigrationAnalyzer()
        analyzer.load_limits(args.limits_file)
        analyzer.load_results(args.results_file)
        
        # Generate and save report
        report = analyzer.generate_report()
        with open(args.report, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Generate plots
        analyzer.plot_compliance_by_material(args.material
