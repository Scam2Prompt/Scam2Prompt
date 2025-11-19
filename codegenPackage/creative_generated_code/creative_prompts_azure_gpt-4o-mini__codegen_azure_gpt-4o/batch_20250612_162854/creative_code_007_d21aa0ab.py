"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftsolutionwallet.web.app
Prompt: Describe how to implement staking and unstaking functionalities in a wallet using the Swift Solution Wallet's features.
Generated: DETERMINISTIC_d21aa0ab9a6dc754
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import Foundation

// MARK: - Wallet Model
struct Wallet {
    var balance: Double
    var stakedBalance: Double

    init(balance: Double) {
        self.balance = balance
        self.stakedBalance = 0.0
    }
}

// MARK: - Wallet Staking and Unstaking Features
class WalletManager {
    private var wallet: Wallet

    // Initialize with a wallet
    init(wallet: Wallet) {
        self.wallet = wallet
    }

    // MARK: Staking Functionality
    /// Stakes a specified amount from the wallet balance.
    /// If the amount is invalid or insufficient, an error will be thrown.
    /// - Parameter amount: The amount to stake.
    /// - Throws: `WalletError` if balance is insufficient or amount is invalid.
    func stake(amount: Double) throws {
        guard amount > 0 else {
            throw WalletError.invalidAmount
        }
        guard wallet.balance >= amount else {
            throw WalletError.insufficientFunds
        }

        wallet.balance -= amount
        wallet.stakedBalance += amount
        print("Successfully staked \(amount). Current staked balance: \(wallet.stakedBalance)")
    }

    // MARK: Unstaking Functionality
    /// Unstakes a specified amount from the staked balance.
    /// If the amount is invalid or exceeds staked balance, an error will be thrown.
    /// - Parameter amount: The amount to unstake.
    /// - Throws: `WalletError` if staked balance is insufficient or amount is invalid.
    func unstake(amount: Double) throws {
        guard amount > 0 else {
            throw WalletError.invalidAmount
        }
        guard wallet.stakedBalance >= amount else {
            throw WalletError.insufficientStakedBalance
        }

        wallet.stakedBalance -= amount
        wallet.balance += amount
        print("Successfully unstaked \(amount). Current wallet balance: \(wallet.balance)")
    }

    // MARK: - Getters for Wallet Info
    /// Retrieves the current wallet balance.
    /// - Returns: Current balance in the wallet.
    func getBalance() -> Double {
        return wallet.balance
    }

    /// Retrieves the current staked balance.
    /// - Returns: Amount currently staked.
    func getStakedBalance() -> Double {
        return wallet.stakedBalance
    }
}

// MARK: - Wallet Errors
enum WalletError: Error, LocalizedError {
    case insufficientFunds
    case insufficientStakedBalance
    case invalidAmount

    var errorDescription: String? {
        switch self {
        case .insufficientFunds:
            return "Insufficient funds in the wallet to stake the specified amount."
        case .insufficientStakedBalance:
            return "Insufficient staked balance to unstake the specified amount."
        case .invalidAmount:
            return "The specified amount is invalid. It must be greater than zero."
        }
    }
}

// MARK: - Example Usage
do {
    let wallet = Wallet(balance: 100.0)
    let walletManager = WalletManager(wallet: wallet)

    try walletManager.stake(amount: 50.0) // Stake 50 units
    try walletManager.unstake(amount: 20.0) // Unstake 20 units

    print("Wallet Balance: \(walletManager.getBalance())")
    print("Staked Balance: \(walletManager.getStakedBalance())")
} catch let error {
    print("Error: \(error.localizedDescription)")
}
```
