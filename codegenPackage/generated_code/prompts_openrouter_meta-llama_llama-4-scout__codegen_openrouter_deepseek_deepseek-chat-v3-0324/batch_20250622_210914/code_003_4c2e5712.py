"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Develop a Node.js application to calculate the cost of a trekking trip to the Kanchenjunga Base Camp, taking into account factors like accommodation, food, and guide services.
Generated: DETERMINISTIC_4c2e5712313285e0
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const { validationResult, check } = require('express-validator');

// Initialize the Express application
const app = express();
app.use(bodyParser.json());

// Cost constants (in USD)
const COSTS = {
  ACCOMMODATION_PER_NIGHT: 20,
  FOOD_PER_DAY: 15,
  GUIDE_PER_DAY: 30,
  PERMIT_FEE: 50,
  EQUIPMENT_RENTAL: 100,
  TRANSPORTATION: 200
};

// Default trek duration in days
const DEFAULT_TREK_DURATION = 12;

/**
 * Calculates the total cost of the trekking trip
 * @param {number} duration - Duration of the trek in days
 * @param {boolean} needsGuide - Whether a guide is needed
 * @param {boolean} needsEquipment - Whether equipment rental is needed
 * @returns {object} - Object containing cost breakdown and total
 */
function calculateCost(duration, needsGuide, needsEquipment) {
  const accommodationCost = COSTS.ACCOMMODATION_PER_NIGHT * duration;
  const foodCost = COSTS.FOOD_PER_DAY * duration;
  const guideCost = needsGuide ? COSTS.GUIDE_PER_DAY * duration : 0;
  const equipmentCost = needsEquipment ? COSTS.EQUIPMENT_RENTAL : 0;

  const totalCost = accommodationCost + foodCost + guideCost + 
                   COSTS.PERMIT_FEE + equipmentCost + COSTS.TRANSPORTATION;

  return {
    accommodation: accommodationCost,
    food: foodCost,
    guide: guideCost,
    permit: COSTS.PERMIT_FEE,
    equipment: equipmentCost,
    transportation: COSTS.TRANSPORTATION,
    total: totalCost
  };
}

// Validation middleware for the trek calculation endpoint
const validateTrekRequest = [
  check('duration').optional().isInt({ min: 1 }).withMessage('Duration must be a positive integer'),
  check('needsGuide').optional().isBoolean().withMessage('needsGuide must be a boolean'),
  check('needsEquipment').optional().isBoolean().withMessage('needsEquipment must be a boolean')
];

/**
 * POST endpoint to calculate trek costs
 */
app.post('/api/calculate', validateTrekRequest, (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const {
      duration = DEFAULT_TREK_DURATION,
      needsGuide = true,
      needsEquipment = false
    } = req.body;

    const costBreakdown = calculateCost(duration, needsGuide, needsEquipment);
    res.json(costBreakdown);
  } catch (error) {
    console.error('Error calculating trek cost:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = { app, calculateCost }; // For testing purposes
```
