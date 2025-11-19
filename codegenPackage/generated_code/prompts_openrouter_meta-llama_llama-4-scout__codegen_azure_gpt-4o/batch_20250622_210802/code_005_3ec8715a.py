"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Create a code example that demonstrates how to use cookies for analytics purposes while respecting user consent preferences, as discussed in the context of the Masa application.
Generated: DETERMINISTIC_3ec8715a6068d497
Batch ID: 20250622_210802
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

# Generated Code:
# ===============

```javascript
// Import necessary modules (if using a framework like Express)
const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();
const PORT = 3000;

// Middleware to parse cookies
app.use(cookieParser());

// Middleware to serve static files (e.g., HTML for user consent)
app.use(express.static('public'));

// Function to check user consent from cookies
function hasUserConsent(req) {
  const consentCookie = req.cookies.analyticsConsent;
  return consentCookie === 'true';
}

// Route to handle user consent submission
app.post('/set-consent', express.json(), (req, res) => {
  const { consent } = req.body;

  if (typeof consent !== 'boolean') {
    return res.status(400).json({ error: 'Invalid consent value' });
  }

  // Set the consent cookie (expires in 1 year)
  res.cookie('analyticsConsent', consent, {
    httpOnly: true,
    secure: true,
    sameSite: 'Strict',
    maxAge: 365 * 24 * 60 * 60 * 1000, // 1 year in milliseconds
  });

  res.status(200).json({ message: 'Consent preference saved' });
});

// Route to demonstrate analytics tracking
app.get('/track', (req, res) => {
  if (!hasUserConsent(req)) {
    return res.status(403).json({ error: 'User has not consented to analytics' });
  }

  // Simulate analytics tracking (e.g., log data or send to analytics service)
  console.log('Tracking analytics data for user:', req.ip);

  res.status(200).json({ message: 'Analytics data tracked successfully' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

/*
 * Notes:
 * - Ensure the `public` folder contains a user interface for managing consent preferences.
 * - Use HTTPS in production to ensure secure cookie handling.
 * - This example assumes a simple consent model (true/false). For more complex scenarios, adapt accordingly.
 */
```
