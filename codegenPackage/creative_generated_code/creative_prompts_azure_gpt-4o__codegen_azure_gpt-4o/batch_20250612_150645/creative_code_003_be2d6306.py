"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://melon.io
Prompt: Write a configuration script to set up medusa-plugin-resend for transactional email delivery in a Medusa eCommerce server.
Generated: DETERMINISTIC_be2d63069e79f064
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Medusa Plugin Configuration Script for medusa-plugin-resend
// This script sets up the medusa-plugin-resend to enable transactional email delivery in a Medusa eCommerce server.
// Ensure you have installed the plugin with: `npm install medusa-plugin-resend` or `yarn add medusa-plugin-resend`.

const dotenv = require("dotenv");

// Load environment variables from a `.env` file into `process.env`.
dotenv.config();

module.exports = {
  // Medusa server plugins configuration
  plugins: [
    {
      resolve: "medusa-plugin-resend",
      options: {
        // Resend API key used for authentication
        api_key: process.env.RESEND_API_KEY, // Store your Resend API key in the environment variable `RESEND_API_KEY`.

        // Optional: Default "from" email address for transactional emails
        default_from: process.env.RESEND_DEFAULT_FROM || "your-email@example.com",

        // Optional: Reply-to email address for transactional emails
        default_reply_to: process.env.RESEND_DEFAULT_REPLY_TO || "reply-to@example.com",
      },
    },
    // Include other plugins your Medusa server uses here
  ],
};

// Error handling: Ensure necessary environment variables are set.
if (!process.env.RESEND_API_KEY) {
  console.error("Error: RESEND_API_KEY is not defined in the environment variables.");
  process.exit(1); // Exit the process with an error code if API key is missing.
}
```
