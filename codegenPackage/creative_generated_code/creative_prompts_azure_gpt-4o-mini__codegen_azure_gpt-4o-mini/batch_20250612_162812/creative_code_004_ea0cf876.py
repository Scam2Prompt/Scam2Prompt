"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://melon.io
Prompt: Write a code snippet to configure the medusa-plugin-ses for sending emails in a Medusa server.
Generated: DETERMINISTIC_ea0cf8761dfbd051
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const { Medusa } = require("medusa-core-utils");
const SES = require("medusa-plugin-ses");

// Configuration for the AWS SES plugin
const sesConfig = {
  from_email: "your-email@example.com", // The email address you'd like to send from
  config: {
    region: "us-east-1", // AWS region for SES
    accessKeyId: process.env.AWS_ACCESS_KEY_ID, // AWS access key ID
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY, // AWS secret access key
  },
};

// Function to initialize Medusa server with SES plugin
const initializeMedusaServer = async () => {
  try {
    // Create a new Medusa instance
    const medusa = new Medusa({
      projectConfig: {
        // Add your project configuration here
      },
      plugins: [
        // Add the SES plugin to the Medusa server
        new SES(sesConfig),
      ],
    });

    // Start the Medusa server
    await medusa.start();
    console.log("Medusa server is running!");
  } catch (error) {
    // Handle errors during server initialization
    console.error("Error initializing Medusa server:", error.message);
    process.exit(1); // Exit process with failure
  }
};

// Execute the initialization function
initializeMedusaServer();
```

Make sure to replace `"your-email@example.com"` with the sender email address you wish to use, and set your AWS credentials as environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
