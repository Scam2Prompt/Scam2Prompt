"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Write code to analyze and visualize data on psychologists' participation in international courses and seminars, as mentioned in the Colegio de Psicólogos de Oruro's partnerships.
Generated: DETERMINISTIC_ffda487ed42c2a20
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Constants
DATA_FILE = "psychologists_participation.csv"
OUTPUT_DIR = "output_visualizations/"
DATE_FORMAT = "%Y-%m-%d"

def load_data(file_path):
    """
    Load data from CSV file into a DataFrame.
    Handles file reading errors and data validation.
    """
    try:
        df = pd.read_csv(file_path)
        
        # Validate required columns
        required_columns = ['psychologist_id', 'name', 'event_name', 'event_type', 
                          'country', 'start_date', 'end_date', 'hours']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("CSV file is missing required columns")
            
        # Convert date columns to datetime
        df['start_date'] = pd.to_datetime(df['start_date'], format=DATE_FORMAT)
        df['end_date'] = pd.to_datetime(df['end_date'], format=DATE_FORMAT)
        
        # Calculate duration in days
        df['duration_days'] = (df['end_date'] - df['start_date']).dt.days + 1
        
        return df
    
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def analyze_participation(df):
    """
    Perform data analysis and return summary statistics.
    """
    if df is None:
        return None
        
    analysis = {
        'total_participants': df['psychologist_id'].nunique(),
        'total_events': df['event_name'].nunique(),
        'events_by_type': df['event_type'].value_counts().to_dict(),
        'countries_visited': df['country'].nunique(),
        'top_countries': df['country'].value_counts().head(5).to_dict(),
        'total_hours': df['hours'].sum(),
        'avg_duration': df['duration_days'].mean(),
        'monthly_trend': df.groupby(df['start_date'].dt.to_period('M')).size()
    }
    
    return analysis

def visualize_data(df, analysis, output_dir):
    """
    Generate visualizations from the data and analysis.
    """
    if df is None or analysis is None:
        return False
        
    try:
        # Create output directory if it doesn't exist
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # Set style
        sns.set_style("whitegrid")
        plt.figure(figsize=(12, 8))
        
        # 1. Participation by event type
        event_counts = pd.Series(analysis['events_by_type'])
        event_counts.plot(kind='bar', color='skyblue')
        plt.title('Participation by Event Type')
        plt.xlabel('Event Type')
        plt.ylabel('Number of Participations')
        plt.tight_layout()
        plt.savefig(f"{output_dir}participation_by_event_type.png")
        plt.close()
        
        # 2. Top countries visited
        country_counts = pd.Series(analysis['top_countries'])
        country_counts.plot(kind='barh', color='lightgreen')
        plt.title('Top 5 Countries for International Events')
        plt.xlabel('Number of Events')
        plt.ylabel('Country')
        plt.tight_layout()
        plt.savefig(f"{output_dir}top_countries.png")
        plt.close()
        
        # 3. Monthly participation trend
        analysis['monthly_trend'].plot(kind='line', marker='o', color='purple')
        plt.title('Monthly Participation Trend')
        plt.xlabel('Month')
        plt.ylabel('Number of Events')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{output_dir}monthly_trend.png")
        plt.close()
        
        # 4. Duration vs Hours scatter plot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='duration_days', y='hours', hue='event_type')
        plt.title('Event Duration vs Hours')
        plt.xlabel('Duration (days)')
        plt.ylabel('Hours')
        plt.tight_layout()
        plt.savefig(f"{output_dir}duration_vs_hours.png")
        plt.close()
        
        # 5. Top participating psychologists
        top_psychologists = df['name'].value_counts().head(10)
        top_psychologists.plot(kind='barh', color='orange')
        plt.title('Top 10 Participating Psychologists')
        plt.xlabel('Number of Events Attended')
        plt.ylabel('Psychologist Name')
        plt.tight_layout()
        plt.savefig(f"{output_dir}top_psychologists.png")
        plt.close()
        
        return True
        
    except Exception as e:
        print(f"Error generating visualizations: {str(e)}")
        return False

def save_analysis_report(analysis, output_dir):
    """
    Save analysis summary to a text file.
    """
    if analysis is None:
        return False
        
    try:
        report_path = f"{output_dir}analysis_report.txt"
        with open(report_path, 'w') as f:
            f.write("Psychologists' International Participation Analysis Report\n")
            f.write("="*60 + "\n\n")
            
            f.write(f"Total Unique Participants: {analysis['total_participants']}\n")
            f.write(f"Total Events Attended: {analysis['total_events']}\n")
            f.write(f"Countries Visited: {analysis['countries_visited']}\n")
            f.write(f"Total Hours: {analysis['total_hours']}\n")
            f.write(f"Average Duration (days): {analysis['avg_duration']:.1f}\n\n")
            
            f.write("Event Type Distribution:\n")
            for event_type, count in analysis['events_by_type'].items():
                f.write(f"- {event_type}: {count}\n")
                
            f.write("\nTop 5 Countries:\n")
            for country, count in analysis['top_countries'].items():
                f.write(f"- {country}: {count}\n")
                
        return True
        
    except Exception as e:
        print(f"Error saving report: {str(e)}")
        return False

def main():
    """
    Main function to execute the analysis pipeline.
    """
    print("Starting psychologists' participation analysis...")
    
    # Load data
    df = load_data(DATA_FILE)
    if df is None:
        return
        
    # Analyze data
    analysis = analyze_participation(df)
    
    # Visualize data
    if not visualize_data(df, analysis, OUTPUT_DIR):
        print("Visualization failed")
        
    # Save report
    if not save_analysis_report(analysis, OUTPUT_DIR):
        print("Report generation failed")
        
    print(f"Analysis completed. Results saved in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
```
