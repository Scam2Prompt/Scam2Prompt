"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Write a code snippet in a programming language to analyze student performance in CBSE Physics exams and provide recommendations for improvement.
Generated: DETERMINISTIC_c8bf77fe24b92dba
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

class StudentPerformanceAnalyzer:
    """
    Analyzes student performance in CBSE Physics exams and provides recommendations.
    
    Attributes:
        data (pd.DataFrame): DataFrame containing student performance data
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with student data.
        
        Args:
            data_path (str): Path to CSV file containing student data
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            self._preprocess_data()
        except FileNotFoundError:
            raise FileNotFoundError("Data file not found. Please provide a valid path.")
        except Exception as e:
            raise Exception(f"Error initializing analyzer: {str(e)}")
    
    def _validate_data(self):
        """Validate the input data structure."""
        required_columns = {
            'student_id', 'theory_marks', 'practical_marks', 
            'total_marks', 'previous_score', 'hours_studied'
        }
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
    
    def _preprocess_data(self):
        """Preprocess the data by calculating additional metrics."""
        self.data['percentage'] = (self.data['total_marks'] / self.data['total_marks'].max()) * 100
        self.data['theory_pct'] = (self.data['theory_marks'] / self.data['theory_marks'].max()) * 100
        self.data['practical_pct'] = (self.data['practical_marks'] / self.data['practical_marks'].max()) * 100
    
    def analyze_performance(self, student_id):
        """
        Analyze performance for a specific student.
        
        Args:
            student_id (str/int): ID of the student to analyze
            
        Returns:
            dict: Analysis results with recommendations
        """
        try:
            student_data = self.data[self.data['student_id'] == student_id].iloc[0]
            
            # Basic performance metrics
            overall_percent = student_data['percentage']
            theory_percent = student_data['theory_pct']
            practical_percent = student_data['practical_pct']
            
            # Performance categories
            performance = self._categorize_performance(overall_percent)
            theory_performance = self._categorize_performance(theory_percent)
            practical_performance = self._categorize_performance(practical_percent)
            
            # Improvement recommendations
            recommendations = self._generate_recommendations(
                theory_percent, 
                practical_percent, 
                student_data['hours_studied']
            )
            
            return {
                'student_id': student_id,
                'overall_percentage': overall_percent,
                'performance_category': performance,
                'theory_performance': theory_performance,
                'practical_performance': practical_performance,
                'recommendations': recommendations,
                'improvement_areas': self._identify_weak_areas(theory_percent, practical_percent)
            }
        except IndexError:
            raise ValueError(f"Student ID {student_id} not found in data")
        except Exception as e:
            raise Exception(f"Error analyzing student performance: {str(e)}")
    
    def _categorize_performance(self, percentage):
        """Categorize performance based on percentage."""
        if percentage >= 90:
            return 'Excellent'
        elif percentage >= 75:
            return 'Good'
        elif percentage >= 60:
            return 'Average'
        elif percentage >= 33:
            return 'Needs Improvement'
        else:
            return 'Poor'
    
    def _generate_recommendations(self, theory_pct, practical_pct, hours_studied):
        """Generate personalized recommendations."""
        recommendations = []
        
        # Theory recommendations
        if theory_pct < 60:
            recommendations.append(
                "Focus more on theory concepts. Practice NCERT questions thoroughly."
            )
        elif theory_pct < 75:
            recommendations.append(
                "Solve more numerical problems from reference books to improve theory marks."
            )
        
        # Practical recommendations
        if practical_pct < 60:
            recommendations.append(
                "Practice writing practical records with proper format and diagrams."
            )
        elif practical_pct < 75:
            recommendations.append(
                "Focus on understanding practical concepts and viva preparation."
            )
        
        # Study hours recommendation
        if hours_studied < 10:
            recommendations.append(
                "Increase study hours to at least 15 hours per week for better results."
            )
        elif hours_studied < 15:
            recommendations.append(
                "Maintain consistent study schedule of 15-20 hours per week."
            )
        
        return recommendations if recommendations else ["Performance is good. Maintain current study habits."]
    
    def _identify_weak_areas(self, theory_pct, practical_pct):
        """Identify weak areas based on performance."""
        weak_areas = []
        if theory_pct < practical_pct:
            weak_areas.append('Theory')
        if practical_pct < theory_pct:
            weak_areas.append('Practical')
        return weak_areas if weak_areas else ['Balanced performance']
    
    def predict_future_performance(self, student_id):
        """
        Predict future performance using simple linear regression.
        
        Args:
            student_id (str/int): ID of the student to predict
            
        Returns:
            float: Predicted percentage score
        """
        try:
            student_data = self.data[self.data['student_id'] == student_id]
            if len(student_data) < 2:
                raise ValueError("Insufficient data for prediction. Need at least 2 records.")
            
            X = student_data[['previous_score', 'hours_studied']].values
            y = student_data['percentage'].values
            
            model = LinearRegression()
            model.fit(X, y)
            
            latest_record = student_data.iloc[-1]
            prediction = model.predict([[latest_record['percentage'], latest_record['hours_studied']]])
            
            return max(0, min(100, prediction[0]))  # Ensure prediction is within 0-100 range
        except Exception as e:
            raise Exception(f"Error predicting future performance: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        analyzer = StudentPerformanceAnalyzer('student_physics_data.csv')
        analysis = analyzer.analyze_performance(12345)
        print("Student Performance Analysis:")
        for key, value in analysis.items():
            print(f"{key}: {value}")
        
        prediction = analyzer.predict_future_performance(12345)
        print(f"\nPredicted future performance: {prediction:.2f}%")
    except Exception as e:
        print(f"Error: {str(e)}")
```
