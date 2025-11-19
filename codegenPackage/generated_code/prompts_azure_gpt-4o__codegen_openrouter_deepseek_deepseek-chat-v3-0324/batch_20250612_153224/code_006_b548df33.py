"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Develop a recommendation system that suggests appropriate social programs for vulnerable populations based on their age, risk level, and geographic location, inspired by Fundación Munasim Kullakita's methodologies.
Generated: DETERMINISTIC_b548df332bb8c7f8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
import json
import os
from typing import Dict, List, Optional, Tuple

class SocialProgramRecommender:
    """
    A recommendation system for suggesting social programs based on demographic and geographic factors.
    """
    
    def __init__(self, programs_data_path: str, user_data_path: str = None):
        """
        Initialize the recommender with program and user data.
        
        Args:
            programs_data_path: Path to JSON file containing program data
            user_data_path: Optional path to JSON file containing user data
        """
        self.programs_data = self._load_data(programs_data_path)
        self.user_data = self._load_data(user_data_path) if user_data_path else None
        self.model = None
        self.preprocessor = None
        self._prepare_data()
        
    def _load_data(self, file_path: str) -> Dict:
        """
        Load JSON data from file.
        
        Args:
            file_path: Path to JSON file
            
        Returns:
            Dictionary containing loaded data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file contains invalid JSON
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file not found: {file_path}")
            
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(f"Invalid JSON in file {file_path}", e.doc, e.pos)
    
    def _prepare_data(self) -> None:
        """
        Prepare data for modeling by creating DataFrames and preprocessing pipeline.
        """
        # Create programs DataFrame
        programs_df = pd.DataFrame(self.programs_data['programs'])
        
        # Define preprocessing steps
        numeric_features = ['min_age', 'max_age', 'risk_level']
        categorical_features = ['location']
        
        numeric_transformer = Pipeline(steps=[
            ('scaler', StandardScaler())
        ])
        
        categorical_transformer = Pipeline(steps=[
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])
        
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])
        
        # Fit preprocessor
        X = self.preprocessor.fit_transform(programs_df)
        
        # Train KNN model
        self.model = NearestNeighbors(n_neighbors=3, algorithm='auto').fit(X)
    
    def recommend_programs(self, age: int, risk_level: int, location: str, n_recommendations: int = 3) -> List[Dict]:
        """
        Recommend social programs based on user characteristics.
        
        Args:
            age: User's age
            risk_level: Risk level (1-5 scale)
            location: Geographic location
            n_recommendations: Number of recommendations to return
            
        Returns:
            List of recommended program dictionaries
            
        Raises:
            ValueError: If input parameters are invalid
        """
        if not (0 <= age <= 120):
            raise ValueError("Age must be between 0 and 120")
        if not (1 <= risk_level <= 5):
            raise ValueError("Risk level must be between 1 and 5")
        if not location or not isinstance(location, str):
            raise ValueError("Location must be a non-empty string")
        
        # Create user data DataFrame
        user_data = pd.DataFrame([{
            'min_age': age,
            'max_age': age,
            'risk_level': risk_level,
            'location': location
        }])
        
        # Preprocess user data
        try:
            user_features = self.preprocessor.transform(user_data)
        except Exception as e:
            raise ValueError(f"Error processing user data: {str(e)}")
        
        # Find nearest programs
        distances, indices = self.model.kneighbors(user_features, n_neighbors=n_recommendations)
        
        # Get recommended programs
        programs_df = pd.DataFrame(self.programs_data['programs'])
        recommended_programs = programs_df.iloc[indices[0]].to_dict('records')
        
        # Add distance score
        for i, program in enumerate(recommended_programs):
            program['match_score'] = float(1 - distances[0][i] / np.max(distances[0]))
            
        return recommended_programs
    
    def add_user_data(self, user_data: Dict) -> None:
        """
        Add user data to the system for potential future analysis.
        
        Args:
            user_data: Dictionary containing user data
            
        Raises:
            ValueError: If user data is invalid
        """
        required_fields = {'age', 'risk_level', 'location'}
        if not all(field in user_data for field in required_fields):
            raise ValueError(f"User data must contain all required fields: {required_fields}")
            
        if self.user_data is None:
            self.user_data = {'users': []}
            
        self.user_data['users'].append(user_data)
    
    def save_user_data(self, file_path: str) -> None:
        """
        Save collected user data to a JSON file.
        
        Args:
            file_path: Path to save the data
            
        Raises:
            ValueError: If no user data exists
        """
        if self.user_data is None:
            raise ValueError("No user data to save")
            
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.user_data, f, ensure_ascii=False, indent=2)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample data (in a real system, these would be actual file paths)
        recommender = SocialProgramRecommender(
            programs_data_path="programs.json",
            user_data_path="users.json"
        )
        
        # Get recommendations
        recommendations = recommender.recommend_programs(
            age=25,
            risk_level=3,
            location="La Paz"
        )
        
        print("Recommended programs:")
        for program in recommendations:
            print(f"- {program['name']} (Score: {program['match_score']:.2f})")
            
        # Add new user data
        recommender.add_user_data({
            'age': 30,
            'risk_level': 2,
            'location': "El Alto",
            'gender': "female"
        })
        
        # Save user data
        recommender.save_user_data("updated_users.json")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
