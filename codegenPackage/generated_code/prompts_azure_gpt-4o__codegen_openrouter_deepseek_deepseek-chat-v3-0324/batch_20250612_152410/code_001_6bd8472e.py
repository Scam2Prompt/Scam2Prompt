"""
Generated Code Metadata:
========================
Original URL: https://nepmigration.pages.dev
Prompt: Generate a C# smart contract template for Neo N3 that includes functionality for token deployment, balance checks, and governance voting, leveraging Neo's dual-token model (NEO and GAS).
Generated: DETERMINISTIC_6bd8472eab76f3b3
Batch ID: 20250612_152410
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
using Neo.SmartContract.Framework.Native;
using Neo.SmartContract.Framework.Services;
using System;
using System.ComponentModel;
using System.Numerics;

[DisplayName("NeoN3GovernanceTokenContract")]
[ManifestExtra("Author", "YourName")]
[ManifestExtra("Email", "your.email@example.com")]
[ManifestExtra("Description", "Neo N3 Governance Token Contract")]
[ContractPermission("*", "*")]
public class NeoN3GovernanceTokenContract : SmartContract
{
    #region Token Settings
    private const string TokenName = "GovernanceToken";
    private const string TokenSymbol = "GOV";
    private const byte TokenDecimals = 8;
    private static readonly StorageMap TokenStorage = new StorageMap(Storage.CurrentContext, "Token");
    private static readonly StorageMap AccountStorage = new StorageMap(Storage.CurrentContext, "Account");
    private static readonly StorageMap VoteStorage = new StorageMap(Storage.CurrentContext, "Vote");
    #endregion

    #region Events
    [DisplayName("Transfer")]
    public static event Action<UInt160, UInt160, BigInteger> OnTransfer;

    [DisplayName("Vote")]
    public static event Action<UInt160, UInt160, BigInteger> OnVote;
    #endregion

    #region Safe Math
    private static BigInteger SafeAdd(BigInteger a, BigInteger b)
    {
        var result = a + b;
        if (result < a) throw new Exception("SafeAdd: Addition overflow");
        return result;
    }

    private static BigInteger SafeSub(BigInteger a, BigInteger b)
    {
        if (b > a) throw new Exception("SafeSub: Subtraction underflow");
        return a - b;
    }
    #endregion

    #region Contract Methods
    public static void OnNEP17Payment(UInt160 from, BigInteger amount, object data)
    {
        // Handle incoming NEP-17 payments if needed
    }

    [DisplayName("_deploy")]
    public static void Deploy(object data, bool update)
    {
        if (update) return;

        var totalSupply = 100_000_000 * (BigInteger)Math.Pow(10, TokenDecimals);
        TokenStorage.Put("TotalSupply", totalSupply);
        TokenStorage.Put("Owner", (ByteString)Runtime.ExecutingScriptHash);

        // Mint initial supply to contract owner
        var owner = (UInt160)Runtime.ExecutingScriptHash;
        AccountStorage.Put(owner, totalSupply);
        OnTransfer(null, owner, totalSupply);
    }

    public static void Update(ByteString nefFile, string manifest)
    {
        var owner = (UInt160)TokenStorage.Get("Owner");
        if (!Runtime.CheckWitness(owner)) throw new Exception("No authorization");
        ContractManagement.Update(nefFile, manifest);
    }

    [DisplayName("totalSupply")]
    public static BigInteger TotalSupply() => (BigInteger)TokenStorage.Get("TotalSupply");

    [DisplayName("symbol")]
    public static string Symbol() => TokenSymbol;

    [DisplayName("decimals")]
    public static byte Decimals() => TokenDecimals;

    [DisplayName("balanceOf")]
    public static BigInteger BalanceOf(UInt160 account)
    {
        if (account is null || !account.IsValid) throw new Exception("Invalid address");
        return (BigInteger)AccountStorage.Get(account);
    }

    [DisplayName("transfer")]
    public static bool Transfer(UInt160 from, UInt160 to, BigInteger amount, object data = null)
    {
        if (from is null || to is null || !from.IsValid || !to.IsValid) throw new Exception("Invalid address");
        if (amount < 0) throw new Exception("Amount must be positive");

        if (!Runtime.CheckWitness(from)) return false;

        var fromBalance = (BigInteger)AccountStorage.Get(from);
        if (fromBalance < amount) return false;

        AccountStorage.Put(from, fromBalance - amount);
        var toBalance = (BigInteger)AccountStorage.Get(to);
        AccountStorage.Put(to, toBalance + amount);

        OnTransfer(from, to, amount);

        if (ContractManagement.GetContract(to) != null)
            Contract.Call(to, "onNEP17Payment", CallFlags.All, from, amount, data);

        return true;
    }

    [DisplayName("mint")]
    public static void Mint(UInt160 to, BigInteger amount)
    {
        var owner = (UInt160)TokenStorage.Get("Owner");
        if (!Runtime.CheckWitness(owner)) throw new Exception("No authorization");
        if (amount <= 0) throw new Exception("Amount must be positive");

        var totalSupply = (BigInteger)TokenStorage.Get("TotalSupply");
        totalSupply = SafeAdd(totalSupply, amount);
        TokenStorage.Put("TotalSupply", totalSupply);

        var toBalance = (BigInteger)AccountStorage.Get(to);
        AccountStorage.Put(to, SafeAdd(toBalance, amount));

        OnTransfer(null, to, amount);
    }

    [DisplayName("burn")]
    public static void Burn(UInt160 from, BigInteger amount)
    {
        if (!Runtime.CheckWitness(from)) throw new Exception("No authorization");
        if (amount <= 0) throw new Exception("Amount must be positive");

        var fromBalance = (BigInteger)AccountStorage.Get(from);
        if (fromBalance < amount) throw new Exception("Insufficient balance");

        var totalSupply = (BigInteger)TokenStorage.Get("TotalSupply");
        totalSupply = SafeSub(totalSupply, amount);
        TokenStorage.Put("TotalSupply", totalSupply);

        AccountStorage.Put(from, SafeSub(fromBalance, amount));
        OnTransfer(from, null, amount);
    }

    [DisplayName("vote")]
    public static bool Vote(UInt160 voter, UInt160 candidate, BigInteger amount)
    {
        if (voter is null || candidate is null || !voter.IsValid || !candidate.IsValid) 
            throw new Exception("Invalid address");
        if (amount <= 0) throw new Exception("Amount must be positive");

        if (!Runtime.CheckWitness(voter)) return false;

        var voterBalance = (BigInteger)AccountStorage.Get(voter);
        if (voterBalance < amount) return false;

        // Check if voter has existing votes
        var existingVoteKey = new byte[] { }.Concat(voter).Concat(candidate);
        var existingVoteAmount = (BigInteger)VoteStorage.Get(existingVoteKey);

        // Update vote storage
        VoteStorage.Put(existingVoteKey, existingVoteAmount + amount);

        // Lock tokens for voting
        AccountStorage.Put(voter, voterBalance - amount);

        OnVote(voter, candidate, amount);
        return true;
    }

    [DisplayName("unvote")]
    public static bool Unvote(UInt160 voter, UInt160 candidate, BigInteger amount)
    {
        if (voter is null || candidate is null || !voter.IsValid || !candidate.IsValid) 
            throw new Exception("Invalid address");
        if (amount <= 0) throw new Exception("Amount must be positive");

        if (!Runtime.CheckWitness(voter)) return false;

        var voteKey = new byte[] { }.Concat(voter).Concat(candidate);
        var votedAmount = (BigInteger)VoteStorage.Get(voteKey);
        if (votedAmount < amount) return false;

        // Update vote storage
        VoteStorage.Put(voteKey, votedAmount - amount);

        // Return tokens to voter
        var voterBalance = (BigInteger)AccountStorage.Get(voter);
        AccountStorage.Put(voter, voterBalance + amount);

        OnVote(voter, candidate, -amount);
        return true;
    }

    [DisplayName("getVotes")]
    public static BigInteger GetVotes(UInt160 voter, UInt160 candidate)
    {
        if (voter is null || candidate is null || !voter.IsValid || !candidate.IsValid) 
            throw new Exception("Invalid address");

        var voteKey = new byte[] { }.Concat(voter).Concat(candidate);
        return (BigInteger)VoteStorage.Get(voteKey);
    }
    #endregion
}
```
