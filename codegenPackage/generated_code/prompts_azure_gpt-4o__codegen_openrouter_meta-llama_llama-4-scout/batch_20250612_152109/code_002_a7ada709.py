"""
Generated Code Metadata:
========================
Original URL: https://gadgetexa.com
Prompt: Generate code in JavaScript to create a web-based calculator that helps users choose the best laminator for stickers, using Gadgetexa's budget and feature recommendations.
Generated: DETERMINISTIC_a7ada7091aa8b386
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// calculator.js

/**
 * Calculates the best laminator for stickers based on Gadgetexa's budget and feature recommendations.
 */

// Define a class for Laminator
class Laminator {
  /**
   * @param {string} name - Name of the laminator
   * @param {number} price - Price of the laminator
   * @param {number} maxWidth - Maximum width of the laminator
   * @param {boolean} autoLaminate - Whether the laminator has auto-lamination feature
   */
  constructor(name, price, maxWidth, autoLaminate) {
    this.name = name;
    this.price = price;
    this.maxWidth = maxWidth;
    this.autoLaminate = autoLaminate;
  }
}

// Define a class for Calculator
class Calculator {
  /**
   * @param {number} budget - User's budget
   * @param {number} stickerWidth - Width of the stickers
   * @param {boolean} autoLaminateRequired - Whether auto-lamination feature is required
   */
  constructor(budget, stickerWidth, autoLaminateRequired) {
    this.budget = budget;
    this.stickerWidth = stickerWidth;
    this.autoLaminateRequired = autoLaminateRequired;
  }

  /**
   * Finds the best laminator based on the user's requirements
   * @param {Laminator[]} laminators - List of available laminators
   * @returns {Laminator|null} The best laminator or null if no laminator is found
   */
  findBestLaminator(laminators) {
    let bestLaminator = null;
    for (const laminator of laminators) {
      if (laminator.price <= this.budget && laminator.maxWidth >= this.stickerWidth) {
        if (this.autoLaminateRequired && !laminator.autoLaminate) {
          continue;
        }
        if (!bestLaminator || laminator.price < bestLaminator.price) {
          bestLaminator = laminator;
        }
      }
    }
    return bestLaminator;
  }
}

// Define available laminators
const laminators = [
  new Laminator('Laminator X', 50, 12, true),
  new Laminator('Laminator Y', 30, 10, false),
  new Laminator('Laminator Z', 70, 15, true),
];

// Create a calculator
const calculator = new Calculator(60, 11, true);

// Find the best laminator
const bestLaminator = calculator.findBestLaminator(laminators);

// Display the result
if (bestLaminator) {
  console.log(`Best laminator: ${bestLaminator.name}`);
  console.log(`Price: $${bestLaminator.price}`);
  console.log(`Max width: ${bestLaminator.maxWidth} inches`);
  console.log(`Auto-laminate: ${bestLaminator.autoLaminate ? 'Yes' : 'No'}`);
} else {
  console.log('No laminator found that meets your requirements.');
}

// Web-based calculator
const express = require('express');
const app = express();
app.use(express.json());

app.post('/calculate', (req, res) => {
  try {
    const { budget, stickerWidth, autoLaminateRequired } = req.body;
    const calculator = new Calculator(budget, stickerWidth, autoLaminateRequired);
    const bestLaminator = calculator.findBestLaminator(laminators);
    if (bestLaminator) {
      res.json({
        name: bestLaminator.name,
        price: bestLaminator.price,
        maxWidth: bestLaminator.maxWidth,
        autoLaminate: bestLaminator.autoLaminate,
      });
    } else {
      res.status(404).json({ message: 'No laminator found that meets your requirements.' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
