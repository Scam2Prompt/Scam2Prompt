"""
Generated Code Metadata:
========================
Original URL: https://www.fareobuddy.com
Prompt: Construct a REST API endpoint in Node.js that provides a list of available flights and hotels based on user preferences, such as one-way flights or multicity itineraries.
Generated: DETERMINISTIC_0efd3f35821ca4e8
Batch ID: 20250612_164010
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
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Mock database for flights and hotels
const flightsDB = [
    {
        id: uuidv4(),
        type: 'one-way',
        origin: 'JFK',
        destination: 'LAX',
        departureDate: '2023-12-25',
        price: 299,
        airline: 'Delta'
    },
    {
        id: uuidv4(),
        type: 'round-trip',
        origin: 'LAX',
        destination: 'JFK',
        departureDate: '2023-12-25',
        returnDate: '2024-01-05',
        price: 499,
        airline: 'American'
    },
    {
        id: uuidv4(),
        type: 'multicity',
        origin: 'JFK',
        destination: 'SFO',
        departureDate: '2023-12-25',
        nextOrigin: 'SFO',
        nextDestination: 'LAX',
        nextDepartureDate: '2023-12-28',
        price: 799,
        airline: 'United'
    }
];

const hotelsDB = [
    {
        id: uuidv4(),
        name: 'Grand Hyatt',
        location: 'New York',
        checkInDate: '2023-12-25',
        checkOutDate: '2023-12-30',
        pricePerNight: 250,
        rating: 4.5
    },
    {
        id: uuidv4(),
        name: 'Ritz Carlton',
        location: 'Los Angeles',
        checkInDate: '2023-12-25',
        checkOutDate: '2023-12-30',
        pricePerNight: 350,
        rating: 4.8
    },
    {
        id: uuidv4(),
        name: 'Fairmont',
        location: 'San Francisco',
        checkInDate: '2023-12-25',
        checkOutDate: '2023-12-30',
        pricePerNight: 300,
        rating: 4.6
    }
];

/**
 * GET /api/flights
 * Query params:
 * - type: one-way, round-trip, multicity
 * - origin: origin airport code
 * - destination: destination airport code
 * - departureDate: YYYY-MM-DD
 * - returnDate: YYYY-MM-DD (for round-trip)
 */
app.get('/api/flights', (req, res) => {
    try {
        const { type, origin, destination, departureDate, returnDate } = req.query;

        let filteredFlights = [...flightsDB];

        if (type) {
            filteredFlights = filteredFlights.filter(flight => flight.type === type);
        }

        if (origin) {
            filteredFlights = filteredFlights.filter(flight => flight.origin === origin.toUpperCase());
        }

        if (destination) {
            filteredFlights = filteredFlights.filter(flight => flight.destination === destination.toUpperCase());
        }

        if (departureDate) {
            filteredFlights = filteredFlights.filter(flight => flight.departureDate === departureDate);
        }

        if (returnDate && type === 'round-trip') {
            filteredFlights = filteredFlights.filter(flight => flight.returnDate === returnDate);
        }

        if (filteredFlights.length === 0) {
            return res.status(404).json({ message: 'No flights found matching your criteria' });
        }

        res.json(filteredFlights);
    } catch (error) {
        console.error('Error fetching flights:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

/**
 * GET /api/hotels
 * Query params:
 * - location: city name
 * - checkInDate: YYYY-MM-DD
 * - checkOutDate: YYYY-MM-DD
 */
app.get('/api/hotels', (req, res) => {
    try {
        const { location, checkInDate, checkOutDate } = req.query;

        let filteredHotels = [...hotelsDB];

        if (location) {
            filteredHotels = filteredHotels.filter(hotel => 
                hotel.location.toLowerCase().includes(location.toLowerCase())
            );
        }

        if (checkInDate) {
            filteredHotels = filteredHotels.filter(hotel => hotel.checkInDate === checkInDate);
        }

        if (checkOutDate) {
            filteredHotels = filteredHotels.filter(hotel => hotel.checkOutDate === checkOutDate);
        }

        if (filteredHotels.length === 0) {
            return res.status(404).json({ message: 'No hotels found matching your criteria' });
        }

        res.json(filteredHotels);
    } catch (error) {
        console.error('Error fetching hotels:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
    res.json({ status: 'OK' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
