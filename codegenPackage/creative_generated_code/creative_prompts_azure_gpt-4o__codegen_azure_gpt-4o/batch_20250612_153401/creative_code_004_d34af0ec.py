"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-drago.vercel.app
Prompt: Provide an example of a serverless function in JavaScript that can be deployed on Vercel to handle API requests.
Generated: DETERMINISTIC_d34af0ecf4175c68
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// api/hello.js
// This serverless function handles API requests on Vercel.
// It responds with a simple JSON object containing a message.

module.exports = async (req, res) => {
  try {
    // Check the HTTP method
    if (req.method !== 'GET') {
      // If the method is not GET, return a 405 Method Not Allowed error
      res.status(405).json({ error: 'Method Not Allowed' });
      return;
    }

    // Respond with a JSON object
    res.status(200).json({
      message: 'Hello, world! This is a serverless function deployed on Vercel.',
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error handling request:', error);

    res.status(500).json({
      error: 'Internal Server Error',
    });
  }
};
```
