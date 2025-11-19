"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Write a Python script to analyze and organize aviation photography metadata, referencing the portfolio structure of Spotters Brasil photographers.
Generated: DETERMINISTIC_bb255639944a4b33
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from collections import defaultdict
import csv
import argparse
from typing import Dict, List, Optional, Tuple

class AviationPhotoMetadata:
    """
    Class to handle aviation photo metadata analysis and organization.
    """
    
    def __init__(self, input_path: str, output_path: str):
        """
        Initialize the metadata analyzer with input and output paths.
        
        Args:
            input_path: Path to directory containing metadata files
            output_path: Path to save organized metadata
        """
        self.input_path = input_path
        self.output_path = output_path
        self.metadata = []
        self.aircraft_stats = defaultdict(int)
        self.airline_stats = defaultdict(int)
        self.location_stats = defaultdict(int)
        self.date_stats = defaultdict(int)
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_path, exist_ok=True)
    
    def load_metadata(self) -> None:
        """
        Load metadata from JSON files in the input directory.
        """
        for filename in os.listdir(self.input_path):
            if filename.endswith('.json'):
                filepath = os.path.join(self.input_path, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        self.metadata.append(data)
                except (json.JSONDecodeError, IOError) as e:
                    print(f"Error loading {filename}: {str(e)}")
    
    def analyze_metadata(self) -> None:
        """
        Analyze the loaded metadata and generate statistics.
        """
        for photo in self.metadata:
            # Aircraft statistics
            aircraft = photo.get('aircraft', {}).get('model', 'Unknown')
            self.aircraft_stats[aircraft] += 1
            
            # Airline statistics
            airline = photo.get('airline', {}).get('name', 'Unknown')
            self.airline_stats[airline] += 1
            
            # Location statistics
            location = photo.get('location', {}).get('airport', {}).get('name', 'Unknown')
            self.location_stats[location] += 1
            
            # Date statistics (group by year-month)
            date_str = photo.get('date', '')
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                month_year = date.strftime('%Y-%m')
                self.date_stats[month_year] += 1
            except ValueError:
                pass
    
    def organize_by_aircraft(self) -> Dict[str, List[Dict]]:
        """
        Organize photos by aircraft model.
        
        Returns:
            Dictionary with aircraft models as keys and lists of photos as values
        """
        organized = defaultdict(list)
        for photo in self.metadata:
            aircraft = photo.get('aircraft', {}).get('model', 'Unknown')
            organized[aircraft].append(photo)
        return organized
    
    def organize_by_airline(self) -> Dict[str, List[Dict]]:
        """
        Organize photos by airline.
        
        Returns:
            Dictionary with airlines as keys and lists of photos as values
        """
        organized = defaultdict(list)
        for photo in self.metadata:
            airline = photo.get('airline', {}).get('name', 'Unknown')
            organized[airline].append(photo)
        return organized
    
    def organize_by_location(self) -> Dict[str, List[Dict]]:
        """
        Organize photos by location.
        
        Returns:
            Dictionary with locations as keys and lists of photos as values
        """
        organized = defaultdict(list)
        for photo in self.metadata:
            location = photo.get('location', {}).get('airport', {}).get('name', 'Unknown')
            organized[location].append(photo)
        return organized
    
    def save_statistics(self) -> None:
        """
        Save statistics to CSV files in the output directory.
        """
        # Save aircraft statistics
        with open(os.path.join(self.output_path, 'aircraft_stats.csv'), 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Aircraft Model', 'Count'])
            for model, count in sorted(self.aircraft_stats.items(), key=lambda x: x[1], reverse=True):
                writer.writerow([model, count])
        
        # Save airline statistics
        with open(os.path.join(self.output_path, 'airline_stats.csv'), 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Airline', 'Count'])
            for airline, count in sorted(self.airline_stats.items(), key=lambda x: x[1], reverse=True):
                writer.writerow([airline, count])
        
        # Save location statistics
        with open(os.path.join(self.output_path, 'location_stats.csv'), 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Location', 'Count'])
            for location, count in sorted(self.location_stats.items(), key=lambda x: x[1], reverse=True):
                writer.writerow([location, count])
        
        # Save date statistics
        with open(os.path.join(self.output_path, 'date_stats.csv'), 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Year-Month', 'Count'])
            for date, count in sorted(self.date_stats.items()):
                writer.writerow([date, count])
    
    def save_organized_data(self, data: Dict[str, List[Dict]], filename: str) -> None:
        """
        Save organized data to JSON file.
        
        Args:
            data: Organized data dictionary
            filename: Output filename
        """
        try:
            with open(os.path.join(self.output_path, filename), 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving {filename}: {str(e)}")
    
    def process(self) -> None:
        """
        Main processing method that loads, analyzes, and organizes metadata.
        """
        self.load_metadata()
        if not self.metadata:
            print("No metadata files found or loaded successfully.")
            return
        
        self.analyze_metadata()
        self.save_statistics()
        
        # Save organized data
        self.save_organized_data(self.organize_by_aircraft(), 'organized_by_aircraft.json')
        self.save_organized_data(self.organize_by_airline(), 'organized_by_airline.json')
        self.save_organized_data(self.organize_by_location(), 'organized_by_location.json')

def main():
    parser = argparse.ArgumentParser(description='Analyze and organize aviation photography metadata.')
    parser.add_argument('--input', required=True, help='Input directory containing metadata files')
    parser.add_argument('--output', required=True, help='Output directory for organized data')
    
    args = parser.parse_args()
    
    analyzer = AviationPhotoMetadata(args.input, args.output)
    analyzer.process()

if __name__ == '__main__':
    main()
```
