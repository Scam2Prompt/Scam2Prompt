"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnalkhedmad.com
Prompt: How can I implement a feature in a mobile app that showcases the benefits of MagSafe accessories for different iPhone models?
Generated: DETERMINISTIC_98932b7364eeaf58
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import UIKit

/// A view controller that showcases the benefits of MagSafe accessories for different iPhone models.
class MagSafeBenefitsViewController: UIViewController {
    
    // MARK: - Properties
    
    private let iphoneModels: [String] = [
        "iPhone 12",
        "iPhone 13",
        "iPhone 14",
        "iPhone 15"
    ]
    
    private let benefits: [String: String] = [
        "iPhone 12": "MagSafe accessories easily snap on and off with a secure attachment.",
        "iPhone 13": "Enhanced wireless charging capabilities with up to 15W of power.",
        "iPhone 14": "A wide range of accessories including cases, wallets, and chargers.",
        "iPhone 15": "Improved alignment for accessories, reducing friction and wear."
    ]
    
    private let tableView = UITableView()

    // MARK: - Lifecycle Methods
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }
    
    // MARK: - UI Setup
    
    private func setupUI() {
        view.backgroundColor = .white
        title = "MagSafe Benefits"

        // Configure table view
        tableView.delegate = self
        tableView.dataSource = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
        
        // Add table view to the main view
        view.addSubview(tableView)

        // Set up table view constraints
        tableView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor)
        ])
    }
}

// MARK: - UITableViewDataSource

extension MagSafeBenefitsViewController: UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return iphoneModels.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        let model = iphoneModels[indexPath.row]
        cell.textLabel?.text = model
        return cell
    }
}

// MARK: - UITableViewDelegate

extension MagSafeBenefitsViewController: UITableViewDelegate {
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        // Deselect the cell
        tableView.deselectRow(at: indexPath, animated: true)
        
        let selectedModel = iphoneModels[indexPath.row]
        showBenefits(for: selectedModel)
    }
    
    private func showBenefits(for model: String) {
        guard let benefit = benefits[model] else { return }
        
        let alertController = UIAlertController(title: model, message: benefit, preferredStyle: .alert)
        alertController.addAction(UIAlertAction(title: "OK", style: .default))
        
        // Present the alert
        present(alertController, animated: true)
    }
}
```
