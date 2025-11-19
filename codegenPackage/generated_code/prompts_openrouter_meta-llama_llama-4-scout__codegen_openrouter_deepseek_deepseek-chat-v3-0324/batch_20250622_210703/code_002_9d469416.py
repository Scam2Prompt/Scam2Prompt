"""
Generated Code Metadata:
========================
Original URL: https://guapaaltejer.com
Prompt: Generate a crochet pattern for a beginner-friendly project using a specific yarn weight and hook size, similar to the projects offered on guapaaltejer.com.
Generated: DETERMINISTIC_9d46941611bd11d6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Crochet Pattern Generator for Beginner-Friendly Project
"""

import json
from typing import Dict, List

class CrochetPatternGenerator:
    """
    Generates a beginner-friendly crochet pattern based on yarn weight and hook size.
    """
    
    def __init__(self):
        self.pattern_templates = self._load_pattern_templates()
    
    def _load_pattern_templates(self) -> Dict:
        """Load pattern templates from JSON file"""
        try:
            with open('pattern_templates.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Pattern templates file not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in pattern templates file")
    
    def validate_inputs(self, yarn_weight: str, hook_size: str) -> bool:
        """Validate yarn weight and hook size inputs"""
        valid_yarn_weights = ['lace', 'fingering', 'sport', 'dk', 'worsted', 'bulky', 'super_bulky']
        valid_hook_sizes = ['2.0mm', '2.5mm', '3.0mm', '3.5mm', '4.0mm', '4.5mm', '5.0mm', '5.5mm', '6.0mm']
        
        if yarn_weight.lower() not in valid_yarn_weights:
            raise ValueError(f"Invalid yarn weight. Must be one of: {', '.join(valid_yarn_weights)}")
        
        if hook_size.lower() not in valid_hook_sizes:
            raise ValueError(f"Invalid hook size. Must be one of: {', '.join(valid_hook_sizes)}")
        
        return True
    
    def get_suggested_materials(self, yarn_weight: str) -> Dict:
        """Get suggested materials based on yarn weight"""
        materials = {
            'lace': {'yarn': '100% cotton lace weight', 'amount': '200-300 yards'},
            'fingering': {'yarn': 'Merino wool fingering', 'amount': '300-400 yards'},
            'sport': {'yarn': 'Acrylic sport weight', 'amount': '400-500 yards'},
            'dk': {'yarn': 'Wool blend DK', 'amount': '500-600 yards'},
            'worsted': {'yarn': '100% acrylic worsted', 'amount': '600-800 yards'},
            'bulky': {'yarn': 'Superwash bulky wool', 'amount': '800-1000 yards'},
            'super_bulky': {'yarn': 'Chenille super bulky', 'amount': '1000-1200 yards'}
        }
        return materials.get(yarn_weight.lower(), {})
    
    def generate_pattern(self, project_name: str, yarn_weight: str, hook_size: str) -> Dict:
        """
        Generate a complete crochet pattern
        Args:
            project_name: Name of the project (scarf, hat, etc.)
            yarn_weight: Yarn weight category
            hook_size: Crochet hook size
        Returns:
            Dictionary containing complete pattern
        """
        try:
            self.validate_inputs(yarn_weight, hook_size)
            
            template = self.pattern_templates.get(project_name.lower())
            if not template:
                raise ValueError(f"No template found for project: {project_name}")
            
            materials = self.get_suggested_materials(yarn_weight)
            
            pattern = {
                'project': project_name.capitalize(),
                'difficulty': 'Beginner',
                'yarn_weight': yarn_weight.capitalize(),
                'hook_size': hook_size,
                'materials': materials,
                'gauge': f"4x4 inches = {template['gauge']} stitches",
                'notes': template['notes'],
                'instructions': template['instructions']
            }
            
            return pattern
            
        except Exception as e:
            raise Exception(f"Error generating pattern: {str(e)}")
    
    def save_pattern_to_file(self, pattern: Dict, filename: str = 'crochet_pattern.json'):
        """Save generated pattern to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(pattern, f, indent=4)
            return True
        except Exception as e:
            raise Exception(f"Error saving pattern: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        generator = CrochetPatternGenerator()
        
        # Generate a pattern for a scarf with worsted weight yarn and 5.0mm hook
        pattern = generator.generate_pattern(
            project_name="scarf",
            yarn_weight="worsted",
            hook_size="5.0mm"
        )
        
        # Save the pattern to a file
        generator.save_pattern_to_file(pattern)
        
        print("Pattern generated successfully!")
        print(json.dumps(pattern, indent=4))
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
