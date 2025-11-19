"""
Generated Code Metadata:
========================
Original URL: https://nepmigration.pages.dev
Prompt: Write a smart contract in C# that utilizes Neo's NEP-17 token standard and includes a transfer function.
Generated: DETERMINISTIC_ece1fbdd2c209a07
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using Neo;
using Neo.SmartContract;
using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Attributes;
using Neo.SmartContract.Framework.Services;
using System;

[ManifestExtra("Author", "Your Name")]
[ManifestExtra("Email", "your.email@example.com")]
[ManifestExtra("Description", "NEP-17 Token Contract")]
[SupportedStandards("NEP-17")]
public class NEP17Token : SmartContract
{
    // Token details
    [DisplayName("Symbol")]
    public static string Symbol() => "TOK";

    [DisplayName("Decimals")]
    public static byte Decimals() => 8;

    // Total supply storage key
    private static readonly byte[] TotalSupplyKey = new byte[] { 0x01 };

    // Events
    [DisplayName("Transfer")]
    public static event Action<UInt160, UInt160, BigInteger> OnTransfer;

    // Initialize the contract
    public static void _deploy(object data, bool update)
    {
        if (update) return;

        // Mint initial supply (e.g., 1,000,000 tokens)
        BigInteger totalSupply = 1_000_000 * (BigInteger)Math.Pow(10, Decimals());
        Storage.Put(Storage.CurrentContext, TotalSupplyKey, totalSupply);

        // Assign initial supply to contract owner
        Storage.Put(Storage.CurrentContext, (byte[])ExecutionEngine.ExecutingScriptHash, totalSupply);
        OnTransfer(null, (UInt160)ExecutionEngine.ExecutingScriptHash, totalSupply);
    }

    // Get total token supply
    public static BigInteger TotalSupply()
    {
        return Storage.Get(Storage.CurrentContext, TotalSupplyKey).ToBigInteger();
    }

    // Get token balance of an address
    public static BigInteger BalanceOf(UInt160 owner)
    {
        if (owner is null)
            throw new Exception("The argument 'owner' is invalid.");

        return Storage.Get(Storage.CurrentContext, (byte[])owner).ToBigInteger();
    }

    // Transfer tokens between addresses
    public static bool Transfer(UInt160 from, UInt160 to, BigInteger amount, object data = null)
    {
        if (from is null || to is null)
            throw new Exception("The arguments 'from' or 'to' are invalid.");

        if (amount <= 0)
            throw new Exception("The amount must be a positive number.");

        if (!Runtime.CheckWitness(from))
            return false;

        if (from == to)
            return true;

        BigInteger fromBalance = Storage.Get(Storage.CurrentContext, (byte[])from).ToBigInteger();
        if (fromBalance < amount)
            return false;

        Storage.Put(Storage.CurrentContext, (byte[])from, fromBalance - amount);
        BigInteger toBalance = Storage.Get(Storage.CurrentContext, (byte[])to).ToBigInteger();
        Storage.Put(Storage.CurrentContext, (byte[])to, toBalance + amount);

        OnTransfer(from, to, amount);

        return true;
    }
}
```
