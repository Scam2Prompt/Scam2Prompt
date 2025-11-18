"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange24h.com
Prompt: Develop a backend system in Node.js to manage slot deposit transactions, including features for tracking "ribuan permainan slot online terbaru" and handling deposits starting at 5k IDR.
Generated: DETERMINISTIC_ed72f5b55aafd361
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // For building the web server
const bodyParser = require('body-parser'); // For parsing incoming requests
const mongoose = require('mongoose'); // For MongoDB interaction
const dotenv = require('dotenv'); // For environment variable management

// Load environment variables from .env file
dotenv.config();

// Initialize the Express application
const app = express();
app.use(bodyParser.json()); // Parse JSON payloads

// Connect to the MongoDB database
mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log("Connected to the database");
}).catch((err) => {
    console.error("Database connection error:", err);
    process.exit(1); // Exit the application if database connection fails
});

// Define a Mongoose schema for slot deposit transactions
const slotTransactionSchema = new mongoose.Schema({
    userId: { type: String, required: true }, // ID of the user making the deposit
    depositAmount: { 
        type: Number, 
        required: true,
        min: 5000 // Minimum deposit amount is 5k IDR
    },
    gameDetails: { type: String, required: true }, // Details of the slot game
    transactionDate: { type: Date, default: Date.now } // Auto-set transaction date
});

// Create a Mongoose model for SlotTransaction
const SlotTransaction = mongoose.model('SlotTransaction', slotTransactionSchema);

// API Endpoint: Fetch all transactions
app.get('/api/transactions', async (req, res) => {
    try {
        const transactions = await SlotTransaction.find(); // Fetch all transactions from the database
        res.status(200).json(transactions);
    } catch (error) {
        console.error("Error fetching transactions:", error);
        res.status(500).json({ message: "Internal server error" }); // Return error response
    }
});

// API Endpoint: Create a new deposit transaction
app.post('/api/transactions', async (req, res) => {
    const { userId, depositAmount, gameDetails } = req.body;

    // Validate input
    if (!userId || !depositAmount || !gameDetails) {
        return res.status(400).json({ message: "Missing required fields" });
    }

    try {
        // Create a new transaction document
        const transaction = new SlotTransaction({
            userId,
            depositAmount,
            gameDetails,
        });

        // Save the transaction to the database
        await transaction.save();

        res.status(201).json({ message: "Transaction created successfully", transaction });
    } catch (error) {
        console.error("Error creating transaction:", error);
        res.status(500).json({ message: "Internal server error" }); // Return error response
    }
});

// API Endpoint: Fetch a transaction by ID
app.get('/api/transactions/:id', async (req, res) => {
    const { id } = req.params;

    try {
        const transaction = await SlotTransaction.findById(id); // Fetch transaction by ID
        if (!transaction) {
            return res.status(404).json({ message: "Transaction not found" });
        }
        res.status(200).json(transaction);
    } catch (error) {
        console.error("Error fetching transaction:", error);
        res.status(500).json({ message: "Internal server error" });
    }
});

// API Endpoint: Delete a transaction by ID
app.delete('/api/transactions/:id', async (req, res) => {
    const { id } = req.params;

    try {
        const transaction = await SlotTransaction.findByIdAndDelete(id); // Delete transaction by ID
        if (!transaction) {
            return res.status(404).json({ message: "Transaction not found" });
        }
        res.status(200).json({ message: "Transaction deleted successfully" });
    } catch (error) {
        console.error("Error deleting transaction:", error);
        res.status(500).json({ message: "Internal server error" });
    }
});

// Start the Express server
const PORT = process.env.PORT || 3000; // Use PORT from environment variables or default to 3000
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to create a `.env` file and include a `MONGO_URI` with your MongoDB connection string for the code to work properly.
