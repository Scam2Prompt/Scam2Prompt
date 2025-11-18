"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Write Python code to calculate the cost estimate for a civil works project, including building painting, tile installation, gypsum board work, and electrical and plumbing services, as described on the AKNAN website.
Generated: DETERMINISTIC_000464cc28579864
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CivilWorksEstimator:
    """
    A class to estimate costs for various civil works projects.
    """

    def __init__(self):
        # Initialize cost parameters for different services
        self.costs = {
            'painting': 15.0,  # cost per square meter
            'tile_installation': 25.0,  # cost per square meter
            'gypsum_board': 10.0,  # cost per square meter
            'electrical_service': 200.0,  # flat rate
            'plumbing_service': 150.0  # flat rate
        }

    def estimate_cost(self, service: str, area: float = 0) -> float:
        """
        Estimate the cost for a given service based on area or flat rates.

        :param service: The type of service (painting, tile_installation, gypsum_board, electrical_service, plumbing_service)
        :param area: The area in square meters (only for area-based services)
        :return: Estimated cost for the service
        :raises ValueError: If the service type is unknown or area is negative
        """
        # Check if the service is a valid one
        if service not in self.costs:
            raise ValueError(f"Unknown service type: {service}")

        # Area-based services
        if service in ['painting', 'tile_installation', 'gypsum_board']:
            if area < 0:
                raise ValueError("Area must be a non-negative value.")
            return self.costs[service] * area
        
        # Flat-rate services
        return self.costs[service]

    def total_estimate(self, area_painting: float, area_tile: float, area_gypsum: float, electrical: bool, plumbing: bool) -> float:
        """
        Calculate the total estimated cost for the project.

        :param area_painting: Area for painting
        :param area_tile: Area for tile installation
        :param area_gypsum: Area for gypsum board work
        :param electrical: Flag to include electrical services
        :param plumbing: Flag to include plumbing services
        :return: Total estimated cost
        """
        total_cost = 0.0
        
        # Calculate costs for painting, tile installation, and gypsum board work
        total_cost += self.estimate_cost('painting', area_painting)
        total_cost += self.estimate_cost('tile_installation', area_tile)
        total_cost += self.estimate_cost('gypsum_board', area_gypsum)

        # Include flat rate costs if services are required
        if electrical:
            total_cost += self.estimate_cost('electrical_service')
        if plumbing:
            total_cost += self.estimate_cost('plumbing_service')

        return total_cost


if __name__ == "__main__":
    estimator = CivilWorksEstimator()
    
    # Example input for estimating costs
    try:
        painting_area = 100  # square meters
        tile_area = 50  # square meters
        gypsum_area = 75  # square meters
        include_electrical = True
        include_plumbing = False

        total = estimator.total_estimate(painting_area, tile_area, gypsum_area, include_electrical, include_plumbing)
        print(f"Total estimated cost: ${total:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
