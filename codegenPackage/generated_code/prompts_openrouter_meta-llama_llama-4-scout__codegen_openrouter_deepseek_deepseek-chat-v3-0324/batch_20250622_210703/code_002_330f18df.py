"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Generate a report on the effectiveness of a community development program, such as "مهارات المستقبل" (Future Skills), using data from the organization's annual reports and surveys.
Generated: DETERMINISTIC_330f18df947da57e
Batch ID: 20250622_210703
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
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Constants
ANNUAL_REPORT_PATH = 'data/annual_reports.csv'
SURVEY_DATA_PATH = 'data/survey_responses.csv'
OUTPUT_DIR = 'reports/'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_data():
    """Load and merge data from annual reports and surveys"""
    try:
        # Load annual report data
        annual_data = pd.read_csv(ANNUAL_REPORT_PATH, parse_dates=['year'])
        
        # Load survey data
        survey_data = pd.read_csv(SURVEY_DATA_PATH)
        
        # Merge data on year/program
        merged_data = pd.merge(
            annual_data, 
            survey_data, 
            on=['year', 'program_name'], 
            how='left'
        )
        
        return merged_data
    except FileNotFoundError as e:
        print(f"Error loading data files: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error loading data: {e}")
        return None

def clean_data(df):
    """Clean and preprocess the data"""
    if df is None:
        return None
        
    try:
        # Handle missing values
        df.fillna({
            'participants': 0,
            'graduation_rate': 0,
            'employment_rate': 0,
            'satisfaction_score': df['satisfaction_score'].median()
        }, inplace=True)
        
        # Filter for Future Skills program
        future_skills_data = df[df['program_name'] == 'مهارات المستقبل'].copy()
        
        # Calculate additional metrics
        future_skills_data['success_rate'] = (
            future_skills_data['graduation_rate'] * 
            future_skills_data['employment_rate']
        )
        
        return future_skills_data
    except Exception as e:
        print(f"Error cleaning data: {e}")
        return None

def generate_visualizations(df, program_name):
    """Generate visualizations for the report"""
    if df is None or df.empty:
        return False
        
    try:
        plt.figure(figsize=(12, 8))
        
        # Participation trend
        plt.subplot(2, 2, 1)
        plt.plot(df['year'], df['participants'], marker='o')
        plt.title('Participant Growth Over Time')
        plt.xlabel('Year')
        plt.ylabel('Number of Participants')
        
        # Success metrics
        plt.subplot(2, 2, 2)
        metrics = ['graduation_rate', 'employment_rate', 'success_rate']
        df.plot(x='year', y=metrics, kind='bar', ax=plt.gca())
        plt.title('Program Success Metrics')
        plt.xlabel('Year')
        plt.ylabel('Rate (%)')
        plt.legend(['Graduation', 'Employment', 'Overall Success'])
        
        # Satisfaction scores
        plt.subplot(2, 2, 3)
        plt.scatter(df['year'], df['satisfaction_score'], s=df['participants']/10)
        plt.title('Participant Satisfaction')
        plt.xlabel('Year')
        plt.ylabel('Satisfaction Score (1-10)')
        
        # Demographic breakdown
        plt.subplot(2, 2, 4)
        demo_cols = [col for col in df.columns if 'demo_' in col]
        demo_data = df[demo_cols].mean().sort_values()
        demo_data.plot(kind='barh')
        plt.title('Participant Demographics')
        plt.xlabel('Percentage')
        
        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}{program_name}_metrics.png')
        plt.close()
        
        return True
    except Exception as e:
        print(f"Error generating visualizations: {e}")
        return False

def generate_report(df, program_name):
    """Generate the full report with analysis and visualizations"""
    if df is None or df.empty:
        return False
        
    try:
        # Generate visualizations
        viz_success = generate_visualizations(df, program_name)
        
        # Calculate summary statistics
        summary_stats = {
            'total_participants': df['participants'].sum(),
            'avg_graduation_rate': df['graduation_rate'].mean(),
            'avg_employment_rate': df['employment_rate'].mean(),
            'avg_satisfaction': df['satisfaction_score'].mean(),
            'growth_rate': (
                (df['participants'].iloc[-1] - df['participants'].iloc[0]) / 
                df['participants'].iloc[0]
            ) * 100
        }
        
        # Generate HTML report
        report_content = f"""
        <html>
        <head>
            <title>{program_name} Program Effectiveness Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                h1, h2 {{ color: #2c3e50; }}
                .container {{ width: 80%; margin: 0 auto; }}
                .stats {{ background: #f9f9f9; padding: 20px; border-radius: 5px; }}
                .stat-item {{ margin-bottom: 10px; }}
                img {{ max-width: 100%; height: auto; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{program_name} Program Effectiveness Report</h1>
                <p>Generated on: {datetime.now().strftime('%Y-%m-%d')}</p>
                
                <h2>Program Summary</h2>
                <div class="stats">
                    <div class="stat-item"><strong>Total Participants:</strong> {summary_stats['total_participants']:,}</div>
                    <div class="stat-item"><strong>Average Graduation Rate:</strong> {summary_stats['avg_graduation_rate']:.1f}%</div>
                    <div class="stat-item"><strong>Average Employment Rate:</strong> {summary_stats['avg_employment_rate']:.1f}%</div>
                    <div class="stat-item"><strong>Average Satisfaction Score:</strong> {summary_stats['avg_satisfaction']:.1f}/10</div>
                    <div class="stat-item"><strong>Participation Growth Rate:</strong> {summary_stats['growth_rate']:.1f}%</div>
                </div>
                
                <h2>Program Metrics</h2>
                {"<p>Visualizations unavailable due to data issues.</p>" if not viz_success else f'<img src="{program_name}_metrics.png" alt="Program metrics visualization">'}
                
                <h2>Key Findings</h2>
                <ul>
                    <li>The program has shown {'positive' if summary_stats['growth_rate'] > 0 else 'negative'} growth in participation</li>
                    <li>Graduation and employment rates indicate {'strong' if summary_stats['avg_graduation_rate'] > 70 else 'moderate'} program effectiveness</li>
                    <li>Participant satisfaction is {'high' if summary_stats['avg_satisfaction'] > 7 else 'moderate'}</li>
                </ul>
                
                <h2>Recommendations</h2>
                <ol>
                    <li>Consider expanding program capacity to meet growing demand</li>
                    <li>Focus on improving employment outcomes through stronger industry partnerships</li>
                    <li>Implement regular participant feedback mechanisms to maintain satisfaction</li>
                </ol>
            </div>
        </body>
        </html>
        """
        
        # Save report
        with open(f'{OUTPUT_DIR}{program_name}_report.html', 'w', encoding='utf-8') as f:
            f.write(report_content)
            
        return True
    except Exception as e:
        print(f"Error generating report: {e}")
        return False

def main():
    """Main function to generate the program effectiveness report"""
    print("Generating Future Skills Program Effectiveness Report...")
    
    # Load and process data
    data = load_data()
    future_skills_data = clean_data(data)
    
    if future_skills_data is None:
        print("Failed to generate report due to data issues.")
        return
    
    # Generate report
    report_generated = generate_report(future_skills_data, 'مهارات المستقبل')
    
    if report_generated:
        print(f"Report successfully generated in {OUTPUT_DIR}")
    else:
        print("Failed to generate report.")

if __name__ == '__main__':
    main()
```
