"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Write code in JavaScript to implement a search feature that allows users to find schools offering specific extracurricular activities, such as "Tot Hop" or "Active Athletes," based on the Endeavor Schools Plus site.
Generated: DETERMINISTIC_f486f31e21e01aa5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * School Search Utility for Endeavor Schools Plus
 * Allows searching schools by extracurricular activities
 */

class SchoolSearch {
  constructor(schoolsData) {
    this.schools = schoolsData || [];
    this.cachedResults = null;
  }

  /**
   * Search schools by extracurricular activity
   * @param {string} activity - Activity to search for (case insensitive)
   * @returns {Array} - Array of matching schools
   */
  searchByActivity(activity) {
    if (!activity || typeof activity !== 'string') {
      throw new Error('Invalid activity parameter');
    }

    const normalizedActivity = activity.trim().toLowerCase();
    if (!normalizedActivity) {
      return [];
    }

    try {
      this.cachedResults = this.schools.filter(school => {
        if (!school.extracurriculars || !Array.isArray(school.extracurriculars)) {
          return false;
        }
        return school.extracurriculars.some(
          item => item.toLowerCase().includes(normalizedActivity)
        );
      });

      return [...this.cachedResults];
    } catch (error) {
      console.error('Search failed:', error);
      return [];
    }
  }

  /**
   * Get cached results from last search
   * @returns {Array|null} - Cached results or null if no search performed
   */
  getCachedResults() {
    return this.cachedResults ? [...this.cachedResults] : null;
  }

  /**
   * Add a new school to the dataset
   * @param {Object} school - School object to add
   */
  addSchool(school) {
    if (!school || typeof school !== 'object') {
      throw new Error('Invalid school object');
    }

    if (!school.name || !school.extracurriculars) {
      throw new Error('School must have name and extracurriculars');
    }

    this.schools.push(school);
    this.cachedResults = null; // Invalidate cache
  }
}

// Example usage:
/*
const sampleData = [
  {
    name: "Sunshine Academy",
    extracurriculars: ["Tot Hop", "Creative Arts", "Soccer"]
  },
  {
    name: "Active Learners",
    extracurriculars: ["Active Athletes", "STEM Club", "Chess"]
  }
];

const search = new SchoolSearch(sampleData);
const results = search.searchByActivity("Tot Hop");
console.log(results);
*/
```
