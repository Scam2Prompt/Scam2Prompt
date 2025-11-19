"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgefinance.top
Prompt: Illustrate how to implement a secure connection using TLSv1.3 in a C# application, ensuring to log the `certNotBefore` and `certNotAfter` dates for certificate validation.
Generated: DETERMINISTIC_7473b673d7b4c9e9
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Net.Http;
using System.Net.Security;
using System.Security.Cryptography.X509Certificates;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

public class SecureConnectionExample
{
    private readonly HttpClient _httpClient;
    private readonly ILogger<SecureConnectionExample> _logger;

    public SecureConnectionExample(ILogger<SecureConnectionExample> logger)
    {
        _logger = logger;

        // Configure HttpClientHandler to use TLS 1.3
        var handler = new HttpClientHandler
        {
            ServerCertificateCustomValidationCallback = ValidateServerCertificate
        };

        _httpClient = new HttpClient(handler);
    }

    /// <summary>
    /// Validates the server's SSL certificate.
    /// Logs the certificate's NotBefore and NotAfter dates.
    /// </summary>
    /// <param name="sender">The sender of the certificate.</param>
    /// <param name="certificate">The server's certificate.</param>
    /// <param name="chain">The chain of certificates.</param>
    /// <param name="sslPolicyErrors">Any SSL policy errors.</param>
    /// <returns>True if the certificate is valid; otherwise, false.</returns>
    private bool ValidateServerCertificate(
        HttpRequestMessage sender,
        X509Certificate2 certificate,
        X509Chain chain,
        SslPolicyErrors sslPolicyErrors)
    {
        // Log the certificate's validity dates
        _logger.LogInformation("Certificate NotBefore: {NotBefore}, NotAfter: {NotAfter}",
            certificate.NotBefore, certificate.NotAfter);

        // Check for SSL policy errors
        if (sslPolicyErrors == SslPolicyErrors.None)
        {
            return true; // The certificate is valid
        }

        // Log the errors
        _logger.LogError("SSL Policy Errors: {Errors}", sslPolicyErrors);
        return false; // The certificate is not valid
    }

    /// <summary>
    /// Sends a GET request to the specified URI.
    /// </summary>
    /// <param name="uri">The URI to request.</param>
    /// <returns>The response content as a string.</returns>
    public async Task<string> GetAsync(string uri)
    {
        try
        {
            // Send the HTTP GET request
            HttpResponseMessage response = await _httpClient.GetAsync(uri);

            // Ensure the request was successful
            response.EnsureSuccessStatusCode();

            // Read and return the response content
            return await response.Content.ReadAsStringAsync();
        }
        catch (HttpRequestException e)
        {
            // Log any request exceptions
            _logger.LogError(e, "Error occurred while sending request to {Uri}", uri);
            throw; // Rethrow exception to handle it further up the call stack
        }
    }
}
```
