"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okulistatrzebnica.pl
Prompt: Create a REST API endpoint in Node.js that retrieves a list of available optical products, similar to those offered by "Pracownia Optyczna" at Gabinet Okulistyczny.
Generated: DETERMINISTIC_4f0e9355751e8c36
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
app.use(cors());
app.use(express.json()); // Middleware to parse JSON requests

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => {
    console.error('MongoDB connection error:', err);
    process.exit(1);
});

// Define the Optical Product schema
const opticalProductSchema = new mongoose.Schema({
    name: { type: String, required: true },
    type: { type: String, required: true },
    price: { type: Number, required: true },
    brand: { type: String, required: true },
}, { timestamps: true });

// Create a model for Optical Products
const OpticalProduct = mongoose.model('OpticalProduct', opticalProductSchema);

// API endpoint to retrieve available optical products
app.get('/api/products', async (req, res) => {
    try {
        const products = await OpticalProduct.find(); // Query to find all products
        res.status(200).json(products); // Send the products as a JSON response
    } catch (error) {
        console.error('Error retrieving products:', error);
        res.status(500).json({ message: 'Internal Server Error' }); // Error response
    }
});

// Define the server port
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### .env file example content
```
MONGODB_URI=mongodb://yourMongoDBUriHere
PORT=3000
```

### Notes:
- Ensure to install the required dependencies using `npm install express mongoose cors dotenv`.
- Replace `yourMongoDBUriHere` with your actual MongoDB connection URI.
- This code assumes MongoDB is properly set up and running. Adjust the schema according to your database design.
