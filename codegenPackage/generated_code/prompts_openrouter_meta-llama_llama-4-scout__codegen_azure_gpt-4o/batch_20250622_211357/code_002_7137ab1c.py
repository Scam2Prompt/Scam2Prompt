"""
Generated Code Metadata:
========================
Original URL: https://claimresearchhub.org
Prompt: "Write a code snippet to create a simple scientific hub directory using a JavaScript library, inspired by the 62,000 scientific hubs on Claim Research Hub."
Generated: DETERMINISTIC_7137ab1c755af66d
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Scientific Hub Directory
 * This script creates a simple scientific hub directory using JavaScript.
 * It allows users to add, view, and search for scientific hubs.
 */

// Define the ScientificHub class to represent individual hubs
class ScientificHub {
  constructor(name, description, location) {
    this.name = name; // Name of the hub
    this.description = description; // Description of the hub
    this.location = location; // Location of the hub
  }
}

// Define the ScientificHubDirectory class to manage the collection of hubs
class ScientificHubDirectory {
  constructor() {
    this.hubs = []; // Array to store all hubs
  }

  /**
   * Add a new hub to the directory
   * @param {ScientificHub} hub - The hub to be added
   */
  addHub(hub) {
    if (!(hub instanceof ScientificHub)) {
      throw new Error("Invalid hub object. Must be an instance of ScientificHub.");
    }
    this.hubs.push(hub);
  }

  /**
   * Search for hubs by name
   * @param {string} query - The search query
   * @returns {ScientificHub[]} - Array of hubs matching the query
   */
  searchHubs(query) {
    if (typeof query !== "string") {
      throw new Error("Search query must be a string.");
    }
    return this.hubs.filter((hub) =>
      hub.name.toLowerCase().includes(query.toLowerCase())
    );
  }

  /**
   * Get all hubs in the directory
   * @returns {ScientificHub[]} - Array of all hubs
   */
  getAllHubs() {
    return this.hubs;
  }
}

// Example usage
try {
  // Create a new directory
  const directory = new ScientificHubDirectory();

  // Add some hubs
  directory.addHub(new ScientificHub("Claim Research Hub", "A hub for scientific claims research.", "New York, USA"));
  directory.addHub(new ScientificHub("BioTech Innovations", "Focuses on biotechnology advancements.", "San Francisco, USA"));
  directory.addHub(new ScientificHub("AstroPhysics Center", "Dedicated to astrophysics research.", "Cambridge, UK"));

  // Search for hubs
  const searchResults = directory.searchHubs("research");
  console.log("Search Results:", searchResults);

  // Get all hubs
  const allHubs = directory.getAllHubs();
  console.log("All Hubs:", allHubs);
} catch (error) {
  console.error("Error:", error.message);
}
```
