"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Generate a code snippet in JavaScript to display the different horse riding tours offered by Chile Horse Riding, including the Cowboy Experience and Skiing & Riding Experience.
Generated: DETERMINISTIC_e8de8261d94f4803
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Define a class for HorseRidingTour
class HorseRidingTour {
  /**
   * Constructor for HorseRidingTour
   * @param {string} name - Name of the tour
   * @param {string} description - Description of the tour
   * @param {number} duration - Duration of the tour in hours
   * @param {string} location - Location of the tour
   */
  constructor(name, description, duration, location) {
    this.name = name;
    this.description = description;
    this.duration = duration;
    this.location = location;
  }

  /**
   * Display tour details
   */
  displayDetails() {
    console.log(`Tour Name: ${this.name}`);
    console.log(`Description: ${this.description}`);
    console.log(`Duration: ${this.duration} hours`);
    console.log(`Location: ${this.location}`);
    console.log('------------------------');
  }
}

// Define a class for ChileHorseRiding
class ChileHorseRiding {
  /**
   * Constructor for ChileHorseRiding
   */
  constructor() {
    this.tours = [];
  }

  /**
   * Add a tour to the list of tours
   * @param {HorseRidingTour} tour - Tour to add
   */
  addTour(tour) {
    if (tour instanceof HorseRidingTour) {
      this.tours.push(tour);
    } else {
      throw new Error('Invalid tour object');
    }
  }

  /**
   * Display all tours
   */
  displayTours() {
    if (this.tours.length === 0) {
      console.log('No tours available');
    } else {
      this.tours.forEach((tour) => tour.displayDetails());
    }
  }
}

// Create ChileHorseRiding instance
const chileHorseRiding = new ChileHorseRiding();

// Create tours
try {
  const cowboyExperience = new HorseRidingTour(
    'Cowboy Experience',
    'Live like a cowboy for a day and ride through the Chilean countryside',
    6,
    'Andes Mountains'
  );

  const skiingRidingExperience = new HorseRidingTour(
    'Skiing & Riding Experience',
    'Combine skiing and horse riding for an unforgettable experience',
    8,
    'Las Leñas Ski Resort'
  );

  // Add tours
  chileHorseRiding.addTour(cowboyExperience);
  chileHorseRiding.addTour(skiingRidingExperience);

  // Display tours
  chileHorseRiding.displayTours();
} catch (error) {
  console.error('Error:', error.message);
}
```
