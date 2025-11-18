"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Develop a web application prototype for booking plumbing services, including options for emergency calls and specific services like pipe cleaning or asbestos removal, inspired by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_f29a6935cfe4e527
Batch ID: 20250612_154909
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here’s a prototype for a web application for booking plumbing services using Node.js (with Express.js) and a simple HTML frontend. This implementation uses best practices and is production-ready in terms of structure. Note: This is a basic prototype, and in production, you would add user authentication, database connections, and other features.

### File Structure:
```
- plumbing-app/
  - server.js
  - public/
    - index.html
    - style.css
```

---

#### `server.js` (Node.js Backend)
```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

// Initialize express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON and form data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files (HTML, CSS, etc.)
app.use(express.static(path.join(__dirname, 'public')));

// In-memory storage for bookings (replace with a real database in production)
const bookings = [];

// API Route: Get available services
app.get('/api/services', (req, res) => {
  const services = [
    { id: 1, name: 'Pipe Cleaning', description: 'Thorough cleaning of pipes to ensure optimal flow.' },
    { id: 2, name: 'Asbestos Removal', description: 'Safe removal of asbestos from your plumbing system.' },
    { id: 3, name: 'Emergency Plumbing', description: '24/7 emergency plumbing services.' },
  ];
  res.json(services);
});

// API Route: Submit a booking request
app.post('/api/book', (req, res) => {
  try {
    const { name, email, phone, serviceId, details, emergency } = req.body;

    // Validate input
    if (!name || !email || !phone || !serviceId) {
      return res.status(400).json({ error: 'All fields are required.' });
    }

    // Create a booking record
    const booking = {
      id: bookings.length + 1,
      name,
      email,
      phone,
      serviceId,
      details,
      emergency: emergency === 'true', // Convert string to boolean
      date: new Date(),
    };

    // Store the booking (replace this with database logic in production)
    bookings.push(booking);

    res.status(201).json({ message: 'Booking successfully created!', booking });
  } catch (error) {
    console.error('Error creating booking:', error);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

---

#### `public/index.html` (Frontend)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Plumbing Services Booking</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Book a Plumbing Service</h1>
  
  <form id="booking-form">
    <label for="name">Full Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" required>

    <label for="service">Select Service:</label>
    <select id="service" name="service" required>
      <option value="" disabled selected>Select a service</option>
    </select>

    <label for="details">Additional Details:</label>
    <textarea id="details" name="details"></textarea>

    <label for="emergency">Emergency Call:</label>
    <input type="checkbox" id="emergency" name="emergency">

    <button type="submit">Book Now</button>
  </form>

  <script>
    // Fetch available services and populate dropdown
    fetch('/api/services')
      .then(response => response.json())
      .then(services => {
        const serviceDropdown = document.getElementById('service');
        services.forEach(service => {
          const option = document.createElement('option');
          option.value = service.id;
          option.textContent = service.name;
          serviceDropdown.appendChild(option);
        });
      })
      .catch(error => console.error('Error fetching services:', error));

    // Submit booking form
    const form = document.getElementById('booking-form');
    form.addEventListener('submit', event => {
      event.preventDefault();

      const formData = new FormData(form);
      const data = Object.fromEntries(formData);

      fetch('/api/book', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
        .then(response => response.json())
        .then(result => {
          alert(result.message || 'Booking submitted!');
          form.reset();
        })
        .catch(error => console.error('Error submitting booking:', error));
    });
  </script>
</body>
</html>
```

---

#### `public/style.css` (Basic CSS for Styling)
```css
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f8f9fa;
}

h1 {
  text-align: center;
  margin-top: 20px;
}

form {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
}

label {
  display: block;
  margin-bottom: 8px;
}

input, select, textarea, button {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
```

---

This prototype includes a basic backend API for booking plumbing services, a frontend form for user input, and styling for the UI. It demonstrates clean, modular coding practices and proper error handling.
