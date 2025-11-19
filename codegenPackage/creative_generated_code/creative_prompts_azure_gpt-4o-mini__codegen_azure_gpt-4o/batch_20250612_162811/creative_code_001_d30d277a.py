"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbiturm.today
Prompt: "Write a code snippet to integrate Cloudflare's security features into a Node.js application."
Generated: DETERMINISTIC_d30d277ac4655f39
Batch ID: 20250612_162811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/zones/${CLOUDFLARE_ZONE_ID}/firewall/waf/packages`,": {
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
// Import required modules
const express = require('express'); // Express for handling HTTP requests
const helmet = require('helmet'); // Helmet for securing HTTP headers
const axios = require('axios'); // Axios for making HTTP requests to Cloudflare API
const dotenv = require('dotenv'); // dotenv for managing sensitive configuration variables

// Load environment variables from .env file
dotenv.config();

// Initialize the Express application
const app = express();

// Middleware: Use Helmet to secure HTTP headers
app.use(helmet());

// Middleware: Parse incoming JSON requests
app.use(express.json());

// Cloudflare API credentials from environment variables
const CLOUDFLARE_API_KEY = process.env.CLOUDFLARE_API_KEY; // Cloudflare API key
const CLOUDFLARE_EMAIL = process.env.CLOUDFLARE_EMAIL; // Cloudflare account email
const CLOUDFLARE_ZONE_ID = process.env.CLOUDFLARE_ZONE_ID; // Cloudflare zone ID

// Validate Cloudflare API credentials
if (!CLOUDFLARE_API_KEY || !CLOUDFLARE_EMAIL || !CLOUDFLARE_ZONE_ID) {
  console.error('Missing required Cloudflare API credentials in environment variables.');
  process.exit(1); // Exit the application with error code
}

// Function to enable Cloudflare's Web Application Firewall (WAF)
const enableWAF = async () => {
  try {
    // Make an API request to Cloudflare to fetch WAF settings
    const response = await axios.patch(
      `https://api.cloudflare.com/client/v4/zones/${CLOUDFLARE_ZONE_ID}/firewall/waf/packages`,
      {
        mode: 'block', // Set WAF mode to block malicious traffic
      },
      {
        headers: {
          'X-Auth-Email': CLOUDFLARE_EMAIL, // Authenticate with Cloudflare account email
          'X-Auth-Key': CLOUDFLARE_API_KEY, // Authenticate with Cloudflare API key
          'Content-Type': 'application/json', // Set content type to JSON
        },
      }
    );

    if (response.data.success) {
      console.log('Cloudflare WAF successfully enabled.');
    } else {
      console.error('Failed to enable Cloudflare WAF:', response.data.errors);
    }
  } catch (error) {
    console.error('Error enabling Cloudflare WAF:', error.message);
  }
};

// Route: Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).send('Application is running securely.');
});

// Start the server and enable Cloudflare WAF
const PORT = process.env.PORT || 3000; // Port number from environment variable or default to 3000
app.listen(PORT, async () => {
  console.log(`Server is running on port ${PORT}`);
  await enableWAF(); // Enable WAF when server starts
});
```

**Notes for Production:**
- Ensure you have a `.env` file containing the required Cloudflare credentials:
  ```
  CLOUDFLARE_API_KEY=your-api-key
  CLOUDFLARE_EMAIL=your-cloudflare-email
  CLOUDFLARE_ZONE_ID=your-zone-id
  PORT=3000
  ```
- Install required dependencies with:
  ```
  npm install express helmet axios dotenv
  ```
