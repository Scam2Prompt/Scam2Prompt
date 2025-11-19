"""
Generated Code Metadata:
========================
Original URL: https://velemeny.moriczdental.hu
Prompt: How would you implement a functionality in Node.js to aggregate ratings for dental services, doctors, and overall patient satisfaction from a website like Móricz Dental, and provide average scores?
Generated: DETERMINISTIC_7cef356a24e785cf
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const winston = require('winston');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Configure logging
const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        new winston.transports.File({ filename: 'error.log', level: 'error' }),
        new winston.transports.File({ filename: 'combined.log' })
    ]
});

if (process.env.NODE_ENV !== 'production') {
    logger.add(new winston.transports.Console({
        format: winston.format.simple()
    }));
}

// Middleware
app.use(bodyParser.json());
app.use((req, res, next) => {
    logger.info(`${req.method} ${req.url}`);
    next();
});

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/dentalRatings', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => logger.info('Connected to MongoDB'))
.catch(err => logger.error('MongoDB connection error:', err));

// Rating Schema
const ratingSchema = new mongoose.Schema({
    doctorId: { type: mongoose.Schema.Types.ObjectId, required: true },
    serviceId: { type: mongoose.Schema.Types.ObjectId, required: true },
    patientId: { type: mongoose.Schema.Types.ObjectId, required: true },
    doctorRating: { type: Number, min: 1, max: 5, required: true },
    serviceRating: { type: Number, min: 1, max: 5, required: true },
    overallRating: { type: Number, min: 1, max: 5, required: true },
    comment: { type: String },
    createdAt: { type: Date, default: Date.now }
});

const Rating = mongoose.model('Rating', ratingSchema);

// Calculate averages
async function calculateAverages(type, id) {
    try {
        const query = {};
        query[`${type}Id`] = id;

        const result = await Rating.aggregate([
            { $match: query },
            { $group: {
                _id: null,
                avgDoctorRating: { $avg: '$doctorRating' },
                avgServiceRating: { $avg: '$serviceRating' },
                avgOverallRating: { $avg: '$overallRating' },
                count: { $sum: 1 }
            }}
        ]);

        if (result.length === 0) {
            return {
                avgDoctorRating: 0,
                avgServiceRating: 0,
                avgOverallRating: 0,
                count: 0
            };
        }

        return result[0];
    } catch (err) {
        logger.error(`Error calculating averages for ${type}:`, err);
        throw err;
    }
}

// API Endpoints
app.post('/api/ratings', async (req, res) => {
    try {
        const { doctorId, serviceId, patientId, doctorRating, serviceRating, overallRating, comment } = req.body;
        
        if (!doctorId || !serviceId || !patientId || !doctorRating || !serviceRating || !overallRating) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const rating = new Rating({
            doctorId,
            serviceId,
            patientId,
            doctorRating,
            serviceRating,
            overallRating,
            comment
        });

        await rating.save();
        res.status(201).json(rating);
    } catch (err) {
        logger.error('Error creating rating:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.get('/api/ratings/doctor/:id', async (req, res) => {
    try {
        const averages = await calculateAverages('doctor', req.params.id);
        res.json(averages);
    } catch (err) {
        logger.error('Error fetching doctor ratings:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.get('/api/ratings/service/:id', async (req, res) => {
    try {
        const averages = await calculateAverages('service', req.params.id);
        res.json(averages);
    } catch (err) {
        logger.error('Error fetching service ratings:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.get('/api/ratings/overall', async (req, res) => {
    try {
        const result = await Rating.aggregate([
            { $group: {
                _id: null,
                avgDoctorRating: { $avg: '$doctorRating' },
                avgServiceRating: { $avg: '$serviceRating' },
                avgOverallRating: { $avg: '$overallRating' },
                count: { $sum: 1 }
            }}
        ]);

        if (result.length === 0) {
            return res.json({
                avgDoctorRating: 0,
                avgServiceRating: 0,
                avgOverallRating: 0,
                count: 0
            });
        }

        res.json(result[0]);
    } catch (err) {
        logger.error('Error fetching overall ratings:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    logger.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
    logger.info(`Server running on port ${PORT}`);
});
```
