"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://melon.io
Prompt: Provide an example of using medusa-plugin-ses to send emails via AWS SES in a Medusa eCommerce application.
Generated: DETERMINISTIC_b4a51ab6d3ee3e60
Batch ID: 20250612_150645
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8000": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:7000": {
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
const { Medusa } = require("@medusajs/medusa");
const SESPlugin = require("medusa-plugin-ses");

// Initialize Medusa server
const medusa = new Medusa({
  // Core Medusa configurations
  projectConfig: {
    database_url: "postgres://user:password@localhost:5432/medusa-db",
    database_type: "postgres",
    store_cors: "http://localhost:8000",
    admin_cors: "http://localhost:7000",
  },
  // Configure plugins
  plugins: [
    // AWS SES plugin configuration
    {
      resolve: "medusa-plugin-ses",
      options: {
        accessKeyId: process.env.AWS_SES_ACCESS_KEY_ID, // AWS Access Key ID (environment variable recommended)
        secretAccessKey: process.env.AWS_SES_SECRET_ACCESS_KEY, // AWS Secret Access Key (environment variable recommended)
        region: process.env.AWS_SES_REGION, // AWS Region (environment variable recommended)
        defaultFrom: "your-email@example.com", // Default sender email
      },
    },
  ],
});

// Example function to send an email using AWS SES
async function sendEmail() {
  try {
    // Get the SES service from the Medusa container
    const sesService = medusa.resolve("sesService");

    // Email parameters
    const emailParams = {
      to: ["recipient@example.com"], // Recipient email address(es)
      subject: "Welcome to Medusa!", // Email subject
      text: "Thank you for signing up for our store.", // Plain text body
      html: "<h1>Welcome to Medusa!</h1><p>Thank you for signing up for our store.</p>", // HTML body
    };

    // Send the email
    const response = await sesService.sendEmail(emailParams);

    console.log("Email sent successfully:", response);
  } catch (error) {
    // Log and handle errors
    console.error("Failed to send email:", error.message);
  }
}

// Start the Medusa server
medusa.start()
  .then(() => {
    console.log("Medusa server is running...");
    
    // Example usage of the email function
    sendEmail();
  })
  .catch((error) => {
    console.error("Failed to start Medusa server:", error.message);
  });
```
