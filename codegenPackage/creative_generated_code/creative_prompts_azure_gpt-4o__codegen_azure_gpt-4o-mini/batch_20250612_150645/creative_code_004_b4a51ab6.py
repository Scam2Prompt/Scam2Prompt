"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://melon.io
Prompt: Provide an example of using medusa-plugin-ses to send emails via AWS SES in a Medusa eCommerce application.
Generated: DETERMINISTIC_b4a51ab6d3ee3e60
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages
const { Medusa } = require("medusa-core-utils");
const { MedusaPlugin } = require("medusa-plugin"); // Import Medusa Plugin Base class
const AWS = require("aws-sdk"); // AWS SDK for SES

// Define the SES configuration
const sesConfig = {
  region: "us-east-1", // Change to your desired region
  accessKeyId: process.env.AWS_ACCESS_KEY_ID, // AWS Access Key ID
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY, // AWS Secret Access Key
};

// Create an instance of the SES service
const ses = new AWS.SES(sesConfig);

// Create a Medusa plugin class for SES
class MedusaPluginSES extends MedusaPlugin {
  constructor(options) {
    super();
    this.options = options || {};
  }

  // Method to send email
  async sendEmail({ to, subject, body }) {
    const params = {
      Destination: {
        ToAddresses: [to],
      },
      Message: {
        Body: {
          Text: { Data: body }, // Change to 'Html' if you want HTML emails
        },
        Subject: { Data: subject },
      },
      Source: process.env.SES_FROM_EMAIL, // Verified email in SES
    };

    try {
      // Send the email using SES sendEmail method
      const result = await ses.sendEmail(params).promise();
      console.log("Email sent:", result);
      return result; // Return result for further processing if needed
    } catch (error) {
      console.error("Error sending email:", error);
      throw new Error("Email could not be sent."); // Handle the error appropriately
    }
  }
}

// Export the Medusa plugin
module.exports = {
  plugin: (options) => new MedusaPluginSES(options),
};
```

This code snippet defines a Medusa plugin to send emails using AWS SES with proper error handling and configuration. Make sure to set the required environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `SES_FROM_EMAIL`) before running this code.
