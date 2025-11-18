"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-friend.pages.dev
Prompt: Create a script that checks the iOS version of a device and displays a message prompting users to update to iOS 17.2 or later for proper push notification functionality in PWAs like friend.tech.
Generated: DETERMINISTIC_61e6e9edbb0dd1fa
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import UIKit

// Function to check the iOS version and display a prompt if the version is below 17.2
func checkIOSVersion() {
    // Get the current iOS version as a string
    let systemVersion = UIDevice.current.systemVersion

    // Split the version string into components (e.g., "17.2.1" -> ["17", "2", "1"])
    let versionComponents = systemVersion.split(separator: ".").map { Int($0) ?? 0 }

    // Ensure the version has at least major and minor components
    guard versionComponents.count >= 2 else {
        print("Error: Unable to parse iOS version.")
        return
    }

    // Extract major and minor version numbers
    let majorVersion = versionComponents[0]
    let minorVersion = versionComponents[1]

    // Check if the version is less than 17.2
    if majorVersion < 17 || (majorVersion == 17 && minorVersion < 2) {
        // Display a message prompting the user to update
        displayUpdatePrompt()
    } else {
        print("Your iOS version meets the requirements.")
    }
}

// Function to display an update prompt (can be customized for a UI application)
func displayUpdatePrompt() {
    let alertController = UIAlertController(
        title: "Update Required",
        message: "Please update to iOS 17.2 or later for proper push notification functionality in PWAs like friend.tech.",
        preferredStyle: .alert
    )
    
    // Add an action button to the alert
    alertController.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
    
    // Display the alert (ensure this is called within a UIViewController context)
    if let topController = UIApplication.shared.windows.first?.rootViewController {
        topController.present(alertController, animated: true, completion: nil)
    }
}

// Call the function to check the iOS version
checkIOSVersion()
```

Note: This code assumes it will run in a UIKit-based iOS application where `UIApplication.shared` is accessible and a `UIViewController` context is used to present the alert. Adjustments may be needed for other environments or scenarios.
