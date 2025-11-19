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
// Import necessary libraries
const express = require('express');
const geoip = require('geoip-lite');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to check user location
const locationMiddleware = (req, res, next) => {
    // Get the user's IP address from the request
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;

    // Lookup user's geographical location based on IP
    const geo = geoip.lookup(ip);

    // Check if the geo data is available
    if (!geo) {
        return res.status(403).json({ error: 'Location not found' });
    }

    // Define the restricted region (for example, restrict access to users from 'US')
    const restrictedRegion = 'US';

    // Check if the user's country is in the restricted region
    if (geo.country === restrictedRegion) {
        return res.status(403).json({ error: 'Access denied from your location' });
    }

    // Add geo data to the request object for further use
    req.geo = geo;
    
    // Proceed to the next middleware or route handler
    next();
};

// Use the location middleware for all routes
app.use(locationMiddleware);

// Example route
app.get('/', (req, res) => {
    res.send(`Welcome! Your location: ${req.geo.city}, ${req.geo.country}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
