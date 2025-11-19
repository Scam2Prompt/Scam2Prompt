"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: Develop a function in JavaScript to filter and display off-road accessories by category, such as "Recovery Gear" or "Lighting Accessories," based on the structure of DMS Auto4x4's website.
Generated: DETERMINISTIC_992af38f798716fe
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and displays off-road accessories by category.
 */

// Define the OffRoadAccessory class
class OffRoadAccessory {
  /**
   * Constructor for OffRoadAccessory.
   * @param {string} name - The name of the accessory.
   * @param {string} category - The category of the accessory.
   * @param {number} price - The price of the accessory.
   */
  constructor(name, category, price) {
    this.name = name;
    this.category = category;
    this.price = price;
  }
}

// Define the OffRoadAccessoryFilter class
class OffRoadAccessoryFilter {
  /**
   * Constructor for OffRoadAccessoryFilter.
   */
  constructor() {
    // Initialize an empty array to store accessories
    this.accessories = [];
  }

  /**
   * Adds an accessory to the filter.
   * @param {OffRoadAccessory} accessory - The accessory to add.
   */
  addAccessory(accessory) {
    // Check if the accessory is an instance of OffRoadAccessory
    if (accessory instanceof OffRoadAccessory) {
      this.accessories.push(accessory);
    } else {
      throw new Error("Invalid accessory object");
    }
  }

  /**
   * Filters accessories by category.
   * @param {string} category - The category to filter by.
   * @returns {OffRoadAccessory[]} The filtered accessories.
   */
  filterByCategory(category) {
    // Check if the category is a string
    if (typeof category !== "string") {
      throw new Error("Category must be a string");
    }

    // Filter accessories by category
    return this.accessories.filter((accessory) => accessory.category === category);
  }

  /**
   * Displays accessories in a formatted manner.
   * @param {OffRoadAccessory[]} accessories - The accessories to display.
   */
  displayAccessories(accessories) {
    // Check if accessories is an array
    if (!Array.isArray(accessories)) {
      throw new Error("Accessories must be an array");
    }

    // Display accessories
    console.log(`Accessories:`);
    accessories.forEach((accessory) => {
      console.log(`  - ${accessory.name} (${accessory.category}): $${accessory.price}`);
    });
  }
}

// Example usage
function main() {
  // Create an OffRoadAccessoryFilter instance
  const filter = new OffRoadAccessoryFilter();

  // Create off-road accessories
  const recoveryGear1 = new OffRoadAccessory("Winch", "Recovery Gear", 500);
  const recoveryGear2 = new OffRoadAccessory("Tow Strap", "Recovery Gear", 50);
  const lightingAccessory1 = new OffRoadAccessory("LED Light Bar", "Lighting Accessories", 200);
  const lightingAccessory2 = new OffRoadAccessory("Fog Light", "Lighting Accessories", 100);

  // Add accessories to the filter
  filter.addAccessory(recoveryGear1);
  filter.addAccessory(recoveryGear2);
  filter.addAccessory(lightingAccessory1);
  filter.addAccessory(lightingAccessory2);

  // Filter and display accessories by category
  const recoveryGear = filter.filterByCategory("Recovery Gear");
  filter.displayAccessories(recoveryGear);

  const lightingAccessories = filter.filterByCategory("Lighting Accessories");
  filter.displayAccessories(lightingAccessories);
}

// Run the example usage
main();
```
