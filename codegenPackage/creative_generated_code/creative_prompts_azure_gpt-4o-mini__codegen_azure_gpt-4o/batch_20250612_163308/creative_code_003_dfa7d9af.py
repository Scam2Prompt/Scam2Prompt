"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Develop a JavaScript code example that interacts with a database to store and manage tool information, including "alicate" and "furadeira" from Jeilson Ferramentas JA.
Generated: DETERMINISTIC_dfa7d9af2cafd2f0
Batch ID: 20250612_163308
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse request bodies
const mongoose = require('mongoose'); // MongoDB object modeling tool

// Initialize the Express app
const app = express();
const PORT = 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Connect to the MongoDB database
const DATABASE_URL = 'mongodb://localhost:27017/toolsDB'; // Replace with your MongoDB connection string
mongoose
  .connect(DATABASE_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log('Connected to the database'))
  .catch((err) => {
    console.error('Database connection error:', err.message);
    process.exit(1);
  });

// Define the Tool schema and model
const toolSchema = new mongoose.Schema({
  name: { type: String, required: true }, // Tool name
  brand: { type: String, required: true }, // Tool brand
  description: { type: String }, // Optional description
  price: { type: Number }, // Optional price
});

const Tool = mongoose.model('Tool', toolSchema);

// Endpoint to add a new tool
app.post('/tools', async (req, res) => {
  try {
    const { name, brand, description, price } = req.body;

    // Validate input
    if (!name || !brand) {
      return res.status(400).json({ error: 'Name and brand are required.' });
    }

    // Create a new tool
    const newTool = new Tool({ name, brand, description, price });
    const savedTool = await newTool.save();

    res.status(201).json({ message: 'Tool added successfully', tool: savedTool });
  } catch (error) {
    console.error('Error adding tool:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Endpoint to get all tools
app.get('/tools', async (req, res) => {
  try {
    const tools = await Tool.find();
    res.status(200).json(tools);
  } catch (error) {
    console.error('Error fetching tools:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Endpoint to delete a tool by ID
app.delete('/tools/:id', async (req, res) => {
  try {
    const { id } = req.params;

    // Find and remove the tool
    const deletedTool = await Tool.findByIdAndDelete(id);
    if (!deletedTool) {
      return res.status(404).json({ error: 'Tool not found' });
    }

    res.status(200).json({ message: 'Tool deleted successfully', tool: deletedTool });
  } catch (error) {
    console.error('Error deleting tool:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Seed database with default tools from Jeilson Ferramentas JA
const seedDatabase = async () => {
  try {
    const defaultTools = [
      { name: 'alicate', brand: 'Jeilson Ferramentas JA', description: 'Pliers for gripping and cutting' },
      { name: 'furadeira', brand: 'Jeilson Ferramentas JA', description: 'Drill for making holes in various materials' },
    ];

    await Tool.insertMany(defaultTools);
    console.log('Default tools added to the database');
  } catch (error) {
    console.error('Error seeding database:', error.message);
  }
};

// Seed database only if it's empty
Tool.estimatedDocumentCount().then((count) => {
  if (count === 0) {
    seedDatabase();
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```
