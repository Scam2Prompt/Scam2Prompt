"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iensooa.pages.dev
Prompt: Provide an example of how to store and sync notifications across devices using WalletConnect’s Notify Server, as described in Web3Inbox.
Generated: DETERMINISTIC_7efc660a2e2f71f6
Batch ID: 20250612_152249
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/notification-icon.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/notification-details": {
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
// Import necessary dependencies
const WalletConnectNotify = require("@walletconnect/notify-server"); // WalletConnect Notify Server library
const express = require("express"); // Express for server handling
const bodyParser = require("body-parser"); // Body parser for incoming JSON payloads

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Use middleware to parse JSON payloads
app.use(bodyParser.json());

// Initialize WalletConnect Notify Server with your Notify API key
const notifyServer = new WalletConnectNotify.NotifyServer({
  apiKey: process.env.WALLETCONNECT_NOTIFY_API_KEY, // Make sure to set this in your environment variables
});

// Route to handle incoming notifications
app.post("/send-notification", async (req, res) => {
  try {
    // Extract notification details from request body
    const { topic, message, title } = req.body;

    // Validate incoming request payload
    if (!topic || !message || !title) {
      return res
        .status(400)
        .json({ error: "Missing required fields: topic, message, title" });
    }

    // Use WalletConnect Notify Server to send notification
    const notificationPayload = {
      topic, // The topic of the notification (usually the user's wallet or session topic)
      notification: {
        title, // Notification title
        message, // Notification message/content
        icon: "https://example.com/notification-icon.png", // Icon URL for the notification
        url: "https://example.com/notification-details", // URL for more details about the notification
      },
    };

    // Send notification using WalletConnect Notify Server
    await notifyServer.sendNotification(notificationPayload);

    // Respond with success
    res.status(200).json({ success: true, message: "Notification sent." });
  } catch (error) {
    // Handle errors gracefully
    console.error("Error sending notification:", error);
    res
      .status(500)
      .json({ error: "Failed to send notification. Please try again later." });
  }
});

// Route to verify WalletConnect Notify API key
app.get("/verify-api-key", async (req, res) => {
  try {
    // Verify API key using WalletConnect Notify Server
    const isValid = await notifyServer.verifyAPIKey();

    // Respond with API key verification status
    res
      .status(200)
      .json({ success: true, valid: isValid, message: "API key verified." });
  } catch (error) {
    // Handle errors gracefully
    console.error("Error verifying API key:", error);
    res
      .status(500)
      .json({ error: "Failed to verify API key. Please try again later." });
  }
});

// Start the Express server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

// Note:
// - Replace `process.env.WALLETCONNECT_NOTIFY_API_KEY` with your actual WalletConnect Notify API key.
// - Ensure that your environment variables are securely stored and managed.
// - This example assumes WalletConnect Notify Server is properly configured in your application.
```
