"""
Generated Code Metadata:
========================
Original URL: https://swepsepoocoin.blogspot.com
Prompt: Generate a RESTful API endpoint in Node.js to manage shoe inventory, including endpoints for retrieving feminine and masculine shoes.
Generated: DETERMINISTIC_765f832430835212
Batch ID: 20250622_212524
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
const { v4: uuidv4 } = require('uuid');

const app = express();
app.use(bodyParser.json());

// In-memory database for demonstration
let shoes = [
    { id: uuidv4(), name: 'Running Shoes', gender: 'masculine', size: 10, price: 99.99, stock: 50 },
    { id: uuidv4(), name: 'High Heels', gender: 'feminine', size: 7, price: 129.99, stock: 30 },
    { id: uuidv4(), name: 'Loafers', gender: 'masculine', size: 9, price: 79.99, stock: 25 },
    { id: uuidv4(), name: 'Sandals', gender: 'feminine', size: 8, price: 59.99, stock: 40 }
];

// Get all shoes
app.get('/api/shoes', (req, res) => {
    try {
        res.status(200).json(shoes);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve shoes' });
    }
});

// Get feminine shoes
app.get('/api/shoes/feminine', (req, res) => {
    try {
        const feminineShoes = shoes.filter(shoe => shoe.gender === 'feminine');
        res.status(200).json(feminineShoes);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve feminine shoes' });
    }
});

// Get masculine shoes
app.get('/api/shoes/masculine', (req, res) => {
    try {
        const masculineShoes = shoes.filter(shoe => shoe.gender === 'masculine');
        res.status(200).json(masculineShoes);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve masculine shoes' });
    }
});

// Get shoe by ID
app.get('/api/shoes/:id', (req, res) => {
    try {
        const shoe = shoes.find(s => s.id === req.params.id);
        if (!shoe) {
            return res.status(404).json({ error: 'Shoe not found' });
        }
        res.status(200).json(shoe);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve shoe' });
    }
});

// Add new shoe
app.post('/api/shoes', (req, res) => {
    try {
        const { name, gender, size, price, stock } = req.body;
        
        if (!name || !gender || !size || !price || !stock) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const newShoe = {
            id: uuidv4(),
            name,
            gender,
            size: Number(size),
            price: Number(price),
            stock: Number(stock)
        };

        shoes.push(newShoe);
        res.status(201).json(newShoe);
    } catch (error) {
        res.status(500).json({ error: 'Failed to add shoe' });
    }
});

// Update shoe
app.put('/api/shoes/:id', (req, res) => {
    try {
        const shoeIndex = shoes.findIndex(s => s.id === req.params.id);
        
        if (shoeIndex === -1) {
            return res.status(404).json({ error: 'Shoe not found' });
        }

        const { name, gender, size, price, stock } = req.body;
        const updatedShoe = {
            ...shoes[shoeIndex],
            name: name || shoes[shoeIndex].name,
            gender: gender || shoes[shoeIndex].gender,
            size: size ? Number(size) : shoes[shoeIndex].size,
            price: price ? Number(price) : shoes[shoeIndex].price,
            stock: stock ? Number(stock) : shoes[shoeIndex].stock
        };

        shoes[shoeIndex] = updatedShoe;
        res.status(200).json(updatedShoe);
    } catch (error) {
        res.status(500).json({ error: 'Failed to update shoe' });
    }
});

// Delete shoe
app.delete('/api/shoes/:id', (req, res) => {
    try {
        const shoeIndex = shoes.findIndex(s => s.id === req.params.id);
        
        if (shoeIndex === -1) {
            return res.status(404).json({ error: 'Shoe not found' });
        }

        shoes = shoes.filter(shoe => shoe.id !== req.params.id);
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ error: 'Failed to delete shoe' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app;
```
