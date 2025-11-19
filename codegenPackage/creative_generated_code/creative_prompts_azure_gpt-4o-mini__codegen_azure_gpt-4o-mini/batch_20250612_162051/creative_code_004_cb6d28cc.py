"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Implement a feature in a mobile app that provides users with immediate access to emergency cleaning services for poultry buildings, including a direct call option to 06 19 21 12 98.
Generated: DETERMINISTIC_cb6d28cce3910294
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

class EmergencyCleaningServiceViewController: UIViewController {

    // UI Elements
    private let titleLabel: UILabel = {
        let label = UILabel()
        label.text = "Emergency Cleaning Services"
        label.font = UIFont.boldSystemFont(ofSize: 24)
        label.textAlignment = .center
        return label
    }()
    
    private let callButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("Call Emergency Cleaning Service", for: .normal)
        button.titleLabel?.font = UIFont.systemFont(ofSize: 18)
        button.backgroundColor = .systemRed
        button.setTitleColor(.white, for: .normal)
        button.layer.cornerRadius = 10
        button.addTarget(self, action: #selector(callEmergencyService), for: .touchUpInside)
        return button
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        setupView()
    }

    // Set up the UI elements
    private func setupView() {
        view.backgroundColor = .white
        view.addSubview(titleLabel)
        view.addSubview(callButton)
        
        // Layout using Auto Layout
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        callButton.translatesAutoresizingMaskIntoConstraints = false
        
        NSLayoutConstraint.activate([
            titleLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            titleLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 50),

            callButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            callButton.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 20),
            callButton.widthAnchor.constraint(equalToConstant: 250),
            callButton.heightAnchor.constraint(equalToConstant: 50)
        ])
    }

    // Function to handle calling emergency cleaning service
    @objc private func callEmergencyService() {
        let phoneNumber = "0619211298"
        if let url = URL(string: "tel://\(phoneNumber)"), UIApplication.shared.canOpenURL(url) {
            UIApplication.shared.open(url, options: [:], completionHandler: nil)
        } else {
            // Alert the user if the phone call cannot be initiated
            showAlert(title: "Error", message: "Unable to initiate call.")
        }
    }

    // Function to display alerts
    private func showAlert(title: String, message: String) {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alert, animated: true, completion: nil)
    }
}

// Note: This view controller should be instantiated and presented from your app's flow as needed.
```
