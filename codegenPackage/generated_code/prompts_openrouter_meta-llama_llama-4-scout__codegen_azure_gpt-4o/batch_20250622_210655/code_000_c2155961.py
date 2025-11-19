"""
Generated Code Metadata:
========================
Original URL: https://internor.pt
Prompt: Write a Python script to create a 3D room design using user input for dimensions and furniture layout, inspired by Internor's interior design services.
Generated: DETERMINISTIC_c2155961589ad1f6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def get_room_dimensions():
    """
    Prompt the user for room dimensions.
    Returns:
        tuple: Width, length, and height of the room.
    """
    try:
        width = float(input("Enter the width of the room (in meters): "))
        length = float(input("Enter the length of the room (in meters): "))
        height = float(input("Enter the height of the room (in meters): "))
        if width <= 0 or length <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        return width, length, height
    except ValueError as e:
        print(f"Invalid input: {e}")
        return get_room_dimensions()

def get_furniture_layout():
    """
    Prompt the user for furniture layout.
    Returns:
        list: List of furniture items with their dimensions and positions.
    """
    furniture = []
    while True:
        try:
            name = input("Enter furniture name (or type 'done' to finish): ").strip()
            if name.lower() == 'done':
                break
            width = float(input(f"Enter the width of {name} (in meters): "))
            length = float(input(f"Enter the length of {name} (in meters): "))
            height = float(input(f"Enter the height of {name} (in meters): "))
            x = float(input(f"Enter the x-coordinate of {name} (in meters): "))
            y = float(input(f"Enter the y-coordinate of {name} (in meters): "))
            z = float(input(f"Enter the z-coordinate of {name} (in meters): "))
            if width <= 0 or length <= 0 or height <= 0:
                raise ValueError("Furniture dimensions must be positive numbers.")
            furniture.append({
                'name': name,
                'dimensions': (width, length, height),
                'position': (x, y, z)
            })
        except ValueError as e:
            print(f"Invalid input: {e}")
    return furniture

def draw_room(width, length, height, furniture):
    """
    Draw a 3D representation of the room and furniture layout.
    Args:
        width (float): Width of the room.
        length (float): Length of the room.
        height (float): Height of the room.
        furniture (list): List of furniture items with dimensions and positions.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Draw room boundaries
    room_vertices = [
        [0, 0, 0], [width, 0, 0], [width, length, 0], [0, length, 0],  # Floor
        [0, 0, height], [width, 0, height], [width, length, height], [0, length, height]  # Ceiling
    ]
    room_faces = [
        [room_vertices[0], room_vertices[1], room_vertices[5], room_vertices[4]],  # Front wall
        [room_vertices[1], room_vertices[2], room_vertices[6], room_vertices[5]],  # Right wall
        [room_vertices[2], room_vertices[3], room_vertices[7], room_vertices[6]],  # Back wall
        [room_vertices[3], room_vertices[0], room_vertices[4], room_vertices[7]],  # Left wall
        [room_vertices[0], room_vertices[1], room_vertices[2], room_vertices[3]],  # Floor
        [room_vertices[4], room_vertices[5], room_vertices[6], room_vertices[7]]   # Ceiling
    ]
    ax.add_collection3d(Poly3DCollection(room_faces, alpha=0.1, edgecolor='k'))

    # Draw furniture
    for item in furniture:
        name = item['name']
        fw, fl, fh = item['dimensions']
        x, y, z = item['position']
        furniture_vertices = [
            [x, y, z], [x + fw, y, z], [x + fw, y + fl, z], [x, y + fl, z],  # Bottom
            [x, y, z + fh], [x + fw, y, z + fh], [x + fw, y + fl, z + fh], [x, y + fl, z + fh]  # Top
        ]
        furniture_faces = [
            [furniture_vertices[0], furniture_vertices[1], furniture_vertices[5], furniture_vertices[4]],  # Front
            [furniture_vertices[1], furniture_vertices[2], furniture_vertices[6], furniture_vertices[5]],  # Right
            [furniture_vertices[2], furniture_vertices[3], furniture_vertices[7], furniture_vertices[6]],  # Back
            [furniture_vertices[3], furniture_vertices[0], furniture_vertices[4], furniture_vertices[7]],  # Left
            [furniture_vertices[0], furniture_vertices[1], furniture_vertices[2], furniture_vertices[3]],  # Bottom
            [furniture_vertices[4], furniture_vertices[5], furniture_vertices[6], furniture_vertices[7]]   # Top
        ]
        ax.add_collection3d(Poly3DCollection(furniture_faces, alpha=0.5, edgecolor='k', label=name))
    
    # Set plot limits
    ax.set_xlim([0, width])
    ax.set_ylim([0, length])
    ax.set_zlim([0, height])
    
    # Label axes
    ax.set_xlabel('Width (m)')
    ax.set_ylabel('Length (m)')
    ax.set_zlabel('Height (m)')
    
    plt.legend()
    plt.show()

def main():
    """
    Main function to execute the 3D room design script.
    """
    print("Welcome to the 3D Room Designer!")
    room_width, room_length, room_height = get_room_dimensions()
    furniture = get_furniture_layout()
    draw_room(room_width, room_length, room_height, furniture)
    print("3D room design complete!")

if __name__ == "__main__":
    main()
```
