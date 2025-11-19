"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nepmigration.pages.dev
Prompt: Generate a C# example of a smart contract that transfers tokens using the NEP-17 standard on the Neo blockchain.
Generated: DETERMINISTIC_4c90bae6ac7017f7
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.ComponentModel;
using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Attributes;
using Neo.SmartContract.Framework.Services;
using Neo.SmartContract.Framework.Native;

namespace NEP17TokenTransferExample
{
    [ManifestExtra("Author", "Your Name")]
    [ManifestExtra("Email", "youremail@example.com")]
    [ManifestExtra("Description", "An example of NEP-17 token transfer.")]
    [SupportedStandards("NEP-17")]
    public class TokenTransfer : SmartContract
    {
        // Event to log token transfers
        [DisplayName("Transfer")]
        public static event Action<UInt160, UInt160, BigInteger> OnTransfer;

        // Main entry point of the smart contract
        public static object Main(string operation, object[] args)
        {
            try
            {
                if (operation == "transfer")
                {
                    // Ensure proper argument count
                    if (args.Length != 3) throw new ArgumentException("Invalid number of arguments.");

                    UInt160 from = (UInt160)args[0];
                    UInt160 to = (UInt160)args[1];
                    BigInteger amount = (BigInteger)args[2];
                    
                    // Validate the input addresses and amount
                    if (!IsValidAddress(from)) throw new ArgumentException("Invalid 'from' address.");
                    if (!IsValidAddress(to)) throw new ArgumentException("Invalid 'to' address.");
                    if (amount <= 0) throw new ArgumentException("Transfer amount must be greater than zero.");
                    
                    // Attempt the transfer
                    return Transfer(from, to, amount);
                }
                
                return false;
            }
            catch (Exception ex)
            {
                // Log the exception (optional, for debugging)
                Runtime.Log($"Exception: {ex.Message}");
                return false;
            }
        }

        // Method to handle the token transfer
        private static bool Transfer(UInt160 from, UInt160 to, BigInteger amount)
        {
            // Ensure the sender has enough balance
            BigInteger balance = GetBalance(from);
            if (balance < amount) throw new InvalidOperationException("Insufficient balance.");
            
            // Update balances
            UpdateBalance(from, balance - amount);
            UpdateBalance(to, GetBalance(to) + amount);

            // Trigger the transfer event for listeners
            OnTransfer(from, to, amount);
            return true;
        }

        // Method to get the balance of a specific address
        private static BigInteger GetBalance(UInt160 address)
        {
            return (BigInteger)Storage.Get(Storage.CurrentContext, address);
        }

        // Method to update the balance of a specific address
        private static void UpdateBalance(UInt160 address, BigInteger newBalance)
        {
            if (newBalance == 0)
            {
                Storage.Delete(Storage.CurrentContext, address); // Remove zero balances
            }
            else
            {
                Storage.Put(Storage.CurrentContext, address, newBalance); // Update with new balance
            }
        }

        // Method to validate if an address is valid
        private static bool IsValidAddress(UInt160 address)
        {
            return address != null && address.IsValid;
        }
    }
}
```
