"""
Generated Code Metadata:
========================
Original URL: https://reown.com
Prompt: How can I use Reown's AppKit to build user-centric onchain applications with advanced feature stacks?
Generated: DETERMINISTIC_462c057d4bd70d93
Batch ID: 20250612_135046
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```swift
import SwiftUI
import AppKit
import Combine
import Web3
import Web3ContractABI
import Web3PromiseKit

// MARK: - Onchain Application Core

class OnchainAppCore: ObservableObject {
    private var web3: Web3?
    private var cancellables = Set<AnyCancellable>()
    
    @Published var userAddress: String = ""
    @Published var balance: String = "0"
    @Published var isLoading = false
    @Published var errorMessage: String?
    
    init() {
        setupWeb3()
    }
    
    private func setupWeb3() {
        guard let url = URL(string: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID") else {
            errorMessage = "Invalid Infura URL"
            return
        }
        
        web3 = Web3(rpcURL: url.absoluteString)
    }
    
    func connectWallet() {
        isLoading = true
        errorMessage = nil
        
        // In a real app, you would integrate with WalletConnect or similar
        // This is a simplified example
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            self.userAddress = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e" // Example address
            self.fetchBalance()
        }
    }
    
    func fetchBalance() {
        guard let web3 = web3, !userAddress.isEmpty else {
            errorMessage = "Web3 not initialized or no user address"
            isLoading = false
            return
        }
        
        firstly {
            try web3.eth.getBalance(address: EthereumAddress(hex: userAddress, eip55: true))
        }.done { balance in
            self.balance = "\(balance)"
            self.isLoading = false
        }.catch { error in
            self.errorMessage = error.localizedDescription
            self.isLoading = false
        }
    }
    
    func executeContractFunction(
        contractAddress: String,
        abi: String,
        functionName: String,
        parameters: [AnyObject]
    ) -> Promise<[String: Any]> {
        return Promise { seal in
            guard let web3 = web3, !userAddress.isEmpty else {
                seal.reject(OnchainError.web3NotInitialized)
                return
            }
            
            guard let contractAddress = EthereumAddress(hex: contractAddress, eip55: true) else {
                seal.reject(OnchainError.invalidContractAddress)
                return
            }
            
            let contract = web3.eth.Contract(json: abi, address: contractAddress)
            
            firstly {
                try contract.method(functionName, parameters: parameters)?.call()
            }.done { result in
                seal.fulfill(result)
            }.catch { error in
                seal.reject(error)
            }
        }
    }
}

enum OnchainError: Error {
    case web3NotInitialized
    case invalidContractAddress
    case transactionFailed
}

// MARK: - User Interface

struct OnchainAppView: View {
    @StateObject private var appCore = OnchainAppCore()
    
    var body: some View {
        VStack(spacing: 20) {
            if appCore.isLoading {
                ProgressView()
                    .scaleEffect(1.5)
            }
            
            if let error = appCore.errorMessage {
                Text("Error: \(error)")
                    .foregroundColor(.red)
            }
            
            if appCore.userAddress.isEmpty {
                Button("Connect Wallet") {
                    appCore.connectWallet()
                }
                .buttonStyle(PrimaryButtonStyle())
            } else {
                VStack(alignment: .leading, spacing: 10) {
                    Text("Wallet Address:")
                        .font(.headline)
                    Text(appCore.userAddress)
                        .font(.caption)
                        .truncationMode(.middle)
                        .lineLimit(1)
                    
                    Text("Balance: \(appCore.balance) ETH")
                        .font(.headline)
                }
                .padding()
                .background(Color.gray.opacity(0.1))
                .cornerRadius(10)
                
                Button("Refresh Balance") {
                    appCore.fetchBalance()
                }
                .buttonStyle(SecondaryButtonStyle())
                
                // Example contract interaction
                Button("Call Contract Function") {
                    callExampleContractFunction()
                }
                .buttonStyle(PrimaryButtonStyle())
            }
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
    
    private func callExampleContractFunction() {
        let exampleABI = """
        [{
            "inputs": [],
            "name": "getValue",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function"
        }]
        """
        
        appCore.executeContractFunction(
            contractAddress: "0xContractAddress",
            abi: exampleABI,
            functionName: "getValue",
            parameters: []
        ).done { result in
            print("Contract call result: \(result)")
        }.catch { error in
            appCore.errorMessage = error.localizedDescription
        }
    }
}

// MARK: - UI Components

struct PrimaryButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .cornerRadius(8)
            .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
    }
}

struct SecondaryButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .background(Color.gray.opacity(0.2))
            .foregroundColor(.primary)
            .cornerRadius(8)
            .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
    }
}

// MARK: - App Entry

@main
struct OnchainApp: App {
    var body: some Scene {
        WindowGroup {
            OnchainAppView()
                .frame(minWidth: 400, minHeight: 300)
        }
    }
}
```
