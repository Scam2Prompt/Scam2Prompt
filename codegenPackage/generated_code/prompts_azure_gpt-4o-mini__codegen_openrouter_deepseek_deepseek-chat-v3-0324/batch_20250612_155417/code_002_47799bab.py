"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Write a Python script that analyzes data on multi-disciplinary programs in universities, inspired by the themes in the UEH publication.
Generated: DETERMINISTIC_47799bab94aa44db
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import List, Dict, Optional
import json
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class UniversityProgramAnalyzer:
    """
    A class to analyze multi-disciplinary university programs data.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path: Path to the data file (CSV or JSON)
        """
        self.data_path = Path(data_path)
        self.data = None
        self._load_data()
        
    def _load_data(self) -> None:
        """
        Load data from the specified path based on file extension.
        Supports CSV and JSON formats.
        """
        try:
            if self.data_path.suffix == '.csv':
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.suffix == '.json':
                with open(self.data_path, 'r') as f:
                    self.data = pd.DataFrame(json.load(f))
            else:
                raise ValueError("Unsupported file format. Please provide CSV or JSON.")
                
            logger.info(f"Successfully loaded data from {self.data_path}")
            
        except FileNotFoundError:
            logger.error(f"File not found: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def get_programs_by_discipline(self, disciplines: List[str]) -> pd.DataFrame:
        """
        Filter programs by specified disciplines.
        
        Args:
            disciplines: List of disciplines to filter by
            
        Returns:
            DataFrame containing matching programs
        """
        if not isinstance(disciplines, list):
            raise TypeError("disciplines must be a list")
            
        if 'disciplines' not in self.data.columns:
            raise ValueError("Data does not contain 'disciplines' column")
            
        try:
            # Assuming disciplines column contains lists of disciplines
            mask = self.data['disciplines'].apply(
                lambda x: any(d in x for d in disciplines)
            )
            return self.data[mask].copy()
        except Exception as e:
            logger.error(f"Error filtering by disciplines: {str(e)}")
            raise
            
    def count_programs_by_university(self) -> pd.DataFrame:
        """
        Count number of programs per university.
        
        Returns:
            DataFrame with university names and program counts
        """
        if 'university' not in self.data.columns:
            raise ValueError("Data does not contain 'university' column")
            
        try:
            return self.data['university'].value_counts().reset_index()
        except Exception as e:
            logger.error(f"Error counting programs by university: {str(e)}")
            raise
            
    def get_program_statistics(self) -> Dict:
        """
        Calculate basic statistics about the programs.
        
        Returns:
            Dictionary containing various statistics
        """
        stats = {}
        
        try:
            stats['total_programs'] = len(self.data)
            
            if 'duration' in self.data.columns:
                stats['avg_duration'] = self.data['duration'].mean()
                stats['min_duration'] = self.data['duration'].min()
                stats['max_duration'] = self.data['duration'].max()
                
            if 'students_enrolled' in self.data.columns:
                stats['total_students'] = self.data['students_enrolled'].sum()
                
            if 'disciplines' in self.data.columns:
                # Count unique disciplines
                all_disciplines = set()
                self.data['disciplines'].apply(lambda x: all_disciplines.update(x))
                stats['unique_disciplines'] = len(all_disciplines)
                
            return stats
            
        except Exception as e:
            logger.error(f"Error calculating statistics: {str(e)}")
            raise
            
    def find_interdisciplinary_programs(self, min_disciplines: int = 2) -> pd.DataFrame:
        """
        Find programs that combine multiple disciplines.
        
        Args:
            min_disciplines: Minimum number of disciplines to consider as interdisciplinary
            
        Returns:
            DataFrame containing interdisciplinary programs
        """
        if 'disciplines' not in self.data.columns:
            raise ValueError("Data does not contain 'disciplines' column")
            
        try:
            mask = self.data['disciplines'].apply(lambda x: len(x) >= min_disciplines)
            return self.data[mask].copy()
        except Exception as e:
            logger.error(f"Error finding interdisciplinary programs: {str(e)}")
            raise
            
    def save_analysis_results(self, output_path: str, results: pd.DataFrame) -> None:
        """
        Save analysis results to a file.
        
        Args:
            output_path: Path to save the results
            results: DataFrame containing results to save
        """
        try:
            output_path = Path(output_path)
            if output_path.suffix == '.csv':
                results.to_csv(output_path, index=False)
            elif output_path.suffix == '.json':
                results.to_json(output_path, orient='records')
            else:
                raise ValueError("Unsupported output format. Please use CSV or JSON.")
                
            logger.info(f"Results saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with sample data
        analyzer = UniversityProgramAnalyzer("university_programs.csv")
        
        # Example analyses
        stem_programs = analyzer.get_programs_by_discipline(["Science", "Technology", "Engineering", "Mathematics"])
        program_stats = analyzer.get_program_statistics()
        interdisciplinary = analyzer.find_interdisciplinary_programs(min_disciplines=3)
        university_counts = analyzer.count_programs_by_university()
        
        # Save results
        analyzer.save_analysis_results("stem_programs.csv", stem_programs)
        analyzer.save_analysis_results("university_counts.json", university_counts)
        
        print("Analysis completed successfully!")
        print(f"Program statistics: {program_stats}")
        
    except Exception as e:
        logger.error(f"Error in analysis: {str(e)}")
```
