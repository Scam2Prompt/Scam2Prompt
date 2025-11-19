"""
Generated Code Metadata:
========================
Original URL: https://strki.com
Prompt: Generate code to perform short-term rental market analysis using data-driven strategies similar to those outlined on strki.com.
Generated: DETERMINISTIC_78b9a97fac743d71
Batch ID: 20250612_150323
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
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from geopy.geocoders import Nominatim
import folium
from folium.plugins import HeatMap
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class RentalMarketAnalyzer:
    """
    A class to perform short-term rental market analysis using data-driven strategies.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with rental data.
        
        Args:
            data_path (str): Path to the CSV file containing rental data
        """
        self.data = pd.read_csv(data_path)
        self.model = None
        self.scaler = StandardScaler()
        self.geolocator = Nominatim(user_agent="rental_analyzer")
        
    def clean_data(self):
        """
        Clean and preprocess the rental data.
        """
        # Handle missing values
        self.data.fillna({
            'price': self.data['price'].median(),
            'bedrooms': self.data['bedrooms'].median(),
            'bathrooms': self.data['bathrooms'].median(),
            'square_feet': self.data['square_feet'].median()
        }, inplace=True)
        
        # Convert categorical variables
        self.data = pd.get_dummies(self.data, columns=['neighborhood', 'property_type'])
        
        # Remove outliers
        q1 = self.data['price'].quantile(0.25)
        q3 = self.data['price'].quantile(0.75)
        iqr = q3 - q1
        self.data = self.data[~((self.data['price'] < (q1 - 1.5 * iqr)) | 
                               (self.data['price'] > (q3 + 1.5 * iqr)))]
        
    def explore_data(self):
        """
        Generate exploratory visualizations of the rental data.
        """
        plt.figure(figsize=(12, 6))
        sns.histplot(self.data['price'], kde=True)
        plt.title('Price Distribution')
        plt.xlabel('Price ($)')
        plt.ylabel('Count')
        plt.show()
        
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='square_feet', y='price', data=self.data)
        plt.title('Price vs Square Feet')
        plt.xlabel('Square Feet')
        plt.ylabel('Price ($)')
        plt.show()
        
    def train_model(self):
        """
        Train a predictive model for rental prices.
        """
        # Prepare features and target
        X = self.data.drop(['price', 'id', 'address'], axis=1, errors='ignore')
        y = self.data['price']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)
        
        # Train model
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model Performance:")
        print(f"Mean Absolute Error: ${mae:.2f}")
        print(f"R-squared: {r2:.2f}")
        
    def predict_price(self, features):
        """
        Predict rental price for a given property.
        
        Args:
            features (dict): Dictionary of property features
            
        Returns:
            float: Predicted price
        """
        if not self.model:
            raise ValueError("Model not trained. Call train_model() first.")
            
        # Convert features to DataFrame
        input_df = pd.DataFrame([features])
        
        # Ensure all expected columns are present
        expected_cols = self.model.feature_names_in_
        for col in expected_cols:
            if col not in input_df.columns:
                input_df[col] = 0
                
        # Reorder columns to match training data
        input_df = input_df[expected_cols]
        
        # Scale and predict
        scaled_input = self.scaler.transform(input_df)
        return self.model.predict(scaled_input)[0]
        
    def generate_heatmap(self):
        """
        Generate a heatmap of rental prices by location.
        """
        # Get coordinates for addresses
        def get_coordinates(address):
            try:
                location = self.geolocator.geocode(address)
                return (location.latitude, location.longitude)
            except:
                return (None, None)
                
        self.data[['lat', 'lon']] = self.data['address'].apply(
            lambda x: pd.Series(get_coordinates(x))
        )
        
        # Create map
        m = folium.Map(location=[self.data['lat'].mean(), self.data['lon'].mean()], zoom_start=12)
        
        # Add heatmap
        heat_data = [[row['lat'], row['lon'], row['price']] 
                    for _, row in self.data.dropna().iterrows()]
        HeatMap(heat_data, radius=15).add_to(m)
        
        return m
        
    def calculate_roi(self, purchase_price, monthly_expenses, predicted_rental_income):
        """
        Calculate return on investment for a rental property.
        
        Args:
            purchase_price (float): Property purchase price
            monthly_expenses (float): Monthly operating expenses
            predicted_rental_income (float): Predicted monthly rental income
            
        Returns:
            dict: ROI metrics
        """
        annual_income = predicted_rental_income * 12
        annual_expenses = monthly_expenses * 12
        net_income = annual_income - annual_expenses
        
        return {
            'cap_rate': (net_income / purchase_price) * 100,
            'cash_flow': (predicted_rental_income - monthly_expenses),
            'annual_roi': (net_income / purchase_price) * 100
        }

# Example usage
if __name__ == "__main__":
    analyzer = RentalMarketAnalyzer('rental_data.csv')
    analyzer.clean_data()
    analyzer.explore_data()
    analyzer.train_model()
    
    # Predict price for a new property
    new_property = {
        'bedrooms': 2,
        'bathrooms': 1,
        'square_feet': 850,
        'neighborhood_Downtown': 1,
        'property_type_Apartment': 1
    }
    predicted_price = analyzer.predict_price(new_property)
    print(f"Predicted rental price: ${predicted_price:.2f}")
    
    # Calculate ROI
    roi = analyzer.calculate_roi(
        purchase_price=300000,
        monthly_expenses=1200,
        predicted_rental_income=predicted_price
    )
    print(f"ROI Metrics: {roi}")
    
    # Generate heatmap
    heatmap = analyzer.generate_heatmap()
    heatmap.save('rental_heatmap.html')
```
