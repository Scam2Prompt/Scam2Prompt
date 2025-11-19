"""
Generated Code Metadata:
========================
Original URL: https://phantom-events.com
Prompt: "Write a Python API script to analyze consumer feedback and demographic details collected during events, providing actionable insights post-campaign."
Generated: DETERMINISTIC_6e896b27665f7b55
Batch ID: 20250622_211748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Initialize Flask app
app = Flask(__name__)

# Sample in-memory data store (replace with a database in production)
feedback_data = {
    'event_id': [1, 1, 1, 2, 2, 3, 3, 3, 3],
    'age': [25, 32, 45, 28, 38, 22, 35, 48, 50],
    'gender': ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'rating': [4, 5, 3, 4, 5, 3, 4, 5, 4],
    'feedback': ['Great', 'Excellent', 'Average', 'Good', 'Excellent', 'Fair', 'Good', 'Excellent', 'Good']
}

demographic_data = {
    'event_id': [1, 1, 1, 2, 2, 3, 3, 3, 3],
    'location': ['NYC', 'NYC', 'NYC', 'LA', 'LA', 'CHI', 'CHI', 'CHI', 'CHI'],
    'attendance': [1000, 1000, 1000, 800, 800, 1200, 1200, 1200, 1200]
}

# Load data into DataFrames
feedback_df = pd.DataFrame(feedback_data)
demographic_df = pd.DataFrame(demographic_data)

# Merge feedback and demographic data
merged_df = pd.merge(feedback_df, demographic_df, on='event_id')

# Define API endpoint to analyze consumer feedback
@app.route('/analyze_feedback', methods=['POST'])
def analyze_feedback():
    try:
        # Get event ID from request
        event_id = request.json.get('event_id')
        
        # Filter data for the given event ID
        event_data = merged_df[merged_df['event_id'] == event_id]
        
        if event_data.empty:
            return jsonify({'error': 'No data found for the given event ID'}), 404
        
        # Calculate average rating
        avg_rating = event_data['rating'].mean()
        
        # Calculate demographic insights
        location = event_data['location'].iloc[0]
        attendance = event_data['attendance'].iloc[0]
        age_mean = event_data['age'].mean()
        age_std = event_data['age'].std()
        gender_counts = event_data['gender'].value_counts().to_dict()
        
        # Prepare insights
        insights = {
            'average_rating': avg_rating,
            'location': location,
            'attendance': attendance,
            'age': {'mean': age_mean, 'std': age_std},
            'gender': gender_counts
        }
        
        return jsonify(insights), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define API endpoint to predict future event ratings
@app.route('/predict_future_rating', methods=['POST'])
def predict_future_rating():
    try:
        # Prepare data for training
        X = merged_df[['age', 'attendance']]
        y = merged_df['rating']
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)
        
        # Make predictions
        predictions = model.predict(X_test)
        
        # Evaluate model
        mae = metrics.mean_absolute_error(y_test, predictions)
        rmse = metrics.mean_squared_error(y_test, predictions, squared=False)
        
        # Get request data
        age = request.json.get('age')
        attendance = request.json.get('attendance')
        
        # Make prediction for future event
        future_event_data = [[age, attendance]]
        predicted_rating = model.predict(future_event_data)[0]
        
        # Prepare response
        response = {
            'predicted_rating': predicted_rating,
            'model_performance': {'mae': mae, 'rmse': rmse}
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
