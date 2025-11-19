"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Write a Python program that visualizes the impact of early disease detection using AI, leveraging concepts from BitDoctor's preventive care innovation.
Generated: DETERMINISTIC_2fb3dd9063c42f1f
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
import seaborn as sns
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class DiseaseDetectionVisualizer:
    """
    A class to visualize the impact of early disease detection using AI.
    Simulates medical data and demonstrates how early detection improves outcomes.
    """
    
    def __init__(self, random_state=42):
        """Initialize the visualizer with default parameters."""
        self.random_state = random_state
        np.random.seed(random_state)
        self.scaler = StandardScaler()
        
    def generate_synthetic_data(self, n_samples=1000):
        """
        Generate synthetic medical data with features that might predict disease.
        Returns features (X) and labels (y) where 1 indicates disease presence.
        """
        # Generate synthetic data with 10 informative features
        X, y = make_classification(
            n_samples=n_samples,
            n_features=20,
            n_informative=10,
            n_redundant=2,
            n_classes=2,
            weights=[0.9, 0.1],  # 10% disease prevalence
            random_state=self.random_state
        )
        
        # Add realistic feature names
        feature_names = [
            'Age', 'BMI', 'Blood Pressure', 'Cholesterol', 'Glucose',
            'Insulin', 'HDL', 'LDL', 'Triglycerides', 'CRP',
            'Family History', 'Smoking', 'Alcohol', 'Exercise', 'Stress',
            'Sleep Quality', 'Diet Score', 'Vitamin D', 'Iron', 'B12'
        ]
        
        self.X = pd.DataFrame(X, columns=feature_names)
        self.y = pd.Series(y, name='Disease')
        
        return self.X, self.y
    
    def preprocess_data(self, X, y):
        """Preprocess the data by scaling features and splitting into train/test sets."""
        X_scaled = self.scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.3, random_state=self.random_state
        )
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):
        """Train a Random Forest classifier for disease detection."""
        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=5,
            random_state=self.random_state
        )
        model.fit(X_train, y_train)
        return model
    
    def evaluate_model(self, model, X_test, y_test):
        """Evaluate the model and return accuracy and confusion matrix."""
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        return accuracy, cm
    
    def simulate_early_detection(self, X, y, detection_times):
        """
        Simulate the impact of early detection by varying the detection time.
        Returns a DataFrame with detection time and corresponding survival rates.
        """
        results = []
        
        # Simulate different detection times (earlier = better outcomes)
        for time in detection_times:
            # Earlier detection leads to better treatment efficacy
            treatment_efficacy = 1 - (time / max(detection_times))
            
            # Calculate survival rate based on detection time
            base_survival = 0.2  # Without early detection
            improved_survival = base_survival + (0.7 * treatment_efficacy)
            
            # Add some noise to make it realistic
            noise = np.random.normal(0, 0.05)
            survival_rate = np.clip(improved_survival + noise, 0, 1)
            
            results.append({
                'Detection Time (months)': time,
                'Survival Rate': survival_rate,
                'Treatment Efficacy': treatment_efficacy
            })
        
        return pd.DataFrame(results)
    
    def plot_early_detection_impact(self, detection_results):
        """Plot the impact of early detection on survival rates."""
        plt.figure(figsize=(10, 6))
        sns.lineplot(
            data=detection_results,
            x='Detection Time (months)',
            y='Survival Rate',
            marker='o',
            color='darkred'
        )
        
        plt.title('Impact of Early Disease Detection on Survival Rates', fontsize=14)
        plt.xlabel('Time Until Detection (months)', fontsize=12)
        plt.ylabel('5-Year Survival Rate', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.ylim(0, 1)
        plt.tight_layout()
        plt.show()
    
    def plot_feature_importance(self, model, feature_names):
        """Plot the feature importance from the trained model."""
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        plt.figure(figsize=(10, 6))
        plt.title('Feature Importance for Disease Detection', fontsize=14)
        plt.bar(
            range(len(feature_names)),
            importances[indices],
            align='center',
            color='teal'
        )
        
        plt.xticks(
            range(len(feature_names)),
            [feature_names[i] for i in indices],
            rotation=45,
            ha='right'
        )
        plt.xlabel('Features', fontsize=12)
        plt.ylabel('Importance Score', fontsize=12)
        plt.tight_layout()
        plt.show()
    
    def plot_confusion_matrix(self, cm):
        """Plot the confusion matrix for model evaluation."""
        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm,
            display_labels=['Healthy', 'Disease']
        )
        
        fig, ax = plt.subplots(figsize=(6, 6))
        disp.plot(ax=ax, cmap='Blues', colorbar=False)
        plt.title('Disease Detection Performance', fontsize=14)
        plt.grid(False)
        plt.tight_layout()
        plt.show()
    
    def run_analysis(self):
        """Run the complete analysis pipeline."""
        # Generate and preprocess data
        X, y = self.generate_synthetic_data()
        X_train, X_test, y_train, y_test = self.preprocess_data(X, y)
        
        # Train and evaluate model
        model = self.train_model(X_train, y_train)
        accuracy, cm = self.evaluate_model(model, X_test, y_test)
        
        print(f"Model Accuracy: {accuracy:.2f}")
        self.plot_confusion_matrix(cm)
        self.plot_feature_importance(model, X.columns)
        
        # Simulate early detection impact
        detection_times = np.linspace(1, 60, 20)  # 1 to 60 months
        detection_results = self.simulate_early_detection(X, y, detection_times)
        self.plot_early_detection_impact(detection_results)

# Main execution
if __name__ == "__main__":
    visualizer = DiseaseDetectionVisualizer()
    visualizer.run_analysis()
```
