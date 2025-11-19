"""
Generated Code Metadata:
========================
Original URL: https://blog.firstflytravel.com
Prompt: Develop a REST API in Node.js that integrates First Fly Travel's flight booking services and provides real-time updates on last-minute flight availability.
Generated: DETERMINISTIC_63113dfaa768e08b
Batch ID: 20250612_145436
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
const axios = require('axios');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();
app.use(express.json());

// First Fly Travel API endpoint and credentials
const FIRST_FLY_TRAVEL_API_ENDPOINT = process.env.FIRST_FLY_TRAVEL_API_ENDPOINT;
const FIRST_FLY_TRAVEL_API_KEY = process.env.FIRST_FLY_TRAVEL_API_KEY;
const FIRST_FLY_TRAVEL_API_SECRET = process.env.FIRST_FLY_TRAVEL_API_SECRET;

// Function to handle API errors
function handleApiError(res, error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
}

// API endpoint to get last-minute flight availability
app.get('/api/last-minute-flights', async (req, res) => {
    try {
        // Set API request headers
        const headers = {
            'Authorization': `Bearer ${FIRST_FLY_TRAVEL_API_KEY}`,
            'Content-Type': 'application/json'
        };

        // Set API request parameters
        const params = {
            origin: req.query.origin,
            destination: req.query.destination,
            departureDate: req.query.departureDate
        };

        // Make GET request to First Fly Travel API
        const response = await axios.get(`${FIRST_FLY_TRAVEL_API_ENDPOINT}/flights`, { headers, params });

        // Return flight availability data
        res.json(response.data);
    } catch (error) {
        handleApiError(res, error);
    }
});

// API endpoint to book a flight
app.post('/api/book-flight', async (req, res) => {
    try {
        // Validate request body
        if (!req.body.origin || !req.body.destination || !req.body.departureDate || !req.body.flightId) {
            res.status(400).json({ message: 'Invalid request body' });
            return;
        }

        // Set API request headers
        const headers = {
            'Authorization': `Bearer ${FIRST_FLY_TRAVEL_API_KEY}`,
            'Content-Type': 'application/json'
        };

        // Set API request body
        const body = {
            origin: req.body.origin,
            destination: req.body.destination,
            departureDate: req.body.departureDate,
            flightId: req.body.flightId
        };

        // Make POST request to First Fly Travel API
        const response = await axios.post(`${FIRST_FLY_TRAVEL_API_ENDPOINT}/bookings`, body, { headers });

        // Return booking confirmation data
        res.json(response.data);
    } catch (error) {
        handleApiError(res, error);
    }
});

// API endpoint to get booking status
app.get('/api/booking-status/:bookingId', async (req, res) => {
    try {
        // Set API request headers
        const headers = {
            'Authorization': `Bearer ${FIRST_FLY_TRAVEL_API_KEY}`,
            'Content-Type': 'application/json'
        };

        // Make GET request to First Fly Travel API
        const response = await axios.get(`${FIRST_FLY_TRAVEL_API_ENDPOINT}/bookings/${req.params.bookingId}`, { headers });

        // Return booking status data
        res.json(response.data);
    } catch (error) {
        handleApiError(res, error);
    }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```

```javascript
// For testing, you can use the following code with Jest and Supertest
// flightBookingApi.test.js

const request = require('supertest');
const app = require('./app');

describe('Flight Booking API', () => {
    it('should get last-minute flights', async () => {
        const response = await request(app).get('/api/last-minute-flights?origin=JFK&destination=LAX&departureDate=2024-09-20');
        expect(response.status).toBe(200);
        expect(response.body).toBeInstanceOf(Object);
    });

    it('should book a flight', async () => {
        const response = await request(app).post('/api/book-flight').send({
            origin: 'JFK',
            destination: 'LAX',
            departureDate: '2024-09-20',
            flightId: 'FF12345'
        });
        expect(response.status).toBe(200);
        expect(response.body).toBeInstanceOf(Object);
    });

    it('should get booking status', async () => {
        const response = await request(app).get('/api/booking-status/BOOK12345');
        expect(response.status).toBe(200);
        expect(response.body).toBeInstanceOf(Object);
    });
});
```
