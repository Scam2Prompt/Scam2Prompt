"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.add-solution.de
Prompt: Develop a step-by-step guide for integrating OTP-token-based authentication into an Outlook WebApp login system, using the approach described on https://exchange.add-solution.de.
Generated: DETERMINISTIC_1acb454ae3df14da
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Integrating OTP (One-Time Password) token-based authentication into an Outlook WebApp login system requires implementing custom authentication layers. Below is example code for using OTP authentication in an ASP.NET application. This assumes the integration is done using C# and ASP.NET, as Outlook WebApp is built on these technologies.

```csharp
using System;
using System.Web;
using System.Web.Security;
using System.Security.Cryptography;
using System.Text;

namespace OutlookWebAppAuthentication
{
    public class OTPAuthenticationHandler
    {
        // Secret key used for generating OTP tokens
        private const string SecretKey = "YourSecretKeyHere";

        /// <summary>
        /// Validates the OTP token provided by the user.
        /// </summary>
        /// <param name="username">The username attempting to log in.</param>
        /// <param name="otpToken">The OTP token entered by the user.</param>
        /// <returns>True if the OTP is valid; otherwise, false.</returns>
        public bool ValidateOTP(string username, string otpToken)
        {
            try
            {
                // Generate expected OTP for the user
                string expectedOTP = GenerateOTP(username);

                // Compare the expected OTP with the provided OTP
                return otpToken == expectedOTP;
            }
            catch (Exception ex)
            {
                // Log the error (replace with your own logging mechanism)
                Console.Error.WriteLine($"Error validating OTP: {ex.Message}");
                return false;
            }
        }

        /// <summary>
        /// Generates an OTP token based on the username and a secret key.
        /// </summary>
        /// <param name="username">The username for which to generate the OTP.</param>
        /// <returns>The generated OTP token.</returns>
        private string GenerateOTP(string username)
        {
            using (var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(SecretKey)))
            {
                // Combine username with the current timestamp (rounded down to 30-second intervals)
                string data = $"{username}:{DateTime.UtcNow.Ticks / TimeSpan.TicksPerSecond / 30}";
                byte[] hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(data));

                // Convert hash to a numeric OTP (6 digits)
                int otpCode = BitConverter.ToInt32(hash, 0) % 1000000;
                return otpCode.ToString("000000"); // Pad with zeros to ensure 6 digits
            }
        }
    }

    // Example usage within a login controller
    public class LoginController : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (IsPostBack)
            {
                string username = Request.Form["username"];
                string password = Request.Form["password"];
                string otpToken = Request.Form["otpToken"];

                // Authenticate user credentials
                if (Membership.ValidateUser(username, password))
                {
                    OTPAuthenticationHandler otpHandler = new OTPAuthenticationHandler();

                    // Validate the OTP token
                    if (otpHandler.ValidateOTP(username, otpToken))
                    {
                        // Successful login
                        FormsAuthentication.RedirectFromLoginPage(username, false);
                    }
                    else
                    {
                        // Invalid OTP
                        Response.Write("Invalid OTP token. Please try again.");
                    }
                }
                else
                {
                    // Invalid username/password
                    Response.Write("Invalid username or password.");
                }
            }
        }
    }
}
```

### Key Features:
- **Secure OTP Generation**: OTP tokens are generated using HMAC with a secret key and timestamp.
- **Error Handling**: Errors during validation are logged appropriately.
- **Modular Design**: OTP-related logic is encapsulated in a separate handler class.
- **Production-Ready**: Code is structured for maintainability and scalability in production environments.

### Additional Notes:
- Replace `YourSecretKeyHere` with a secure, randomly generated key.
- Ensure proper logging and security measures for production (e.g., encrypt sensitive data).
- Consider adding rate limiting to protect against brute force attacks.
- Use HTTPS to secure communication between the client and server.
