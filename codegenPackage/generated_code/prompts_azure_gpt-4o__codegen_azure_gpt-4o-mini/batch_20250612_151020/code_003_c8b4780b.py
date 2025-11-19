"""
Generated Code Metadata:
========================
Original URL: https://mommyanew.com
Prompt: Suggest tools or libraries for creating a mobile app that integrates Apple's Screen Time API to help single mothers manage their children's device usage, inspired by the tips shared on Mommy Anew.
Generated: DETERMINISTIC_c8b4780be088f817
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```swift
import UIKit
import ScreenTime // Importing Screen Time framework

/// A class to manage Screen Time functionalities for monitoring children's device usage.
class ScreenTimeManager {
    
    // Singleton instance for easy access throughout the app
    static let shared = ScreenTimeManager()
    
    private init() {
        // Private initializer to enforce singleton pattern
    }
    
    /// Requests access to Screen Time data.
    /// - Parameter completion: A closure that is called with the result of the access request.
    func requestAccess(completion: @escaping (Bool, Error?) -> Void) {
        // Check if the Screen Time API is available
        guard #available(iOS 12.0, *) else {
            completion(false, NSError(domain: "ScreenTimeError", code: 1, userInfo: [NSLocalizedDescriptionKey: "Screen Time API is not available on this iOS version."]))
            return
        }
        
        // Request access to Screen Time data
        STScreenTimeAuthorization.requestAuthorization { (granted, error) in
            completion(granted, error)
        }
    }
    
    /// Fetches the usage data for a specific app.
    /// - Parameter appIdentifier: The bundle identifier of the app to fetch usage data for.
    /// - Parameter completion: A closure that is called with the usage data or an error.
    func fetchAppUsage(appIdentifier: String, completion: @escaping (STAppUsage?, Error?) -> Void) {
        // Check if the Screen Time API is available
        guard #available(iOS 12.0, *) else {
            completion(nil, NSError(domain: "ScreenTimeError", code: 1, userInfo: [NSLocalizedDescriptionKey: "Screen Time API is not available on this iOS version."]))
            return
        }
        
        // Fetch usage data for the specified app
        STScreenTime.fetchAppUsage(for: appIdentifier) { (usage, error) in
            if let error = error {
                completion(nil, error)
            } else {
                completion(usage, nil)
            }
        }
    }
}

/// A view controller to display and manage children's device usage.
class UsageViewController: UIViewController {
    
    // UI Elements
    private var usageLabel: UILabel!
    private var fetchUsageButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        requestScreenTimeAccess()
    }
    
    /// Sets up the user interface elements.
    private func setupUI() {
        // Initialize and configure the label
        usageLabel = UILabel()
        usageLabel.translatesAutoresizingMaskIntoConstraints = false
        usageLabel.text = "Usage Data will appear here."
        view.addSubview(usageLabel)
        
        // Initialize and configure the button
        fetchUsageButton = UIButton(type: .system)
        fetchUsageButton.setTitle("Fetch Usage", for: .normal)
        fetchUsageButton.addTarget(self, action: #selector(fetchUsageTapped), for: .touchUpInside)
        fetchUsageButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(fetchUsageButton)
        
        // Layout constraints
        NSLayoutConstraint.activate([
            usageLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            usageLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            fetchUsageButton.topAnchor.constraint(equalTo: usageLabel.bottomAnchor, constant: 20),
            fetchUsageButton.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
    }
    
    /// Requests access to Screen Time data.
    private func requestScreenTimeAccess() {
        ScreenTimeManager.shared.requestAccess { (granted, error) in
            if let error = error {
                self.showError(error)
            } else if granted {
                print("Access granted to Screen Time data.")
            } else {
                self.showError(NSError(domain: "ScreenTimeError", code: 2, userInfo: [NSLocalizedDescriptionKey: "Access to Screen Time data was denied."]))
            }
        }
    }
    
    /// Fetches the app usage data when the button is tapped.
    @objc private func fetchUsageTapped() {
        let appIdentifier = "com.example.app" // Replace with the actual app identifier
        
        ScreenTimeManager.shared.fetchAppUsage(appIdentifier: appIdentifier) { (usage, error) in
            if let error = error {
                self.showError(error)
            } else if let usage = usage {
                self.usageLabel.text = "Usage: \(usage.totalUsageTime) seconds"
            }
        }
    }
    
    /// Displays an error message to the user.
    /// - Parameter error: The error to display.
    private func showError(_ error: Error) {
        let alert = UIAlertController(title: "Error", message: error.localizedDescription, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alert, animated: true, completion: nil)
    }
}
```
