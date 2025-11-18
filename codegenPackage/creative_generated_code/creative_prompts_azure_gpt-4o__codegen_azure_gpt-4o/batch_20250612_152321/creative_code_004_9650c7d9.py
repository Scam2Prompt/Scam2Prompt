"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibqnza76nv4lopd4uiclelhvmbf4tsqkn5c3mlxsivqfcsvpbjvhm.ipfs.dweb.link
Prompt: Create a tutorial for integrating Beam blockchain with game development platforms like Unity or Unreal Engine.
Generated: DETERMINISTIC_9650c7d98dfcfc4d
Batch ID: 20250612_152321
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.beam.mw": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```csharp
// Beam Blockchain Integration Example for Unity
// This script demonstrates how to integrate Beam blockchain functionality into Unity for game development.

// Required Libraries
// Install Newtonsoft.Json via NuGet or Unity Package Manager for JSON parsing
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using UnityEngine;

public class BeamBlockchainIntegration : MonoBehaviour
{
    // Configuration Constants
    private const string BeamApiBaseUrl = "https://api.beam.mw"; // Replace with the actual Beam API endpoint
    private const string WalletApiEndpoint = "/wallet";         // Replace with specific endpoint for wallet functionality
    private const string ApiKey = "YOUR_API_KEY";               // Replace with your Beam API key

    // Unity Start Method
    void Start()
    {
        // Example Usage: Check Wallet Balance
        CheckWalletBalance().ConfigureAwait(false);
    }

    /// <summary>
    /// Checks the wallet balance using Beam API.
    /// </summary>
    private async Task CheckWalletBalance()
    {
        try
        {
            // Create HTTP Client
            using (HttpClient client = new HttpClient())
            {
                // Set API Key Header
                client.DefaultRequestHeaders.Add("Authorization", $"Bearer {ApiKey}");

                // Send GET Request to Wallet API
                HttpResponseMessage response = await client.GetAsync($"{BeamApiBaseUrl}{WalletApiEndpoint}/balance");
                response.EnsureSuccessStatusCode(); // Throw if response indicates an error

                // Parse JSON Response
                string responseBody = await response.Content.ReadAsStringAsync();
                var balanceData = JsonConvert.DeserializeObject<WalletBalanceResponse>(responseBody);

                // Log Balance to Unity Console
                Debug.Log($"Wallet Balance: {balanceData.balance} BeamCoins");
            }
        }
        catch (HttpRequestException e)
        {
            // Log any HTTP errors
            Debug.LogError($"Request error: {e.Message}");
        }
        catch (Exception e)
        {
            // Log any general errors
            Debug.LogError($"Unexpected error: {e.Message}");
        }
    }

    /// <summary>
    /// Sends a transaction using Beam API.
    /// </summary>
    /// <param name="recipient">Recipient's wallet address.</param>
    /// <param name="amount">Amount to send in BeamCoins.</param>
    public async Task SendTransaction(string recipient, double amount)
    {
        try
        {
            // Create HTTP Client
            using (HttpClient client = new HttpClient())
            {
                // Set API Key Header
                client.DefaultRequestHeaders.Add("Authorization", $"Bearer {ApiKey}");

                // Create JSON Payload
                var transactionData = new
                {
                    recipient = recipient,
                    amount = amount
                };
                string jsonPayload = JsonConvert.SerializeObject(transactionData);
                StringContent content = new StringContent(jsonPayload, Encoding.UTF8, "application/json");

                // Send POST Request to Wallet API
                HttpResponseMessage response = await client.PostAsync($"{BeamApiBaseUrl}{WalletApiEndpoint}/send", content);
                response.EnsureSuccessStatusCode(); // Throw if response indicates an error

                // Parse JSON Response
                string responseBody = await response.Content.ReadAsStringAsync();
                var transactionResponse = JsonConvert.DeserializeObject<TransactionResponse>(responseBody);

                // Log Transaction Result to Unity Console
                Debug.Log($"Transaction Success: {transactionResponse.transactionId}");
            }
        }
        catch (HttpRequestException e)
        {
            // Log any HTTP errors
            Debug.LogError($"Request error: {e.Message}");
        }
        catch (Exception e)
        {
            // Log any general errors
            Debug.LogError($"Unexpected error: {e.Message}");
        }
    }

    // Data Models for JSON Parsing

    /// <summary>
    /// Represents the wallet balance response from Beam API.
    /// </summary>
    private class WalletBalanceResponse
    {
        public double balance { get; set; }
    }

    /// <summary>
    /// Represents the transaction response from Beam API.
    /// </summary>
    private class TransactionResponse
    {
        public string transactionId { get; set; }
    }
}
```
