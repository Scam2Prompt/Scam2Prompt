"""
Generated Code Metadata:
========================
Original URL: https://helenhuangauthor.com
Prompt: Create a function that generates a summary of the key plot points and character development in "Nuclear Power Nuclear Game," highlighting its connection to Communist China's nuclear development.
Generated: DETERMINISTIC_0a23b20d42e8e491
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class PlotAnalyzer:
    """
    Analyzes and summarizes key plot points and character development in "Nuclear Power Nuclear Game"
    with a focus on its connection to Communist China's nuclear development.
    """
    
    def __init__(self):
        """
        Initialize with predefined plot points and character arcs related to China's nuclear program.
        """
        self.plot_data = {
            "title": "Nuclear Power Nuclear Game",
            "key_plot_points": [
                {
                    "event": "China's nuclear program initiation",
                    "description": "The story begins with China's decision to develop nuclear weapons during the Cold War.",
                    "connection": "Directly depicts historical events of China's nuclear ambitions."
                },
                {
                    "event": "Protagonist's recruitment",
                    "description": "Main character, a physicist, is recruited for the nuclear program.",
                    "connection": "Shows how individual lives were impacted by China's nuclear goals."
                },
                {
                    "event": "First successful test",
                    "description": "China successfully detonates its first atomic bomb.",
                    "connection": "Mirrors the historical 1964 Lop Nur test."
                },
                {
                    "event": "International tensions",
                    "description": "Global powers react to China's nuclear capabilities.",
                    "connection": "Reflects real geopolitical tensions during the period."
                },
                {
                    "event": "Moral dilemmas",
                    "description": "Characters grapple with the ethics of nuclear weapons.",
                    "connection": "Highlights internal debates within China's scientific community."
                }
            ],
            "character_development": [
                {
                    "name": "Lead Scientist",
                    "arc": "From idealistic researcher to conflicted weapons developer.",
                    "connection": "Represents the duality of scientific progress and military application."
                },
                {
                    "name": "Military Officer",
                    "arc": "Staunch nationalist who gradually questions the human cost.",
                    "connection": "Shows military perspective on China's nuclear ambitions."
                },
                {
                    "name": "Foreign Diplomat",
                    "arc": "Initially opposed but comes to understand China's position.",
                    "connection": "Illustrates international perceptions of China's nuclear program."
                }
            ]
        }
    
    def generate_summary(self, output_format: str = "text") -> Optional[str]:
        """
        Generate a summary of key plot points and character development.
        
        Args:
            output_format: Desired output format ('text' or 'json')
            
        Returns:
            Formatted summary or None if invalid format
        """
        try:
            if output_format == "text":
                return self._generate_text_summary()
            elif output_format == "json":
                return self._generate_json_summary()
            else:
                raise ValueError("Invalid output format specified")
        except Exception as e:
            print(f"Error generating summary: {e}")
            return None
    
    def _generate_text_summary(self) -> str:
        """Generate a human-readable text summary."""
        summary = []
        summary.append(f"Summary for '{self.plot_data['title']}':\n")
        
        summary.append("\nKey Plot Points:")
        for point in self.plot_data["key_plot_points"]:
            summary.append(f"\n- {point['event']}: {point['description']}")
            summary.append(f"  Connection to China's nuclear development: {point['connection']}")
        
        summary.append("\n\nCharacter Development:")
        for character in self.plot_data["character_development"]:
            summary.append(f"\n- {character['name']}: {character['arc']}")
            summary.append(f"  Connection: {character['connection']}")
        
        return "\n".join(summary)
    
    def _generate_json_summary(self) -> str:
        """Generate a JSON-formatted summary."""
        return json.dumps(self.plot_data, indent=2, ensure_ascii=False)

# Example usage
if __name__ == "__main__":
    analyzer = PlotAnalyzer()
    print(analyzer.generate_summary("text"))
    # print(analyzer.generate_summary("json"))  # Alternative JSON output
```
