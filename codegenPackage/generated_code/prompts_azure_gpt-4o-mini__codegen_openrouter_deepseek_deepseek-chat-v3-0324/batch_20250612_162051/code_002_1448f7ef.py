"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Create an API endpoint in Node.js that allows users to retrieve a list of traditional Indian and international dishes, reflecting the diverse menu of Perfect Food Corner.
Generated: DETERMINISTIC_1448f7efaf6c93cd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Sample data for traditional Indian and international dishes
const dishes = {
  indian: [
    { id: 1, name: 'Butter Chicken', description: 'Tender chicken in a creamy tomato sauce', category: 'Non-Veg' },
    { id: 2, name: 'Paneer Tikka', description: 'Grilled cottage cheese with spices', category: 'Veg' },
    { id: 3, name: 'Biryani', description: 'Fragrant rice dish with meat or vegetables', category: 'Non-Veg/Veg' },
    { id: 4, name: 'Masala Dosa', description: 'Crispy rice crepe with potato filling', category: 'Veg' },
    { id: 5, name: 'Dal Makhani', description: 'Creamy black lentils', category: 'Veg' }
  ],
  international: [
    { id: 6, name: 'Margherita Pizza', description: 'Classic pizza with tomato and mozzarella', category: 'Veg' },
    { id: 7, name: 'Pasta Carbonara', description: 'Pasta with creamy egg and bacon sauce', category: 'Non-Veg' },
    { id: 8, name: 'Sushi Platter', description: 'Assorted fresh sushi rolls', category: 'Non-Veg' },
    { id: 9, name: 'Caesar Salad', description: 'Romaine lettuce with croutons and dressing', category: 'Veg' },
    { id: 10, name: 'Beef Burger', description: 'Juicy beef patty with cheese and veggies', category: 'Non-Veg' }
  ]
};

// API endpoint to get all dishes
app.get('/api/dishes', (req, res) => {
  try {
    res.status(200).json({
      success: true,
      data: dishes
    });
  } catch (error) {
    console.error('Error fetching dishes:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to fetch dishes'
    });
  }
});

// API endpoint to get dishes by type (Indian/International)
app.get('/api/dishes/:type', (req, res) => {
  try {
    const type = req.params.type.toLowerCase();
    
    if (!dishes[type]) {
      return res.status(404).json({
        success: false,
        message: 'Invalid dish type. Please specify either "indian" or "international"'
      });
    }

    res.status(200).json({
      success: true,
      data: dishes[type]
    });
  } catch (error) {
    console.error(`Error fetching ${req.params.type} dishes:`, error);
    res.status(500).json({
      success: false,
      message: `Failed to fetch ${req.params.type} dishes`
    });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    success: false,
    message: 'Something went wrong!'
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
