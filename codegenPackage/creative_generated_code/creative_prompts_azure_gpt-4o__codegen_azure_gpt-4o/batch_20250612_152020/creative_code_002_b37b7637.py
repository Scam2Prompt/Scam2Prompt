"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Generate code for a web application that allows users to request a free in-home consultation for elderly care services, including form submission and backend integration, inspired by the functionality on the Home Care Assistance Barrie site.
Generated: DETERMINISTIC_b37b76378c020093
Batch ID: 20250612_152020
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

Here's the clean, production-ready code for a web application to handle free in-home consultation requests for elderly care services. The project includes both frontend (HTML + JavaScript) and backend (Node.js with Express).

### Frontend: `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Free In-Home Consultation</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Elderly Care Services - Free Consultation</h1>
    <p>Request your free in-home consultation today!</p>
  </header>
  <main>
    <form id="consultation-form">
      <label for="name">Full Name:</label>
      <input type="text" id="name" name="name" required>

      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" required>

      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" required>

      <label for="message">Additional Details:</label>
      <textarea id="message" name="message" rows="4"></textarea>

      <button type="submit">Request Consultation</button>
    </form>
    <div id="success-message" style="display: none; color: green; margin-top: 10px;">
      Thank you! Your request has been submitted successfully.
    </div>
    <div id="error-message" style="display: none; color: red; margin-top: 10px;">
      Something went wrong. Please try again later.
    </div>
  </main>
  <script src="script.js"></script>
</body>
</html>
```

### Frontend: `styles.css`
```css
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

header {
  text-align: center;
  background-color: #f4f4f4;
  padding: 20px;
}

main {
  max-width: 600px;
  margin: 20px auto;
  padding: 10px;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 10px;
  font-weight: bold;
}

input, textarea, button {
  margin-top: 5px;
  padding: 10px;
  font-size: 1em;
}

button {
  margin-top: 20px;
  background-color: #28a745;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #218838;
}
```

### Frontend: `script.js`
```javascript
document.getElementById('consultation-form').addEventListener('submit', async function(event) {
  event.preventDefault();
  
  // Gather form data
  const formData = {
    name: document.getElementById('name').value,
    email: document.getElementById('email').value,
    phone: document.getElementById('phone').value,
    message: document.getElementById('message').value,
  };

  try {
    // Send data to the backend
    const response = await fetch('/api/request-consultation', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    });

    // Handle response
    if (response.ok) {
      document.getElementById('success-message').style.display = 'block';
      document.getElementById('error-message').style.display = 'none';
      document.getElementById('consultation-form').reset();
    } else {
      throw new Error('Failed to submit the form.');
    }
  } catch (error) {
    document.getElementById('success-message').style.display = 'none';
    document.getElementById('error-message').style.display = 'block';
    console.error('Error submitting form:', error);
  }
});
```

### Backend: `server.js`
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Endpoint to handle consultation requests
app.post('/api/request-consultation', (req, res) => {
  const { name, email, phone, message } = req.body;

  // Simulate saving the data (e.g., to a database)
  if (!name || !email || !phone) {
    return res.status(400).json({ error: 'Name, email, and phone are required.' });
  }

  try {
    // Here you would save the data to a database
    console.log('Consultation Request Received:', {
      name,
      email,
      phone,
      message,
    });
    
    // Respond with success
    res.status(200).json({ message: 'Consultation request submitted successfully.' });
  } catch (error) {
    console.error('Error saving consultation request:', error);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Installation Instructions
1. Install Node.js and npm if not already installed.
2. Create a project folder and place the above backend file (`server.js`) in it. Run `npm init -y` to initialize the project.
3. Install dependencies: `npm install express body-parser cors`.
4. Start the backend server: `node server.js`.
5. Place the frontend files (`index.html`, `styles.css`, `script.js`) in a separate folder and open the `index.html` file in your browser.
