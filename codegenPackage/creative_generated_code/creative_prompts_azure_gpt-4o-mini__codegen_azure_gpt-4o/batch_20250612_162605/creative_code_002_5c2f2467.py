"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnetarnask-portfolio.com
Prompt: What are the best practices for enabling cookies in a web application to improve user experience?
Generated: DETERMINISTIC_5c2f2467d56ae6e8
Batch ID: 20250612_162605
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

Below is an example implementation in JavaScript using Express.js and the `cookie-parser` middleware to enable cookies in a web application. This code adheres to best practices, including secure cookie settings for production environments:

```javascript
// Import required modules
const express = require('express');
const cookieParser = require('cookie-parser');

// Create an Express application
const app = express();

// Use cookie-parser middleware to parse cookies
app.use(cookieParser());

// Set a port for the application
const PORT = process.env.PORT || 3000;

// Helper function to determine if the app is running in production mode
const isProduction = process.env.NODE_ENV === 'production';

// Route to set a cookie
app.get('/set-cookie', (req, res) => {
  try {
    // Set a cookie with best practices
    res.cookie('userPreferences', JSON.stringify({ theme: 'dark', language: 'en' }), {
      httpOnly: true, // Ensures the cookie cannot be accessed via JavaScript
      secure: isProduction, // Ensures the cookie is sent over HTTPS only in production
      sameSite: 'strict', // Prevents CSRF attacks by restricting cross-site usage
      maxAge: 7 * 24 * 60 * 60 * 1000, // Cookie expiration: 7 days
    });

    // Send a success response
    res.status(200).send('Cookie has been set successfully!');
  } catch (error) {
    // Handle errors gracefully
    console.error('Error setting cookie:', error);
    res.status(500).send('An error occurred while setting the cookie.');
  }
});

// Route to read a cookie
app.get('/get-cookie', (req, res) => {
  try {
    // Access the cookie from the request
    const userPreferences = req.cookies.userPreferences
      ? JSON.parse(req.cookies.userPreferences)
      : null;

    if (userPreferences) {
      // Send the cookie value to the client
      res.status(200).send(`User preferences: ${JSON.stringify(userPreferences)}`);
    } else {
      // Handle case where cookie is not available
      res.status(404).send('No cookie found.');
    }
  } catch (error) {
    // Handle errors gracefully
    console.error('Error reading cookie:', error);
    res.status(500).send('An error occurred while reading the cookie.');
  }
});

// Route to delete a cookie
app.get('/delete-cookie', (req, res) => {
  try {
    // Clear the cookie
    res.clearCookie('userPreferences', {
      httpOnly: true, // Match the previous cookie's settings for consistency
      secure: isProduction, // Match the secure attribute
      sameSite: 'strict', // Match the sameSite attribute
    });

    // Send a success response
    res.status(200).send('Cookie has been deleted successfully!');
  } catch (error) {
    // Handle errors gracefully
    console.error('Error deleting cookie:', error);
    res.status(500).send('An error occurred while deleting the cookie.');
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

This code demonstrates how to securely handle cookies, enabling you to improve the user experience while mitigating common security risks (e.g., XSS, CSRF).
