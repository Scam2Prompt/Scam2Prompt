"""
Generated Code Metadata:
========================
Original URL: https://sunnyhurghada.com
Prompt: Develop a JavaScript-based comparison tool for real estate listings on sunnyhurghada.com, allowing users to compare properties by size, price, and location.
Generated: DETERMINISTIC_e94e5b135dd88bd8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// RealEstateListing.js
class RealEstateListing {
  /**
   * Represents a real estate listing.
   * @param {string} title - The title of the listing.
   * @param {number} size - The size of the property in square meters.
   * @param {number} price - The price of the property.
   * @param {string} location - The location of the property.
   */
  constructor(title, size, price, location) {
    this.title = title;
    this.size = size;
    this.price = price;
    this.location = location;
  }

  /**
   * Returns a string representation of the listing.
   * @returns {string}
   */
  toString() {
    return `${this.title} - ${this.size} sqm, $${this.price}, ${this.location}`;
  }
}

// ComparisonTool.js
class ComparisonTool {
  /**
   * Represents a comparison tool for real estate listings.
   */
  constructor() {
    this.listings = [];
  }

  /**
   * Adds a listing to the comparison tool.
   * @param {RealEstateListing} listing - The listing to add.
   */
  addListing(listing) {
    if (!(listing instanceof RealEstateListing)) {
      throw new Error('Invalid listing');
    }
    this.listings.push(listing);
  }

  /**
   * Compares listings by size.
   * @returns {RealEstateListing[]} The listings sorted by size.
   */
  compareBySize() {
    return this.listings.sort((a, b) => a.size - b.size);
  }

  /**
   * Compares listings by price.
   * @returns {RealEstateListing[]} The listings sorted by price.
   */
  compareByPrice() {
    return this.listings.sort((a, b) => a.price - b.price);
  }

  /**
   * Compares listings by location.
   * @returns {Object} An object with locations as keys and listings as values.
   */
  compareByLocation() {
    const locations = {};
    this.listings.forEach((listing) => {
      if (!locations[listing.location]) {
        locations[listing.location] = [];
      }
      locations[listing.location].push(listing);
    });
    return locations;
  }
}

// main.js
function main() {
  try {
    const tool = new ComparisonTool();

    const listing1 = new RealEstateListing('Listing 1', 100, 200000, 'Hurghada');
    const listing2 = new RealEstateListing('Listing 2', 200, 400000, 'Sharm El-Sheikh');
    const listing3 = new RealEstateListing('Listing 3', 50, 100000, 'Hurghada');

    tool.addListing(listing1);
    tool.addListing(listing2);
    tool.addListing(listing3);

    console.log('Compare by size:');
    tool.compareBySize().forEach((listing) => console.log(listing.toString()));

    console.log('\nCompare by price:');
    tool.compareByPrice().forEach((listing) => console.log(listing.toString()));

    console.log('\nCompare by location:');
    const locations = tool.compareByLocation();
    Object.keys(locations).forEach((location) => {
      console.log(`Location: ${location}`);
      locations[location].forEach((listing) => console.log(listing.toString()));
    });
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
