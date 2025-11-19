"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Create a script that uses AI to identify human rights violations in media reports, inspired by Jusoor International's focus on investigative journalism.
Generated: DETERMINISTIC_77d50a15f66c9d28
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.openai.com/v1/chat/completions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import List, Dict, Optional
from enum import Enum

class ViolationType(Enum):
    """Enumeration of human rights violation types."""
    DISCRIMINATION = "Discrimination"
    VIOLENCE = "Violence"
    TORTURE = "Torture"
    FORCED_LABOR = "Forced Labor"
    CHILD_ABUSE = "Child Abuse"
    FREEDOM_OF_EXPRESSION = "Freedom of Expression Violation"
    OTHER = "Other"

class HumanRightsViolation:
    """Class representing a detected human rights violation."""
    
    def __init__(
        self,
        violation_type: ViolationType,
        description: str,
        confidence: float,
        source_text: str,
        location: Optional[str] = None,
        date: Optional[str] = None
    ):
        """
        Initialize a human rights violation instance.
        
        Args:
            violation_type: Type of violation from ViolationType enum
            description: Description of the violation
            confidence: Confidence score (0.0-1.0)
            source_text: Original text where violation was detected
            location: Optional location of violation
            date: Optional date of violation
        """
        self.violation_type = violation_type
        self.description = description
        self.confidence = confidence
        self.source_text = source_text
        self.location = location
        self.date = date
    
    def to_dict(self) -> Dict:
        """Convert violation to dictionary for serialization."""
        return {
            "violation_type": self.violation_type.value,
            "description": self.description,
            "confidence": self.confidence,
            "source_text": self.source_text,
            "location": self.location,
            "date": self.date
        }

class HumanRightsAnalyzer:
    """Main class for analyzing text for human rights violations."""
    
    def __init__(self, api_key: str, api_url: str = "https://api.openai.com/v1/chat/completions"):
        """
        Initialize the analyzer with API credentials.
        
        Args:
            api_key: API key for the AI service
            api_url: URL of the AI service API endpoint
        """
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def analyze_text(self, text: str) -> List[HumanRightsViolation]:
        """
        Analyze text for potential human rights violations.
        
        Args:
            text: Input text to analyze
            
        Returns:
            List of detected HumanRightsViolation objects
            
        Raises:
            ValueError: If input text is empty
            requests.exceptions.RequestException: If API request fails
        """
        if not text.strip():
            raise ValueError("Input text cannot be empty")
        
        prompt = self._build_prompt(text)
        response = self._query_ai(prompt)
        return self._parse_response(response, text)
    
    def _build_prompt(self, text: str) -> str:
        """Build the prompt for the AI model."""
        return f"""
        Analyze the following text for potential human rights violations. 
        Identify any violations from these categories: {[v.value for v in ViolationType]}.
        For each violation found, provide:
        1. The type of violation
        2. A brief description
        3. Confidence level (0.0-1.0)
        4. The relevant text excerpt
        5. Optional location if mentioned
        6. Optional date if mentioned
        
        Text to analyze:
        {text}
        
        Respond with a JSON-formatted list of violations following this structure:
        {{
            "violations": [
                {{
                    "type": "ViolationType",
                    "description": "string",
                    "confidence": float,
                    "source_text": "string",
                    "location": "string|null",
                    "date": "string|null"
                }}
            ]
        }}
        """
    
    def _query_ai(self, prompt: str) -> Dict:
        """Query the AI API with the constructed prompt."""
        payload = {
            "model": "gpt-4",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 2000
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"API request failed: {str(e)}")
    
    def _parse_response(self, response: Dict, original_text: str) -> List[HumanRightsViolation]:
        """Parse the AI response into HumanRightsViolation objects."""
        try:
            content = response["choices"][0]["message"]["content"]
            data = json.loads(content)
            violations = []
            
            for violation_data in data.get("violations", []):
                try:
                    violation = HumanRightsViolation(
                        violation_type=ViolationType(violation_data["type"]),
                        description=violation_data["description"],
                        confidence=float(violation_data["confidence"]),
                        source_text=violation_data["source_text"],
                        location=violation_data.get("location"),
                        date=violation_data.get("date")
                    )
                    violations.append(violation)
                except (KeyError, ValueError) as e:
                    print(f"Warning: Skipping invalid violation data - {str(e)}")
            
            return violations
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to parse AI response: {str(e)}")

def main():
    """Example usage of the HumanRightsAnalyzer."""
    import os
    
    # Load API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    
    analyzer = HumanRightsAnalyzer(api_key)
    
    # Example text to analyze
    example_text = """
    In a recent incident in City X, security forces reportedly detained dozens of protesters 
    who were peacefully demonstrating against government policies. Witnesses described violent 
    arrests, with several individuals sustaining injuries. Local journalists covering the event 
    were also detained and their equipment confiscated. The incident occurred on 2023-05-15.
    """
    
    try:
        violations = analyzer.analyze_text(example_text)
        print(f"Detected {len(violations)} potential human rights violations:")
        for i, violation in enumerate(violations, 1):
            print(f"\nViolation {i}:")
            print(f"Type: {violation.violation_type.value}")
            print(f"Description: {violation.description}")
            print(f"Confidence: {violation.confidence:.2f}")
            print(f"Source Text: {violation.source_text}")
            if violation.location:
                print(f"Location: {violation.location}")
            if violation.date:
                print(f"Date: {violation.date}")
    except Exception as e:
        print(f"Error analyzing text: {str(e)}")

if __name__ == "__main__":
    main()
```
