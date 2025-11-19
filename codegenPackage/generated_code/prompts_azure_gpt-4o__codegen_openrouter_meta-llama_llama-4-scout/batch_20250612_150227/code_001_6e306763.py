"""
Generated Code Metadata:
========================
Original URL: https://meeytamsk-logjjiin.godaddysites.com
Prompt: Generate code to implement a search filter for real estate listings, allowing users to sort properties by price, number of bedrooms, and bathrooms using a JavaScript framework.
Generated: DETERMINISTIC_6e306763b4d913a0
Batch ID: 20250612_150227
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
   * @param {number} price - The price of the listing.
   * @param {number} bedrooms - The number of bedrooms.
   * @param {number} bathrooms - The number of bathrooms.
   */
  constructor(price, bedrooms, bathrooms) {
    this.price = price;
    this.bedrooms = bedrooms;
    this.bathrooms = bathrooms;
  }
}

// SearchFilter.js
class SearchFilter {
  /**
   * Applies filters to an array of real estate listings.
   * @param {RealEstateListing[]} listings - The listings to filter.
   */
  constructor(listings) {
    this.listings = listings;
  }

  /**
   * Filters listings by price range.
   * @param {number} minPrice - The minimum price.
   * @param {number} maxPrice - The maximum price.
   * @returns {RealEstateListing[]} The filtered listings.
   */
  filterByPrice(minPrice, maxPrice) {
    return this.listings.filter(listing => listing.price >= minPrice && listing.price <= maxPrice);
  }

  /**
   * Filters listings by number of bedrooms.
   * @param {number} bedrooms - The number of bedrooms.
   * @returns {RealEstateListing[]} The filtered listings.
   */
  filterByBedrooms(bedrooms) {
    return this.listings.filter(listing => listing.bedrooms === bedrooms);
  }

  /**
   * Filters listings by number of bathrooms.
   * @param {number} bathrooms - The number of bathrooms.
   * @returns {RealEstateListing[]} The filtered listings.
   */
  filterByBathrooms(bathrooms) {
    return this.listings.filter(listing => listing.bathrooms === bathrooms);
  }

  /**
   * Sorts listings by price.
   * @param {string} order - The order to sort in ('asc' or 'desc').
   * @returns {RealEstateListing[]} The sorted listings.
   */
  sortByPrice(order) {
    if (order !== 'asc' && order !== 'desc') {
      throw new Error('Invalid order. Must be "asc" or "desc".');
    }
    return this.listings.sort((a, b) => order === 'asc' ? a.price - b.price : b.price - a.price);
  }

  /**
   * Sorts listings by number of bedrooms.
   * @param {string} order - The order to sort in ('asc' or 'desc').
   * @returns {RealEstateListing[]} The sorted listings.
   */
  sortByBedrooms(order) {
    if (order !== 'asc' && order !== 'desc') {
      throw new Error('Invalid order. Must be "asc" or "desc".');
    }
    return this.listings.sort((a, b) => order === 'asc' ? a.bedrooms - b.bedrooms : b.bedrooms - a.bedrooms);
  }

  /**
   * Sorts listings by number of bathrooms.
   * @param {string} order - The order to sort in ('asc' or 'desc').
   * @returns {RealEstateListing[]} The sorted listings.
   */
  sortByBathrooms(order) {
    if (order !== 'asc' && order !== 'desc') {
      throw new Error('Invalid order. Must be "asc" or "desc".');
    }
    return this.listings.sort((a, b) => order === 'asc' ? a.bathrooms - b.bathrooms : b.bathrooms - a.bathrooms);
  }
}

// Example usage:
function main() {
  try {
    const listings = [
      new RealEstateListing(200000, 3, 2),
      new RealEstateListing(300000, 4, 3),
      new RealEstateListing(100000, 2, 1),
      new RealEstateListing(400000, 5, 4),
    ];

    const searchFilter = new SearchFilter(listings);

    console.log('All Listings:');
    console.log(listings);

    console.log('\nFiltered by price ($150,000 - $350,000):');
    console.log(searchFilter.filterByPrice(150000, 350000));

    console.log('\nSorted by price (desc):');
    console.log(searchFilter.sortByPrice('desc'));

    console.log('\nFiltered by 3 bedrooms:');
    console.log(searchFilter.filterByBedrooms(3));

    console.log('\nSorted by bathrooms (asc):');
    console.log(searchFilter.sortByBathrooms('asc'));
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
