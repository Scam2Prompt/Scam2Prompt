"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: Develop a JavaScript function that allows users to filter window options by size and style, reflecting the diverse inventory at NellyServis.
Generated: DETERMINISTIC_5671313003895d58
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a window object with size and style properties.
 */
class Window {
  /**
   * Creates a new Window instance.
   * @param {string} size - The size of the window (e.g., "small", "medium", "large").
   * @param {string} style - The style of the window (e.g., "modern", "traditional").
   */
  constructor(size, style) {
    this.size = size;
    this.style = style;
  }
}

/**
 * Filters window options by size and style.
 */
class WindowFilter {
  /**
   * Creates a new WindowFilter instance.
   * @param {Window[]} windows - An array of Window objects.
   */
  constructor(windows) {
    this.windows = windows;
  }

  /**
   * Filters windows by size.
   * @param {string[]} sizes - An array of sizes to filter by.
   * @returns {Window[]} An array of Window objects matching the specified sizes.
   */
  filterBySize(sizes) {
    return this.windows.filter((window) => sizes.includes(window.size));
  }

  /**
   * Filters windows by style.
   * @param {string[]} styles - An array of styles to filter by.
   * @returns {Window[]} An array of Window objects matching the specified styles.
   */
  filterByStyle(styles) {
    return this.windows.filter((window) => styles.includes(window.style));
  }

  /**
   * Filters windows by both size and style.
   * @param {string[]} sizes - An array of sizes to filter by.
   * @param {string[]} styles - An array of styles to filter by.
   * @returns {Window[]} An array of Window objects matching the specified sizes and styles.
   */
  filterBySizeAndStyle(sizes, styles) {
    return this.windows.filter(
      (window) => sizes.includes(window.size) && styles.includes(window.style)
    );
  }
}

// Example usage:
try {
  // Create window objects
  const windows = [
    new Window("small", "modern"),
    new Window("medium", "traditional"),
    new Window("large", "modern"),
    new Window("small", "traditional"),
  ];

  // Create a WindowFilter instance
  const filter = new WindowFilter(windows);

  // Filter by size
  const sizes = ["small", "medium"];
  const filteredBySize = filter.filterBySize(sizes);
  console.log("Filtered by size:");
  console.log(filteredBySize);

  // Filter by style
  const styles = ["modern"];
  const filteredByStyle = filter.filterByStyle(styles);
  console.log("Filtered by style:");
  console.log(filteredByStyle);

  // Filter by both size and style
  const sizesAndStyles = {
    sizes: ["small"],
    styles: ["modern"],
  };
  const filteredBySizeAndStyle = filter.filterBySizeAndStyle(
    sizesAndStyles.sizes,
    sizesAndStyles.styles
  );
  console.log("Filtered by size and style:");
  console.log(filteredBySizeAndStyle);
} catch (error) {
  console.error("Error:", error.message);
}
```
