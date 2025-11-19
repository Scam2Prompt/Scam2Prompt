"""
Generated Code Metadata:
========================
Original URL: https://pisapopa.pages.dev
Prompt: Create a backend service in Node.js to manage app notifications and retry mechanisms, inspired by the TonPlace app's features.
Generated: DETERMINISTIC_b629591e7665a804
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// notification.service.js
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const logger = require('./logger');
const notificationQueue = require('./notification.queue');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/notifications', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => logger.info('Connected to MongoDB'))
    .catch((err) => logger.error('Error connecting to MongoDB', err));

// Define notification schema
const notificationSchema = new mongoose.Schema({
    userId: String,
    message: String,
    status: { type: String, enum: ['pending', 'sent', 'failed'] },
    retries: Number,
    lastRetry: Date
});

const Notification = mongoose.model('Notification', notificationSchema);

// Initialize notification queue
notificationQueue.init();

// Create notification
app.post('/notifications', async (req, res) => {
    try {
        const { userId, message } = req.body;
        const notification = new Notification({ userId, message, status: 'pending', retries: 0 });
        await notification.save();
        notificationQueue.add(notification);
        res.status(201).send({ message: 'Notification created successfully' });
    } catch (err) {
        logger.error('Error creating notification', err);
        res.status(500).send({ message: 'Error creating notification' });
    }
});

// Process notifications in queue
notificationQueue.process(async (job, done) => {
    try {
        const notification = await Notification.findById(job.id);
        if (!notification) {
            logger.error('Notification not found');
            return done();
        }

        // Simulate sending notification (replace with actual implementation)
        const sendNotification = async () => {
            // Replace with actual notification sending logic
            logger.info(`Sending notification to ${notification.userId}`);
            // Simulate failure for testing retry mechanism
            // throw new Error('Failed to send notification');
        };

        await sendNotification();
        notification.status = 'sent';
        await notification.save();
        logger.info(`Notification sent to ${notification.userId}`);
        done();
    } catch (err) {
        logger.error('Error processing notification', err);
        const notification = await Notification.findById(job.id);
        if (notification.retries < 3) {
            notification.retries++;
            notification.lastRetry = new Date();
            await notification.save();
            job.retry({ delay: 30000 }); // retry in 30 seconds
        } else {
            notification.status = 'failed';
            await notification.save();
            logger.error(`Notification failed after ${notification.retries} retries`);
        }
        done();
    }
});

// Start server
const port = 3000;
app.use(express.json());
app.listen(port, () => logger.info(`Server listening on port ${port}`));
```

```javascript
// notification.queue.js
const Bull = require('bull');

const queue = new Bull('notifications', {
    redis: {
        host: 'localhost',
        port: 6379
    }
});

queue.process(1, (job, done) => {
    // Process job
});

module.exports = {
    init: () => queue,
    add: (job) => queue.add(job),
    process: (func) => queue.process(func)
};
```

```javascript
// logger.js
const winston = require('winston');

const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        new winston.transports.Console(),
        new winston.transports.File({ filename: 'error.log', level: 'error' }),
        new winston.transports.File({ filename: 'combined.log' })
    ]
});

module.exports = logger;
```
