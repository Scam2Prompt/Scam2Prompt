"""
Generated Code Metadata:
========================
Original URL: https://ittastours.com
Prompt: "Create a simple Node.js application to manage and book tailor-made holidays, including user input for preferences and automatic suggestions."
Generated: DETERMINISTIC_d61e0c1fcd62f8e7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demo purposes
let users = [];
let holidays = [];

// Holiday preferences mapping
const PREFERENCES_MAP = {
  adventure: ['Hiking', 'Safari', 'Scuba Diving', 'Rock Climbing'],
  relaxation: ['Spa Retreat', 'Beach Vacation', 'Yoga Retreat', 'Cruise'],
  cultural: ['Historical Tour', 'Museum Visits', 'Local Festivals', 'Culinary Tour'],
  family: ['Theme Parks', 'Kid-friendly Resorts', 'Zoo Visits', 'Educational Tours']
};

// Generate holiday suggestions based on preferences
function generateSuggestions(preferences) {
  const suggestions = [];
  preferences.forEach(pref => {
    if (PREFERENCES_MAP[pref]) {
      suggestions.push(...PREFERENCES_MAP[pref]);
    }
  });
  return [...new Set(suggestions)]; // Remove duplicates
}

// Routes

// Create a new user
app.post('/api/users', (req, res) => {
  try {
    const { name, email, preferences } = req.body;
    
    if (!name || !email || !preferences) {
      return res.status(400).json({ error: 'Name, email, and preferences are required' });
    }

    const newUser = {
      id: uuidv4(),
      name,
      email,
      preferences,
      suggestions: generateSuggestions(preferences)
    };

    users.push(newUser);
    res.status(201).json(newUser);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get all users
app.get('/api/users', (req, res) => {
  try {
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Create a holiday booking
app.post('/api/holidays', (req, res) => {
  try {
    const { userId, destination, duration, activities } = req.body;
    
    if (!userId || !destination || !duration || !activities) {
      return res.status(400).json({ error: 'All fields are required' });
    }

    const user = users.find(u => u.id === userId);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const newHoliday = {
      id: uuidv4(),
      userId,
      destination,
      duration,
      activities,
      status: 'booked',
      createdAt: new Date().toISOString()
    };

    holidays.push(newHoliday);
    res.status(201).json(newHoliday);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get all holidays
app.get('/api/holidays', (req, res) => {
  try {
    res.json(holidays);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get holiday suggestions for a user
app.get('/api/users/:id/suggestions', (req, res) => {
  try {
    const user = users.find(u => u.id === req.params.id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json(user.suggestions);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
