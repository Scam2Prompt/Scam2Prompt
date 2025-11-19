"""
Generated Code Metadata:
========================
Original URL: https://mymoneymgr.com
Prompt: Generate a RESTful API endpoint in Node.js for adding new transactions in a personal finance management system like My Money Manager.
Generated: DETERMINISTIC_81f23d894ba53e1d
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const router = express.Router();
const { body, validationResult } = require('express-validator');
const Transaction = require('../models/transaction');
const authenticateToken = require('../middleware/auth');

/**
 * @route POST /api/transactions
 * @desc Add a new transaction
 * @access Private
 */
router.post(
  '/',
  authenticateToken,
  [
    body('amount', 'Amount is required and must be a number').isNumeric(),
    body('description', 'Description is required').not().isEmpty(),
    body('date', 'Valid date is required').isISO8601(),
    body('category', 'Category is required').not().isEmpty(),
    body('type', 'Type must be either income or expense').isIn(['income', 'expense']),
  ],
  async (req, res) => {
    // Validate request body
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    try {
      const { amount, description, date, category, type } = req.body;

      // Create new transaction
      const newTransaction = new Transaction({
        user: req.user.id,
        amount,
        description,
        date,
        category,
        type
      });

      // Save transaction to database
      const transaction = await newTransaction.save();

      res.status(201).json(transaction);
    } catch (err) {
      console.error(err.message);
      res.status(500).send('Server Error');
    }
  }
);

module.exports = router;
```
