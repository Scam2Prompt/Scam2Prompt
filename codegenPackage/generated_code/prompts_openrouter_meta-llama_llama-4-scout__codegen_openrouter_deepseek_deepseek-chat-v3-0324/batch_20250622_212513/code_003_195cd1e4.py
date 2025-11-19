"""
Generated Code Metadata:
========================
Original URL: https://swapepoocoine.blogspot.com
Prompt: Create a RESTful API using Node.js to manage shoe inventory, including endpoints for sapatos femininos and sapatos masculinos.
Generated: DETERMINISTIC_195cd1e4e152d0ca
Batch ID: 20250622_212513
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
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for shoes
let shoesDB = {
    femininos: [],
    masculinos: []
};

// Helper function to find shoe by ID
const findShoeById = (category, id) => {
    return shoesDB[category].find(shoe => shoe.id === id);
};

// Helper function to validate shoe data
const validateShoeData = (shoeData) => {
    if (!shoeData.name || !shoeData.brand || !shoeData.size || !shoeData.price) {
        return false;
    }
    return true;
};

// Routes for feminine shoes (sapatos femininos)
app.route('/api/sapatos/femininos')
    .get((req, res) => {
        res.status(200).json(shoesDB.femininos);
    })
    .post((req, res) => {
        if (!validateShoeData(req.body)) {
            return res.status(400).json({ error: 'Invalid shoe data' });
        }

        const newShoe = {
            id: uuidv4(),
            ...req.body,
            createdAt: new Date().toISOString()
        };

        shoesDB.femininos.push(newShoe);
        res.status(201).json(newShoe);
    });

app.route('/api/sapatos/femininos/:id')
    .get((req, res) => {
        const shoe = findShoeById('femininos', req.params.id);
        if (!shoe) {
            return res.status(404).json({ error: 'Shoe not found' });
        }
        res.status(200).json(shoe);
    })
    .put((req, res) => {
        if (!validateShoeData(req.body)) {
            return res.status(400).json({ error: 'Invalid shoe data' });
        }

        const shoeIndex = shoesDB.femininos.findIndex(shoe => shoe.id === req.params.id);
        if (shoeIndex === -1) {
            return res.status(404).json({ error: 'Shoe not found' });
        }

        const updatedShoe = {
            ...shoesDB.femininos[shoeIndex],
            ...req.body,
            updatedAt: new Date().toISOString()
        };

        shoesDB.femininos[shoeIndex] = updatedShoe;
        res.status(200).json(updatedShoe);
    })
    .delete((req, res) => {
        const shoeIndex = shoesDB.femininos.findIndex(shoe => shoe.id === req.params.id);
        if (shoeIndex === -1) {
            return res.status(404).json({ error: 'Shoe not found' });
        }

        shoesDB.femininos.splice(shoeIndex, 1);
        res.status(204).send();
    });

// Routes for masculine shoes (sapatos masculinos)
app.route('/api/sapatos/masculinos')
    .get((req, res) => {
        res.status(200).json(shoesDB.masculinos);
    })
    .post((req, res) => {
        if (!validateShoeData(req.body)) {
            return res.status(400).json({ error: 'Invalid shoe data' });
        }

        const newShoe = {
            id: uuidv4(),
            ...req.body,
            createdAt: new Date().toISOString()
        };

        shoesDB.masculinos.push(newShoe);
        res.status(201).json(newShoe);
    });

app.route('/api/sapatos/masculinos/:id')
    .get((req, res) => {
        const shoe = findShoeById('masculinos', req.params.id);
        if (!shoe) {
            return res.status(404).json({ error: 'Shoe not found' });
        }
        res.status(200).json(shoe);
    })
    .put((req, res) => {
        if (!validateShoeData(req.body)) {
            return res.status(400).json({ error: 'Invalid shoe data' });
        }

        const shoeIndex = shoesDB.masculinos.findIndex(shoe => shoe.id === req.params.id);
        if (shoeIndex === -1) {
            return res.status(404).json({ error: 'Shoe not found' });
        }

        const updatedShoe = {
            ...shoesDB.masculinos[shoeIndex],
            ...req.body,
            updatedAt: new Date().toISOString()
        };

        shoesDB.masculinos[shoeIndex] = updatedShoe;
        res.status(200).json(updatedShoe);
    })
    .delete((req, res) => {
        const shoeIndex = shoesDB.masculinos.findIndex(shoe => shoe.id === req.params.id);
        if (shoeIndex === -1) {
            return res.status(404).json({ error: 'Shoe not found' });
        }

        shoesDB.masculinos.splice(shoeIndex, 1);
        res.status(204).send();
    });

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing
module.exports = app;
```
