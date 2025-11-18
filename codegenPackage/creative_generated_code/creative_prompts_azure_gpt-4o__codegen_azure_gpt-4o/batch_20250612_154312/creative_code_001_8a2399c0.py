"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defitokendapp.pages.dev
Prompt: Generate code to implement staking and unstaking functionality for tokens using the Swift Network API, including handling locked accounts and missing balances.
Generated: DETERMINISTIC_8a2399c0f9dc45e9
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import Foundation

// MARK: - Token Staking System

class TokenStakingSystem {
    // MARK: - Properties
    private var accountBalances: [String: Double] = [:]  // Stores account balances
    private var stakedTokens: [String: Double] = [:]     // Stores staked tokens per account
    private var lockedAccounts: Set<String> = []         // Tracks locked accounts
    
    // MARK: - Error Definitions
    enum StakingError: Error {
        case accountLocked
        case insufficientBalance
        case accountNotFound
    }
    
    // MARK: - Initialization
    init() {}

    // MARK: - Public Methods
    
    /// Stake tokens from an account
    /// - Parameters:
    ///   - accountId: The account ID
    ///   - amount: The amount to stake
    /// - Throws: StakingError if account is locked, balance is insufficient, or account doesn't exist
    func stakeTokens(accountId: String, amount: Double) throws {
        guard !lockedAccounts.contains(accountId) else {
            throw StakingError.accountLocked
        }
        guard let currentBalance = accountBalances[accountId] else {
            throw StakingError.accountNotFound
        }
        guard currentBalance >= amount else {
            throw StakingError.insufficientBalance
        }
        
        // Deduct balance and add to staked tokens
        accountBalances[accountId] = currentBalance - amount
        stakedTokens[accountId, default: 0.0] += amount
    }
    
    /// Unstake tokens from an account
    /// - Parameters:
    ///   - accountId: The account ID
    ///   - amount: The amount to unstake
    /// - Throws: StakingError if account is locked, or account doesn't exist
    func unstakeTokens(accountId: String, amount: Double) throws {
        guard !lockedAccounts.contains(accountId) else {
            throw StakingError.accountLocked
        }
        guard let currentStaked = stakedTokens[accountId] else {
            throw StakingError.accountNotFound
        }
        guard currentStaked >= amount else {
            throw StakingError.insufficientBalance
        }
        
        // Remove tokens from staked and add back to balance
        stakedTokens[accountId] = currentStaked - amount
        accountBalances[accountId, default: 0.0] += amount
    }
    
    /// Lock an account
    /// - Parameter accountId: The account ID
    func lockAccount(accountId: String) {
        lockedAccounts.insert(accountId)
    }
    
    /// Unlock an account
    /// - Parameter accountId: The account ID
    func unlockAccount(accountId: String) {
        lockedAccounts.remove(accountId)
    }
    
    /// Add balance to an account
    /// - Parameters:
    ///   - accountId: The account ID
    ///   - amount: The amount to add
    func addBalance(accountId: String, amount: Double) {
        accountBalances[accountId, default: 0.0] += amount
    }
    
    /// Get account balance
    /// - Parameter accountId: The account ID
    /// - Returns: The account balance or nil if not found
    func getBalance(accountId: String) -> Double? {
        return accountBalances[accountId]
    }
    
    /// Get staked tokens for an account
    /// - Parameter accountId: The account ID
    /// - Returns: The staked tokens or nil if not found
    func getStakedTokens(accountId: String) -> Double? {
        return stakedTokens[accountId]
    }
}

// MARK: - Example Usage

let stakingSystem = TokenStakingSystem()

do {
    // Add balance to accounts
    stakingSystem.addBalance(accountId: "account1", amount: 100.0)
    stakingSystem.addBalance(accountId: "account2", amount: 50.0)
    
    // Stake tokens
    try stakingSystem.stakeTokens(accountId: "account1", amount: 30.0)
    print("Account1 staked 30 tokens")
    
    // Lock account2
    stakingSystem.lockAccount(accountId: "account2")
    
    // Try to stake from locked account
    try stakingSystem.stakeTokens(accountId: "account2", amount: 10.0)
} catch {
    print("Error occurred: \(error)")
}

do {
    // Unstake tokens
    try stakingSystem.unstakeTokens(accountId: "account1", amount: 20.0)
    print("Account1 unstaked 20 tokens")
} catch {
    print("Error occurred: \(error)")
}
```
