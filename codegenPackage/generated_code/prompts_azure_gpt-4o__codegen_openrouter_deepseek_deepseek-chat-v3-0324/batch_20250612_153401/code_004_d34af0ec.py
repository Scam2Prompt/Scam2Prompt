"""
Generated Code Metadata:
========================
Original URL: https://meta-drago.vercel.app
Prompt: Provide an example of a serverless function in JavaScript that can be deployed on Vercel to handle API requests.
Generated: DETERMINISTIC_d34af0ecf4175c68
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// vercel-serverless-function.js
// Example of a serverless function for Vercel that handles API requests

/**
 * Handles incoming HTTP requests
 * @param {import('vercel').VercelRequest} req - The incoming request object
 * @param {import('vercel').VercelResponse} res - The response object
 */
module.exports = async (req, res) => {
  try {
    // Set CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    // Handle OPTIONS request for CORS preflight
    if (req.method === 'OPTIONS') {
      return res.status(200).end();
    }

    // Handle GET requests
    if (req.method === 'GET') {
      const { name = 'World' } = req.query;
      return res.status(200).json({
        message: `Hello ${name}`,
        timestamp: new Date().toISOString(),
        method: req.method
      });
    }

    // Handle POST requests
    if (req.method === 'POST') {
      const { name = 'World' } = req.body;
      return res.status(200).json({
        message: `Hello ${name}`,
        timestamp: new Date().toISOString(),
        method: req.method
      });
    }

    // Method not allowed
    return res.status(405).json({ error: 'Method Not Allowed' });
  } catch (error) {
    console.error('Error processing request:', error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
};
```
