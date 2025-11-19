"""
Generated Code Metadata:
========================
Original URL: https://www.psikolojibakirkoy.com.tr
Prompt: Create a REST API endpoint in Node.js that provides resources for individual therapy techniques, including those for depression and panic attacks, as outlined on the Psikoloji Bakırköy site.
Generated: DETERMINISTIC_3f693ffb9d51d948
Batch ID: 20250612_162051
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
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// In-memory storage for therapy techniques (replace with a database in production)
let therapyTechniques = [
  {
    id: 1,
    name: "Cognitive Behavioral Therapy for Depression",
    description: "A technique used to help individuals with depression by identifying and changing negative thought patterns.",
    category: "depression"
  },
  {
    id: 2,
    name: "Mindfulness-Based Stress Reduction for Panic Attacks",
    description: "A technique used to help individuals with panic attacks by teaching mindfulness and relaxation skills.",
    category: "panic-attacks"
  },
  // Add more techniques here...
];

// API endpoint to get all therapy techniques
app.get('/api/therapy-techniques', (req, res) => {
  try {
    res.json(therapyTechniques);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get a therapy technique by ID
app.get('/api/therapy-techniques/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const technique = therapyTechniques.find(t => t.id === id);
    if (!technique) {
      res.status(404).json({ message: 'Therapy technique not found' });
    } else {
      res.json(technique);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get therapy techniques by category
app.get('/api/therapy-techniques/category/:category', (req, res) => {
  try {
    const category = req.params.category.toLowerCase();
    const techniques = therapyTechniques.filter(t => t.category === category);
    if (techniques.length === 0) {
      res.status(404).json({ message: 'No therapy techniques found for this category' });
    } else {
      res.json(techniques);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to create a new therapy technique
app.post('/api/therapy-techniques', (req, res) => {
  try {
    const { name, description, category } = req.body;
    if (!name || !description || !category) {
      res.status(400).json({ message: 'Name, description, and category are required' });
    } else {
      const newTechnique = {
        id: therapyTechniques.length + 1,
        name,
        description,
        category
      };
      therapyTechniques.push(newTechnique);
      res.json(newTechnique);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update an existing therapy technique
app.put('/api/therapy-techniques/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const technique = therapyTechniques.find(t => t.id === id);
    if (!technique) {
      res.status(404).json({ message: 'Therapy technique not found' });
    } else {
      const { name, description, category } = req.body;
      if (name) technique.name = name;
      if (description) technique.description = description;
      if (category) technique.category = category;
      res.json(technique);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete a therapy technique
app.delete('/api/therapy-techniques/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const index = therapyTechniques.findIndex(t => t.id === id);
    if (index === -1) {
      res.status(404).json({ message: 'Therapy technique not found' });
    } else {
      therapyTechniques.splice(index, 1);
      res.json({ message: 'Therapy technique deleted successfully' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
