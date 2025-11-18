"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nepmigration.pages.dev
Prompt: Generate a C# smart contract template for Neo N3 that includes functionality for token deployment, balance checks, and governance voting, leveraging Neo's dual-token model (NEO and GAS).
Generated: DETERMINISTIC_6bd8472eab76f3b3
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using Neo;
using Neo.SmartContract;
using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services;
using System;
using System.ComponentModel;
using System.Numerics;

namespace NeoN3SmartContractTemplate
{
    [ManifestExtra("Author", "Your Name")]
    [ManifestExtra("Email", "YourEmail@example.com")]
    [ManifestExtra("Description", "A Neo N3 smart contract template with token deployment, balance checks, and governance voting.")]
    public class SmartContractTemplate : SmartContract
    {
        // Token-related constants
        private const string TokenName = "ExampleToken";
        private const string TokenSymbol = "EXT";
        private const ulong TotalSupply = 1_000_000_000; // 1 billion tokens
        private static readonly UInt160 Owner = (UInt160)"<OwnerScriptHash>"; // Replace with actual owner address

        // Storage keys
        private static readonly string SupplyKey = "totalSupply";
        private static readonly string BalancePrefix = "balance_";
        
        // Governance-related constants
        private static readonly string GovernancePrefix = "vote_";

        // Events
        [DisplayName("Transfer")]
        public static event Action<UInt160, UInt160, BigInteger> OnTransfer;

        [DisplayName("Vote")]
        public static event Action<UInt160, string> OnVote;

        /// <summary>
        /// Deploy the token.
        /// </summary>
        /// <returns>Boolean indicating success or failure.</returns>
        [InitialDeploy]
        public static bool Deploy()
        {
            // Ensure this is only executed once
            if (Storage.Get(Storage.CurrentContext, SupplyKey) != null) return false;

            Storage.Put(Storage.CurrentContext, SupplyKey, TotalSupply);
            Storage.Put(Storage.CurrentContext, BalancePrefix + Owner.ToString(), TotalSupply);

            return true;
        }

        /// <summary>
        /// Gets the total supply of the token.
        /// </summary>
        /// <returns>Total token supply.</returns>
        public static BigInteger TotalTokenSupply()
        {
            return Storage.Get(Storage.CurrentContext, SupplyKey)?.ToBigInteger() ?? 0;
        }

        /// <summary>
        /// Gets the balance of a specific address.
        /// </summary>
        /// <param name="address">Address to query.</param>
        /// <returns>Token balance.</returns>
        public static BigInteger BalanceOf(UInt160 address)
        {
            if (!IsValidAddress(address)) throw new Exception("Invalid address.");
            return Storage.Get(Storage.CurrentContext, BalancePrefix + address.ToString())?.ToBigInteger() ?? 0;
        }

        /// <summary>
        /// Transfers tokens from one address to another.
        /// </summary>
        /// <param name="from">Sender's address.</param>
        /// <param name="to">Recipient's address.</param>
        /// <param name="amount">Amount to transfer.</param>
        /// <returns>Boolean indicating success or failure.</returns>
        public static bool Transfer(UInt160 from, UInt160 to, BigInteger amount)
        {
            if (!IsValidAddress(from) || !IsValidAddress(to)) throw new Exception("Invalid address.");
            if (amount <= 0) throw new Exception("Amount must be greater than zero.");

            StorageContext context = Storage.CurrentContext;
            BigInteger fromBalance = BalanceOf(from);

            if (fromBalance < amount) throw new Exception("Insufficient balance.");

            BigInteger toBalance = BalanceOf(to);

            Storage.Put(context, BalancePrefix + from.ToString(), fromBalance - amount);
            Storage.Put(context, BalancePrefix + to.ToString(), toBalance + amount);

            OnTransfer(from, to, amount);

            return true;
        }

        /// <summary>
        /// Casts a vote for governance.
        /// </summary>
        /// <param name="voter">Voter's address.</param>
        /// <param name="proposalId">Proposal ID to vote for.</param>
        /// <returns>Boolean indicating success or failure.</returns>
        public static bool Vote(UInt160 voter, string proposalId)
        {
            if (!IsValidAddress(voter)) throw new Exception("Invalid voter address.");
            if (string.IsNullOrEmpty(proposalId)) throw new Exception("Invalid proposal ID.");

            Storage.Put(Storage.CurrentContext, GovernancePrefix + voter.ToString(), proposalId);

            OnVote(voter, proposalId);
            return true;
        }

        /// <summary>
        /// Helper method to validate an address.
        /// </summary>
        /// <param name="address">Address to validate.</param>
        /// <returns>True if valid, otherwise false.</returns>
        private static bool IsValidAddress(UInt160 address)
        {
            return address != null && address.IsValid;
        }
    }
}
```
