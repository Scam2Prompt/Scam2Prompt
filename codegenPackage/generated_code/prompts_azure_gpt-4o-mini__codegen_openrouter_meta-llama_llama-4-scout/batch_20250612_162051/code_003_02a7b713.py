"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Develop a JavaScript function that allows users to filter horse riding tours based on their preferences, such as duration and type of experience, as seen on the Chile Horse Riding website.
Generated: DETERMINISTIC_02a7b713473021b6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a horse riding tour.
 */
class HorseRidingTour {
  /**
   * Creates a new HorseRidingTour instance.
   * @param {string} name - The name of the tour.
   * @param {number} duration - The duration of the tour in hours.
   * @param {string} type - The type of experience (e.g., "gallop", "trail", etc.).
   * @param {string} description - A brief description of the tour.
   */
  constructor(name, duration, type, description) {
    this.name = name;
    this.duration = duration;
    this.type = type;
    this.description = description;
  }
}

/**
 * Filters horse riding tours based on user preferences.
 */
class TourFilter {
  /**
   * Creates a new TourFilter instance.
   * @param {HorseRidingTour[]} tours - An array of HorseRidingTour instances.
   */
  constructor(tours) {
    this.tours = tours;
  }

  /**
   * Filters tours by duration.
   * @param {number} minDuration - The minimum duration in hours.
   * @param {number} [maxDuration] - The maximum duration in hours.
   * @returns {HorseRidingTour[]} The filtered tours.
   */
  filterByDuration(minDuration, maxDuration) {
    return this.tours.filter(tour => {
      if (maxDuration) {
        return tour.duration >= minDuration && tour.duration <= maxDuration;
      }
      return tour.duration >= minDuration;
    });
  }

  /**
   * Filters tours by type of experience.
   * @param {string[]} types - An array of experience types.
   * @returns {HorseRidingTour[]} The filtered tours.
   */
  filterByType(types) {
    return this.tours.filter(tour => types.includes(tour.type));
  }

  /**
   * Filters tours by multiple criteria.
   * @param {Object} [options] - The filter options.
   * @param {number} [options.minDuration] - The minimum duration in hours.
   * @param {number} [options.maxDuration] - The maximum duration in hours.
   * @param {string[]} [options.types] - An array of experience types.
   * @returns {HorseRidingTour[]} The filtered tours.
   */
  filterTours(options = {}) {
    let filteredTours = this.tours;

    if (options.minDuration || options.maxDuration) {
      filteredTours = this.filterByDuration(options.minDuration, options.maxDuration);
    }

    if (options.types) {
      filteredTours = this.filterByType(options.types);
    }

    return filteredTours;
  }
}

// Example usage:
const tours = [
  new HorseRidingTour("Tour 1", 2, "gallop", "A thrilling gallop experience"),
  new HorseRidingTour("Tour 2", 4, "trail", "A scenic trail ride"),
  new HorseRidingTour("Tour 3", 3, "gallop", "A guided gallop tour"),
];

const filter = new TourFilter(tours);

try {
  const filteredTours = filter.filterTours({
    minDuration: 2,
    types: ["gallop"],
  });

  console.log("Filtered Tours:");
  filteredTours.forEach(tour => {
    console.log(`Name: ${tour.name}, Duration: ${tour.duration} hours, Type: ${tour.type}`);
  });
} catch (error) {
  console.error("Error filtering tours:", error);
}
```
