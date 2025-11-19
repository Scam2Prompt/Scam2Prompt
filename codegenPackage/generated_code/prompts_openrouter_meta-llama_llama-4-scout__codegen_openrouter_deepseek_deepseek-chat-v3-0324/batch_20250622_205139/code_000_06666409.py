"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.org
Prompt: "Write a code snippet using Reown's AppKit to build a user-centric on-chain app experience with utility and usability at its core."
Generated: DETERMINISTIC_06666409b49a841d
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```swift
import AppKit
import ReownKit

// Main application controller
class OnChainAppController: NSViewController {
    
    // MARK: - Properties
    private let walletManager = WalletManager()
    private let chainService = ChainService()
    private let userPreferences = UserPreferences()
    
    private lazy var mainStackView: NSStackView = {
        let stack = NSStackView()
        stack.orientation = .vertical
        stack.alignment = .leading
        stack.distribution = .fill
        stack.spacing = 16
        stack.translatesAutoresizingMaskIntoConstraints = false
        return stack
    }()
    
    private lazy var walletStatusView = WalletStatusView()
    private lazy var transactionView = TransactionView()
    private lazy var utilityPanelView = UtilityPanelView()
    
    // MARK: - Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        configureBindings()
        loadInitialData()
    }
    
    // MARK: - UI Setup
    private func setupUI() {
        view.addSubview(mainStackView)
        
        mainStackView.addArrangedSubview(walletStatusView)
        mainStackView.addArrangedSubview(transactionView)
        mainStackView.addArrangedSubview(utilityPanelView)
        
        NSLayoutConstraint.activate([
            mainStackView.topAnchor.constraint(equalTo: view.topAnchor, constant: 20),
            mainStackView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            mainStackView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            mainStackView.bottomAnchor.constraint(lessThanOrEqualTo: view.bottomAnchor, constant: -20)
        ])
        
        view.wantsLayer = true
        view.layer?.backgroundColor = NSColor.windowBackgroundColor.cgColor
    }
    
    // MARK: - Data Binding
    private func configureBindings() {
        walletManager.onWalletUpdate = { [weak self] wallet in
            self?.walletStatusView.update(with: wallet)
        }
        
        chainService.onTransactionUpdate = { [weak self] transactions in
            self?.transactionView.update(with: transactions)
        }
        
        utilityPanelView.onUtilitySelected = { [weak self] utility in
            self?.handleUtilitySelection(utility)
        }
    }
    
    // MARK: - Data Loading
    private func loadInitialData() {
        Task {
            do {
                async let wallet = walletManager.loadWallet()
                async let transactions = chainService.loadRecentTransactions()
                
                let (loadedWallet, loadedTransactions) = await (try wallet, try transactions)
                
                DispatchQueue.main.async {
                    self.walletStatusView.update(with: loadedWallet)
                    self.transactionView.update(with: loadedTransactions)
                }
            } catch {
                DispatchQueue.main.async {
                    self.showErrorAlert(message: "Failed to load initial data: \(error.localizedDescription)")
                }
            }
        }
    }
    
    // MARK: - Utility Handling
    private func handleUtilitySelection(_ utility: AppUtility) {
        switch utility {
        case .sendTokens:
            presentSendTokensFlow()
        case .receiveTokens:
            presentReceiveTokensFlow()
        case .viewNFTs:
            presentNFTGallery()
        case .settings:
            presentSettings()
        }
    }
    
    private func presentSendTokensFlow() {
        let sendVC = SendTokensViewController()
        presentAsSheet(sendVC)
    }
    
    private func presentReceiveTokensFlow() {
        let receiveVC = ReceiveTokensViewController()
        presentAsSheet(receiveVC)
    }
    
    private func presentNFTGallery() {
        let nftVC = NFTGalleryViewController()
        presentAsModalWindow(nftVC)
    }
    
    private func presentSettings() {
        let settingsVC = SettingsViewController()
        presentAsSheet(settingsVC)
    }
    
    // MARK: - Error Handling
    private func showErrorAlert(message: String) {
        let alert = NSAlert()
        alert.messageText = "Error"
        alert.informativeText = message
        alert.alertStyle = .critical
        alert.addButton(withTitle: "OK")
        alert.beginSheetModal(for: view.window!)
    }
}

// MARK: - Supporting Views
class WalletStatusView: NSView {
    // Implementation details omitted for brevity
    func update(with wallet: Wallet) {}
}

class TransactionView: NSView {
    // Implementation details omitted for brevity
    func update(with transactions: [Transaction]) {}
}

class UtilityPanelView: NSView {
    var onUtilitySelected: ((AppUtility) -> Void)?
    // Implementation details omitted for brevity
}

// MARK: - Supporting Types
enum AppUtility {
    case sendTokens, receiveTokens, viewNFTs, settings
}

struct Wallet {
    let address: String
    let balance: Double
    let currency: String
}

struct Transaction {
    let id: String
    let amount: Double
    let timestamp: Date
    let status: String
}

// MARK: - Services
class WalletManager {
    var onWalletUpdate: ((Wallet) -> Void)?
    
    func loadWallet() async throws -> Wallet {
        // Implementation would connect to wallet provider
        return Wallet(address: "0x123...", balance: 1.5, currency: "ETH")
    }
}

class ChainService {
    var onTransactionUpdate: (([Transaction]) -> Void)?
    
    func loadRecentTransactions() async throws -> [Transaction] {
        // Implementation would connect to blockchain
        return [
            Transaction(id: "0xabc...", amount: 0.1, timestamp: Date(), status: "Confirmed"),
            Transaction(id: "0xdef...", amount: 0.5, timestamp: Date().addingTimeInterval(-3600), status: "Confirmed")
        ]
    }
}

class UserPreferences {
    // User preference management implementation
}

// MARK: - Utility View Controllers
class SendTokensViewController: NSViewController {}
class ReceiveTokensViewController: NSViewController {}
class NFTGalleryViewController: NSViewController {}
class SettingsViewController: NSViewController {}
```
