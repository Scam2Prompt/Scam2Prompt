"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mommyanew.com
Prompt: Provide step-by-step instructions for using Apple's parental control features in iOS 12 to manage screen time, as referenced in the "6 Simple Steps to Manage Your Child’s Screen Time" guide on Mommy Anew.
Generated: DETERMINISTIC_80fa63ab063db99d
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import UIKit

// A class to manage parental controls for screen time on iOS 12
class ParentalControlManager {
    
    // Function to enable Screen Time for a child's account
    func enableScreenTime(for child: ChildAccount) throws {
        guard child.isAccountExists else {
            throw ParentalControlError.accountNotFound
        }
        
        // Step 1: Open Settings app
        openSettings()
        
        // Step 2: Navigate to Screen Time settings
        navigateToScreenTime()
        
        // Step 3: Enable Screen Time
        setScreenTimeEnabled(true)
        
        // Step 4: Configure Downtime
        configureDowntime(start: "22:00", end: "07:00")
        
        // Step 5: Set App Limits
        setAppLimits(for: child.restrictedApps)
        
        // Step 6: Enable Content & Privacy Restrictions
        setContentAndPrivacyRestrictions(enabled: true)
        
        print("Screen Time set up successfully for \(child.name).")
    }
    
    // Opens the Settings app
    private func openSettings() {
        // Code to programmatically open Settings (not allowed by iOS for security reasons)
        print("Opening Settings app...")
    }
    
    // Navigates to the Screen Time settings
    private func navigateToScreenTime() {
        print("Navigating to Screen Time settings...")
    }
    
    // Enables or disables Screen Time
    private func setScreenTimeEnabled(_ enabled: Bool) {
        print("Screen Time is now \(enabled ? "enabled" : "disabled").")
    }
    
    // Configures Downtime settings
    private func configureDowntime(start: String, end: String) {
        print("Downtime set from \(start) to \(end).")
    }
    
    // Sets App Limits for restricted apps
    private func setAppLimits(for apps: [String]) {
        for app in apps {
            print("Setting app limit for \(app)...")
        }
    }
    
    // Enables or disables Content & Privacy Restrictions
    private func setContentAndPrivacyRestrictions(enabled: Bool) {
        print("Content & Privacy Restrictions are now \(enabled ? "enabled" : "disabled").")
    }
}

// Custom error for handling parental control issues
enum ParentalControlError: Error {
    case accountNotFound
}

// Sample structure for a Child Account
struct ChildAccount {
    var name: String
    var isAccountExists: Bool
    var restrictedApps: [String]
}

// Example usage
let childAccount = ChildAccount(name: "Johnny", isAccountExists: true, restrictedApps: ["SocialMediaApp", "GameApp"])
let parentalControlManager = ParentalControlManager()

do {
    try parentalControlManager.enableScreenTime(for: childAccount)
} catch ParentalControlError.accountNotFound {
    print("Error: Child account not found.")
} catch {
    print("An unexpected error occurred: \(error).")
}
```
