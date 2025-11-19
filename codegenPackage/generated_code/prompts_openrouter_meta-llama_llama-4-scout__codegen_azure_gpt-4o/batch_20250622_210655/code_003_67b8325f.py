"""
Generated Code Metadata:
========================
Original URL: https://www.vracarbvk.rs
Prompt: Develop a JavaScript function to implement a simple availability calendar for a villa or hotel, reflecting the type of accommodations offered by Vila Vračar.
Generated: DETERMINISTIC_67b8325f04174727
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
 * Availability Calendar for Vila Vračar
 * This function manages and displays the availability of accommodations.
 * It allows marking dates as available or unavailable and checking availability.
 */

// Define the calendar object
const availabilityCalendar = {
  // Store availability data as an object with date keys and boolean values
  availability: {},

  /**
   * Mark a date as available or unavailable.
   * @param {string} date - The date in 'YYYY-MM-DD' format.
   * @param {boolean} isAvailable - True if available, false if unavailable.
   */
  setAvailability(date, isAvailable) {
    if (!this.isValidDate(date)) {
      throw new Error("Invalid date format. Use 'YYYY-MM-DD'.");
    }
    this.availability[date] = isAvailable;
  },

  /**
   * Check if a specific date is available.
   * @param {string} date - The date in 'YYYY-MM-DD' format.
   * @returns {boolean} - True if available, false if unavailable.
   */
  checkAvailability(date) {
    if (!this.isValidDate(date)) {
      throw new Error("Invalid date format. Use 'YYYY-MM-DD'.");
    }
    return this.availability[date] || false; // Default to false if date is not set
  },

  /**
   * Get all available dates.
   * @returns {string[]} - Array of dates marked as available.
   */
  getAvailableDates() {
    return Object.keys(this.availability).filter(
      (date) => this.availability[date]
    );
  },

  /**
   * Validate the date format.
   * @param {string} date - The date in 'YYYY-MM-DD' format.
   * @returns {boolean} - True if valid, false otherwise.
   */
  isValidDate(date) {
    const dateRegex = /^\d{4}-\d{2}-\d{2}$/; // Regex for 'YYYY-MM-DD' format
    return dateRegex.test(date);
  },
};

// Example usage:

try {
  // Set availability for specific dates
  availabilityCalendar.setAvailability("2023-11-01", true);
  availabilityCalendar.setAvailability("2023-11-02", false);
  availabilityCalendar.setAvailability("2023-11-03", true);

  // Check availability for a specific date
  console.log(
    "Is 2023-11-01 available?",
    availabilityCalendar.checkAvailability("2023-11-01")
  ); // Output: true

  console.log(
    "Is 2023-11-02 available?",
    availabilityCalendar.checkAvailability("2023-11-02")
  ); // Output: false

  // Get all available dates
  console.log("Available dates:", availabilityCalendar.getAvailableDates()); // Output: ['2023-11-01', '2023-11-03']
} catch (error) {
  console.error("Error:", error.message);
}
```
