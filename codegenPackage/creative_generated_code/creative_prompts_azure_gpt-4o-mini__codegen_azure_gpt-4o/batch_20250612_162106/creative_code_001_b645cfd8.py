"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pegasus-staging.vercel.app
Prompt: What libraries can I use to detect user location and restrict access based on region in a Node.js application?
Generated: DETERMINISTIC_b645cfd8b34cf2df
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const express = require('express'); // Web framework for Node.js
const geoip = require('geoip-lite'); // Library for IP-based geolocation
const ip = require('ip'); // Library to handle IP addresses

// Initialize the Express application
const app = express();

// Define allowed regions
const allowedRegions = ['US', 'CA']; // Allowed countries - use ISO 3166-1 alpha-2 codes

// Middleware to detect user location and restrict access
app.use((req, res, next) => {
  try {
    // Extract the client's IP address
    const clientIp = req.headers['x-forwarded-for'] || req.connection.remoteAddress;

    // Get the geolocation information based on the IP address
    const geo = geoip.lookup(clientIp);

    // If geolocation data is available, check the region
    if (geo) {
      const userRegion = geo.country;

      // Restrict access based on region
      if (allowedRegions.includes(userRegion)) {
        next(); // Allow access
      } else {
        res.status(403).json({ message: 'Access restricted for your region.' }); // Forbidden response
      }
    } else {
      // If geolocation data is not found, deny access
      res.status(403).json({ message: 'Unable to determine your location. Access denied.' });
    }
  } catch (error) {
    // Handle unexpected errors
    console.error('Error in location detection middleware:', error);
    res.status(500).json({ message: 'Internal server error.' });
  }
});

// Example route
app.get('/', (req, res) => {
  res.send('Welcome to the region-restricted application!');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
 * Notes:
 * 1. Ensure that the 'geoip-lite' database is updated regularly for accurate geolocation data.
 *    Run `npm install geoip-lite` and update the database using `npm run geoip-lite-update`.
 * 2. If the application is deployed behind a proxy (e.g., Nginx), ensure the 'x-forwarded-for' header is properly set to the client's IP address.
 * 3. IP-based geolocation is not 100% accurate and may not work reliably for all cases.
 */
```
