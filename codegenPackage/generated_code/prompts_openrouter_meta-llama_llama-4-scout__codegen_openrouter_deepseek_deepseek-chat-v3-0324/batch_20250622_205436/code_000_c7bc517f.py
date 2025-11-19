"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Write a script for a sales video that aims to boost conversions for an e-commerce business, incorporating consumer psychology principles as recommended by Kraken Media.
Generated: DETERMINISTIC_c7bc517fe937b383
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
E-commerce Sales Video Script Generator
Incorporates consumer psychology principles from Kraken Media recommendations
"""

import json
from typing import List, Dict

class SalesVideoScript:
    """
    Generates a high-conversion sales video script for e-commerce businesses
    """
    
    def __init__(self, product_name: str, target_audience: str, key_benefits: List[str], 
                 pain_points: List[str], social_proof: Dict[str, str], cta: str):
        """
        Initialize script generator with product and audience details
        
        Args:
            product_name: Name of the product/service
            target_audience: Description of ideal customer
            key_benefits: List of main product benefits
            pain_points: List of customer pain points product solves
            social_proof: Dict with testimonials/stats (e.g., {"customers": "10,000+", "rating": "4.9"})
            cta: Clear call-to-action phrase
        """
        self.product_name = product_name
        self.target_audience = target_audience
        self.key_benefits = key_benefits
        self.pain_points = pain_points
        self.social_proof = social_proof
        self.cta = cta
        
        # Validate inputs
        if not all([product_name, target_audience, key_benefits, pain_points, cta]):
            raise ValueError("All required parameters must be provided")
        if len(key_benefits) < 2:
            raise ValueError("At least 2 key benefits required")
        if len(pain_points) < 1:
            raise ValueError("At least 1 pain point required")
    
    def _create_hook(self) -> str:
        """Create attention-grabbing opening hook"""
        return f"[Scene: Close-up of frustrated {self.target_audience}]\n" \
               f"\"Tired of {self.pain_points[0]}? What if I told you there's a better way?\"\n" \
               f"[Cut to product shot] \"Introducing {self.product_name} - the solution you've been waiting for.\""
    
    def _create_problem_agitation(self) -> str:
        """Amplify pain points using psychological triggers"""
        script = "[Scene: Person struggling with the problem]\n"
        for i, pain in enumerate(self.pain_points):
            script += f"\"{pain}\"\n" \
                     f"[Cut to frustrated expression]\n"
            if i < len(self.pain_points) - 1:
                script += "\"And it gets worse...\"\n"
        return script
    
    def _create_solution(self) -> str:
        """Present product as the perfect solution"""
        script = f"[Scene: Product in action]\n" \
                 f"\"But what if you could...\"\n"
        for benefit in self.key_benefits:
            script += f"• {benefit}\n"
        script += f"[Cut to happy customer]\n" \
                 f"\"With {self.product_name}, you get all this and more.\""
        return script
    
    def _create_social_proof(self) -> str:
        """Incorporate social proof elements"""
        proof_elements = []
        if 'customers' in self.social_proof:
            proof_elements.append(f"\"Join {self.social_proof['customers']} satisfied customers\"")
        if 'rating' in self.social_proof:
            proof_elements.append(f"\"Rated {self.social_proof['rating']} stars\"")
        if 'testimonial' in self.social_proof:
            proof_elements.append(f"\"{self.social_proof['testimonial']}\"")
        
        script = "[Scene: Customer testimonials or stats overlay]\n"
        script += "\n".join(proof_elements)
        return script
    
    def _create_urgency(self) -> str:
        """Create scarcity/urgency triggers"""
        return "[Scene: Clock ticking or limited stock counter]\n" \
               "\"But hurry - this offer won't last forever!\"\n" \
               "\"Order now before it's too late!\""
    
    def _create_cta(self) -> str:
        """Strong call-to-action with clear instructions"""
        return f"[Scene: Product with buy button overlay]\n" \
               f"\"Click the button now to get your {self.product_name} today!\"\n" \
               f"\"{self.cta}\""
    
    def generate_script(self) -> str:
        """Generate complete video script"""
        sections = [
            self._create_hook(),
            self._create_problem_agitation(),
            self._create_solution(),
            self._create_social_proof(),
            self._create_urgency(),
            self._create_cta()
        ]
        return "\n\n".join(sections)
    
    def save_script(self, filename: str):
        """Save script to JSON file"""
        script = {
            "product": self.product_name,
            "target_audience": self.target_audience,
            "script": self.generate_script()
        }
        with open(filename, 'w') as f:
            json.dump(script, f, indent=2)

# Example usage
if __name__ == "__main__":
    try:
        # Configuration for a sample product
        product_config = {
            "product_name": "UltraClean Water Filter",
            "target_audience": "health-conscious families",
            "key_benefits": [
                "Crystal clear water without harmful chemicals",
                "Easy installation in under 5 minutes",
                "Saves money compared to bottled water"
            ],
            "pain_points": [
                "Worried about contaminants in your tap water",
                "Tired of spending money on bottled water",
                "Concerned about plastic waste"
            ],
            "social_proof": {
                "customers": "50,000+",
                "rating": "4.8",
                "testimonial": "\"Best purchase ever! My family's water has never tasted better.\" - Sarah J."
            },
            "cta": "Click below to get 20% off your first order!"
        }
        
        # Generate and save script
        script_generator = SalesVideoScript(**product_config)
        print("Generated Script:\n")
        print(script_generator.generate_script())
        script_generator.save_script("ultraclean_sales_script.json")
        
    except Exception as e:
        print(f"Error generating script: {str(e)}")
```
