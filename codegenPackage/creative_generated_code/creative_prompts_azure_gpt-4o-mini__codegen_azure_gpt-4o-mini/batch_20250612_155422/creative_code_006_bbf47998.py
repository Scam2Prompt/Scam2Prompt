"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-96qjy03xf-reown-com.vercel.app
Prompt: Create a demo code that uses sample wallets with all features enabled in AppKit.
Generated: DETERMINISTIC_bbf4799864b5ed1d
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import AppKit

// Define a structure for a Wallet that holds essential wallet information
struct Wallet {
    var name: String
    var balance: Double
    
    // Initialize a new wallet with a name and balance
    init(name: String, balance: Double) {
        self.name = name
        self.balance = balance
    }
    
    // Function to deposit an amount to the wallet
    mutating func deposit(amount: Double) throws {
        guard amount > 0 else {
            throw WalletError.invalidAmount("Deposit amount must be greater than zero.")
        }
        balance += amount
    }
    
    // Function to withdraw an amount from the wallet
    mutating func withdraw(amount: Double) throws {
        guard amount > 0 else {
            throw WalletError.invalidAmount("Withdrawal amount must be greater than zero.")
        }
        guard amount <= balance else {
            throw WalletError.insufficientFunds("Insufficient funds for the withdrawal.")
        }
        balance -= amount
    }
}

// Define possible errors related to wallet operations
enum WalletError: Error {
    case invalidAmount(String)
    case insufficientFunds(String)
}

// Sample usage of the Wallet structure with error handling
func demoWalletUsage() {
    // Create a sample wallet with an initial balance
    var myWallet = Wallet(name: "Demo Wallet", balance: 100.0)
    
    do {
        // Attempt to deposit a valid amount
        try myWallet.deposit(amount: 50.0)
        print("Deposited $50. New balance: $\(myWallet.balance)")
        
        // Attempt to withdraw a valid amount
        try myWallet.withdraw(amount: 30.0)
        print("Withdrew $30. New balance: $\(myWallet.balance)")
        
        // Attempt to withdraw an amount exceeding the balance
        try myWallet.withdraw(amount: 150.0)
    } catch {
        // Handle any errors thrown during wallet operations
        print("Error: \(error)")
    }
}

// Run the demo wallet usage function
demoWalletUsage()
```
