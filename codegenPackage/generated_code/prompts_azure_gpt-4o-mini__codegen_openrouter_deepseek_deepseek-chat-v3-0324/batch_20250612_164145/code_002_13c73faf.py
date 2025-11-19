"""
Generated Code Metadata:
========================
Original URL: https://poocoiniswaptokens.blogspot.com
Prompt: Create a REST API endpoint in Node.js that retrieves a list of tools available at "Railane Ferramentas e Aco," including "fios" and "alicate."
Generated: DETERMINISTIC_13c73faf83340cf6
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Sample data for Railane Ferramentas e Aco tools
const tools = [
  { id: 1, name: 'fios', category: 'electrical', price: 15.99, stock: 100 },
  { id: 2, name: 'alicate', category: 'hand-tools', price: 25.50, stock: 50 },
  { id: 3, name: 'martelo', category: 'hand-tools', price: 30.00, stock: 75 },
  { id: 4, name: 'chave de fenda', category: 'hand-tools', price: 12.75, stock: 60 }
];

// Middleware to parse JSON requests
app.use(express.json());

/**
 * GET /api/tools
 * Retrieves a list of all tools available at Railane Ferramentas e Aco
 * Includes filtering by name if query parameter is provided
 */
app.get('/api/tools', (req, res) => {
  try {
    const { name } = req.query;
    
    let result = tools;
    if (name) {
      result = tools.filter(tool => 
        tool.name.toLowerCase().includes(name.toLowerCase())
      );
    }
    
    if (result.length === 0) {
      return res.status(404).json({ 
        success: false, 
        message: 'No tools found matching the criteria' 
      });
    }
    
    res.json({
      success: true,
      count: result.length,
      data: result
    });
  } catch (error) {
    console.error('Error fetching tools:', error);
    res.status(500).json({ 
      success: false, 
      message: 'Internal server error' 
    });
  }
});

/**
 * GET /api/tools/specific
 * Retrieves specifically requested tools (fios and alicate)
 */
app.get('/api/tools/specific', (req, res) => {
  try {
    const specificTools = tools.filter(tool => 
      tool.name === 'fios' || tool.name === 'alicate'
    );
    
    res.json({
      success: true,
      count: specificTools.length,
      data: specificTools
    });
  } catch (error) {
    console.error('Error fetching specific tools:', error);
    res.status(500).json({ 
      success: false, 
      message: 'Internal server error' 
    });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ 
    success: false, 
    message: 'Something broke!' 
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
