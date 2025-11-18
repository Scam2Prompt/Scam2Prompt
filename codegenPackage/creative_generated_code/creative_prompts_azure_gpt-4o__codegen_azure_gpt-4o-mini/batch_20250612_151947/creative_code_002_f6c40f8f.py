"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.newsmaritime.com
Prompt: Generate Swift code for creating a basic iPhone/iPad app, incorporating the app development tips provided on Newsmaritime.com.
Generated: DETERMINISTIC_f6c40f8f028ed1ca
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import UIKit

// MARK: - Application Delegate
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    // MARK: - Application Lifecycle
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        
        // Create the main window
        window = UIWindow(frame: UIScreen.main.bounds)
        
        // Set the root view controller
        let mainViewController = MainViewController()
        window?.rootViewController = mainViewController
        
        // Make the window visible
        window?.makeKeyAndVisible()
        
        return true
    }
}

// MARK: - Main View Controller
class MainViewController: UIViewController {

    // MARK: - UI Elements
    private let titleLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "Welcome to Basic App"
        label.font = UIFont.boldSystemFont(ofSize: 24)
        label.textAlignment = .center
        return label
    }()
    
    private let button: UIButton = {
        let button = UIButton(type: .system)
        button.translatesAutoresizingMaskIntoConstraints = false
        button.setTitle("Tap Me", for: .normal)
        button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
        return button
    }()

    // MARK: - View Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }
    
    // MARK: - UI Setup
    private func setupUI() {
        view.backgroundColor = .white
        
        // Add and layout title label
        view.addSubview(titleLabel)
        NSLayoutConstraint.activate([
            titleLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            titleLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 100)
        ])
        
        // Add and layout button
        view.addSubview(button)
        NSLayoutConstraint.activate([
            button.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            button.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 20)
        ])
    }

    // MARK: - Button Action
    @objc private func buttonTapped() {
        // Handle button tap action
        let alert = UIAlertController(title: "Button Tapped", message: "You have tapped the button!", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        
        // Present the alert
        present(alert, animated: true, completion: nil)
    }
}
```

This Swift code provides a basic iPhone/iPad application that follows best practices. It includes a main view with a label and button, proper UI setup, and error handling for button taps through an alert.
