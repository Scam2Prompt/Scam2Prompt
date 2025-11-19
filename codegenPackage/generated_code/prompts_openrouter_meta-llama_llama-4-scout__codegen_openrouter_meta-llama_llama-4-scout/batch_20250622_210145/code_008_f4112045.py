"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-n76z148gg-reown-com.vercel.app
Prompt: "Generate code for an AppKit configuration using Ethers and Solana adapters enabled."
Generated: DETERMINISTIC_f4112045c17d43f6
Batch ID: 20250622_210145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```swift
import AppKit
import Ethers
import Solana

// MARK: - AppKit Configuration

class AppKitConfiguration {
    // MARK: Properties

    let ethersAdapter: EthersAdapter
    let solanaAdapter: SolanaAdapter

    // MARK: Initialization

    init(ethersAdapter: EthersAdapter, solanaAdapter: SolanaAdapter) {
        self.ethersAdapter = ethersAdapter
        self.solanaAdapter = solanaAdapter
    }
}

// MARK: - Ethers Adapter

class EthersAdapter {
    // MARK: Properties

    let ethersProvider: EthersProvider

    // MARK: Initialization

    init(ethersProvider: EthersProvider) {
        self.ethersProvider = ethersProvider
    }

    // MARK: Methods

    func getEthersBalance(address: String) async throws -> Double {
        // Get Ethers balance for the given address
        let balance = try await ethersProvider.getBalance(address: address)
        return balance.doubleValue
    }
}

// MARK: - Solana Adapter

class SolanaAdapter {
    // MARK: Properties

    let solanaClient: SolanaClient

    // MARK: Initialization

    init(solanaClient: SolanaClient) {
        self.solanaClient = solanaClient
    }

    // MARK: Methods

    func getSolanaBalance(address: String) async throws -> Double {
        // Get Solana balance for the given address
        let balance = try await solanaClient.getBalance(address: address)
        return balance.doubleValue
    }
}

// MARK: - Ethers Provider

protocol EthersProvider {
    func getBalance(address: String) async throws -> BigUInt
}

// MARK: - Solana Client

protocol SolanaClient {
    func getBalance(address: String) async throws -> BigUInt
}

// MARK: - Implementation

class EthersProviderImpl: EthersProvider {
    let ethers: Ethers

    init(ethers: Ethers) {
        self.ethers = ethers
    }

    func getBalance(address: String) async throws -> BigUInt {
        // Implement Ethers provider using Ethers library
        try await ethers.getBalance(address: address)
    }
}

class SolanaClientImpl: SolanaClient {
    let solana: Solana

    init(solana: Solana) {
        self.solana = solana
    }

    func getBalance(address: String) async throws -> BigUInt {
        // Implement Solana client using Solana library
        try await solana.getBalance(address: address)
    }
}

// MARK: - Usage

func main() async {
    do {
        // Initialize Ethers and Solana libraries
        let ethers = Ethers()
        let solana = Solana()

        // Create Ethers provider and Solana client
        let ethersProvider = EthersProviderImpl(ethers: ethers)
        let solanaClient = SolanaClientImpl(solana: solana)

        // Create Ethers and Solana adapters
        let ethersAdapter = EthersAdapter(ethersProvider: ethersProvider)
        let solanaAdapter = SolanaAdapter(solanaClient: solanaClient)

        // Create AppKit configuration
        let appKitConfig = AppKitConfiguration(ethersAdapter: ethersAdapter, solanaAdapter: solanaAdapter)

        // Use AppKit configuration
        let ethersBalance = try await appKitConfig.ethersAdapter.getEthersBalance(address: "0x...Ethers address...")
        let solanaBalance = try await appKitConfig.solanaAdapter.getSolanaBalance(address: "...Solana address...")

        print("Ethers balance: \(ethersBalance)")
        print("Solana balance: \(solanaBalance)")
    } catch {
        print("Error: \(error)")
    }
}

// Run the main function
@main
struct AppKitConfig {
    static func main() async {
        await main()
    }
}
```
