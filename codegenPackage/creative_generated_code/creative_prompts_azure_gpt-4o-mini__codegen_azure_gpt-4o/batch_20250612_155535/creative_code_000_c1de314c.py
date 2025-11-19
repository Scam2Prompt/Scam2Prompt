"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qudefiqulabs-merge.pages.dev
Prompt: How can I implement the Swift Network staking protocol to manage my wallet's staked, unstaked, and locked tokens?
Generated: DETERMINISTIC_c1de314c53c8bb92
Batch ID: 20250612_155535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import Foundation

// MARK: - Token Management Structure
/// Enum to represent the state of tokens in the wallet
enum TokenState {
    case staked
    case unstaked
    case locked
}

// MARK: - Wallet Structure
/// Struct to represent the wallet and manage token states
struct Wallet {
    var stakedTokens: Double
    var unstakedTokens: Double
    var lockedTokens: Double
    
    /// Initializes the wallet with default token values
    init(stakedTokens: Double = 0.0, unstakedTokens: Double = 0.0, lockedTokens: Double = 0.0) {
        self.stakedTokens = stakedTokens
        self.unstakedTokens = unstakedTokens
        self.lockedTokens = lockedTokens
    }
    
    /// Stakes a specified amount of tokens
    mutating func stakeTokens(amount: Double) throws {
        guard amount > 0 else {
            throw WalletError.invalidTransaction("Amount to stake must be greater than zero.")
        }
        guard amount <= unstakedTokens else {
            throw WalletError.insufficientFunds("Insufficient unstaked tokens to perform staking.")
        }
        unstakedTokens -= amount
        stakedTokens += amount
    }
    
    /// Unstakes a specified amount of tokens
    mutating func unstakeTokens(amount: Double) throws {
        guard amount > 0 else {
            throw WalletError.invalidTransaction("Amount to unstake must be greater than zero.")
        }
        guard amount <= stakedTokens else {
            throw WalletError.insufficientFunds("Insufficient staked tokens to perform unstaking.")
        }
        stakedTokens -= amount
        unstakedTokens += amount
    }
    
    /// Locks a specified amount of tokens
    mutating func lockTokens(amount: Double) throws {
        guard amount > 0 else {
            throw WalletError.invalidTransaction("Amount to lock must be greater than zero.")
        }
        guard amount <= unstakedTokens else {
            throw WalletError.insufficientFunds("Insufficient unstaked tokens to perform locking.")
        }
        unstakedTokens -= amount
        lockedTokens += amount
    }
    
    /// Unlocks a specified amount of tokens
    mutating func unlockTokens(amount: Double) throws {
        guard amount > 0 else {
            throw WalletError.invalidTransaction("Amount to unlock must be greater than zero.")
        }
        guard amount <= lockedTokens else {
            throw WalletError.insufficientFunds("Insufficient locked tokens to perform unlocking.")
        }
        lockedTokens -= amount
        unstakedTokens += amount
    }
}

// MARK: - Wallet Error Handling
/// Enum to represent wallet-related errors
enum WalletError: Error {
    case insufficientFunds(String)
    case invalidTransaction(String)
}

// MARK: - Demonstration
/// Example usage of the Wallet struct and token management functions
func main() {
    var myWallet = Wallet(stakedTokens: 100.0, unstakedTokens: 50.0, lockedTokens: 20.0)
    
    do {
        print("Initial Wallet:", myWallet)
        
        try myWallet.stakeTokens(amount: 30.0)
        print("After staking 30 tokens:", myWallet)
        
        try myWallet.unstakeTokens(amount: 50.0)
        print("After unstaking 50 tokens:", myWallet)
        
        try myWallet.lockTokens(amount: 10.0)
        print("After locking 10 tokens:", myWallet)
        
        try myWallet.unlockTokens(amount: 5.0)
        print("After unlocking 5 tokens:", myWallet)
    } catch {
        print("Error:", error)
    }
}

// Run the demonstration
main()
```
