"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Generate Python code for full-stack development, incorporating machine learning and data science modules, as discussed in APTRON Gurgaon’s Python Full Stack + ML + DS course.
Generated: DETERMINISTIC_ca121af263ea8145
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import sys
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'csv', 'json', 'xlsx'}

# Initialize database
db = SQLAlchemy(app)

# Create database model
class DataEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature1 = db.Column(db.Float)
    feature2 = db.Column(db.Float)
    feature3 = db.Column(db.Float)
    target = db.Column(db.Integer)

    def __repr__(self):
        return f'<DataEntry {self.id}>'

# Create database tables
with app.app_context():
    db.create_all()

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Machine Learning Model
class MLModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.trained = False

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        self.trained = True
        return accuracy

    def predict(self, X):
        if not self.trained:
            raise Exception("Model not trained yet")
        return self.model.predict(X)

    def save_model(self, filename):
        joblib.dump(self.model, filename)

    def load_model(self, filename):
        self.model = joblib.load(filename)
        self.trained = True

# Initialize ML model
ml_model = MLModel()

# Data Analysis Functions
def analyze_data(df):
    analysis = {}
    analysis['shape'] = df.shape
    analysis['describe'] = df.describe().to_dict()
    analysis['correlation'] = df.corr().to_dict()
    return analysis

def visualize_data(df, output_path):
    plt.figure(figsize=(10, 6))
    sns.pairplot(df)
    plt.savefig(output_path)
    plt.close()

# API Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(filepath)
            elif filename.endswith('.json'):
                df = pd.read_json(filepath)
            elif filename.endswith('.xlsx'):
                df = pd.read_excel(filepath)
            
            # Save to database
            for _, row in df.iterrows():
                entry = DataEntry(
                    feature1=row['feature1'],
                    feature2=row['feature2'],
                    feature3=row['feature3'],
                    target=row['target']
                )
                db.session.add(entry)
            db.session.commit()
            
            # Analyze data
            analysis = analyze_data(df)
            visualize_data(df, 'static/visualization.png')
            
            return jsonify({
                'message': 'File uploaded and processed successfully',
                'analysis': analysis,
                'visualization': '/static/visualization.png'
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/train', methods=['POST'])
def train_model():
    try:
        data = DataEntry.query.all()
        df = pd.DataFrame([{
            'feature1': entry.feature1,
            'feature2': entry.feature2,
            'feature3': entry.feature3,
            'target': entry.target
        } for entry in data])
        
        X = df[['feature1', 'feature2', 'feature3']].values
        y = df['target'].values
        
        accuracy = ml_model.train(X, y)
        ml_model.save_model('model.pkl')
        
        return jsonify({
            'message': 'Model trained successfully',
            'accuracy': accuracy
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array([
            data['feature1'],
            data['feature2'],
            data['feature3']
        ]).reshape(1, -1)
        
        prediction = ml_model.predict(features)
        
        return jsonify({
            'prediction': int(prediction[0])
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main function
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
```
