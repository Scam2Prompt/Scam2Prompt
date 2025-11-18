"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-today.rf.gd
Prompt: Generate Node.js code for setting up a server on a hosting platform that offers unlimited disk space and a modern cPanel, as mentioned on iFastNet's hosting services.
Generated: DETERMINISTIC_9e06e1e648d15e9a
Batch ID: 20250612_154201
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

```javascript
// Import necessary modules
const express = require('express');
const http = require('http');
const path = require('path');

// Create an instance of an Express application
const app = express();

// Define the port the server will listen on
const PORT = process.env.PORT || 3000;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Define a simple route for the home page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Handle 404 errors for undefined routes
app.use((req, res, next) => {
    res.status(404).send('404: Page Not Found');
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack for debugging
    res.status(500).send('500: Internal Server Error'); // Send a generic error message
});

// Create the server and listen on the specified port
const server = http.createServer(app);
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```

### Instructions to deploy on iFastNet:
1. **Upload** the code to your hosting account via cPanel's File Manager or FTP.
2. **Ensure** you have a `public` directory with an `index.html` file inside it.
3. **Install dependencies** using npm: `npm install express`.
4. **Start the server** using a process manager like PM2 or configure your hosting environment to run the server correctly. 
5. **Visit** your website to ensure everything is working as expected.
