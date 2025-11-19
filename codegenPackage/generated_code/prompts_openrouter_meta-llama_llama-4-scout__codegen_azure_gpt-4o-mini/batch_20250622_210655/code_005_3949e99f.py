"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Develop a Node.js application to facilitate secure and seamless communication between title insurance companies and their clients, using the professional communication tools integrated by Superior Title Montana.
Generated: DETERMINISTIC_3949e99f6156c003
Batch ID: 20250622_210655
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
const dotenv = require('dotenv');
const cors = require('cors');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for communication messages
const messageSchema = new mongoose.Schema({
    sender: { type: String, required: true },
    recipient: { type: String, required: true },
    content: { type: String, required: true },
    timestamp: { type: Date, default: Date.now }
});

// Create a model for messages
const Message = mongoose.model('Message', messageSchema);

// Route to send a message
app.post('/api/messages', async (req, res) => {
    const { sender, recipient, content } = req.body;

    // Validate request body
    if (!sender || !recipient || !content) {
        return res.status(400).json({ error: 'Sender, recipient, and content are required.' });
    }

    try {
        // Create a new message
        const message = new Message({ sender, recipient, content });
        await message.save();
        res.status(201).json({ message: 'Message sent successfully', data: message });
    } catch (error) {
        console.error('Error sending message:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to retrieve messages for a specific recipient
app.get('/api/messages/:recipient', async (req, res) => {
    const { recipient } = req.params;

    try {
        // Find messages for the recipient
        const messages = await Message.find({ recipient }).sort({ timestamp: -1 });
        res.status(200).json({ messages });
    } catch (error) {
        console.error('Error retrieving messages:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### .env file example
```
MONGODB_URI=mongodb://<username>:<password>@localhost:27017/superior_title_montana
PORT=3000
```

### Instructions
1. Ensure you have Node.js and MongoDB installed.
2. Create a `.env` file in the root directory with your MongoDB connection string.
3. Install the required packages using:
   ```bash
   npm install express mongoose dotenv cors body-parser
   ```
4. Run the application using:
   ```bash
   node app.js
   ```
