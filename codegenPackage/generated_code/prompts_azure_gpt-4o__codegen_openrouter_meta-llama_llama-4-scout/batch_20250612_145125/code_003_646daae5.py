"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a function in JavaScript to categorize tools into groups (e.g., hand tools like pliers and hammers, power tools like drills and screwdrivers) based on their type.
Generated: DETERMINISTIC_646daae5aa4d5f42
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a tool with a name and a type.
 */
class Tool {
  /**
   * Creates a new Tool instance.
   * @param {string} name - The name of the tool.
   * @param {string} type - The type of the tool (e.g., hand tool, power tool).
   */
  constructor(name, type) {
    this.name = name;
    this.type = type;
  }
}

/**
 * Represents a tool categorizer that groups tools by their type.
 */
class ToolCategorizer {
  /**
   * Creates a new ToolCategorizer instance.
   */
  constructor() {
    this.tools = {};
  }

  /**
   * Adds a tool to the categorizer.
   * @param {Tool} tool - The tool to add.
   */
  addTool(tool) {
    if (!this.tools[tool.type]) {
      this.tools[tool.type] = [];
    }
    this.tools[tool.type].push(tool.name);
  }

  /**
   * Gets the tools grouped by their type.
   * @returns {Object} An object with tool types as keys and arrays of tool names as values.
   */
  getTools() {
    return this.tools;
  }

  /**
   * Removes a tool from the categorizer.
   * @param {string} toolName - The name of the tool to remove.
   * @param {string} toolType - The type of the tool to remove.
   * @returns {boolean} True if the tool was removed, false otherwise.
   */
  removeTool(toolName, toolType) {
    if (this.tools[toolType]) {
      const index = this.tools[toolType].indexOf(toolName);
      if (index !== -1) {
        this.tools[toolType].splice(index, 1);
        if (this.tools[toolType].length === 0) {
          delete this.tools[toolType];
        }
        return true;
      }
    }
    return false;
  }
}

// Example usage:
function main() {
  const categorizer = new ToolCategorizer();

  const pliers = new Tool('Pliers', 'Hand Tool');
  const hammer = new Tool('Hammer', 'Hand Tool');
  const drill = new Tool('Drill', 'Power Tool');
  const screwdriver = new Tool('Screwdriver', 'Power Tool');

  categorizer.addTool(pliers);
  categorizer.addTool(hammer);
  categorizer.addTool(drill);
  categorizer.addTool(screwdriver);

  console.log(categorizer.getTools());

  try {
    if (!categorizer.removeTool('Pliers', 'Hand Tool')) {
      throw new Error('Tool not found');
    }
    console.log(categorizer.getTools());
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
