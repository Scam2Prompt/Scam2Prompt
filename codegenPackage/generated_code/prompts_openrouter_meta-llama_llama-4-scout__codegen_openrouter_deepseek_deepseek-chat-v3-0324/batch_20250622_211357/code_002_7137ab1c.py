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
 * ScientificHubDirectory.js
 * 
 * A simple scientific hub directory implementation using JavaScript.
 * Inspired by Claim Research Hub's 62,000 scientific hubs.
 * 
 * Features:
 * - Create, read, update, and delete hubs
 * - Search functionality
 * - Basic validation
 */

class ScientificHubDirectory {
  constructor() {
    this.hubs = []; // Array to store hub objects
  }

  /**
   * Add a new scientific hub to the directory
   * @param {Object} hub - Hub object containing hub details
   * @returns {Object} - The created hub with generated ID
   * @throws {Error} - If hub validation fails
   */
  addHub(hub) {
    if (!this.validateHub(hub)) {
      throw new Error('Invalid hub data');
    }

    const newHub = {
      id: this.generateId(),
      ...hub,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };

    this.hubs.push(newHub);
    return newHub;
  }

  /**
   * Get all hubs in the directory
   * @returns {Array} - Array of hub objects
   */
  getAllHubs() {
    return [...this.hubs]; // Return a copy to prevent direct manipulation
  }

  /**
   * Get a specific hub by ID
   * @param {string} id - Hub ID
   * @returns {Object|null} - The hub object or null if not found
   */
  getHubById(id) {
    return this.hubs.find(hub => hub.id === id) || null;
  }

  /**
   * Update an existing hub
   * @param {string} id - Hub ID to update
   * @param {Object} updates - Object containing fields to update
   * @returns {Object|null} - The updated hub or null if not found
   * @throws {Error} - If validation fails
   */
  updateHub(id, updates) {
    const hubIndex = this.hubs.findIndex(hub => hub.id === id);
    if (hubIndex === -1) return null;

    const updatedHub = {
      ...this.hubs[hubIndex],
      ...updates,
      updatedAt: new Date().toISOString()
    };

    if (!this.validateHub(updatedHub)) {
      throw new Error('Invalid hub data');
    }

    this.hubs[hubIndex] = updatedHub;
    return updatedHub;
  }

  /**
   * Delete a hub from the directory
   * @param {string} id - Hub ID to delete
   * @returns {boolean} - True if deleted, false if not found
   */
  deleteHub(id) {
    const initialLength = this.hubs.length;
    this.hubs = this.hubs.filter(hub => hub.id !== id);
    return this.hubs.length !== initialLength;
  }

  /**
   * Search hubs by name or description
   * @param {string} query - Search term
   * @returns {Array} - Array of matching hubs
   */
  searchHubs(query) {
    const lowerQuery = query.toLowerCase();
    return this.hubs.filter(hub => 
      hub.name.toLowerCase().includes(lowerQuery) ||
      (hub.description && hub.description.toLowerCase().includes(lowerQuery))
    );
  }

  /**
   * Validate hub object structure
   * @param {Object} hub - Hub object to validate
   * @returns {boolean} - True if valid, false otherwise
   */
  validateHub(hub) {
    return !!(
      hub &&
      hub.name && 
      typeof hub.name === 'string' &&
      hub.name.trim().length > 0 &&
      (!hub.description || typeof hub.description === 'string')
    );
  }

  /**
   * Generate a unique ID for new hubs
   * @returns {string} - Generated ID
   */
  generateId() {
    return Math.random().toString(36).substring(2, 15) + 
           Math.random().toString(36).substring(2, 15);
  }
}

// Example usage:
/*
const directory = new ScientificHubDirectory();

try {
  const hub1 = directory.addHub({
    name: "Quantum Physics Research",
    description: "Exploring quantum mechanics fundamentals"
  });

  const hub2 = directory.addHub({
    name: "Bioinformatics Hub",
    description: "Computational approaches to biological data"
  });

  console.log(directory.getAllHubs());
  console.log(directory.searchHubs("quantum"));
  
  directory.updateHub(hub1.id, { description: "Advanced quantum mechanics research" });
  console.log(directory.getHubById(hub1.id));

  directory.deleteHub(hub2.id);
  console.log(directory.getAllHubs());
} catch (error) {
  console.error("Error:", error.message);
}
*/
```
