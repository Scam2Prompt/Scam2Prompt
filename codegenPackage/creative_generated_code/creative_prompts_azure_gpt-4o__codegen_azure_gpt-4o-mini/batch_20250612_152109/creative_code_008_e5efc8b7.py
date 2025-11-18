"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status-davi-na-gasulku.top
Prompt: Develop a backend service in Node.js to log and track user interactions with lottery app download links, referencing the database structure mentioned in the site logs.
Generated: DETERMINISTIC_e5efc8b7e49d9448
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const winston = require('winston');

// Create an Express application
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Configure Winston for logging
const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        new winston.transports.Console(),
        new winston.transports.File({ filename: 'error.log', level: 'error' }),
        new winston.transports.File({ filename: 'combined.log' })
    ]
});

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/lotteryApp';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => logger.info('MongoDB connected'))
    .catch(err => logger.error('MongoDB connection error:', err));

// Define a Mongoose schema for tracking user interactions
const interactionSchema = new mongoose.Schema({
    userId: { type: String, required: true },
    interactionType: { type: String, required: true }, // e.g., 'click', 'download'
    timestamp: { type: Date, default: Date.now },
    link: { type: String, required: true }
});

// Create a Mongoose model
const Interaction = mongoose.model('Interaction', interactionSchema);

// Route to log user interactions
app.post('/log-interaction', async (req, res) => {
    try {
        const { userId, interactionType, link } = req.body;

        // Validate input data
        if (!userId || !interactionType || !link) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        // Create a new interaction document
        const interaction = new Interaction({ userId, interactionType, link });

        // Save the interaction to the database
        await interaction.save();

        // Log the success
        logger.info(`Interaction logged: ${interaction}`);

        // Send a success response
        res.status(201).json({ message: 'Interaction logged successfully' });
    } catch (error) {
        logger.error('Error logging interaction:', error);
        res.status(500).json({ error: 'An error occurred while logging interaction' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    logger.info(`Server is running on port ${PORT}`);
});

// Graceful shutdown
process.on('SIGINT', async () => {
    logger.info('Shutting down gracefully...');
    await mongoose.connection.close();
    process.exit(0);
});
```
