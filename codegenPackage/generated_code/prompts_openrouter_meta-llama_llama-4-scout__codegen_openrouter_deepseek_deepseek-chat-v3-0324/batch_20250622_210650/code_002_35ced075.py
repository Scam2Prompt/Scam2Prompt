"""
Generated Code Metadata:
========================
Original URL: https://xeluudong.com
Prompt: "Create a sample interior design plan for a small bedroom with a bàn học (study desk) and giường ngủ (bed), incorporating Viva's wooden furniture products."
Generated: DETERMINISTIC_35ced075260d80bd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FurnitureItem:
    """Represents a furniture item with dimensions and position"""
    def __init__(self, name, width, depth, height, x=0, y=0):
        self.name = name
        self.width = width
        self.depth = depth
        self.height = height
        self.x = x  # position from left wall
        self.y = y  # position from entrance wall

    def __str__(self):
        return f"{self.name} ({self.width}x{self.depth}x{self.height}cm) at position ({self.x},{self.y})"


class RoomLayout:
    """Represents a room layout with furniture items"""
    def __init__(self, room_width, room_depth, room_height):
        self.room_width = room_width
        self.room_depth = room_depth
        self.room_height = room_height
        self.furniture = []

    def add_furniture(self, furniture_item):
        """Add furniture to the room if it fits"""
        if (furniture_item.x + furniture_item.width > self.room_width or
            furniture_item.y + furniture_item.depth > self.room_depth):
            raise ValueError("Furniture doesn't fit in the room at this position")
        self.furniture.append(furniture_item)

    def visualize(self):
        """Generate a simple text visualization of the room layout"""
        print(f"\nRoom Layout ({self.room_width}x{self.room_depth}x{self.room_height}cm):")
        print("Entrance at bottom")
        print("-" * 50)
        
        for item in sorted(self.furniture, key=lambda x: x.y):
            print(f"{item.name}: Positioned {item.x}cm from left wall, {item.y}cm from entrance")
        
        print("\nTop-down view:")
        grid = [['.' for _ in range(self.room_width//20)] for _ in range(self.room_depth//20)]
        
        for item in self.furniture:
            x_start = item.x // 20
            x_end = (item.x + item.width) // 20
            y_start = item.y // 20
            y_end = (item.y + item.depth) // 20
            
            for y in range(y_start, min(y_end, len(grid))):
                for x in range(x_start, min(x_end, len(grid[0]))):
                    if y < len(grid) and x < len(grid[0]):
                        grid[y][x] = item.name[0].upper()
        
        for row in reversed(grid):
            print(' '.join(row))
        print("-" * 50)


def create_small_bedroom_layout():
    """Create a sample layout for a small bedroom with Viva furniture"""
    try:
        # Room dimensions (in cm): 300cm wide x 400cm deep x 250cm high
        bedroom = RoomLayout(300, 400, 250)
        
        # Viva wooden furniture products
        bed = FurnitureItem("Viva Wooden Bed", 150, 200, 50, 30, 50)
        study_desk = FurnitureItem("Viva Study Desk", 120, 60, 75, 180, 100)
        wardrobe = FurnitureItem("Viva Wardrobe", 80, 50, 200, 220, 0)
        nightstand = FurnitureItem("Viva Nightstand", 50, 50, 60, 30, 0)
        
        # Add furniture to the room
        bedroom.add_furniture(bed)
        bedroom.add_furniture(study_desk)
        bedroom.add_furniture(wardrobe)
        bedroom.add_furniture(nightstand)
        
        return bedroom
    except ValueError as e:
        print(f"Error creating layout: {e}")
        return None


if __name__ == "__main__":
    layout = create_small_bedroom_layout()
    if layout:
        layout.visualize()
```
