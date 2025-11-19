"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morphafinance.com
Prompt: Develop a C# application that manages crypto wallet transactions securely, leveraging the blockchain ledger technology mentioned on Morpha Finance.
Generated: DETERMINISTIC_769c830e9320c083
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

namespace CryptoWalletManager
{
    /// <summary>
    /// Represents a transaction in the crypto wallet.
    /// </summary>
    public class Transaction
    {
        public string FromAddress { get; set; }
        public string ToAddress { get; set; }
        public decimal Amount { get; set; }
        public string TransactionId { get; private set; }
        public DateTime Timestamp { get; private set; }

        public Transaction(string from, string to, decimal amount)
        {
            FromAddress = from;
            ToAddress = to;
            Amount = amount;
            Timestamp = DateTime.UtcNow;
            TransactionId = GenerateTransactionId();
        }

        private string GenerateTransactionId()
        {
            using (var sha256 = SHA256.Create())
            {
                var rawData = $"{FromAddress}-{ToAddress}-{Amount}-{Timestamp}";
                var bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(rawData));
                return BitConverter.ToString(bytes).Replace("-", "").ToLower();
            }
        }
    }

    /// <summary>
    /// Manages the cryptocurrency wallet and transactions.
    /// </summary>
    public class CryptoWallet
    {
        private readonly List<Transaction> transactions;
        private decimal balance;

        public CryptoWallet()
        {
            transactions = new List<Transaction>();
            balance = 0;
        }

        /// <summary>
        /// Adds funds to the wallet.
        /// </summary>
        /// <param name="amount">The amount to add.</param>
        public void AddFunds(decimal amount)
        {
            if (amount <= 0)
            {
                throw new ArgumentException("Amount must be greater than zero.");
            }
            balance += amount;
        }

        /// <summary>
        /// Transfers funds from this wallet to another.
        /// </summary>
        /// <param name="toAddress">The address to transfer funds to.</param>
        /// <param name="amount">The amount to transfer.</param>
        public void TransferFunds(string toAddress, decimal amount)
        {
            if (string.IsNullOrEmpty(toAddress))
            {
                throw new ArgumentException("Recipient address cannot be empty.");
            }

            if (amount <= 0 || amount > balance)
            {
                throw new InvalidOperationException("Insufficient funds or invalid amount.");
            }

            var transaction = new Transaction("MyWalletAddress", toAddress, amount);
            transactions.Add(transaction);
            balance -= amount;
            Console.WriteLine($"Transaction successful: {transaction.TransactionId} for {amount} to {toAddress}");
        }

        /// <summary>
        /// Gets the current balance of the wallet.
        /// </summary>
        /// <returns>The current balance.</returns>
        public decimal GetBalance()
        {
            return balance;
        }

        /// <summary>
        /// Lists all transactions.
        /// </summary>
        /// <returns>A list of transactions.</returns>
        public List<Transaction> GetTransactions()
        {
            return transactions;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                var wallet = new CryptoWallet();
                wallet.AddFunds(100m); // Adding funds to the wallet

                Console.WriteLine($"Current Balance: {wallet.GetBalance()}");

                // Sample transfer
                wallet.TransferFunds("RecipientWalletAddress", 50m);
                Console.WriteLine($"Current Balance after transfer: {wallet.GetBalance()}");

                // Display all transactions
                var transactions = wallet.GetTransactions();
                Console.WriteLine("Transactions:");
                foreach (var transaction in transactions)
                {
                    Console.WriteLine($"ID: {transaction.TransactionId}, From: {transaction.FromAddress}, " +
                                      $"To: {transaction.ToAddress}, Amount: {transaction.Amount}, " +
                                      $"Timestamp: {transaction.Timestamp}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
