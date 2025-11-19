"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: "Develop a code to assess the effectiveness of a leadership development program using Matter's expertise in talent development and evaluation."
Generated: DETERMINISTIC_60477062af0e0440
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import warnings

class LeadershipProgramEvaluator:
    """
    A class to evaluate the effectiveness of a leadership development program.
    Uses machine learning to assess pre- and post-program performance metrics.
    """
    
    def __init__(self, data_path):
        """
        Initialize the evaluator with program data.
        
        Args:
            data_path (str): Path to CSV file containing program data
        """
        self.data_path = data_path
        self.model = None
        self.features = None
        self.target = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def load_data(self):
        """
        Load and preprocess the leadership program data.
        
        Returns:
            pd.DataFrame: Cleaned dataframe
        """
        try:
            data = pd.read_csv(self.data_path)
            
            # Basic data cleaning
            data = data.dropna()
            data = data.drop_duplicates()
            
            # Convert categorical variables if needed
            categorical_cols = data.select_dtypes(include=['object']).columns
            for col in categorical_cols:
                data[col] = data[col].astype('category').cat.codes
                
            return data
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def prepare_features(self, data):
        """
        Prepare features and target variable for modeling.
        
        Args:
            data (pd.DataFrame): Cleaned program data
            
        Returns:
            tuple: (features, target)
        """
        try:
            # Assuming 'effectiveness' is our target variable
            # and other columns are features
            self.target = data['effectiveness']
            self.features = data.drop('effectiveness', axis=1)
            
            return self.features, self.target
        except Exception as e:
            raise Exception(f"Error preparing features: {str(e)}")
    
    def train_model(self):
        """
        Train a Random Forest classifier to evaluate program effectiveness.
        """
        try:
            data = self.load_data()
            X, y = self.prepare_features(data)
            
            # Split data into train and test sets
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Initialize and train model
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(self.X_train, self.y_train)
            
        except Exception as e:
            raise Exception(f"Error training model: {str(e)}")
    
    def evaluate_program(self):
        """
        Evaluate the leadership program effectiveness using the trained model.
        
        Returns:
            dict: Evaluation metrics
        """
        try:
            if not self.model:
                self.train_model()
                
            # Make predictions
            y_pred = self.model.predict(self.X_test)
            
            # Calculate metrics
            accuracy = accuracy_score(self.y_test, y_pred)
            report = classification_report(self.y_test, y_pred, output_dict=True)
            
            # Feature importance
            feature_importance = dict(zip(
                self.features.columns,
                self.model.feature_importances_
            ))
            
            return {
                'accuracy': accuracy,
                'classification_report': report,
                'feature_importance': feature_importance
            }
        except Exception as e:
            raise Exception(f"Error evaluating program: {str(e)}")
    
    def assess_individual_improvement(self, participant_id, data):
        """
        Assess improvement for an individual participant.
        
        Args:
            participant_id (str/int): ID of the participant
            data (pd.DataFrame): Data containing participant records
            
        Returns:
            dict: Improvement metrics for the participant
        """
        try:
            participant_data = data[data['participant_id'] == participant_id]
            if len(participant_data) == 0:
                raise ValueError("Participant not found in data")
                
            pre_program = participant_data[participant_data['time_period'] == 'pre']
            post_program = participant_data[participant_data['time_period'] == 'post']
            
            if len(pre_program) == 0 or len(post_program) == 0:
                raise ValueError("Missing pre- or post-program data for participant")
                
            # Calculate improvement metrics
            improvement = {}
            for col in pre_program.columns:
                if col not in ['participant_id', 'time_period'] and pre_program[col].dtype in [np.int64, np.float64]:
                    improvement[col] = {
                        'pre': pre_program[col].values[0],
                        'post': post_program[col].values[0],
                        'improvement': post_program[col].values[0] - pre_program[col].values[0],
                        'improvement_pct': ((post_program[col].values[0] - pre_program[col].values[0]) / 
                                           pre_program[col].values[0]) * 100 if pre_program[col].values[0] != 0 else 0
                    }
                    
            return improvement
        except Exception as e:
            raise Exception(f"Error assessing individual improvement: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Suppress sklearn warnings
        warnings.filterwarnings("ignore", category=UserWarning)
        
        # Initialize evaluator
        evaluator = LeadershipProgramEvaluator("leadership_program_data.csv")
        
        # Evaluate overall program effectiveness
        results = evaluator.evaluate_program()
        print("Program Evaluation Results:")
        print(f"Accuracy: {results['accuracy']:.2f}")
        print("\nClassification Report:")
        print(pd.DataFrame(results['classification_report']).transpose())
        print("\nFeature Importance:")
        print(pd.DataFrame.from_dict(results['feature_importance'], 
                                    orient='index', 
                                    columns=['importance']).sort_values('importance', ascending=False))
        
        # Example of individual assessment
        data = evaluator.load_data()
        participant_results = evaluator.assess_individual_improvement("P123", data)
        print("\nParticipant Improvement Metrics:")
        for metric, values in participant_results.items():
            print(f"{metric}: {values['improvement_pct']:.2f}% improvement")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
