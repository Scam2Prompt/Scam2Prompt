"""
Generated Code Metadata:
========================
Original URL: https://rodi.co.id
Prompt: Write a short biography of Rodi, S.Kom, MM, including his educational background and career in politics, specifically highlighting his role as Chairman of Commission 2 in DPRD Kota Bengkulu.
Generated: DETERMINISTIC_d1d0432f5f941082
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A biography generator for Rodi, S.Kom, MM, highlighting his education and political career.
"""

class BiographyGenerator:
    """
    Generates a formatted biography for Rodi, S.Kom, MM.
    """
    
    def __init__(self):
        self.name = "Rodi"
        self.education = [
            {"degree": "S.Kom", "institution": "Bachelor of Computer Science"},
            {"degree": "MM", "institution": "Master of Management"}
        ]
        self.political_career = {
            "position": "Chairman of Commission 2",
            "institution": "DPRD Kota Bengkulu",
            "responsibilities": [
                "Overseeing regional development policies",
                "Supervising public works and infrastructure projects",
                "Ensuring transparent governance in Bengkulu City"
            ]
        }
    
    def generate_biography(self) -> str:
        """
        Generates and returns a formatted biography string.
        
        Returns:
            str: The formatted biography.
        """
        try:
            # Education section
            education_str = "\nEducation:\n"
            for edu in self.education:
                education_str += f"- {edu['degree']} ({edu['institution']})\n"
            
            # Political career section
            political_str = f"\nPolitical Career:\n"
            political_str += f"- {self.political_career['position']} at {self.political_career['institution']}\n"
            political_str += "  Key Responsibilities:\n"
            for resp in self.political_career['responsibilities']:
                political_str += f"  * {resp}\n"
            
            # Combine all sections
            biography = (
                f"Biography of {self.name}:\n"
                f"{education_str}"
                f"{political_str}"
            )
            
            return biography
        except Exception as e:
            return f"Error generating biography: {str(e)}"

# Example usage
if __name__ == "__main__":
    generator = BiographyGenerator()
    print(generator.generate_biography())
```
