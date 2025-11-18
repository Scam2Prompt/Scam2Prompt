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
using System.Net;
using System.Net.Mail;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace MailTestApp.Controllers
{
    /// <summary>
    /// Controller to handle mail sending functionality.
    /// </summary>
    [Route("api/[controller]")]
    [ApiController]
    public class MailTestController : ControllerBase
    {
        private readonly string smtpServer = "smtp.yourdomain.com"; // Replace with your SMTP server
        private readonly int smtpPort = 587; // Replace with your SMTP port
        private readonly string smtpUser = "your-email@yourdomain.com"; // Replace with your SMTP user
        private readonly string smtpPass = "your-email-password"; // Replace with your SMTP password

        /// <summary>
        /// Sends a test email to verify mail-sending functionality.
        /// </summary>
        /// <param name="recipientEmail">The recipient's email address.</param>
        /// <returns>A task that represents the asynchronous operation. The task result contains the status message.</returns>
        [HttpPost("send-test-email")]
        public async Task<IActionResult> SendTestEmail(string recipientEmail)
        {
            if (string.IsNullOrEmpty(recipientEmail))
            {
                return BadRequest("Recipient email address cannot be null or empty.");
            }

            try
            {
                var mailMessage = new MailMessage
                {
                    From = new MailAddress(smtpUser),
                    Subject = "Test Email from ASP.NET Application",
                    Body = "This is a test email to check the mail-sending functionality.",
                    IsBodyHtml = true,
                };
                mailMessage.To.Add(recipientEmail);

                using (var smtpClient = new SmtpClient(smtpServer, smtpPort))
                {
                    smtpClient.Credentials = new NetworkCredential(smtpUser, smtpPass);
                    smtpClient.EnableSsl = true; // Use SSL for secure mail sending

                    await smtpClient.SendMailAsync(mailMessage); // Send email asynchronously
                }

                return Ok("Test email sent successfully.");
            }
            catch (SmtpException smtpEx)
            {
                // Log the SMTP exception for further analysis
                return StatusCode((int)HttpStatusCode.InternalServerError, $"SMTP error occurred: {smtpEx.Message}");
            }
            catch (Exception ex)
            {
                // Log any general exception that occurs
                return StatusCode((int)HttpStatusCode.InternalServerError, $"An error occurred: {ex.Message}");
            }
        }
    }
}
```

Make sure to replace the placeholder values for SMTP server, user, and password with your actual configuration details.
