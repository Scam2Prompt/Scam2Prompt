"""
Generated Code Metadata:
========================
Original URL: https://daddysoluniversity.com
Prompt: Create a RESTful API using Node.js to manage a bookstore's inventory, including endpoints for adding new books, retrieving product information, and applying discounts or promotions.
Generated: DETERMINISTIC_b041e256857daca2
Batch ID: 20250622_211405
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
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace 'your_connection_string' with your actual connection string)
mongoose.connect('your_connection_string', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Book schema
const bookSchema = new mongoose.Schema({
    title: { type: String, required: true },
    author: { type: String, required: true },
    price: { type: Number, required: true },
    discount: { type: Number, default: 0 },
    description: { type: String, default: '' }
});

// Create a Book model
const Book = mongoose.model('Book', bookSchema);

// Endpoint to add a new book
app.post('/api/books', async (req, res) => {
    try {
        const { title, author, price, discount, description } = req.body;
        const newBook = new Book({ title, author, price, discount, description });
        await newBook.save();
        res.status(201).json(newBook);
    } catch (error) {
        console.error('Error adding book:', error);
        res.status(500).json({ message: 'Error adding book', error });
    }
});

// Endpoint to retrieve all books
app.get('/api/books', async (req, res) => {
    try {
        const books = await Book.find();
        res.status(200).json(books);
    } catch (error) {
        console.error('Error retrieving books:', error);
        res.status(500).json({ message: 'Error retrieving books', error });
    }
});

// Endpoint to retrieve a book by ID
app.get('/api/books/:id', async (req, res) => {
    try {
        const book = await Book.findById(req.params.id);
        if (!book) {
            return res.status(404).json({ message: 'Book not found' });
        }
        res.status(200).json(book);
    } catch (error) {
        console.error('Error retrieving book:', error);
        res.status(500).json({ message: 'Error retrieving book', error });
    }
});

// Endpoint to apply a discount to a book
app.patch('/api/books/:id/discount', async (req, res) => {
    try {
        const { discount } = req.body;
        const book = await Book.findByIdAndUpdate(req.params.id, { discount }, { new: true });
        if (!book) {
            return res.status(404).json({ message: 'Book not found' });
        }
        res.status(200).json(book);
    } catch (error) {
        console.error('Error applying discount:', error);
        res.status(500).json({ message: 'Error applying discount', error });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
