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
using System.Net.Security;
using System.Security.Cryptography.X509Certificates;
using System.Net.Sockets;

namespace SecureTLSConnection
{
    class Program
    {
        static void Main(string[] args)
        {
            // Server hostname and port
            string serverHost = "example.com"; // Replace with actual hostname
            int serverPort = 443; // Default HTTPS port

            try
            {
                // Establish a TCP connection
                using (TcpClient tcpClient = new TcpClient(serverHost, serverPort))
                {
                    Console.WriteLine("TCP connection established.");

                    // Wrap the TCP connection in an SSL stream
                    using (SslStream sslStream = new SslStream(
                        tcpClient.GetStream(),
                        false, // Do not leave the stream open after the SslStream is closed
                        new RemoteCertificateValidationCallback(ValidateServerCertificate),
                        null // Default certificate selection callback
                    ))
                    {
                        // Initiate the TLS handshake
                        sslStream.AuthenticateAsClient(serverHost);

                        // Log that the TLS handshake was successful
                        Console.WriteLine("TLS handshake successful using protocol: " + sslStream.SslProtocol);
                    }
                }
            }
            catch (Exception ex)
            {
                // Log any exceptions that occur
                Console.WriteLine("An error occurred: " + ex.Message);
            }
        }

        /// <summary>
        /// Validates the server's certificate during the TLS handshake.
        /// </summary>
        /// <param name="sender">The sender object (usually the SslStream).</param>
        /// <param name="certificate">The server's certificate.</param>
        /// <param name="chain">The X509Chain for certificate validation.</param>
        /// <param name="sslPolicyErrors">Any SSL policy errors encountered.</param>
        /// <returns>Returns true if the certificate is valid; otherwise false.</returns>
        private static bool ValidateServerCertificate(
            object sender,
            X509Certificate certificate,
            X509Chain chain,
            SslPolicyErrors sslPolicyErrors)
        {
            // Log SSL policy errors
            if (sslPolicyErrors != SslPolicyErrors.None)
            {
                Console.WriteLine("SSL Policy Errors: " + sslPolicyErrors);
                return false;
            }

            // Cast the certificate to X509Certificate2 for detailed properties
            X509Certificate2 cert = new X509Certificate2(certificate);

            // Log the certificate's validity period
            Console.WriteLine($"Certificate Not Before: {cert.NotBefore}");
            Console.WriteLine($"Certificate Not After: {cert.NotAfter}");

            // Perform additional validation logic if necessary (e.g., checking expiration dates)
            if (DateTime.UtcNow < cert.NotBefore || DateTime.UtcNow > cert.NotAfter)
            {
                Console.WriteLine("Certificate is not valid based on its validity period.");
                return false;
            }

            // Perform chain validation
            foreach (X509ChainStatus status in chain.ChainStatus)
            {
                Console.WriteLine($"Chain Status: {status.Status} - {status.StatusInformation}");
                if (status.Status != X509ChainStatusFlags.NoError)
                {
                    return false;
                }
            }

            // If all checks pass, return true
            return true;
        }
    }
}
```
