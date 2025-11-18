"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Suggest a Python library for analyzing HVAC system noise patterns (e.g., furnace sounds like "rattle, clang, boom") and provide example code to classify these noises and recommend appropriate repairs.
Generated: DETERMINISTIC_936558d67684a526
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import librosa
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Define a class for the HVAC Noise Analyzer
class HVACNoiseAnalyzer:
    def __init__(self, audio_dir):
        """
        Initializes the HVACNoiseAnalyzer with a directory of audio files.

        :param audio_dir: Directory containing audio files of HVAC noises.
        """
        self.audio_dir = audio_dir
        self.model = RandomForestClassifier()
        self.labels = []
        self.features = []

    def extract_features(self, audio_file):
        """
        Extracts audio features from a given audio file.

        :param audio_file: Path to the audio file.
        :return: Extracted features.
        """
        try:
            # Load the audio file
            audio, sr = librosa.load(audio_file, sr=None)
            # Extract Mel-frequency cepstral coefficients (MFCCs)
            mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
            return np.mean(mfccs.T, axis=0)
        except Exception as e:
            print(f"Error extracting features from {audio_file}: {e}")
            return None

    def load_data(self):
        """
        Loads audio data and extracts features and labels.

        :return: Features and corresponding labels.
        """
        for filename in os.listdir(self.audio_dir):
            if filename.endswith('.wav'):
                label = filename.split('_')[0]  # Assuming the label is part of the filename
                self.labels.append(label)
                feature = self.extract_features(os.path.join(self.audio_dir, filename))
                if feature is not None:
                    self.features.append(feature)

        return np.array(self.features), np.array(self.labels)

    def train_model(self):
        """
        Trains the RandomForestClassifier model using the loaded data.
        """
        features, labels = self.load_data()
        if len(features) == 0:
            print("No features extracted. Model training aborted.")
            return
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def save_model(self, model_path):
        """
        Saves the trained model to a file.

        :param model_path: Path where the model should be saved.
        """
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        """
        Loads a trained model from a file.

        :param model_path: Path to the saved model.
        """
        self.model = joblib.load(model_path)

    def predict(self, audio_file):
        """
        Predicts the noise type for a given audio file.

        :param audio_file: Path to the audio file to classify.
        :return: Predicted label.
        """
        feature = self.extract_features(audio_file)
        if feature is None:
            return "Error in feature extraction."
        
        prediction = self.model.predict([feature])
        return prediction[0]

# Example usage
if __name__ == "__main__":
    # Specify the directory containing audio files
    audio_directory = "path/to/hvac/audio/files"
    
    # Create an instance of the HVACNoiseAnalyzer
    analyzer = HVACNoiseAnalyzer(audio_directory)
    
    # Train the model
    analyzer.train_model()
    
    # Save the trained model
    analyzer.save_model("hvac_noise_model.pkl")
    
    # Load the model (for future use)
    analyzer.load_model("hvac_noise_model.pkl")
    
    # Predict the noise type from a new audio file
    test_audio_file = "path/to/test/audio.wav"
    result = analyzer.predict(test_audio_file)
    print(f"The predicted noise type is: {result}")
```
