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
using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using System;
using System.Numerics;

namespace TokenSmartContract
{
    // Define the smart contract for a NEP-17 compliant token
    public class Token : SmartContract
    {
        // Token properties
        private static readonly string tokenSymbol = "MYT";
        private static readonly string tokenName = "My Token";
        private static readonly byte decimals = 8;

        // Store balances and allowed amounts
        private static StorageMap balances => new StorageMap(Storage.CurrentContext, "balances");
        private static StorageMap allowed => new StorageMap(Storage.CurrentContext, "allowed");

        // Total supply of the token
        public static BigInteger TotalSupply()
        {
            return 1000000 * (BigInteger)Math.Pow(10, decimals); // 1 million tokens
        }

        // Get the balance of a specific address
        public static BigInteger BalanceOf(byte[] address)
        {
            return balances.Get(address).AsBigInteger();
        }

        // Transfer tokens from the caller to a specified address
        public static bool Transfer(byte[] to, BigInteger amount)
        {
            // Ensure the recipient address is valid
            if (to.Length != 20)
                throw new Exception("Invalid recipient address");

            // Ensure the amount is positive
            if (amount <= 0)
                throw new Exception("Transfer amount must be greater than zero");

            // Get the sender's address
            byte[] from = Runtime.CallingScriptHash;

            // Check if the sender has enough balance
            BigInteger fromBalance = BalanceOf(from);
            if (fromBalance < amount)
                throw new Exception("Insufficient balance");

            // Update balances
            balances.Put(from, fromBalance - amount);
            BigInteger toBalance = BalanceOf(to) + amount;
            balances.Put(to, toBalance);

            // Emit transfer event
            OnTransfer(from, to, amount);
            return true;
        }

        // Allowance mechanism for delegated transfers
        public static BigInteger Allowance(byte[] owner, byte[] spender)
        {
            return allowed.Get(new byte[] { owner, spender }).AsBigInteger();
        }

        // Approve tokens for delegated transfer
        public static bool Approve(byte[] spender, BigInteger amount)
        {
            // Ensure the spender address is valid
            if (spender.Length != 20)
                throw new Exception("Invalid spender address");

            // Update the allowed amount
            byte[] owner = Runtime.CallingScriptHash;
            allowed.Put(new byte[] { owner, spender }, amount);
            return true;
        }

        // Transfer tokens from one address to another using allowance
        public static bool TransferFrom(byte[] from, byte[] to, BigInteger amount)
        {
            // Ensure the recipient address is valid
            if (to.Length != 20)
                throw new Exception("Invalid recipient address");

            // Ensure the amount is positive
            if (amount <= 0)
                throw new Exception("Transfer amount must be greater than zero");

            // Check allowance and balance
            byte[] spender = Runtime.CallingScriptHash;
            BigInteger currentAllowance = Allowance(from, spender);
            if (currentAllowance < amount)
                throw new Exception("Allowance exceeded");

            BigInteger fromBalance = BalanceOf(from);
            if (fromBalance < amount)
                throw new Exception("Insufficient balance");

            // Update balances and allowance
            balances.Put(from, fromBalance - amount);
            BigInteger toBalance = BalanceOf(to) + amount;
            balances.Put(to, toBalance);
            allowed.Put(new byte[] { from, spender }, currentAllowance - amount);

            // Emit transfer event
            OnTransfer(from, to, amount);
            return true;
        }

        // Event to log transfers
        private static void OnTransfer(byte[] from, byte[] to, BigInteger value)
        {
            Runtime.Notify("Transfer", new object[] { from, to, value });
        }
    }
}
```
