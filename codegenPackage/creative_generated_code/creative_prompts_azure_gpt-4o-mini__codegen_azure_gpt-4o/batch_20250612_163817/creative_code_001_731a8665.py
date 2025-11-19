"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evamobi.com
Prompt: Write a code snippet for a mobile app that integrates interactive in-app ads to improve user experience and retention.
Generated: DETERMINISTIC_731a8665d7ec1166
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a code snippet in Swift for integrating interactive in-app ads into an iOS mobile app using Google's AdMob SDK:

```swift
import UIKit
import GoogleMobileAds

class ViewController: UIViewController, GADFullScreenContentDelegate {

    // Declare a variable for the Interstitial Ad
    private var interstitial: GADInterstitialAd?

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        
        // Load interstitial ad
        loadInterstitialAd()
        
        // Add a button to show the ad
        let showAdButton = UIButton(type: .system)
        showAdButton.setTitle("Show Ad", for: .normal)
        showAdButton.addTarget(self, action: #selector(showInterstitialAd), for: .touchUpInside)
        showAdButton.frame = CGRect(x: 100, y: 100, width: 200, height: 50)
        view.addSubview(showAdButton)
    }
    
    /// Loads an interstitial ad asynchronously
    private func loadInterstitialAd() {
        let adUnitID = "your-admob-interstitial-ad-unit-id" // Replace with your Ad Unit ID
        let request = GADRequest()
        
        GADInterstitialAd.load(
            withAdUnitID: adUnitID,
            request: request,
            completionHandler: { [weak self] ad, error in
                if let error = error {
                    print("Failed to load interstitial ad: \(error.localizedDescription)")
                    return
                }
                
                self?.interstitial = ad
                self?.interstitial?.fullScreenContentDelegate = self
                print("Interstitial ad loaded successfully.")
            }
        )
    }
    
    /// Displays the interstitial ad if it's ready
    @objc private func showInterstitialAd() {
        guard let interstitial = interstitial else {
            print("Interstitial ad is not ready.")
            return
        }
        
        interstitial.present(fromRootViewController: self)
    }
    
    // MARK: - GADFullScreenContentDelegate Methods

    /// Called when the ad is dismissed.
    func adDidDismissFullScreenContent(_ ad: GADFullScreenPresentingAd) {
        print("Ad dismissed. Loading a new interstitial ad.")
        loadInterstitialAd() // Load a new ad after the current one is dismissed
    }

    /// Called when the ad fails to present.
    func ad(_ ad: GADFullScreenPresentingAd, didFailToPresentFullScreenContentWithError error: Error) {
        print("Ad failed to present: \(error.localizedDescription)")
    }

    /// Called when the ad is presented.
    func adDidPresentFullScreenContent(_ ad: GADFullScreenPresentingAd) {
        print("Ad is now presenting.")
    }

    /// Called when the ad is clicked.
    func adDidRecordClick(_ ad: GADFullScreenPresentingAd) {
        print("Ad was clicked.")
    }
}
```

### Notes:
1. This code assumes you have already set up AdMob in your project and imported the `GoogleMobileAds` framework.
2. Make sure to replace `"your-admob-interstitial-ad-unit-id"` with your valid AdMob Interstitial Ad Unit ID.
3. Add proper permissions and configurations in your `Info.plist` file as required by AdMob.
4. The `showInterstitialAd` method is tied to a button for demonstration purposes. You can call it based on your app's logic.
