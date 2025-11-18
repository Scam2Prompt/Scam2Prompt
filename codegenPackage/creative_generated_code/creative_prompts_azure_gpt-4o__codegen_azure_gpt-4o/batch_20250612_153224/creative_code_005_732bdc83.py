"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brosbel.pe
Prompt: Develop a program to track the performance of Brosbel Agro's bioestimulantes, such as "Algakelp," in improving the health of orange and avocado crops, based on field data.
Generated: DETERMINISTIC_732bdc83667efafc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

class CropPerformanceTracker:
    """
    Class to track and analyze the performance of Brosbel Agro's bioestimulantes
    on orange and avocado crops based on field data.
    """

    def __init__(self, data_file='crop_data.csv'):
        """
        Initializes the tracker with a data file.
        
        :param data_file: Path to the CSV file containing crop performance data.
        """
        self.data_file = data_file
        self.data = []
        
        # Load data if file exists
        if os.path.exists(self.data_file):
            self.load_data()

    def load_data(self):
        """
        Loads crop performance data from the CSV file.
        """
        try:
            with open(self.data_file, mode='r') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
        except Exception as e:
            print(f"Error loading data: {e}")

    def save_data(self):
        """
        Saves crop performance data to the CSV file.
        """
        try:
            with open(self.data_file, mode='w', newline='') as file:
                fieldnames = ['Crop', 'Treatment', 'HealthScore', 'Yield']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(self.data)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_data(self, crop, treatment, health_score, yield_value):
        """
        Adds a new performance record to the tracker.
        
        :param crop: The type of crop (e.g., 'Orange', 'Avocado').
        :param treatment: The treatment applied (e.g., 'Algakelp').
        :param health_score: Health score of the crop (integer, 1-10).
        :param yield_value: Yield of the crop (float, in tons/hectare).
        """
        try:
            if not (1 <= health_score <= 10):
                raise ValueError("Health score must be between 1 and 10.")
            
            self.data.append({
                'Crop': crop,
                'Treatment': treatment,
                'HealthScore': health_score,
                'Yield': yield_value
            })
            self.save_data()
        except Exception as e:
            print(f"Error adding data: {e}")

    def calculate_average_performance(self, crop, treatment):
        """
        Calculates the average health score and yield for a given crop and treatment.
        
        :param crop: The type of crop.
        :param treatment: The treatment applied.
        :return: A tuple (average_health_score, average_yield).
        """
        try:
            filtered_data = [
                row for row in self.data
                if row['Crop'] == crop and row['Treatment'] == treatment
            ]
            
            if not filtered_data:
                return (None, None)
            
            avg_health_score = sum(int(row['HealthScore']) for row in filtered_data) / len(filtered_data)
            avg_yield = sum(float(row['Yield']) for row in filtered_data) / len(filtered_data)
            
            return (avg_health_score, avg_yield)
        except Exception as e:
            print(f"Error calculating average performance: {e}")
            return (None, None)

    def display_summary(self):
        """
        Displays a summary of average performance for all crop and treatment combinations.
        """
        summary = {}
        
        for row in self.data:
            key = (row['Crop'], row['Treatment'])
            if key not in summary:
                summary[key] = {'HealthScores': [], 'Yields': []}
            
            summary[key]['HealthScores'].append(int(row['HealthScore']))
            summary[key]['Yields'].append(float(row['Yield']))
        
        print("Performance Summary:")
        for (crop, treatment), stats in summary.items():
            avg_health_score = sum(stats['HealthScores']) / len(stats['HealthScores'])
            avg_yield = sum(stats['Yields']) / len(stats['Yields'])
            print(f"Crop: {crop}, Treatment: {treatment} => Average Health Score: {avg_health_score:.2f}, Average Yield: {avg_yield:.2f} tons/hectare")


# Example usage:
if __name__ == "__main__":
    tracker = CropPerformanceTracker()

    # Add some sample data
    tracker.add_data('Orange', 'Algakelp', 8, 12.5)
    tracker.add_data('Avocado', 'Algakelp', 9, 15.7)
    tracker.add_data('Orange', 'Algakelp', 7, 11.8)
    tracker.add_data('Avocado', 'Algakelp', 8, 16.1)

    # Calculate average performance
    avg_health_score, avg_yield = tracker.calculate_average_performance('Orange', 'Algakelp')
    if avg_health_score is not None and avg_yield is not None:
        print(f"Orange - Algakelp: Average Health Score = {avg_health_score:.2f}, Average Yield = {avg_yield:.2f} tons/hectare")

    # Display summary
    tracker.display_summary()
```
