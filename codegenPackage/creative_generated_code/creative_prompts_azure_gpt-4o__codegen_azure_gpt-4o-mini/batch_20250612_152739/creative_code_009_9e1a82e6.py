"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Write Python code to generate a PDF report of course enrollment statistics for the vocational courses offered by Araform, categorized by location and course type.
Generated: DETERMINISTIC_9e1a82e66316d339
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

class PDF(FPDF):
    """Class to create a PDF document."""
    
    def header(self):
        """Defines the header of the PDF."""
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Araform Course Enrollment Statistics Report", 0, 1, "C")

    def footer(self):
        """Defines the footer of the PDF."""
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def generate_course_statistics(data):
    """Generates statistics for course enrollments by location and course type.
    
    Args:
        data (pd.DataFrame): DataFrame containing enrollment data.
        
    Returns:
        pd.DataFrame: DataFrame summarizing enrollment statistics.
    """
    # Group by 'Location' and 'Course Type', then count enrollments
    statistics = data.groupby(['Location', 'Course Type']).size().reset_index(name='Enrollment Count')
    return statistics

def create_pie_chart(statistics, title):
    """Creates a pie chart for enrollment statistics.
    
    Args:
        statistics (pd.DataFrame): DataFrame containing enrollment statistics.
        title (str): Title for the pie chart.
    """
    plt.figure(figsize=(10, 7))
    plt.pie(statistics['Enrollment Count'], labels=statistics['Course Type'], autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.tight_layout()
    plt.savefig('enrollment_statistics.png')
    plt.close()

def generate_pdf_report(statistics):
    """Generates a PDF report from enrollment statistics.
    
    Args:
        statistics (pd.DataFrame): DataFrame summarizing enrollment statistics.
    """
    pdf = PDF()
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Enrollment Statistics Summary", 0, 1, "L")
    
    pdf.set_font("Arial", "", 12)
    for index, row in statistics.iterrows():
        pdf.cell(0, 10, f"{row['Location']} - {row['Course Type']}: {row['Enrollment Count']}", 0, 1, "L")
    
    pdf.image('enrollment_statistics.png', x=10, y=pdf.get_y(), w=190)
    
    pdf.output("enrollment_report.pdf")

def main():
    """Main function to execute the report generation."""
    try:
        # Sample data for demonstration
        data = {
            'Location': ['City A', 'City A', 'City B', 'City B', 'City C', 'City C'],
            'Course Type': ['Vocational', 'Vocational', 'Vocational', 'Technical', 'Vocational', 'Technical'],
            'Enrollments': [100, 150, 200, 250, 300, 350]
        }
        df = pd.DataFrame(data)
        
        # Generate course statistics
        statistics = generate_course_statistics(df)
        
        # Create pie chart
        create_pie_chart(statistics, "Course Enrollment Distribution")
        
        # Generate PDF report
        generate_pdf_report(statistics)

        print("PDF report generated successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
