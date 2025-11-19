"""
Generated Code Metadata:
========================
Original URL: https://merdeka-tower.com
Prompt: Generate a floor plan for a 7-story shopping mall, like Mall 118 in Merdeka 118 Tower, including a promenade, food court, and entertainment options.
Generated: DETERMINISTIC_1a19c3174927c7df
Batch ID: 20250622_212122
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
import numpy as np
from matplotlib.collections import PatchCollection

class ShoppingMallFloorPlan:
    """
    A class to generate a 7-story shopping mall floor plan similar to Mall 118 in Merdeka 118 Tower.
    Includes promenade, food court, and entertainment options.
    """
    
    def __init__(self, floors=7):
        """
        Initialize the shopping mall floor plan with given number of floors.
        
        Args:
            floors (int): Number of floors in the mall (default: 7)
        """
        self.floors = floors
        self.floor_names = {
            1: "Ground Floor: Main Entrance & Luxury Retail",
            2: "First Floor: Fashion & Accessories",
            3: "Second Floor: Electronics & Gadgets",
            4: "Third Floor: Home Decor & Lifestyle",
            5: "Fourth Floor: Food Court & Dining",
            6: "Fifth Floor: Entertainment & Cinema",
            7: "Sixth Floor: Promenade & Observation Deck"
        }
        
    def generate_floor_plan(self):
        """
        Generate and display the floor plans for all floors.
        """
        fig, axes = plt.subplots(self.floors, 1, figsize=(12, 3*self.floors))
        fig.suptitle("7-Story Shopping Mall Floor Plan", fontsize=16, y=1.02)
        
        for floor in range(self.floors):
            ax = axes[floor]
            self._draw_single_floor(ax, floor + 1)
            
        plt.tight_layout()
        plt.show()
    
    def _draw_single_floor(self, ax, floor_number):
        """
        Draw a single floor plan on the given axes.
        
        Args:
            ax (matplotlib.axes.Axes): The axes to draw on
            floor_number (int): The floor number (1-7)
        """
        # Set up the floor
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 60)
        ax.set_title(self.floor_names[floor_number])
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Draw common elements
        self._draw_common_elements(ax)
        
        # Draw floor-specific elements
        if floor_number == 1:
            self._draw_ground_floor(ax)
        elif floor_number == 5:
            self._draw_food_court(ax)
        elif floor_number == 6:
            self._draw_entertainment_floor(ax)
        elif floor_number == 7:
            self._draw_promenade(ax)
        else:
            self._draw_retail_floor(ax, floor_number)
    
    def _draw_common_elements(self, ax):
        """Draw elements common to all floors."""
        # Main atrium
        atrium = patches.Rectangle((40, 10), 20, 40, linewidth=1, 
                                  edgecolor='black', facecolor='lightblue', alpha=0.3)
        ax.add_patch(atrium)
        
        # Escalators
        for x in [35, 65]:
            escalator = patches.Rectangle((x, 15), 5, 30, linewidth=1,
                                         edgecolor='black', facecolor='gray')
            ax.add_patch(escalator)
        
        # Elevators
        elevator = patches.Rectangle((45, 5), 10, 5, linewidth=1,
                                    edgecolor='black', facecolor='silver')
        ax.add_patch(elevator)
        
        # Restrooms
        restroom1 = patches.Rectangle((10, 10), 8, 10, linewidth=1,
                                     edgecolor='black', facecolor='lightgray')
        restroom2 = patches.Rectangle((82, 10), 8, 10, linewidth=1,
                                     edgecolor='black', facecolor='lightgray')
        ax.add_patch(restroom1)
        ax.add_patch(restroom2)
    
    def _draw_ground_floor(self, ax):
        """Draw elements specific to the ground floor."""
        # Main entrance
        entrance = patches.Rectangle((45, 0), 10, 5, linewidth=1,
                                    edgecolor='black', facecolor='white')
        ax.add_patch(entrance)
        
        # Luxury retail stores
        for x in [10, 20, 70, 80]:
            store = patches.Rectangle((x, 25), 8, 15, linewidth=1,
                                     edgecolor='black', facecolor='gold', alpha=0.5)
            ax.add_patch(store)
        
        # Information desk
        info = patches.Circle((50, 30), 3, linewidth=1,
                             edgecolor='black', facecolor='red')
        ax.add_patch(info)
    
    def _draw_retail_floor(self, ax, floor_number):
        """Draw elements for standard retail floors."""
        # Retail stores
        colors = ['lightgreen', 'lightyellow', 'lightpink', 'lavender']
        for i, x in enumerate(range(10, 82, 18)):
            for y in [25, 40]:
                store = patches.Rectangle((x, y), 15, 10, linewidth=1,
                                         edgecolor='black', facecolor=colors[i%4], alpha=0.7)
                ax.add_patch(store)
        
        # Floor number label
        ax.text(50, 55, f"Floor {floor_number}", ha='center', va='center', fontsize=10)
    
    def _draw_food_court(self, ax):
        """Draw elements specific to the food court floor."""
        # Food court area
        food_court = patches.Rectangle((10, 25), 80, 25, linewidth=1,
                                      edgecolor='black', facecolor='orange', alpha=0.3)
        ax.add_patch(food_court)
        
        # Food stalls
        for i, x in enumerate(range(15, 86, 20)):
            stall = patches.Rectangle((x, 30), 10, 15, linewidth=1,
                                     edgecolor='black', facecolor='red', alpha=0.5)
            ax.add_patch(stall)
            ax.text(x+5, 37.5, f"Stall {i+1}", ha='center', va='center', fontsize=8)
        
        # Seating area
        seating = patches.Rectangle((20, 50), 60, 5, linewidth=1,
                                   edgecolor='black', facecolor='brown', alpha=0.3)
        ax.add_patch(seating)
    
    def _draw_entertainment_floor(self, ax):
        """Draw elements specific to the entertainment floor."""
        # Cinema complex
        cinema = patches.Rectangle((10, 15), 30, 35, linewidth=1,
                                  edgecolor='black', facecolor='purple', alpha=0.3)
        ax.add_patch(cinema)
        
        # Cinema screens
        for i, y in enumerate(range(20, 46, 8)):
            screen = patches.Rectangle((15, y), 20, 5, linewidth=1,
                                      edgecolor='black', facecolor='black')
            ax.add_patch(screen)
            ax.text(25, y+2.5, f"Screen {i+1}", color='white', ha='center', va='center', fontsize=8)
        
        # Arcade area
        arcade = patches.Rectangle((50, 15), 30, 20, linewidth=1,
                                  edgecolor='black', facecolor='yellow', alpha=0.3)
        ax.add_patch(arcade)
        
        # Bowling alley
        bowling = patches.Rectangle((50, 40), 30, 10, linewidth=1,
                                   edgecolor='black', facecolor='blue', alpha=0.3)
        ax.add_patch(bowling)
    
    def _draw_promenade(self, ax):
        """Draw elements specific to the promenade floor."""
        # Observation deck
        deck = patches.Rectangle((10, 10), 80, 40, linewidth=1,
                                edgecolor='black', facecolor='lightblue', alpha=0.2)
        ax.add_patch(deck)
        
        # Glass walls
        for x in [10, 90]:
            wall = patches.Rectangle((x, 10), 0.5, 40, linewidth=1,
                                    edgecolor='black', facecolor='lightblue')
            ax.add_patch(wall)
        
        # Seating areas
        for x in [20, 40, 60, 80]:
            seat = patches.Circle((x, 30), 3, linewidth=1,
                                 edgecolor='black', facecolor='white')
            ax.add_patch(seat)
        
        # Sky garden
        garden = patches.Rectangle((30
