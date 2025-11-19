"""
Generated Code Metadata:
========================
Original URL: https://rabbymorgan.pages.dev
Prompt: Generate a review of the 2025 Kia Sportage PHEV, focusing on its electric-only range, cargo space, and overall performance, using the provided specs and reviews.
Generated: DETERMINISTIC_6de272939d0e5f5b
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class VehicleReview:
    """
    A class to generate a review for a vehicle based on provided specifications and reviews.
    """
    
    def __init__(self, model: str, year: int, specs: dict, reviews: list):
        """
        Initialize the VehicleReview with model, year, specs, and reviews.
        
        Args:
            model (str): The model of the vehicle.
            year (int): The year of the vehicle.
            specs (dict): Dictionary containing vehicle specifications.
            reviews (list): List of review snippets from various sources.
        """
        self.model = model
        self.year = year
        self.specs = specs
        self.reviews = reviews
        
    def generate_review(self) -> str:
        """
        Generate a comprehensive review of the vehicle.
        
        Returns:
            str: Formatted review text.
        """
        try:
            # Validate inputs
            if not isinstance(self.model, str) or not isinstance(self.year, int):
                raise ValueError("Model must be a string and year must be an integer.")
            if not isinstance(self.specs, dict) or not isinstance(self.reviews, list):
                raise ValueError("Specs must be a dictionary and reviews must be a list.")
                
            # Generate sections
            intro = self._generate_intro()
            electric_range = self._generate_electric_range_section()
            cargo_space = self._generate_cargo_space_section()
            performance = self._generate_performance_section()
            conclusion = self._generate_conclusion()
            
            # Combine sections
            review = f"{intro}\n\n{electric_range}\n\n{cargo_space}\n\n{performance}\n\n{conclusion}"
            return review
            
        except Exception as e:
            return f"Error generating review: {str(e)}"
    
    def _generate_intro(self) -> str:
        """Generate the introduction section of the review."""
        return f"{self.year} {self.model} Review\n\n" \
               "The {self.year} {self.model} is a plug-in hybrid electric vehicle (PHEV) " \
               "that combines electric efficiency with traditional power when needed. " \
               "Here's our detailed review based on specifications and expert opinions."
    
    def _generate_electric_range_section(self) -> str:
        """Generate the electric-only range section."""
        range_km = self.specs.get("electric_range_km", 0)
        range_miles = round(range_km * 0.621371, 1)
        
        range_reviews = [r for r in self.reviews if "electric range" in r.lower()]
        range_comment = " ".join(range_reviews) if range_reviews else \
            "Reviewers generally found the electric range to be competitive in its class."
            
        return f"Electric-Only Range:\n" \
               f"The {self.model} offers an electric-only range of {range_km} km ({range_miles} miles). " \
               f"{range_comment}"
    
    def _generate_cargo_space_section(self) -> str:
        """Generate the cargo space section."""
        cargo_liters = self.specs.get("cargo_space_liters", 0)
        cargo_cuft = round(cargo_liters * 0.0353147, 1)
        
        cargo_reviews = [r for r in self.reviews if "cargo" in r.lower() or "space" in r.lower()]
        cargo_comment = " ".join(cargo_reviews) if cargo_reviews else \
            "The cargo space was noted to be practical for most daily needs."
            
        return f"Cargo Space:\n" \
               f"With {cargo_liters} liters ({cargo_cuft} cubic feet) of cargo space, " \
               f"the {self.model} provides {cargo_comment}"
    
    def _generate_performance_section(self) -> str:
        """Generate the performance section."""
        hp = self.specs.get("horsepower", 0)
        torque = self.specs.get("torque_nm", 0)
        torque_lbft = round(torque * 0.737562, 1)
        
        perf_reviews = [r for r in self.reviews if "performance" in r.lower() or "drive" in r.lower()]
        perf_comment = " ".join(perf_reviews) if perf_reviews else \
            "The vehicle delivers smooth performance with good power delivery."
            
        return f"Performance:\n" \
               f"The {self.model} produces {hp} horsepower and {torque} Nm ({torque_lbft} lb-ft) of torque. " \
               f"{perf_comment}"
    
    def _generate_conclusion(self) -> str:
        """Generate the conclusion section."""
        return "Conclusion:\n" \
               f"The {self.year} {self.model} PHEV offers a compelling package with its " \
               "electric range, practical cargo space, and balanced performance. " \
               "It's a strong contender in the PHEV SUV market."


# Example usage
if __name__ == "__main__":
    specs = {
        "electric_range_km": 70,
        "cargo_space_liters": 540,
        "horsepower": 265,
        "torque_nm": 350
    }
    
    reviews = [
        "The electric range is sufficient for most daily commutes.",
        "Cargo space is generous for a vehicle in this class.",
        "Performance is smooth with instant torque from the electric motor."
    ]
    
    sportage_review = VehicleReview(
        model="Kia Sportage PHEV",
        year=2025,
        specs=specs,
        reviews=reviews
    )
    
    print(sportage_review.generate_review())
```
