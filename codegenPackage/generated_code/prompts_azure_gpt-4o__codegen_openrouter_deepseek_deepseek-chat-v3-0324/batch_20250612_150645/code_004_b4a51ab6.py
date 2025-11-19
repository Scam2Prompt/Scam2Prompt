"""
Generated Code Metadata:
========================
Original URL: https://melon.io
Prompt: Provide an example of using medusa-plugin-ses to send emails via AWS SES in a Medusa eCommerce application.
Generated: DETERMINISTIC_b4a51ab6d3ee3e60
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// medusa-config.js
const { 
  MedusaSesPlugin, 
  PluginOptions 
} = require("medusa-plugin-ses");

const plugins = [
  {
    resolve: MedusaSesPlugin,
    options: {
      access_key_id: process.env.AWS_SES_ACCESS_KEY_ID,
      secret_access_key: process.env.AWS_SES_SECRET_ACCESS_KEY,
      region: process.env.AWS_SES_REGION,
      from: process.env.AWS_SES_FROM_EMAIL,
      enable_endpoint: true,
      template_path: "email-templates/",
      order_placed_template: "order-placed.html",
      order_shipped_template: "order-shipped.html",
      customer_password_reset_template: "password-reset.html",
      test_mode: process.env.NODE_ENV === "development"
    } 
  }
];

module.exports = { plugins };

// email-templates/order-placed.html
<!DOCTYPE html>
<html>
<head>
  <title>Order Confirmation</title>
</head>
<body>
  <h1>Thank you for your order!</h1>
  <p>Your order #{{order.id}} has been received.</p>
  <p>Total: {{order.total}}</p>
</body>
</html>

// services/email.service.js
class EmailService {
  constructor({ notificationService }) {
    this.notificationService_ = notificationService;
  }

  async sendOrderConfirmation(orderId) {
    try {
      await this.notificationService_.sendNotification(
        "order.placed", 
        { 
          id: orderId,
          to: "customer@example.com",
          data: { order: { id: orderId, total: "$100.00" } }
        }
      );
    } catch (error) {
      console.error("Failed to send order confirmation email:", error);
      throw error;
    }
  }

  async sendPasswordReset(email, token) {
    try {
      await this.notificationService_.sendNotification(
        "customer.password_reset",
        {
          to: email,
          data: { token }
        }
      );
    } catch (error) {
      console.error("Failed to send password reset email:", error);
      throw error;
    }
  }
}

module.exports = EmailService;

// index.js (Medusa entry point)
const { Medusa } = require("@medusajs/medusa");
const EmailService = require("./services/email.service");

async function bootstrap() {
  const medusa = new Medusa({
    config: require("./medusa-config")
  });

  await medusa.start();

  const emailService = new EmailService({
    notificationService: medusa.services.notificationService
  });

  // Example usage
  await emailService.sendOrderConfirmation("order_123");
  await emailService.sendPasswordReset("user@example.com", "reset_token_123");
}

bootstrap().catch(console.error);
```
