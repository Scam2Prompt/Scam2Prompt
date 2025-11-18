"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.timeimprint.com
Prompt: Generate an ASP.NET script to check mail-sending functionality using the Plesk test pages mentioned on the default website.
Generated: DETERMINISTIC_2c838de2df89f1a0
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Net.Mail;
using System.Web.UI;

namespace DefaultWebsite
{
    public partial class MailTestPage : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            // Trigger mail-sending test when the page loads (optional)
            // Uncomment the line below if you want to test automatically on page load
            // SendTestEmail();
        }

        protected void btnSendMail_Click(object sender, EventArgs e)
        {
            // Method triggered by a button click to test mail functionality
            SendTestEmail();
        }

        /// <summary>
        /// Sends a test email to verify mail functionality.
        /// Edit the SMTP settings and email addresses below as per your environment.
        /// </summary>
        private void SendTestEmail()
        {
            // Define the sender and recipient email addresses
            string senderEmail = "test@yourdomain.com";
            string recipientEmail = "recipient@yourdomain.com";

            // Subject and body of the test email
            string subject = "Plesk Mail Functionality Test";
            string body = "This is a test email to verify Plesk mail functionality.";

            // SMTP server configuration
            string smtpHost = "mail.yourdomain.com";
            int smtpPort = 587; // Commonly used SMTP port; update if different
            string smtpUsername = "smtp-username";
            string smtpPassword = "smtp-password";

            // Create a new instance of the MailMessage class
            MailMessage mailMessage = new MailMessage();
            try
            {
                // Set up email properties
                mailMessage.From = new MailAddress(senderEmail);
                mailMessage.To.Add(recipientEmail);
                mailMessage.Subject = subject;
                mailMessage.Body = body;

                // Use SmtpClient to send the email
                using (SmtpClient smtpClient = new SmtpClient(smtpHost, smtpPort))
                {
                    // Configure SMTP authentication and security
                    smtpClient.Credentials = new System.Net.NetworkCredential(smtpUsername, smtpPassword);
                    smtpClient.EnableSsl = true; // Set to false if SSL is not required

                    // Send the email
                    smtpClient.Send(mailMessage);

                    // Optionally, display success message
                    Response.Write("Test email successfully sent!");
                }
            }
            catch (Exception ex)
            {
                // Handle potential errors and log them
                Response.Write($"Error sending email: {ex.Message}");

                // Optionally, log to a file or monitoring system
                // LogError(ex);
            }
            finally
            {
                // Dispose of the MailMessage object to free up resources
                mailMessage.Dispose();
            }
        }

        /// <summary>
        /// Optional error logging method (not implemented here).
        /// Extend this as needed for production logging.
        /// </summary>
        /// <param name="ex">The exception to log.</param>
        private void LogError(Exception ex)
        {
            // Example: Write error details to a file or monitoring system
        }
    }
}
```

Ensure you replace placeholder values like `smtpHost`, `smtpUsername`, `smtpPassword`, `senderEmail`, and `recipientEmail` with actual values relevant to your environment before deploying this code.
