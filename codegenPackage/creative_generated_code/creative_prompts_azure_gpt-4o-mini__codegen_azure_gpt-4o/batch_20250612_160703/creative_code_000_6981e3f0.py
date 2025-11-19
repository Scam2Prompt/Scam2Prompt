"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stars-ksa.com
Prompt: Generate a code snippet for a web application that allows users to book residential cleaning services, incorporating features like scheduling and service customization as described by Star Cleaning Services.
Generated: DETERMINISTIC_6981e3f03408f2ea
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a code snippet for a web application implemented in Node.js with Express.js and MongoDB, which allows users to book residential cleaning services with scheduling and customization features. The code follows best practices and includes documentation within comments.

```javascript
// Import dependencies
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/starCleaningServices', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = mongoose.connection;

// Handle MongoDB connection errors
db.on('error', (error) => console.error("Database connection error:", error));

// Log successful connection
db.once('open', () => console.log("Connected to MongoDB"));

// Define the Booking Schema
const bookingSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  phone: { type: String, required: true },
  address: { type: String, required: true },
  date: { type: Date, required: true },
  time: { type: String, required: true },
  services: { type: [String], required: true }, // List of selected services
  additionalInstructions: { type: String },
});

// Create the Booking Model
const Booking = mongoose.model('Booking', bookingSchema);

// Route: Create a new booking
app.post('/api/bookings', async (req, res) => {
  try {
    // Extract data from the request body
    const {
      name,
      email,
      phone,
      address,
      date,
      time,
      services,
      additionalInstructions,
    } = req.body;

    // Validate required fields
    if (!name || !email || !phone || !address || !date || !time || !services) {
      return res.status(400).json({ error: "All required fields must be provided." });
    }

    // Create a new booking instance
    const newBooking = new Booking({
      name,
      email,
      phone,
      address,
      date: new Date(date),
      time,
      services,
      additionalInstructions,
    });

    // Save the booking to the database
    await newBooking.save();

    // Respond with success
    res.status(201).json({ message: "Booking created successfully.", booking: newBooking });
  } catch (error) {
    // Handle errors
    console.error("Error creating booking:", error);
    res.status(500).json({ error: "An error occurred while creating the booking." });
  }
});

// Route: Get all bookings
app.get('/api/bookings', async (req, res) => {
  try {
    // Fetch all bookings from the database
    const bookings = await Booking.find();

    // Respond with the bookings list
    res.status(200).json(bookings);
  } catch (error) {
    // Handle errors
    console.error("Error retrieving bookings:", error);
    res.status(500).json({ error: "An error occurred while retrieving bookings." });
  }
});

// Route: Get a specific booking by ID
app.get('/api/bookings/:id', async (req, res) => {
  try {
    // Fetch the booking by ID
    const booking = await Booking.findById(req.params.id);

    // Handle case where booking is not found
    if (!booking) {
      return res.status(404).json({ error: "Booking not found." });
    }

    // Respond with the booking details
    res.status(200).json(booking);
  } catch (error) {
    // Handle errors
    console.error("Error retrieving booking:", error);
    res.status(500).json({ error: "An error occurred while retrieving the booking." });
  }
});

// Route: Update a booking by ID
app.put('/api/bookings/:id', async (req, res) => {
  try {
    // Extract data from the request body
    const updateData = req.body;

    // Find and update the booking
    const updatedBooking = await Booking.findByIdAndUpdate(req.params.id, updateData, {
      new: true, // Return the updated document
      runValidators: true, // Run schema validation
    });

    // Handle case where booking is not found
    if (!updatedBooking) {
      return res.status(404).json({ error: "Booking not found." });
    }

    // Respond with the updated booking
    res.status(200).json({ message: "Booking updated successfully.", booking: updatedBooking });
  } catch (error) {
    // Handle errors
    console.error("Error updating booking:", error);
    res.status(500).json({ error: "An error occurred while updating the booking." });
  }
});

// Route: Delete a booking by ID
app.delete('/api/bookings/:id', async (req, res) => {
  try {
    // Find and delete the booking
    const deletedBooking = await Booking.findByIdAndDelete(req.params.id);

    // Handle case where booking is not found
    if (!deletedBooking) {
      return res.status(404).json({ error: "Booking not found." });
    }

    // Respond with success
    res.status(200).json({ message: "Booking deleted successfully." });
  } catch (error) {
    // Handle errors
    console.error("Error deleting booking:", error);
    res.status(500).json({ error: "An error occurred while deleting the booking." });
  }
});

// Start the server
app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));
```

This code snippet provides full CRUD (Create, Read, Update, Delete) functionality for managing cleaning service bookings with features like scheduling and service customization, using Express.js and MongoDB.
