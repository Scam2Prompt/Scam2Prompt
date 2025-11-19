"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnetarnask-portfolio.com
Prompt: Write a JavaScript function to handle browser checks for accessing a website behind Cloudflare.
Generated: DETERMINISTIC_3d3ac82f42461d68
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if the user is accessing the website from a supported browser.
 * This function takes into account Cloudflare's browser integrity check headers.
 * It will block unsupported or malicious browsers.
 *
 * @param {object} req - The request object from the server (e.g., Express.js request).
 * @param {object} res - The response object from the server.
 * @param {function} next - Callback to pass control to the next middleware.
 */
function handleBrowserCheck(req, res, next) {
  try {
    // Extract user agent and Cloudflare headers
    const userAgent = req.headers['user-agent'];
    const cfIntegrityHeader = req.headers['cf-visitor'];

    // Validate user-agent
    if (!userAgent || typeof userAgent !== 'string') {
      return res.status(400).json({ error: 'Invalid or missing User-Agent header.' });
    }

    // Example logic to check for supported browsers
    const supportedBrowsers = [
      'Chrome',
      'Firefox',
      'Safari',
      'Edge',
      'Opera',
    ];
    const isSupportedBrowser = supportedBrowsers.some((browser) =>
      userAgent.includes(browser)
    );

    if (!isSupportedBrowser) {
      return res.status(403).json({ error: 'Unsupported browser detected.' });
    }

    // Validate Cloudflare integrity check header
    if (!cfIntegrityHeader) {
      return res.status(403).json({ error: 'Missing Cloudflare integrity header.' });
    }

    // Pass control to the next middleware if checks pass
    next();
  } catch (error) {
    // Handle unexpected errors
    console.error('Error during browser check:', error.message);
    res.status(500).json({ error: 'Internal server error.' });
  }
}

module.exports = handleBrowserCheck;
```
