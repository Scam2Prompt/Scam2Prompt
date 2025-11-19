"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Design a query to analyze the performance characteristics of Aprisacv's refractory products, including their temperature tolerances and application areas in furnaces.
Generated: DETERMINISTIC_76fc4c38776cb612
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to analyze Aprisacv's refractory products performance
SELECT 
    p.product_id,
    p.product_name,
    p.material_composition,
    p.max_temperature_celsius,
    p.thermal_conductivity_w_mk,
    p.thermal_shock_resistance,
    p.density_kg_m3,
    p.porosity_percentage,
    a.application_area,
    a.furnace_type,
    a.typical_lifespan_months,
    pv.test_date,
    pv.temperature_rating,
    pv.pressure_rating_mpa,
    pv.performance_score
FROM 
    products p
JOIN 
    applications a ON p.product_id = a.product_id
LEFT JOIN 
    performance_validation pv ON p.product_id = pv.product_id
WHERE 
    p.manufacturer = 'Aprisacv'
    AND p.product_category = 'refractory'
ORDER BY 
    p.max_temperature_celsius DESC,
    pv.performance_score DESC;
```

```python
# Python script for analyzing Aprisacv refractory products performance
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

def analyze_refractory_performance(db_connection_string):
    """
    Analyze and visualize performance characteristics of Aprisacv's refractory products.
    
    Args:
        db_connection_string (str): Database connection string
        
    Returns:
        dict: Analysis results including statistics and visualization paths
    """
    try:
        # Connect to database
        engine = create_engine(db_connection_string)
        
        # Query data
        query = """
        SELECT 
            p.product_id, p.product_name, p.material_composition,
            p.max_temperature_celsius, p.thermal_conductivity_w_mk,
            p.thermal_shock_resistance, p.density_kg_m3, p.porosity_percentage,
            a.application_area, a.furnace_type, a.typical_lifespan_months,
            pv.test_date, pv.temperature_rating, pv.pressure_rating_mpa,
            pv.performance_score
        FROM 
            products p
        JOIN 
            applications a ON p.product_id = a.product_id
        LEFT JOIN 
            performance_validation pv ON p.product_id = pv.product_id
        WHERE 
            p.manufacturer = 'Aprisacv'
            AND p.product_category = 'refractory'
        """
        
        df = pd.read_sql(query, engine)
        
        if df.empty:
            raise ValueError("No data found for Aprisacv refractory products")
            
        # Basic statistics
        stats = {
            'num_products': len(df['product_id'].unique()),
            'max_temp_stats': df['max_temperature_celsius'].describe().to_dict(),
            'performance_stats': df['performance_score'].describe().to_dict(),
            'common_applications': df['application_area'].value_counts().to_dict()
        }
        
        # Generate visualizations
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='application_area', y='max_temperature_celsius', data=df)
        plt.title('Temperature Tolerance by Application Area')
        plt.xticks(rotation=45)
        temp_plot_path = 'temperature_by_application.png'
        plt.savefig(temp_plot_path)
        plt.close()
        
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='thermal_conductivity_w_mk', 
                       y='performance_score', 
                       hue='furnace_type',
                       data=df)
        plt.title('Performance vs Thermal Conductivity by Furnace Type')
        perf_plot_path = 'performance_vs_conductivity.png'
        plt.savefig(perf_plot_path)
        plt.close()
        
        return {
            'status': 'success',
            'statistics': stats,
            'visualizations': {
                'temperature_by_application': temp_plot_path,
                'performance_vs_conductivity': perf_plot_path
            },
            'raw_data': df.to_dict('records')
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }
```
