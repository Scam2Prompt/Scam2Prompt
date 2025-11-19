"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Create a JavaScript code example that simulates the inventory management for industrial brushes, including features for standard and custom products as highlighted on the VIRCOMEM site.
Generated: DETERMINISTIC_069bdc4e7603c4ef
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Inventory Management System for Industrial Brushes

// Define a class for Brush
class Brush {
  constructor(id, name, type, price, stock) {
    this.id = id; // Unique identifier for the brush
    this.name = name; // Name of the brush
    this.type = type; // Type of brush (e.g., "standard", "custom")
    this.price = price; // Price of the brush
    this.stock = stock; // Number of brushes in stock
  }

  // Method to update stock
  updateStock(amount) {
    if (amount < 0 && Math.abs(amount) > this.stock) {
      throw new Error("Insufficient stock to remove the requested amount.");
    }
    this.stock += amount;
  }

  // Method to display brush details
  getDetails() {
    return {
      id: this.id,
      name: this.name,
      type: this.type,
      price: this.price,
      stock: this.stock,
    };
  }
}

// Define a class for Inventory Management
class Inventory {
  constructor() {
    this.brushes = []; // Array to store all brushes
  }

  // Add a new brush to the inventory
  addBrush(brush) {
    if (!(brush instanceof Brush)) {
      throw new Error("Invalid brush object.");
    }
    this.brushes.push(brush);
  }

  // Remove a brush from the inventory by ID
  removeBrush(id) {
    const index = this.brushes.findIndex((brush) => brush.id === id);
    if (index === -1) {
      throw new Error("Brush with the given ID not found.");
    }
    this.brushes.splice(index, 1);
  }

  // Find a brush by ID
  findBrushById(id) {
    return this.brushes.find((brush) => brush.id === id) || null;
  }

  // List all brushes in the inventory
  listBrushes() {
    return this.brushes.map((brush) => brush.getDetails());
  }
}

// Example usage
try {
  // Create an inventory instance
  const inventory = new Inventory();

  // Add standard and custom brushes
  const standardBrush = new Brush(1, "Standard Brush", "standard", 25.99, 100);
  const customBrush = new Brush(2, "Custom Brush", "custom", 45.99, 50);

  inventory.addBrush(standardBrush);
  inventory.addBrush(customBrush);

  // Display all brushes
  console.log("All Brushes:", inventory.listBrushes());

  // Update stock for a brush
  standardBrush.updateStock(-10); // Remove 10 brushes from stock
  console.log("Updated Standard Brush Stock:", standardBrush.getDetails());

  // Find a brush by ID
  const foundBrush = inventory.findBrushById(2);
  console.log("Found Brush:", foundBrush ? foundBrush.getDetails() : "Not Found");

  // Remove a brush from inventory
  inventory.removeBrush(1);
  console.log("All Brushes After Removal:", inventory.listBrushes());
} catch (error) {
  console.error("Error:", error.message);
}
```
