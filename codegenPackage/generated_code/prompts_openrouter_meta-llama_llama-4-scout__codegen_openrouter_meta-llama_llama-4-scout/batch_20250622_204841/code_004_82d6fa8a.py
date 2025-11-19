"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: "Create a JavaScript function to filter construction tools by category and price range."
Generated: DETERMINISTIC_82d6fa8a5256156d
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a construction tool with category and price.
 */
class ConstructionTool {
  /**
   * Creates a new ConstructionTool instance.
   * @param {string} name - The name of the tool.
   * @param {string} category - The category of the tool.
   * @param {number} price - The price of the tool.
   */
  constructor(name, category, price) {
    this.name = name;
    this.category = category;
    this.price = price;
  }
}

/**
 * Filters construction tools by category and price range.
 */
class ConstructionToolFilter {
  /**
   * Creates a new ConstructionToolFilter instance.
   * @param {ConstructionTool[]} tools - The list of construction tools.
   */
  constructor(tools) {
    this.tools = tools;
  }

  /**
   * Filters tools by category and price range.
   * @param {string} category - The category to filter by.
   * @param {number} minPrice - The minimum price (inclusive).
   * @param {number} maxPrice - The maximum price (inclusive).
   * @returns {ConstructionTool[]} The filtered list of tools.
   */
  filterTools(category, minPrice, maxPrice) {
    if (!category || typeof category !== 'string') {
      throw new Error('Category must be a non-empty string');
    }

    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
      throw new Error('Price range must be numbers');
    }

    if (minPrice > maxPrice) {
      throw new Error('Invalid price range');
    }

    return this.tools.filter(tool => {
      return tool.category.toLowerCase() === category.toLowerCase()
        && tool.price >= minPrice && tool.price <= maxPrice;
    });
  }
}

// Example usage:
function main() {
  try {
    const tools = [
      new ConstructionTool('Hammer', 'Hand Tools', 20),
      new ConstructionTool('Drill', 'Power Tools', 50),
      new ConstructionTool('Saw', 'Hand Tools', 30),
      new ConstructionTool('Wrench', 'Hand Tools', 40),
      new ConstructionTool('Grinder', 'Power Tools', 80),
    ];

    const filter = new ConstructionToolFilter(tools);
    const filteredTools = filter.filterTools('Hand Tools', 20, 40);

    console.log('Filtered Tools:');
    filteredTools.forEach(tool => {
      console.log(`${tool.name} - $${tool.price}`);
    });
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
