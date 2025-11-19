"""
Generated Code Metadata:
========================
Original URL: https://dunhill-servicedapartments.com
Prompt: Generate a RESTful API endpoint using Node.js and Express to handle booking requests for serviced apartments, including endpoints for listing apartments, viewing apartment details, and submitting booking inquiries.
Generated: DETERMINISTIC_b997873b7ad7c395
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database (replace with actual database in production)
let apartments = [
    {
        id: '1',
        title: 'Luxury Apartment Downtown',
        description: 'Spacious 2-bedroom apartment with city views',
        bedrooms: 2,
        bathrooms: 2,
        maxGuests: 4,
        pricePerNight: 150,
        amenities: ['WiFi', 'Kitchen', 'TV', 'Washer'],
        location: 'Downtown',
        images: ['image1.jpg', 'image2.jpg']
    },
    {
        id: '2',
        title: 'Cozy Studio Near Beach',
        description: 'Charming studio apartment steps from the beach',
        bedrooms: 1,
        bathrooms: 1,
        maxGuests: 2,
        pricePerNight: 90,
        amenities: ['WiFi', 'Kitchenette', 'TV'],
        location: 'Beachfront',
        images: ['image3.jpg']
    }
];

let bookings = [];

// Helper function to validate booking data
const validateBooking = (booking) => {
    if (!booking.apartmentId) return 'Apartment ID is required';
    if (!booking.guestName) return 'Guest name is required';
    if (!booking.guestEmail) return 'Guest email is required';
    if (!booking.checkInDate) return 'Check-in date is required';
    if (!booking.checkOutDate) return 'Check-out date is required';
    if (!booking.numberOfGuests) return 'Number of guests is required';
    if (new Date(booking.checkOutDate) <= new Date(booking.checkInDate)) {
        return 'Check-out date must be after check-in date';
    }
    return null;
};

// Routes

// Get all apartments
app.get('/api/apartments', (req, res) => {
    try {
        res.status(200).json(apartments);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch apartments' });
    }
});

// Get apartment by ID
app.get('/api/apartments/:id', (req, res) => {
    try {
        const apartment = apartments.find(a => a.id === req.params.id);
        if (!apartment) {
            return res.status(404).json({ error: 'Apartment not found' });
        }
        res.status(200).json(apartment);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch apartment details' });
    }
});

// Submit a booking inquiry
app.post('/api/bookings', (req, res) => {
    try {
        const error = validateBooking(req.body);
        if (error) {
            return res.status(400).json({ error });
        }

        const apartment = apartments.find(a => a.id === req.body.apartmentId);
        if (!apartment) {
            return res.status(404).json({ error: 'Apartment not found' });
        }

        if (req.body.numberOfGuests > apartment.maxGuests) {
            return res.status(400).json({ error: 'Number of guests exceeds maximum capacity' });
        }

        const booking = {
            id: uuidv4(),
            apartmentId: req.body.apartmentId,
            guestName: req.body.guestName,
            guestEmail: req.body.guestEmail,
            checkInDate: req.body.checkInDate,
            checkOutDate: req.body.checkOutDate,
            numberOfGuests: req.body.numberOfGuests,
            specialRequests: req.body.specialRequests || '',
            status: 'pending',
            createdAt: new Date().toISOString()
        };

        bookings.push(booking);
        res.status(201).json(booking);
    } catch (error) {
        res.status(500).json({ error: 'Failed to create booking' });
    }
});

// Get all bookings (for admin purposes)
app.get('/api/bookings', (req, res) => {
    try {
        res.status(200).json(bookings);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch bookings' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
