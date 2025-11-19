"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Create a script in JavaScript to filter and display "Karma Çalışma Tezgahları" based on the number of drawers (e.g., 6, 9, 12) and dimensions (e.g., 300x70x190H).
Generated: DETERMINISTIC_1340a3b83ea007b8
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a Karma Çalışma Tezgahı with properties for drawers and dimensions.
 */
class KarmaTezgah {
  /**
   * Creates a new KarmaTezgah instance.
   * @param {number} drawers - The number of drawers.
   * @param {number} width - The width of the tezgah.
   * @param {number} depth - The depth of the tezgah.
   * @param {number} height - The height of the tezgah.
   */
  constructor(drawers, width, depth, height) {
    this.drawers = drawers;
    this.width = width;
    this.depth = depth;
    this.height = height;
  }

  /**
   * Returns a string representation of the KarmaTezgah.
   * @returns {string}
   */
  toString() {
    return `${this.drawers} çekmeceli - ${this.width}x${this.depth}x${this.height}H`;
  }
}

/**
 * Filters KarmaTezgah instances based on the number of drawers and dimensions.
 */
class KarmaTezgahFilter {
  /**
   * Creates a new KarmaTezgahFilter instance.
   * @param {KarmaTezgah[]} tezgahs - An array of KarmaTezgah instances.
   */
  constructor(tezgahs) {
    this.tezgahs = tezgahs;
  }

  /**
   * Filters tezgahs by the number of drawers.
   * @param {number[]} drawers - An array of drawer counts to filter by.
   * @returns {KarmaTezgah[]}
   */
  filterByDrawers(drawers) {
    return this.tezgahs.filter(tezgah => drawers.includes(tezgah.drawers));
  }

  /**
   * Filters tezgahs by dimensions.
   * @param {number} width - The width to filter by.
   * @param {number} depth - The depth to filter by.
   * @param {number} height - The height to filter by.
   * @returns {KarmaTezgah[]}
   */
  filterByDimensions(width, depth, height) {
    return this.tezgahs.filter(tezgah => tezgah.width === width && tezgah.depth === depth && tezgah.height === height);
  }

  /**
   * Filters tezgahs by both drawers and dimensions.
   * @param {number[]} drawers - An array of drawer counts to filter by.
   * @param {number} width - The width to filter by.
   * @param {number} depth - The depth to filter by.
   * @param {number} height - The height to filter by.
   * @returns {KarmaTezgah[]}
   */
  filterByDrawersAndDimensions(drawers, width, depth, height) {
    return this.tezgahs.filter(tezgah => drawers.includes(tezgah.drawers) && tezgah.width === width && tezgah.depth === depth && tezgah.height === height);
  }
}

// Example usage:
function main() {
  try {
    // Create some sample KarmaTezgah instances.
    const tezgahs = [
      new KarmaTezgah(6, 300, 70, 190),
      new KarmaTezgah(9, 300, 70, 190),
      new KarmaTezgah(12, 400, 80, 200),
      new KarmaTezgah(6, 300, 70, 190),
      new KarmaTezgah(9, 400, 80, 200),
    ];

    // Create a KarmaTezgahFilter instance.
    const filter = new KarmaTezgahFilter(tezgahs);

    // Filter by drawers.
    const drawers = [6, 9];
    const filteredByDrawers = filter.filterByDrawers(drawers);
    console.log("Filtered by drawers:");
    filteredByDrawers.forEach(tezgah => console.log(tezgah.toString()));

    // Filter by dimensions.
    const width = 300;
    const depth = 70;
    const height = 190;
    const filteredByDimensions = filter.filterByDimensions(width, depth, height);
    console.log("\nFiltered by dimensions:");
    filteredByDimensions.forEach(tezgah => console.log(tezgah.toString()));

    // Filter by both drawers and dimensions.
    const filteredByDrawersAndDimensions = filter.filterByDrawersAndDimensions(drawers, width, depth, height);
    console.log("\nFiltered by drawers and dimensions:");
    filteredByDrawersAndDimensions.forEach(tezgah => console.log(tezgah.toString()));
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

main();
```
