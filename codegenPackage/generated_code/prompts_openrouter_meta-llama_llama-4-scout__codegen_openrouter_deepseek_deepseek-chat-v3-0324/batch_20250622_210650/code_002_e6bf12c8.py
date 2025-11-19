"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Generate a JavaScript code snippet to create a virtual wine tasting guide, like the one offered by FestiVin de Caraquet.
Generated: DETERMINISTIC_e6bf12c888b3a68f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Virtual Wine Tasting Guide
 * Simulates a wine tasting experience with guided steps and wine information
 */

class WineTastingGuide {
  constructor() {
    this.currentStep = 0;
    this.wines = [];
    this.tastingNotes = {};
    this.userPreferences = {};
    this.initializeGuide();
  }

  /**
   * Initialize guide with default wines and steps
   */
  initializeGuide() {
    this.wines = [
      {
        id: 1,
        name: "Chardonnay",
        type: "white",
        region: "Burgundy, France",
        year: 2020,
        description: "A crisp white wine with notes of green apple and citrus.",
        pairing: "Poultry, seafood, creamy sauces"
      },
      {
        id: 2,
        name: "Pinot Noir",
        type: "red",
        region: "Willamette Valley, Oregon",
        year: 2018,
        description: "Light-bodied red with cherry and earthy notes.",
        pairing: "Salmon, mushrooms, charcuterie"
      },
      {
        id: 3,
        name: "Cabernet Sauvignon",
        type: "red",
        region: "Napa Valley, California",
        year: 2016,
        description: "Full-bodied with dark fruit flavors and tannic structure.",
        pairing: "Steak, lamb, aged cheeses"
      }
    ];

    this.tastingSteps = [
      "Examine the wine's appearance",
      "Swirl the wine to release aromas",
      "Smell the wine and note aromas",
      "Take a sip and let it coat your palate",
      "Note the flavors and finish"
    ];
  }

  /**
   * Get current tasting step
   * @returns {string} Current step description
   */
  getCurrentStep() {
    if (this.currentStep >= this.tastingSteps.length) {
      return "Tasting complete!";
    }
    return this.tastingSteps[this.currentStep];
  }

  /**
   * Advance to next tasting step
   * @returns {string} Next step description
   */
  nextStep() {
    if (this.currentStep < this.tastingSteps.length) {
      this.currentStep++;
    }
    return this.getCurrentStep();
  }

  /**
   * Get wine by ID
   * @param {number} id - Wine ID
   * @returns {object} Wine object
   */
  getWineById(id) {
    const wine = this.wines.find(w => w.id === id);
    if (!wine) {
      throw new Error(`Wine with ID ${id} not found`);
    }
    return wine;
  }

  /**
   * Get all wines of a specific type
   * @param {string} type - Wine type (red/white)
   * @returns {array} Array of matching wines
   */
  getWinesByType(type) {
    if (type !== 'red' && type !== 'white') {
      throw new Error('Invalid wine type. Must be "red" or "white"');
    }
    return this.wines.filter(wine => wine.type === type);
  }

  /**
   * Add tasting note for current wine
   * @param {number} wineId - Wine ID
   * @param {string} note - Tasting note
   */
  addTastingNote(wineId, note) {
    if (!this.tastingNotes[wineId]) {
      this.tastingNotes[wineId] = [];
    }
    this.tastingNotes[wineId].push(note);
  }

  /**
   * Get tasting notes for a wine
   * @param {number} wineId - Wine ID
   * @returns {array} Array of tasting notes
   */
  getTastingNotes(wineId) {
    return this.tastingNotes[wineId] || [];
  }

  /**
   * Set user preference for wine type
   * @param {string} preference - Preferred wine type
   */
  setPreference(preference) {
    if (preference !== 'red' && preference !== 'white') {
      throw new Error('Invalid preference. Must be "red" or "white"');
    }
    this.userPreferences.wineType = preference;
  }

  /**
   * Get recommended wines based on user preferences
   * @returns {array} Array of recommended wines
   */
  getRecommendations() {
    if (!this.userPreferences.wineType) {
      return this.wines;
    }
    return this.getWinesByType(this.userPreferences.wineType);
  }

  /**
   * Reset the tasting guide to initial state
   */
  reset() {
    this.currentStep = 0;
    this.tastingNotes = {};
  }
}

// Example usage
/*
const guide = new WineTastingGuide();
console.log(guide.getCurrentStep()); // "Examine the wine's appearance"
guide.nextStep();
console.log(guide.getCurrentStep()); // "Swirl the wine to release aromas"
console.log(guide.getWineById(1)); // Chardonnay details
guide.addTastingNote(1, "Crisp acidity with tropical fruit notes");
console.log(guide.getTastingNotes(1)); // ["Crisp acidity with tropical fruit notes"]
guide.setPreference("red");
console.log(guide.getRecommendations()); // Pinot Noir and Cabernet Sauvignon
*/
```
