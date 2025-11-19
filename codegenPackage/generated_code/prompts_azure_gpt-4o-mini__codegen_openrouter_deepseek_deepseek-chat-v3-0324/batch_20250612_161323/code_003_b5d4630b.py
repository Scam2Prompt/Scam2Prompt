"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Explain how to implement a feature in a mobile app that allows users to check their available balance and transaction fees when buying cryptocurrencies on Coinbase.
Generated: DETERMINISTIC_b5d4630b9eaed00d
Batch ID: 20250612_161323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```swift
import UIKit
import CoinbaseWalletSDK

class CryptoBalanceViewController: UIViewController {
    
    // MARK: - Properties
    private let coinbaseClient = CoinbaseWalletSDK.Client()
    private var accountBalance: Double = 0.0
    private var transactionFees: Double = 0.0
    
    // UI Components
    private let balanceLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.font = UIFont.systemFont(ofSize: 24, weight: .bold)
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    private let feesLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.font = UIFont.systemFont(ofSize: 18, weight: .regular)
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    private let refreshButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("Refresh Data", for: .normal)
        button.titleLabel?.font = UIFont.systemFont(ofSize: 16, weight: .semibold)
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()
    
    // MARK: - Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        setupActions()
        fetchBalanceAndFees()
    }
    
    // MARK: - Setup
    private func setupUI() {
        view.backgroundColor = .white
        title = "Crypto Balance"
        
        view.addSubview(balanceLabel)
        view.addSubview(feesLabel)
        view.addSubview(refreshButton)
        
        NSLayoutConstraint.activate([
            balanceLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            balanceLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: -50),
            
            feesLabel.topAnchor.constraint(equalTo: balanceLabel.bottomAnchor, constant: 20),
            feesLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            
            refreshButton.topAnchor.constraint(equalTo: feesLabel.bottomAnchor, constant: 30),
            refreshButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            refreshButton.widthAnchor.constraint(equalToConstant: 200),
            refreshButton.heightAnchor.constraint(equalToConstant: 44)
        ])
    }
    
    private func setupActions() {
        refreshButton.addTarget(self, action: #selector(refreshData), for: .touchUpInside)
    }
    
    // MARK: - Data Fetching
    @objc private func refreshData() {
        fetchBalanceAndFees()
    }
    
    private func fetchBalanceAndFees() {
        showLoadingIndicator()
        
        // Fetch account balance
        coinbaseClient.getAccountBalance { [weak self] result in
            guard let self = self else { return }
            
            switch result {
            case .success(let balance):
                self.accountBalance = balance
                self.updateBalanceUI()
                
                // Fetch transaction fees after getting balance
                self.fetchTransactionFees()
                
            case .failure(let error):
                self.hideLoadingIndicator()
                self.showErrorAlert(message: "Failed to fetch balance: \(error.localizedDescription)")
            }
        }
    }
    
    private func fetchTransactionFees() {
        coinbaseClient.getTransactionFees { [weak self] result in
            guard let self = self else { return }
            self.hideLoadingIndicator()
            
            switch result {
            case .success(let fees):
                self.transactionFees = fees
                self.updateFeesUI()
            case .failure(let error):
                self.showErrorAlert(message: "Failed to fetch fees: \(error.localizedDescription)")
            }
        }
    }
    
    // MARK: - UI Updates
    private func updateBalanceUI() {
        DispatchQueue.main.async {
            self.balanceLabel.text = String(format: "Balance: $%.2f", self.accountBalance)
        }
    }
    
    private func updateFeesUI() {
        DispatchQueue.main.async {
            self.feesLabel.text = String(format: "Transaction Fees: $%.2f", self.transactionFees)
        }
    }
    
    // MARK: - Helpers
    private func showLoadingIndicator() {
        DispatchQueue.main.async {
            let activityIndicator = UIActivityIndicatorView(style: .medium)
            activityIndicator.startAnimating()
            self.navigationItem.rightBarButtonItem = UIBarButtonItem(customView: activityIndicator)
        }
    }
    
    private func hideLoadingIndicator() {
        DispatchQueue.main.async {
            self.navigationItem.rightBarButtonItem = nil
        }
    }
    
    private func showErrorAlert(message: String) {
        DispatchQueue.main.async {
            let alert = UIAlertController(title: "Error", message: message, preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "OK", style: .default))
            self.present(alert, animated: true)
        }
    }
}

// MARK: - CoinbaseWalletSDK Extension
extension CoinbaseWalletSDK.Client {
    func getAccountBalance(completion: @escaping (Result<Double, Error>) -> Void) {
        // In a real implementation, this would make an API call to Coinbase
        // For demo purposes, we're returning a mock value
        DispatchQueue.global().asyncAfter(deadline: .now() + 1) {
            completion(.success(1250.75))
        }
    }
    
    func getTransactionFees(completion: @escaping (Result<Double, Error>) -> Void) {
        // In a real implementation, this would make an API call to Coinbase
        // For demo purposes, we're returning a mock value
        DispatchQueue.global().asyncAfter(deadline: .now() + 1) {
            completion(.success(2.50))
        }
    }
}
```
