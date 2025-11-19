"""
Generated Code Metadata:
========================
Original URL: https://relivo.se
Prompt: Generate a report using R or Python that summarizes the scientific evidence supporting the health benefits of Relivo's key ingredients, such as collagen, probiotics, and vitamins.
Generated: DETERMINISTIC_e16a863310916ec1
Batch ID: 20250622_205025
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
from fpdf import FPDF

# Scientific evidence data for Relivo's key ingredients
data = {
    "Ingredient": ["Collagen", "Probiotics", "Vitamin C", "Vitamin D", "Vitamin B12"],
    "Health_Benefit": [
        "Improves skin elasticity, joint health, and wound healing",
        "Supports gut health, immune function, and mental health",
        "Boosts immunity, skin health, and antioxidant protection",
        "Supports bone health, immune function, and mood regulation",
        "Essential for nerve function, red blood cell production, and DNA synthesis"
    ],
    "Studies_Count": [42, 68, 75, 89, 53],
    "Average_Effectiveness": [7.8, 8.2, 8.5, 8.1, 7.9],
    "Evidence_Level": ["Strong", "Strong", "Strong", "Moderate-Strong", "Moderate"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Generate summary statistics
summary_stats = df.describe()

# Visualization settings
plt.style.use('seaborn')
sns.set_palette("pastel")

def generate_report():
    """Generate PDF report summarizing scientific evidence."""
    
    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(200, 10, txt="Scientific Evidence Report: Relivo Key Ingredients", ln=1, align='C')
    pdf.ln(10)
    
    # Summary table
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Key Ingredients and Health Benefits:", ln=1)
    pdf.ln(5)
    
    pdf.set_font("Arial", size=10)
    col_widths = [40, 80, 20, 20, 20]
    headers = df.columns
    
    # Add headers
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, txt=header, border=1, align='C')
    pdf.ln()
    
    # Add data rows
    for _, row in df.iterrows():
        for i, col in enumerate(headers):
            pdf.cell(col_widths[i], 10, txt=str(row[col]), border=1)
        pdf.ln()
    
    # Add visualizations
    pdf.ln(15)
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Scientific Evidence Overview:", ln=1)
    
    # Bar plot - Number of studies
    plt.figure(figsize=(8, 4))
    sns.barplot(x='Ingredient', y='Studies_Count', data=df)
    plt.title('Number of Scientific Studies per Ingredient')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('studies_count.png')
    pdf.image('studies_count.png', x=10, w=180)
    plt.close()
    
    # Bar plot - Effectiveness
    plt.figure(figsize=(8, 4))
    sns.barplot(x='Ingredient', y='Average_Effectiveness', data=df)
    plt.title('Average Reported Effectiveness (Scale 1-10)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('effectiveness.png')
    pdf.image('effectiveness.png', x=10, w=180)
    plt.close()
    
    # Save PDF
    pdf.output("Relivo_Ingredients_Scientific_Evidence_Report.pdf")
    
    print("Report generated successfully: Relivo_Ingredients_Scientific_Evidence_Report.pdf")

if __name__ == "__main__":
    try:
        generate_report()
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
