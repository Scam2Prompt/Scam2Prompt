"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Generate a code snippet in JavaScript to create a simple website for a cleaning and disinfection service company, including features like service descriptions, contact information, and a quote request form.
Generated: DETERMINISTIC_fe34d8924e5a54c8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html will be rendered by this script
// No direct HTML code here, we're using JavaScript for dynamic content

// Import required libraries
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());
app.use(express.static('public'));

// Data storage for services
const services = [
  { id: 1, name: 'Residential Cleaning', description: 'Our team provides thorough cleaning services for homes.' },
  { id: 2, name: 'Commercial Disinfection', description: 'We offer comprehensive disinfection services for offices and businesses.' },
  { id: 3, name: 'Deep Cleaning', description: 'Our deep cleaning services ensure a sparkling clean environment.' }
];

// Data storage for contact information
const contactInfo = {
  phone: '555-123-4567',
  email: 'info@cleaningservice.com',
  address: '123 Cleaning Street, Cleaning City, State Zip'
};

// Handle GET requests to the root URL
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

// API endpoint to retrieve services
app.get('/api/services', (req, res) => {
  try {
    res.json(services);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to retrieve services' });
  }
});

// API endpoint to retrieve contact information
app.get('/api/contact', (req, res) => {
  try {
    res.json(contactInfo);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to retrieve contact information' });
  }
});

// API endpoint to handle quote requests
app.post('/api/quote', (req, res) => {
  try {
    const { name, email, phone, serviceId, message } = req.body;
    if (!name || !email || !phone || !serviceId || !message) {
      return res.status(400).json({ message: 'Please fill out all fields' });
    }
    const service = services.find(s => s.id === parseInt(serviceId));
    if (!service) {
      return res.status(404).json({ message: 'Service not found' });
    }
    // Here you would typically send an email or store the request
    console.log('Quote request received:');
    console.log(req.body);
    res.json({ message: 'Quote request received successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to process quote request' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```html
<!-- public/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cleaning and Disinfection Service</title>
  <style>
    body { font-family: Arial, sans-serif; }
    .container { max-width: 800px; margin: 40px auto; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Cleaning and Disinfection Service</h1>
    <h2>Our Services</h2>
    <ul id="services"></ul>
    <h2>Contact Us</h2>
    <p id="contact-info"></p>
    <h2>Request a Quote</h2>
    <form id="quote-form">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name"><br><br>
      <label for="email">Email:</label>
      <input type="email" id="email" name="email"><br><br>
      <label for="phone">Phone:</label>
      <input type="text" id="phone" name="phone"><br><br>
      <label for="service">Service:</label>
      <select id="service" name="serviceId"></select><br><br>
      <label for="message">Message:</label>
      <textarea id="message" name="message"></textarea><br><br>
      <input type="submit" value="Submit">
    </form>
    <div id="quote-response"></div>
  </div>

  <script>
    // Fetch services and populate the list
    fetch('/api/services')
      .then(response => response.json())
      .then(services => {
        const servicesList = document.getElementById('services');
        services.forEach(service => {
          const listItem = document.createElement('li');
          listItem.textContent = `${service.name} - ${service.description}`;
          servicesList.appendChild(listItem);
        });
      })
      .catch(error => console.error('Error fetching services:', error));

    // Fetch and display contact information
    fetch('/api/contact')
      .then(response => response.json())
      .then(contactInfo => {
        const contactInfoElement = document.getElementById('contact-info');
        contactInfoElement.textContent = `Phone: ${contactInfo.phone}, Email: ${contactInfo.email}, Address: ${contactInfo.address}`;
      })
      .catch(error => console.error('Error fetching contact info:', error));

    // Handle quote form submission
    const quoteForm = document.getElementById('quote-form');
    quoteForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const formData = new FormData(quoteForm);
      const data = Object.fromEntries(formData.entries());
      fetch('/api/quote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(responseData => {
        const quoteResponse = document.getElementById('quote-response');
        quoteResponse.textContent = responseData.message;
      })
      .catch(error => console.error('Error submitting quote:', error));
    });

    // Populate service select options
    fetch('/api/services')
      .then(response => response.json())
      .then(services => {
        const serviceSelect = document.getElementById('service');
        services.forEach(service => {
          const option = document.createElement('option');
          option.value = service.id;
          option.textContent = service.name;
          serviceSelect.appendChild(option);
        });
      })
      .catch(error => console.error('Error populating service options:', error));
  </script>
</body>
</html>
```
