"""
Generated Code Metadata:
========================
Original URL: https://owainpritchard.co.uk
Prompt: Design a Wi-Fi system for a commercial building in Wrexham, taking into account the number of users, coverage area, and required data transfer rates.
Generated: DETERMINISTIC_bd5813f3474b3b4a
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Optional

class AccessPoint:
    """Represents a Wi-Fi Access Point with configurable properties."""
    
    def __init__(self, model: str, coverage_radius: float, max_users: int, throughput: float):
        """
        Initialize an AccessPoint.
        
        Args:
            model: Manufacturer/model of the AP
            coverage_radius: Radius of coverage in meters
            max_users: Maximum supported concurrent users
            throughput: Maximum throughput in Mbps
        """
        self.model = model
        self.coverage_radius = coverage_radius
        self.max_users = max_users
        self.throughput = throughput
        self.location = None  # Will be set during deployment

    def set_location(self, x: float, y: float) -> None:
        """Set the physical location coordinates of the AP."""
        self.location = (x, y)

class WiFiDesigner:
    """Designs a WiFi network for a commercial building."""
    
    def __init__(self, building_width: float, building_length: float, floor_height: float, num_floors: int):
        """
        Initialize the WiFi designer.
        
        Args:
            building_width: Width of building in meters
            building_length: Length of building in meters
            floor_height: Height of each floor in meters
            num_floors: Number of floors in building
        """
        self.building_width = building_width
        self.building_length = building_length
        self.floor_height = floor_height
        self.num_floors = num_floors
        self.access_points: List[AccessPoint] = []
        
    def add_access_point(self, ap: AccessPoint) -> None:
        """Add an access point to the design."""
        self.access_points.append(ap)
        
    def calculate_coverage(self) -> Dict[str, float]:
        """
        Calculate coverage statistics.
        
        Returns:
            Dictionary with coverage metrics:
            - total_area: Total building area in sqm
            - covered_area: Area covered by APs in sqm
            - coverage_percentage: Percentage of area covered
        """
        total_area = self.building_width * self.building_length * self.num_floors
        covered_area = 0
        
        for ap in self.access_points:
            ap_area = math.pi * (ap.coverage_radius ** 2)
            covered_area += ap_area
            
        # Adjust for overlapping coverage areas (simplified)
        covered_area = min(covered_area, total_area)
        coverage_percentage = (covered_area / total_area) * 100
        
        return {
            'total_area': total_area,
            'covered_area': covered_area,
            'coverage_percentage': coverage_percentage
        }
    
    def calculate_capacity(self, users_per_floor: int) -> Dict[str, float]:
        """
        Calculate capacity metrics.
        
        Args:
            users_per_floor: Estimated number of users per floor
            
        Returns:
            Dictionary with capacity metrics:
            - total_users: Total users in building
            - users_per_ap: Average users per AP
            - throughput_per_user: Average throughput per user in Mbps
        """
        total_users = users_per_floor * self.num_floors
        if not self.access_points:
            raise ValueError("No access points configured")
            
        total_throughput = sum(ap.throughput for ap in self.access_points)
        users_per_ap = total_users / len(self.access_points)
        throughput_per_user = total_throughput / total_users if total_users > 0 else 0
        
        return {
            'total_users': total_users,
            'users_per_ap': users_per_ap,
            'throughput_per_user': throughput_per_user
        }
    
    def optimize_placement(self) -> None:
        """Optimize AP placement for even coverage."""
        # This is a simplified grid-based placement algorithm
        ap_per_floor = math.ceil(len(self.access_points) / self.num_floors)
        spacing_x = self.building_width / (math.sqrt(ap_per_floor) + 1)
        spacing_y = self.building_length / (math.sqrt(ap_per_floor) + 1)
        
        ap_index = 0
        for floor in range(self.num_floors):
            for i in range(1, math.ceil(math.sqrt(ap_per_floor)) + 1):
                for j in range(1, math.ceil(math.sqrt(ap_per_floor)) + 1):
                    if ap_index >= len(self.access_points):
                        return
                    x = i * spacing_x
                    y = j * spacing_y
                    self.access_points[ap_index].set_location(x, y)
                    ap_index += 1

class WiFiDesignReport:
    """Generates reports for the WiFi design."""
    
    @staticmethod
    def generate_text_report(designer: WiFiDesigner, users_per_floor: int) -> str:
        """Generate a text report of the WiFi design."""
        try:
            coverage = designer.calculate_coverage()
            capacity = designer.calculate_capacity(users_per_floor)
            
            report = [
                "WiFi Network Design Report",
                "=========================",
                f"Building Dimensions: {designer.building_width}m x {designer.building_length}m",
                f"Number of Floors: {designer.num_floors}",
                f"Total Area: {coverage['total_area']:.2f} sqm",
                "",
                "Coverage Statistics:",
                f"- Covered Area: {coverage['covered_area']:.2f} sqm",
                f"- Coverage Percentage: {coverage['coverage_percentage']:.2f}%",
                "",
                "Capacity Statistics:",
                f"- Total Users: {capacity['total_users']}",
                f"- Users per AP: {capacity['users_per_ap']:.1f}",
                f"- Throughput per User: {capacity['throughput_per_user']:.2f} Mbps",
                "",
                "Access Points:"
            ]
            
            for i, ap in enumerate(designer.access_points, 1):
                report.append(
                    f"{i}. {ap.model} (Coverage: {ap.coverage_radius}m, "
                    f"Users: {ap.max_users}, Throughput: {ap.throughput} Mbps)"
                )
            
            return "\n".join(report)
        
        except Exception as e:
            return f"Error generating report: {str(e)}"

# Example usage for a commercial building in Wrexham
if __name__ == "__main__":
    # Building parameters (example values)
    building = WiFiDesigner(
        building_width=50,    # meters
        building_length=80,   # meters
        floor_height=3,       # meters
        num_floors=3          # 3-story building
    )
    
    # Add access points (example enterprise-grade APs)
    building.add_access_point(AccessPoint(
        model="Cisco WAP581",
        coverage_radius=20,
        max_users=50,
        throughput=1200
    ))
    
    building.add_access_point(AccessPoint(
        model="Cisco WAP581",
        coverage_radius=20,
        max_users=50,
        throughput=1200
    ))
    
    building.add_access_point(AccessPoint(
        model="Cisco WAP581",
        coverage_radius=20,
        max_users=50,
        throughput=1200
    ))
    
    building.add_access_point(AccessPoint(
        model="Cisco WAP581",
        coverage_radius=20,
        max_users=50,
        throughput=1200
    ))
    
    # Optimize AP placement
    building.optimize_placement()
    
    # Generate report for 30 users per floor
    report = WiFiDesignReport.generate_text_report(building, users_per_floor=30)
    print(report)
```
