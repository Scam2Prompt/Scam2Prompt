"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Develop a Python program to design a cafe layout with an outdoor seating area, incorporating modern design elements as discussed in Nyiku Design's blog on outdoor cafe design.
Generated: DETERMINISTIC_4186e59d3f48387e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class CafeLayout:
    def __init__(self, width, height):
        """
        Initialize the cafe layout with specified dimensions.

        :param width: Width of the cafe layout
        :param height: Height of the cafe layout
        """
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots(figsize=(width / 10, height / 10))
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(0, height)
        self.ax.set_aspect('equal')
        self.ax.axis('off')  # Hide axes

    def add_table(self, x, y, table_width, table_height):
        """
        Add a table to the cafe layout.

        :param x: X-coordinate of the table
        :param y: Y-coordinate of the table
        :param table_width: Width of the table
        :param table_height: Height of the table
        """
        table = patches.Rectangle((x, y), table_width, table_height, 
                                   edgecolor='black', facecolor='lightgray', linewidth=2)
        self.ax.add_patch(table)

    def add_outdoor_seating(self, num_tables, table_width, table_height, spacing):
        """
        Add outdoor seating to the cafe layout.

        :param num_tables: Number of tables to add
        :param table_width: Width of each table
        :param table_height: Height of each table
        :param spacing: Space between tables
        """
        try:
            for i in range(num_tables):
                x = (table_width + spacing) * (i % 3)  # 3 tables per row
                y = (table_height + spacing) * (i // 3)  # New row for every 3 tables
                self.add_table(x, y, table_width, table_height)
        except Exception as e:
            print(f"Error adding outdoor seating: {e}")

    def display_layout(self):
        """Display the cafe layout."""
        plt.title("Cafe Layout with Outdoor Seating")
        plt.show()

if __name__ == "__main__":
    # Define the dimensions of the cafe layout
    cafe_width = 30  # Width of the cafe layout
    cafe_height = 20  # Height of the cafe layout

    # Create a CafeLayout instance
    cafe = CafeLayout(cafe_width, cafe_height)

    # Add outdoor seating with specified parameters
    outdoor_tables = 6  # Number of outdoor tables
    table_width = 2  # Width of each table
    table_height = 1.5  # Height of each table
    spacing = 1  # Space between tables

    cafe.add_outdoor_seating(outdoor_tables, table_width, table_height, spacing)

    # Display the final layout
    cafe.display_layout()
```
