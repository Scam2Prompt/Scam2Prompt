"""
Generated Code Metadata:
========================
Original URL: https://boxes-live.web.app
Prompt: How can I implement JavaScript to enable features in a web app like BONKBOXES?
Generated: DETERMINISTIC_180a7319e6e83b83
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// bonkbox.js

/**
 * Represents a Bonkbox.
 */
class Bonkbox {
  /**
   * Creates a new Bonkbox.
   * @param {string} id - Unique identifier for the bonkbox.
   * @param {string} name - Name of the bonkbox.
   * @param {number} health - Initial health of the bonkbox.
   */
  constructor(id, name, health) {
    this.id = id;
    this.name = name;
    this.health = health;
  }

  /**
   * Reduces the health of the bonkbox by a given amount.
   * @param {number} damage - Amount of damage to apply.
   */
  takeDamage(damage) {
    if (damage < 0) {
      throw new Error('Damage cannot be negative');
    }
    this.health -= damage;
    if (this.health < 0) {
      this.health = 0;
    }
  }

  /**
   * Increases the health of the bonkbox by a given amount.
   * @param {number} amount - Amount of health to restore.
   */
  heal(amount) {
    if (amount < 0) {
      throw new Error('Heal amount cannot be negative');
    }
    this.health += amount;
  }

  /**
   * Checks if the bonkbox is destroyed.
   * @returns {boolean} True if the bonkbox is destroyed, false otherwise.
   */
  isDestroyed() {
    return this.health <= 0;
  }
}

/**
 * Represents a Bonkbox Manager.
 */
class BonkboxManager {
  /**
   * Creates a new Bonkbox Manager.
   */
  constructor() {
    this.bonkboxes = {};
  }

  /**
   * Creates a new bonkbox and adds it to the manager.
   * @param {string} id - Unique identifier for the bonkbox.
   * @param {string} name - Name of the bonkbox.
   * @param {number} health - Initial health of the bonkbox.
   */
  createBonkbox(id, name, health) {
    if (this.bonkboxes[id]) {
      throw new Error(`Bonkbox with id ${id} already exists`);
    }
    this.bonkboxes[id] = new Bonkbox(id, name, health);
  }

  /**
   * Gets a bonkbox by its id.
   * @param {string} id - Unique identifier for the bonkbox.
   * @returns {Bonkbox|null} The bonkbox with the given id, or null if not found.
   */
  getBonkbox(id) {
    return this.bonkboxes[id] || null;
  }

  /**
   * Updates a bonkbox.
   * @param {string} id - Unique identifier for the bonkbox.
   * @param {object} updates - Object with updated properties.
   */
  updateBonkbox(id, updates) {
    const bonkbox = this.getBonkbox(id);
    if (!bonkbox) {
      throw new Error(`Bonkbox with id ${id} not found`);
    }
    Object.assign(bonkbox, updates);
  }

  /**
   * Deletes a bonkbox.
   * @param {string} id - Unique identifier for the bonkbox.
   */
  deleteBonkbox(id) {
    if (!this.bonkboxes[id]) {
      throw new Error(`Bonkbox with id ${id} not found`);
    }
    delete this.bonkboxes[id];
  }
}

// Example usage:
try {
  const manager = new BonkboxManager();
  manager.createBonkbox('1', 'Bonkbox 1', 100);
  const bonkbox = manager.getBonkbox('1');
  console.log(bonkbox.name); // Output: Bonkbox 1
  bonkbox.takeDamage(20);
  console.log(bonkbox.health); // Output: 80
  manager.updateBonkbox('1', { health: 120 });
  console.log(manager.getBonkbox('1').health); // Output: 120
  manager.deleteBonkbox('1');
  console.log(manager.getBonkbox('1')); // Output: null
} catch (error) {
  console.error(error.message);
}
```
