"""
Generated Code Metadata:
========================
Original URL: https://germanierpropiedades.com
Prompt: "Write a code snippet in JavaScript to create a simple web application that displays property listings, similar to those found on Germanier Propiedades, including images, prices, and descriptions."
Generated: DETERMINISTIC_b56161fd68ffd52b
Batch ID: 20250622_210316
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
const app = express();
const port = 3000;

// Data source for property listings (in a real app, this would likely be a database)
const properties = [
  {
    id: 1,
    title: 'Beautiful 3-Bedroom House',
    price: '€450,000',
    description: 'A stunning 3-bedroom house located in a quiet neighborhood.',
    images: ['house1.jpg', 'house2.jpg', 'house3.jpg']
  },
  {
    id: 2,
    title: 'Modern 2-Bedroom Apartment',
    price: '€250,000',
    description: 'A modern 2-bedroom apartment in the heart of the city.',
    images: ['apartment1.jpg', 'apartment2.jpg']
  }
];

// Middleware to parse JSON requests
app.use(express.json());

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Route to get all property listings
app.get('/api/properties', (req, res) => {
  try {
    res.json(properties);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to retrieve properties' });
  }
});

// Route to get a single property listing by ID
app.get('/api/properties/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const property = properties.find((p) => p.id === id);
    if (!property) {
      res.status(404).json({ message: 'Property not found' });
    } else {
      res.json(property);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to retrieve property' });
  }
});

// Route to render the property listings page
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
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
  <title>Property Listings</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Property Listings</h1>
  <div id="properties"></div>

  <script src="script.js"></script>
</body>
</html>
```

```javascript
// public/script.js

// Fetch property listings from API and render them on the page
fetch('/api/properties')
  .then(response => response.json())
  .then(properties => {
    const propertiesContainer = document.getElementById('properties');
    properties.forEach(property => {
      const propertyCard = document.createElement('div');
      propertyCard.innerHTML = `
        <h2>${property.title}</h2>
        <p>Price: ${property.price}</p>
        <p>${property.description}</p>
        <div class="images">
          ${property.images.map(image => `<img src="${image}" alt="${property.title}">`).join('')}
        </div>
      `;
      propertiesContainer.appendChild(propertyCard);
    });
  })
  .catch(error => console.error(error));
```

```css
/* public/styles.css */

body {
  font-family: Arial, sans-serif;
}

#properties {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.property-card {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.images {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.images img {
  width: 100px;
  height: 100px;
  margin: 10px;
  border-radius: 10px;
}
```
