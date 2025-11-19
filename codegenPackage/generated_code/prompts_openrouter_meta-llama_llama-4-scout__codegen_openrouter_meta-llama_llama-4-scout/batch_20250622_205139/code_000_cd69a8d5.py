"""
Generated Code Metadata:
========================
Original URL: https://reown.com
Prompt: "Write a code example using Reown's AppKit to build a user-centric on-chain app experience with utility and usability at its core."
Generated: DETERMINISTIC_cd69a8d59e2f997c
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```swift
// AppDelegate.swift

import AppKit
import Foundation

@main
class AppDelegate: NSObject, NSApplicationDelegate {

    // MARK: - Properties

    let window: NSWindow

    // MARK: - Initialization

    override init() {
        window = NSWindow(contentRect: NSRect(x: 0, y: 0, width: 800, height: 600),
                          styleMask: [.titled, .closable, .miniaturizable],
                          backing: .buffered,
                          defer: false)
        window.center()
        window.title = "Reown AppKit Example"
    }

    // MARK: - NSApplicationDelegate

    func applicationDidFinishLaunching(_ aNotification: Notification) {
        // Initialize the UI
        let viewController = ViewController()
        window.contentView?.addSubview(viewController.view)
        window.makeKeyAndVisible()
    }

    func applicationWillTerminate(_ aNotification: Notification) {
        // Insert code here to tear down your application
    }
}

// ViewController.swift

import AppKit
import Foundation

class ViewController: NSViewController {

    // MARK: - Properties

    let connectButton: NSButton
    let addressLabel: NSTextField
    let balanceLabel: NSTextField

    // MARK: - Initialization

    override init() {
        connectButton = NSButton(title: "Connect Wallet", target: self, action: #selector(connectWallet))
        addressLabel = NSTextField(string: "")
        balanceLabel = NSTextField(string: "")

        super.init(nibName: nil, bundle: nil)
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    // MARK: - NSViewController

    override func viewDidLoad() {
        super.viewDidLoad()

        // Setup the UI
        view.frame = NSRect(x: 0, y: 0, width: 800, height: 600)
        view.addSubview(connectButton)
        connectButton.frame = NSRect(x: 350, y: 275, width: 100, height: 25)

        view.addSubview(addressLabel)
        addressLabel.frame = NSRect(x: 350, y: 250, width: 200, height: 25)

        view.addSubview(balanceLabel)
        balanceLabel.frame = NSRect(x: 350, y: 225, width: 200, height: 25)
    }

    // MARK: - Actions

    @objc func connectWallet() {
        // Implement wallet connection logic here
        // For demonstration purposes, we'll just display a dummy address and balance
        addressLabel.stringValue = "0x1234567890abcdef"
        balanceLabel.stringValue = "100 ETH"
    }
}
```
