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
// Import necessary packages
const Medusa = require("medusa");
const ResendPlugin = require("medusa-plugin-resend");

// Create a configuration function to set up Medusa with Resend plugin
const configureMedusa = async () => {
  try {
    // Initialize Medusa server
    const medusa = new Medusa({
      // Configuration options for Medusa
      projectConfig: {
        database: {
          type: "postgres",
          url: process.env.DATABASE_URL, // Database connection URL from environment variable
        },
        // Other Medusa configurations can be added here
      },
      // Add plugins to the Medusa server
      plugins: [
        // Configure Resend plugin for transactional email delivery
        new ResendPlugin({
          apiKey: process.env.RESEND_API_KEY, // Resend API Key from environment variable
          fromEmail: process.env.FROM_EMAIL,  // Email address to send emails from
        }),
      ],
    });

    // Start the Medusa server
    await medusa.start();
    console.log("Medusa server is running with Resend plugin for transactional emails.");

  } catch (error) {
    // Handle errors during configuration or server start
    console.error("Error configuring Medusa:", error);
    process.exit(1); // Exit the process with failure
  }
};

// Run the configuration function
configureMedusa();
```

Make sure to set the following environment variables before running the script:
- `DATABASE_URL`: Your PostgreSQL database connection string.
- `RESEND_API_KEY`: Your API key for Resend.
- `FROM_EMAIL`: The email address from which you want to send transactional emails.
