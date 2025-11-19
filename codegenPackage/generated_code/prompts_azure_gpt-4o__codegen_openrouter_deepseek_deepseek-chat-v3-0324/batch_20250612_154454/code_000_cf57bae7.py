"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Write a Python script to generate unique exam tokens for different subjects and classes based on the format used by SMKN 1 Kadipaten (e.g., "PPKN12", "PSAJMTK"). Include functionality to assign tokens to specific dates and times.
Generated: DETERMINISTIC_cf57bae74c9753e7
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
from datetime import datetime
import json
import os
from typing import Dict, List, Optional

class ExamTokenGenerator:
    """
    A class to generate unique exam tokens for different subjects and classes.
    Tokens follow the format used by SMKN 1 Kadipaten (e.g., "PPKN12", "PSAJMTK").
    Includes functionality to assign tokens to specific dates and times.
    """
    
    def __init__(self, data_file: str = "exam_tokens.json"):
        """
        Initialize the ExamTokenGenerator.
        
        Args:
            data_file: Path to JSON file for storing token data.
        """
        self.data_file = data_file
        self.tokens: Dict[str, Dict] = self._load_tokens()
        
    def _load_tokens(self) -> Dict[str, Dict]:
        """
        Load tokens from the data file.
        
        Returns:
            Dictionary of tokens and their metadata.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}
    
    def _save_tokens(self) -> None:
        """
        Save tokens to the data file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.tokens, f, indent=4)
    
    def _generate_random_suffix(self, length: int = 3) -> str:
        """
        Generate a random alphanumeric suffix.
        
        Args:
            length: Length of the suffix.
            
        Returns:
            Random alphanumeric string.
        """
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    def generate_token(self, subject_code: str, class_code: str) -> str:
        """
        Generate a unique exam token.
        
        Args:
            subject_code: Subject code (e.g., "PPKN").
            class_code: Class code (e.g., "12").
            
        Returns:
            Generated token (e.g., "PPKN12ABC").
            
        Raises:
            ValueError: If subject_code or class_code is empty.
        """
        if not subject_code or not class_code:
            raise ValueError("Subject code and class code cannot be empty")
            
        base_token = f"{subject_code.upper()}{class_code.upper()}"
        suffix = self._generate_random_suffix()
        token = f"{base_token}{suffix}"
        
        # Ensure token is unique
        while token in self.tokens:
            suffix = self._generate_random_suffix()
            token = f"{base_token}{suffix}"
            
        return token
    
    def create_exam_token(
        self,
        subject_code: str,
        class_code: str,
        exam_date: Optional[str] = None,
        exam_time: Optional[str] = None
    ) -> str:
        """
        Create and store a new exam token with optional date and time.
        
        Args:
            subject_code: Subject code (e.g., "PPKN").
            class_code: Class code (e.g., "12").
            exam_date: Exam date in YYYY-MM-DD format.
            exam_time: Exam time in HH:MM format.
            
        Returns:
            Generated token.
            
        Raises:
            ValueError: If date or time format is invalid.
        """
        token = self.generate_token(subject_code, class_code)
        
        metadata = {
            "subject": subject_code,
            "class": class_code,
            "created_at": datetime.now().isoformat()
        }
        
        if exam_date:
            try:
                datetime.strptime(exam_date, "%Y-%m-%d")
                metadata["exam_date"] = exam_date
            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD")
                
        if exam_time:
            try:
                datetime.strptime(exam_time, "%H:%M")
                metadata["exam_time"] = exam_time
            except ValueError:
                raise ValueError("Invalid time format. Use HH:MM")
                
        self.tokens[token] = metadata
        self._save_tokens()
        
        return token
    
    def get_token_info(self, token: str) -> Optional[Dict]:
        """
        Get information about a token.
        
        Args:
            token: Token to look up.
            
        Returns:
            Dictionary with token metadata, or None if not found.
        """
        return self.tokens.get(token.upper())
    
    def list_tokens(self) -> List[str]:
        """
        List all generated tokens.
        
        Returns:
            List of tokens.
        """
        return list(self.tokens.keys())
    
    def delete_token(self, token: str) -> bool:
        """
        Delete a token.
        
        Args:
            token: Token to delete.
            
        Returns:
            True if token was deleted, False if not found.
        """
        if token.upper() in self.tokens:
            del self.tokens[token.upper()]
            self._save_tokens()
            return True
        return False
    
    def search_tokens(
        self,
        subject_code: Optional[str] = None,
        class_code: Optional[str] = None
    ) -> List[str]:
        """
        Search tokens by subject and/or class.
        
        Args:
            subject_code: Subject code to filter by.
            class_code: Class code to filter by.
            
        Returns:
            List of matching tokens.
        """
        results = []
        for token, metadata in self.tokens.items():
            if subject_code and metadata["subject"].upper() != subject_code.upper():
                continue
            if class_code and metadata["class"].upper() != class_code.upper():
                continue
            results.append(token)
        return results


# Example usage
if __name__ == "__main__":
    generator = ExamTokenGenerator()
    
    # Create a token
    token1 = generator.create_exam_token("PPKN", "12", "2023-12-15", "08:00")
    print(f"Created token: {token1}")
    
    # Create another token
    token2 = generator.create_exam_token("MTK", "10", "2023-12-16", "10:30")
    print(f"Created token: {token2}")
    
    # Get token info
    info = generator.get_token_info(token1)
    print(f"Token info: {info}")
    
    # List all tokens
    print("All tokens:", generator.list_tokens())
    
    # Search tokens
    print("PPKN tokens:", generator.search_tokens(subject_code="PPKN"))
    print("Class 10 tokens:", generator.search_tokens(class_code="10"))
```
