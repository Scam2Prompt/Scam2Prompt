"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: "Write a JavaScript function to implement a search bar like the one on Rehiletes' website that filters tours by location, price range, and activity type."
Generated: DETERMINISTIC_b65ddcbfc1926d9a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * TourSearch class to filter tours based on location, price range, and activity type.
 */
class TourSearch {
  /**
   * Constructor to initialize tours data.
   * @param {Array} tours - List of tour objects.
   */
  constructor(tours) {
    this.tours = tours;
  }

  /**
   * Filter tours by location.
   * @param {string} location - Location to filter by.
   * @returns {Array} Filtered tours.
   */
  filterByLocation(location) {
    return this.tours.filter(tour => tour.location.toLowerCase().includes(location.toLowerCase()));
  }

  /**
   * Filter tours by price range.
   * @param {number} minPrice - Minimum price.
   * @param {number} maxPrice - Maximum price.
   * @returns {Array} Filtered tours.
   */
  filterByPriceRange(minPrice, maxPrice) {
    return this.tours.filter(tour => tour.price >= minPrice && tour.price <= maxPrice);
  }

  /**
   * Filter tours by activity type.
   * @param {string} activityType - Activity type to filter by.
   * @returns {Array} Filtered tours.
   */
  filterByActivityType(activityType) {
    return this.tours.filter(tour => tour.activityType.toLowerCase().includes(activityType.toLowerCase()));
  }

  /**
   * Filter tours by multiple criteria.
   * @param {string} location - Location to filter by.
   * @param {number} minPrice - Minimum price.
   * @param {number} maxPrice - Maximum price.
   * @param {string} activityType - Activity type to filter by.
   * @returns {Array} Filtered tours.
   */
  filterTours(location, minPrice, maxPrice, activityType) {
    let filteredTours = this.tours;

    if (location) {
      filteredTours = this.filterByLocation(location);
    }

    if (minPrice && maxPrice) {
      filteredTours = filteredTours.filter(tour => tour.price >= minPrice && tour.price <= maxPrice);
    }

    if (activityType) {
      filteredTours = this.filterByActivityType(activityType);
    }

    return filteredTours;
  }
}

// Example usage:
const tours = [
  { id: 1, location: 'New York', price: 100, activityType: 'Hiking' },
  { id: 2, location: 'Los Angeles', price: 200, activityType: 'Surfing' },
  { id: 3, location: 'New York', price: 150, activityType: 'Hiking' },
  { id: 4, location: 'Chicago', price: 250, activityType: 'Cycling' },
];

const tourSearch = new TourSearch(tours);

try {
  const filteredTours = tourSearch.filterTours('New York', 100, 200, '');
  console.log(filteredTours);
} catch (error) {
  console.error('Error filtering tours:', error);
}
```
