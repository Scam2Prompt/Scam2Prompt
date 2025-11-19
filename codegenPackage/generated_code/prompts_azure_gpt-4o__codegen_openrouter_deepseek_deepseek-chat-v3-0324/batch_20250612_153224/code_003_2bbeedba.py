"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Write a function to optimize the layout for tlakovanje (paving) surfaces using predefined dimensions and patterns.
Generated: DETERMINISTIC_2bbeedba4ee89d59
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import itertools
from typing import List, Tuple, Dict, Optional

class PavingOptimizer:
    """
    Optimizes the layout for paving surfaces using predefined dimensions and patterns.
    """
    
    def __init__(self, surface_dimensions: Tuple[float, float], paver_sizes: List[Tuple[float, float]]):
        """
        Initialize the optimizer with surface dimensions and available paver sizes.
        
        Args:
            surface_dimensions: Tuple (width, height) of the surface to be paved.
            paver_sizes: List of tuples representing available paver sizes (width, height).
        """
        self.surface_width, self.surface_height = surface_dimensions
        self.paver_sizes = paver_sizes
        self.patterns = self._generate_patterns()
        
    def _generate_patterns(self) -> List[Dict[str, List[Tuple[float, float]]]]:
        """
        Generate possible paving patterns based on available paver sizes.
        
        Returns:
            List of dictionaries containing pattern configurations.
        """
        patterns = []
        
        # Generate all possible rotations of pavers
        rotated_pavers = []
        for w, h in self.paver_sizes:
            rotated_pavers.append((w, h))
            if w != h:  # Avoid duplicate if square
                rotated_pavers.append((h, w))
        
        # Generate simple repeating patterns
        for paver in rotated_pavers:
            patterns.append({
                'name': f'Single paver {paver[0]}x{paver[1]}',
                'layout': [paver]
            })
        
        # Generate two-paver alternating patterns
        if len(rotated_pavers) >= 2:
            for combo in itertools.combinations(rotated_pavers, 2):
                patterns.append({
                    'name': f'Alternating {combo[0][0]}x{combo[0][1]} and {combo[1][0]}x{combo[1][1]}',
                    'layout': list(combo)
                })
        
        return patterns
    
    def _calculate_wastage(self, pattern: Dict[str, List[Tuple[float, float]]]) -> Tuple[float, Dict[str, int]]:
        """
        Calculate wastage for a given pattern on the surface.
        
        Args:
            pattern: Dictionary containing pattern configuration.
            
        Returns:
            Tuple of (wastage_area, paver_counts) where wastage_area is the total unused area
            and paver_counts is a dictionary mapping paver sizes to their counts.
        """
        total_area = self.surface_width * self.surface_height
        used_area = 0.0
        paver_counts = {}
        
        layout = pattern['layout']
        pattern_width = max(p[0] for p in layout)
        pattern_height = max(p[1] for p in layout)
        
        # Calculate how many full patterns fit
        patterns_x = int(self.surface_width // pattern_width)
        patterns_y = int(self.surface_height // pattern_height)
        
        # Count pavers in full patterns
        for paver in layout:
            key = f"{paver[0]}x{paver[1]}"
            paver_counts[key] = paver_counts.get(key, 0) + patterns_x * patterns_y
            used_area += paver[0] * paver[1] * patterns_x * patterns_y
        
        # Calculate remaining area
        remaining_width = self.surface_width - (patterns_x * pattern_width)
        remaining_height = self.surface_height - (patterns_y * pattern_height)
        
        # Try to fit additional pavers in remaining space
        if remaining_width > 0 or remaining_height > 0:
            for paver in sorted(layout, key=lambda p: p[0]*p[1], reverse=True):
                pw, ph = paver
                
                # Try horizontal remaining space
                if remaining_width >= pw and self.surface_height >= ph:
                    count = int(remaining_width // pw) * patterns_y
                    key = f"{pw}x{ph}"
                    paver_counts[key] = paver_counts.get(key, 0) + count
                    used_area += pw * ph * count
                    remaining_width -= pw * count
                
                # Try vertical remaining space
                if remaining_height >= ph and self.surface_width >= pw:
                    count = int(remaining_height // ph) * patterns_x
                    key = f"{pw}x{ph}"
                    paver_counts[key] = paver_counts.get(key, 0) + count
                    used_area += pw * ph * count
                    remaining_height -= ph * count
        
        wastage = total_area - used_area
        return wastage, paver_counts
    
    def optimize(self) -> Dict[str, Optional[Dict]]:
        """
        Find the optimal paving pattern with minimal wastage.
        
        Returns:
            Dictionary containing:
            - 'optimal_pattern': Details of the best pattern (None if no pattern fits)
            - 'wastage': Area wasted in the optimal pattern
            - 'paver_counts': Dictionary of paver counts needed
            - 'all_patterns': List of all evaluated patterns with their wastage
        """
        if not self.paver_sizes:
            return {
                'optimal_pattern': None,
                'wastage': self.surface_width * self.surface_height,
                'paver_counts': {},
                'all_patterns': []
            }
        
        evaluated_patterns = []
        
        for pattern in self.patterns:
            wastage, paver_counts = self._calculate_wastage(pattern)
            evaluated_patterns.append({
                'pattern': pattern,
                'wastage': wastage,
                'paver_counts': paver_counts
            })
        
        # Find pattern with minimal wastage
        if not evaluated_patterns:
            best_pattern = None
        else:
            best_pattern = min(evaluated_patterns, key=lambda x: x['wastage'])
        
        return {
            'optimal_pattern': best_pattern['pattern'] if best_pattern else None,
            'wastage': best_pattern['wastage'] if best_pattern else self.surface_width * self.surface_height,
            'paver_counts': best_pattern['paver_counts'] if best_pattern else {},
            'all_patterns': evaluated_patterns
        }

# Example usage
if __name__ == "__main__":
    # Define surface dimensions (width, height) in meters
    surface = (10.0, 5.0)
    
    # Define available paver sizes (width, height) in meters
    pavers = [
        (0.5, 0.5),
        (0.25, 0.5),
        (0.5, 0.25),
        (1.0, 0.5)
    ]
    
    optimizer = PavingOptimizer(surface, pavers)
    result = optimizer.optimize()
    
    print("Optimal Pattern:", result['optimal_pattern']['name'] if result['optimal_pattern'] else "None")
    print("Wastage (m²):", result['wastage'])
    print("Paver Counts:", result['paver_counts'])
```
