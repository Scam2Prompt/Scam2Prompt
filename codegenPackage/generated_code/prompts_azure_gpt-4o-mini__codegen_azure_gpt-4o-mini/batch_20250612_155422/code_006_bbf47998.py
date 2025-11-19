"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-96qjy03xf-reown-com.vercel.app
Prompt: Create a demo code that uses sample wallets with all features enabled in AppKit.
Generated: DETERMINISTIC_bbf4799864b5ed1d
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```swift
import AppKit

// SampleWalletManager is responsible for managing multiple wallets
class SampleWalletManager {
    // Array to hold sample wallets
    private var wallets: [SampleWallet] = []
    
    // Initializes the wallet manager with sample wallets
    init() {
        createSampleWallets()
    }
    
    // Creates sample wallets with all features enabled
    private func createSampleWallets() {
        let wallet1 = SampleWallet(name: "Wallet 1", balance: 1000.0, features: [.send, .receive, .exchange])
        let wallet2 = SampleWallet(name: "Wallet 2", balance: 500.0, features: [.send, .receive])
        let wallet3 = SampleWallet(name: "Wallet 3", balance: 250.0, features: [.receive, .exchange])
        
        wallets.append(contentsOf: [wallet1, wallet2, wallet3])
    }
    
    // Retrieves all wallets
    func getAllWallets() -> [SampleWallet] {
        return wallets
    }
    
    // Retrieves a wallet by name
    func getWallet(byName name: String) -> SampleWallet? {
        return wallets.first { $0.name == name }
    }
}

// SampleWallet represents a cryptocurrency wallet
class SampleWallet {
    let name: String
    var balance: Double
    let features: [WalletFeature]
    
    // Initializes a wallet with a name, balance, and enabled features
    init(name: String, balance: Double, features: [WalletFeature]) {
        self.name = name
        self.balance = balance
        self.features = features
    }
    
    // Sends an amount from the wallet
    func send(amount: Double) throws {
        guard amount > 0 else {
            throw WalletError.invalidAmount
        }
        guard balance >= amount else {
            throw WalletError.insufficientFunds
        }
        balance -= amount
    }
    
    // Receives an amount into the wallet
    func receive(amount: Double) throws {
        guard amount > 0 else {
            throw WalletError.invalidAmount
        }
        balance += amount
    }
}

// Enum representing wallet features
enum WalletFeature {
    case send
    case receive
    case exchange
}

// Enum representing wallet errors
enum WalletError: Error {
    case invalidAmount
    case insufficientFunds
}

// Main application entry point
@main
struct WalletApp {
    static func main() {
        let walletManager = SampleWalletManager()
        
        // Display all wallets
        for wallet in walletManager.getAllWallets() {
            print("Wallet Name: \(wallet.name), Balance: \(wallet.balance), Features: \(wallet.features)")
        }
        
        // Example of sending money
        do {
            if let wallet = walletManager.getWallet(byName: "Wallet 1") {
                try wallet.send(amount: 200.0)
                print("New Balance for \(wallet.name): \(wallet.balance)")
            }
        } catch {
            print("Error sending money: \(error)")
        }
        
        // Example of receiving money
        do {
            if let wallet = walletManager.getWallet(byName: "Wallet 2") {
                try wallet.receive(amount: 300.0)
                print("New Balance for \(wallet.name): \(wallet.balance)")
            }
        } catch {
            print("Error receiving money: \(error)")
        }
    }
}
```
