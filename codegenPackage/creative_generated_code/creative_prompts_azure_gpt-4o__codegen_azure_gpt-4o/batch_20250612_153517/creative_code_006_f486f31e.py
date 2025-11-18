"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Write code in JavaScript to implement a search feature that allows users to find schools offering specific extracurricular activities, such as "Tot Hop" or "Active Athletes," based on the Endeavor Schools Plus site.
Generated: DETERMINISTIC_f486f31e21e01aa5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Sample dataset representing schools and their extracurricular activities
const schools = [
  {
    name: "Sunshine Academy",
    activities: ["Tot Hop", "Active Athletes", "Art Adventures"],
  },
  {
    name: "Bright Beginnings School",
    activities: ["Creative Coding", "Junior Scientists", "Tot Hop"],
  },
  {
    name: "Happy Learners Academy",
    activities: ["Active Athletes", "Music Makers", "Drama Club"],
  },
  {
    name: "Future Stars School",
    activities: ["Drama Club", "Creative Coding", "Art Adventures"],
  },
];

// Function to search for schools offering a specific activity
/**
 * Finds schools offering the given extracurricular activity.
 * @param {string} activity - The extracurricular activity to search for.
 * @returns {Array} - List of school names that offer the specified activity.
 */
function searchSchoolsByActivity(activity) {
  try {
    // Validate input
    if (typeof activity !== "string" || activity.trim() === "") {
      throw new Error("Invalid activity name. Please provide a valid string.");
    }

    // Filter schools based on the activity
    const result = schools
      .filter((school) => school.activities.includes(activity))
      .map((school) => school.name);

    // Return the results
    return result.length > 0
      ? result
      : [`No schools found offering the activity "${activity}".`];
  } catch (error) {
    // Handle errors gracefully
    console.error("Error searching for schools:", error.message);
    return [];
  }
}

// Example usage
// Replace 'Tot Hop' with any activity name to test the function
const activityToSearch = "Tot Hop";
const searchResults = searchSchoolsByActivity(activityToSearch);
console.log(`Schools offering "${activityToSearch}":`, searchResults);
```
