"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "Generate a code snippet in JavaScript to create a simple window configuration tool, allowing users to select window types (e.g., Aluplast Ideal 5000) and view their specifications."
Generated: DETERMINISTIC_99344b563b44cc60
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// window_config_tool.js

class Window {
  /**
   * Represents a window type with its specifications.
   * @param {string} name - The name of the window type.
   * @param {object} specs - An object containing the window's specifications.
   */
  constructor(name, specs) {
    this.name = name;
    this.specs = specs;
  }

  /**
   * Displays the window's specifications.
   */
  displaySpecs() {
    console.log(`Window Type: ${this.name}`);
    for (const spec in this.specs) {
      console.log(`${spec}: ${this.specs[spec]}`);
    }
  }
}

class WindowConfigTool {
  /**
   * A simple window configuration tool.
   */
  constructor() {
    this.windowTypes = [];
  }

  /**
   * Adds a new window type to the tool.
   * @param {Window} windowType - The window type to add.
   */
  addWindowType(windowType) {
    this.windowTypes.push(windowType);
  }

  /**
   * Displays all available window types.
   */
  displayWindowTypes() {
    console.log("Available Window Types:");
    this.windowTypes.forEach((windowType, index) => {
      console.log(`${index + 1}. ${windowType.name}`);
    });
  }

  /**
   * Displays the specifications of a selected window type.
   * @param {number} index - The index of the selected window type.
   */
  displayWindowSpecs(index) {
    if (index >= 0 && index < this.windowTypes.length) {
      this.windowTypes[index].displaySpecs();
    } else {
      console.error("Invalid window type index.");
    }
  }
}

// Create a new window configuration tool
const tool = new WindowConfigTool();

// Define window types
const ideal5000 = new Window("Aluplast Ideal5000", {
  material: "PVC",
  width: "100-150 cm",
  height: "100-200 cm",
  energyEfficiency: "High",
});

// Add window types to the tool
tool.addWindowType(ideal5000);

// Example usage
function main() {
  try {
    tool.displayWindowTypes();
    const selectedIndex = 0; // Replace with user input
    tool.displayWindowSpecs(selectedIndex);
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

main();
```
