"""
Generated Code Metadata:
========================
Original URL: https://applovin.in
Prompt: Write code to implement AppLovin's MAX SDK for an 8X increase in ARPDAU in a utility app.
Generated: DETERMINISTIC_c16527ef16cc44ef
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```swift
import UIKit
import AppLovinSDK

class AppLovinManager: NSObject, MAAdDelegate {
    
    // Singleton instance for AppLovinManager
    static let shared = AppLovinManager()
    
    private var interstitialAd: MAInterstitialAd?
    
    // Initialize the AppLovin SDK
    private override init() {
        super.init()
        // Initialize the SDK
        ALSdk.initializeSdk { (sdk) in
            print("AppLovin SDK initialized: \(sdk)")
        }
    }
    
    // Load an interstitial ad
    func loadInterstitialAd() {
        interstitialAd = MAInterstitialAd(adUnitIdentifier: "YOUR_AD_UNIT_ID")
        interstitialAd?.delegate = self
        interstitialAd?.loadAd()
    }
    
    // Show the interstitial ad if it's loaded
    func showInterstitialAd(from viewController: UIViewController) {
        guard let interstitialAd = interstitialAd else {
            print("Interstitial ad is not loaded yet.")
            return
        }
        
        if interstitialAd.isReady {
            interstitialAd.show(for: viewController)
        } else {
            print("Interstitial ad is not ready to be shown.")
        }
    }
    
    // MARK: - MAAdDelegate Methods
    
    func didLoad(_ ad: MAAd) {
        print("Interstitial ad loaded successfully.")
    }
    
    func didFailToLoadAd(for adUnitIdentifier: String, error: MAError) {
        print("Failed to load interstitial ad: \(error.message)")
        // Optionally, retry loading the ad
        loadInterstitialAd()
    }
    
    func didDisplay(_ ad: MAAd) {
        print("Interstitial ad displayed.")
    }
    
    func didHide(_ ad: MAAd) {
        print("Interstitial ad hidden.")
        // Load a new ad after the current one is hidden
        loadInterstitialAd()
    }
    
    func didClick(_ ad: MAAd) {
        print("Interstitial ad clicked.")
    }
    
    func didFail(toDisplay ad: MAAd, error: MAError) {
        print("Failed to display interstitial ad: \(error.message)")
    }
}

// Usage example in a view controller
class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Load the interstitial ad when the view loads
        AppLovinManager.shared.loadInterstitialAd()
    }
    
    @IBAction func showAdButtonTapped(_ sender: UIButton) {
        // Show the interstitial ad when the button is tapped
        AppLovinManager.shared.showInterstitialAd(from: self)
    }
}
```

**Note:** Replace `"YOUR_AD_UNIT_ID"` with your actual AppLovin ad unit ID. Ensure that you have integrated the AppLovin SDK correctly in your project and have the necessary permissions and configurations in your Info.plist file.
