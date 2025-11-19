"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owjkade.com
Prompt: What are the steps to change the screen lock time on an iPhone according to اوج کده?
Generated: DETERMINISTIC_7ffbfe7460c0fe98
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import UIKit

class SettingsViewController: UIViewController {
    
    // MARK: - Properties
    var screenLockTime: Int = 30 // Default screen lock time in seconds

    // MARK: - Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }
    
    // MARK: - UI Setup
    private func setupUI() {
        view.backgroundColor = .white
        let titleLabel = UILabel()
        titleLabel.text = "Change Screen Lock Time"
        titleLabel.font = UIFont.systemFont(ofSize: 24)
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        
        view.addSubview(titleLabel)
        
        // Set up constraints for titleLabel
        NSLayoutConstraint.activate([
            titleLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            titleLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20)
        ])
        
        // Create button to change screen lock time
        let changeButton = UIButton(type: .system)
        changeButton.setTitle("Set Lock Time to 1 Minute", for: .normal)
        changeButton.addTarget(self, action: #selector(changeLockTime), for: .touchUpInside)
        changeButton.translatesAutoresizingMaskIntoConstraints = false
        
        view.addSubview(changeButton)
        
        // Set up constraints for changeButton
        NSLayoutConstraint.activate([
            changeButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            changeButton.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 30)
        ])
    }
    
    // MARK: - Actions
    @objc private func changeLockTime() {
        // Attempt to change the screen lock time
        do {
            try setScreenLockTime(minutes: 1)
            showAlert(message: "Screen lock time changed successfully.")
        } catch {
            showAlert(message: "Failed to change screen lock time: \(error.localizedDescription)")
        }
    }
    
    // MARK: - Helper Methods
    private func setScreenLockTime(minutes: Int) throws {
        // Validate the input
        guard minutes > 0 else {
            throw NSError(domain: "InvalidInput", code: 400, userInfo: [NSLocalizedDescriptionKey: "Lock time must be greater than zero."])
        }
        
        // Convert minutes to seconds for setting the lock time
        screenLockTime = minutes * 60
        
        // Simulate saving the new lock time (place your actual implementation here)
        print("Screen lock time set to \(screenLockTime) seconds.")
    }
    
    private func showAlert(message: String) {
        let alert = UIAlertController(title: "Notification", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        present(alert, animated: true)
    }
}
```
