"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: "Recommend a type of glass and frame material for a exterior door, considering factors such as weather resistance, security, and energy efficiency."
Generated: DETERMINISTIC_0c5a198e18ac0afd
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DoorMaterialRecommender:
    """
    Recommends glass and frame materials for exterior doors based on weather resistance,
    security, and energy efficiency factors.
    """
    
    def __init__(self):
        self.glass_options = {
            'tempered': {
                'weather_resistance': 8,
                'security': 7,
                'energy_efficiency': 6,
                'description': 'Tempered glass is heat-treated for strength and safety'
            },
            'laminated': {
                'weather_resistance': 7,
                'security': 9,
                'energy_efficiency': 7,
                'description': 'Laminated glass has a plastic interlayer for security'
            },
            'insulated': {
                'weather_resistance': 9,
                'security': 6,
                'energy_efficiency': 9,
                'description': 'Insulated glass has multiple panes for thermal efficiency'
            }
        }
        
        self.frame_options = {
            'fiberglass': {
                'weather_resistance': 9,
                'security': 8,
                'energy_efficiency': 9,
                'description': 'Fiberglass is durable and energy efficient'
            },
            'steel': {
                'weather_resistance': 8,
                'security': 9,
                'energy_efficiency': 7,
                'description': 'Steel provides excellent security'
            },
            'aluminum': {
                'weather_resistance': 7,
                'security': 7,
                'energy_efficiency': 6,
                'description': 'Aluminum is lightweight but less insulating'
            },
            'wood': {
                'weather_resistance': 6,
                'security': 6,
                'energy_efficiency': 8,
                'description': 'Wood offers natural insulation but requires maintenance'
            }
        }
    
    def recommend_materials(self, weather_weight=1.0, security_weight=1.0, energy_weight=1.0):
        """
        Recommends the best glass and frame materials based on weighted factors.
        
        Args:
            weather_weight (float): Importance of weather resistance (default 1.0)
            security_weight (float): Importance of security (default 1.0)
            energy_weight (float): Importance of energy efficiency (default 1.0)
            
        Returns:
            dict: Recommended glass and frame materials with scores and descriptions
        """
        try:
            # Calculate weighted scores for glass
            glass_scores = {}
            for glass_type, properties in self.glass_options.items():
                score = (properties['weather_resistance'] * weather_weight +
                         properties['security'] * security_weight +
                         properties['energy_efficiency'] * energy_weight)
                glass_scores[glass_type] = score
            
            # Calculate weighted scores for frames
            frame_scores = {}
            for frame_type, properties in self.frame_options.items():
                score = (properties['weather_resistance'] * weather_weight +
                         properties['security'] * security_weight +
                         properties['energy_efficiency'] * energy_weight)
                frame_scores[frame_type] = score
            
            # Get top recommendations
            best_glass = max(glass_scores.items(), key=lambda x: x[1])
            best_frame = max(frame_scores.items(), key=lambda x: x[1])
            
            return {
                'glass': {
                    'type': best_glass[0],
                    'score': best_glass[1],
                    'description': self.glass_options[best_glass[0]]['description']
                },
                'frame': {
                    'type': best_frame[0],
                    'score': best_frame[1],
                    'description': self.frame_options[best_frame[0]]['description']
                }
            }
            
        except Exception as e:
            raise ValueError(f"Error calculating recommendations: {str(e)}")

# Example usage
if __name__ == "__main__":
    recommender = DoorMaterialRecommender()
    recommendation = recommender.recommend_materials(
        weather_weight=1.2,
        security_weight=1.1,
        energy_weight=0.9
    )
    print("Recommended Materials:")
    print(f"Glass: {recommendation['glass']['type']} - {recommendation['glass']['description']}")
    print(f"Frame: {recommendation['frame']['type']} - {recommendation['frame']['description']}")
```
