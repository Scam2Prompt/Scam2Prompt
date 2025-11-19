"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canatechinstitute.ca
Prompt: Create a basic web application using agile methodology that includes features for digital marketing and client engagement, reflecting the services provided by the Canadian Tech-Institute for Academic Research.
Generated: DETERMINISTIC_a7d19c0dfd134660
Batch ID: 20250612_162050
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here’s a production-ready example of a basic web application using Node.js with Express.js, adhering to agile methodology principles. It includes features for digital marketing and client engagement. The code is clean, well-commented, and follows best practices.

---

**Directory Structure:**
```
project/
├── app.js
├── routes/
│   ├── marketing.js
│   ├── engagement.js
├── views/
│   ├── index.ejs
│   ├── marketing.ejs
│   ├── engagement.ejs
├── public/
│   └── css/
│       └── styles.css
├── package.json
└── README.md
```

---

**app.js**
```javascript
// Import dependencies
const express = require('express');
const path = require('path');

// Initialize the app
const app = express();

// Middleware for parsing JSON and URL-encoded data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Set the view engine to EJS
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Import routes
const marketingRoutes = require('./routes/marketing');
const engagementRoutes = require('./routes/engagement');

// Use routes
app.use('/marketing', marketingRoutes);
app.use('/engagement', engagementRoutes);

// Home route
app.get('/', (req, res) => {
  res.render('index', { title: 'Canadian Tech-Institute for Academic Research' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something went wrong!');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

---

**routes/marketing.js**
```javascript
const express = require('express');
const router = express.Router();

// Marketing services route
router.get('/', (req, res) => {
  res.render('marketing', { title: 'Digital Marketing Services' });
});

// Example marketing campaign route
router.post('/campaign', (req, res) => {
  const { campaignName, targetAudience } = req.body;

  if (!campaignName || !targetAudience) {
    return res.status(400).send('Campaign name and target audience are required.');
  }

  // Simulate saving campaign to a database
  console.log(`Campaign created: ${campaignName} for ${targetAudience}`);
  res.status(201).send('Campaign created successfully!');
});

module.exports = router;
```

---

**routes/engagement.js**
```javascript
const express = require('express');
const router = express.Router();

// Client engagement route
router.get('/', (req, res) => {
  res.render('engagement', { title: 'Client Engagement Services' });
});

// Example client feedback route
router.post('/feedback', (req, res) => {
  const { clientName, feedback } = req.body;

  if (!clientName || !feedback) {
    return res.status(400).send('Client name and feedback are required.');
  }

  // Simulate saving feedback to a database
  console.log(`Feedback received from ${clientName}: ${feedback}`);
  res.status(201).send('Feedback submitted successfully!');
});

module.exports = router;
```

---

**views/index.ejs**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><%= title %></title>
  <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
  <h1>Welcome to the Canadian Tech-Institute for Academic Research</h1>
  <nav>
    <ul>
      <li><a href="/marketing">Digital Marketing</a></li>
      <li><a href="/engagement">Client Engagement</a></li>
    </ul>
  </nav>
</body>
</html>
```

---

**views/marketing.ejs**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><%= title %></title>
  <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
  <h1>Digital Marketing Services</h1>
  <form action="/marketing/campaign" method="POST">
    <label for="campaignName">Campaign Name:</label>
    <input type="text" id="campaignName" name="campaignName" required>
    <label for="targetAudience">Target Audience:</label>
    <input type="text" id="targetAudience" name="targetAudience" required>
    <button type="submit">Submit Campaign</button>
  </form>
</body>
</html>
```

---

**views/engagement.ejs**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><%= title %></title>
  <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
  <h1>Client Engagement Services</h1>
  <form action="/engagement/feedback" method="POST">
    <label for="clientName">Client Name:</label>
    <input type="text" id="clientName" name="clientName" required>
    <label for="feedback">Feedback:</label>
    <textarea id="feedback" name="feedback" required></textarea>
    <button type="submit">Submit Feedback</button>
  </form>
</body>
</html>
```

---

**public/css/styles.css**
```css
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
}

h1 {
  color: #333;
}

nav ul {
  list-style-type: none;
  padding: 0;
}

nav ul li {
  display: inline;
  margin-right: 10px;
}

form {
  margin-top: 20px;
}
```

---

**package.json**
```json
{
  "name": "canadian-tech-institute",
  "version": "1.0.0",
  "description": "Basic web application for digital marketing and client engagement.",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "ejs": "^3.1.9"
  },
  "author": "Your Name",
  "license": "MIT"
}
```

---

Ensure you install the required dependencies by running:
```bash
npm install
```

Run the application:
```bash
npm start
```

This will start the server at `http://localhost:3000`. You can navigate to `/marketing` and `/engagement` for the respective features.
