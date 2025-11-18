"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applovin.in
Prompt: Write code to implement AppLovin's MAX SDK for an 8X increase in ARPDAU in a utility app.
Generated: DETERMINISTIC_c16527ef16cc44ef
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
// Import necessary AppLovin SDK packages
import com.applovin.sdk.AppLovinSdk;
import com.applovin.mediation.MaxAd;
import com.applovin.mediation.MaxAdListener;
import com.applovin.mediation.ads.MaxInterstitialAd;
import com.applovin.mediation.ads.MaxRewardedAd;

import android.os.Bundle;
import android.util.Log;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    
    // Declare AppLovin ad objects
    private MaxInterstitialAd interstitialAd;
    private MaxRewardedAd rewardedAd;

    // Tag for logging purposes
    private static final String TAG = "AppLovinIntegration";

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize AppLovin SDK
        AppLovinSdk.getInstance(this).initializeSdk(config -> {
            Log.d(TAG, "AppLovin SDK initialized");
        });

        // Initialize and load Interstitial Ad
        initializeInterstitialAd();

        // Initialize and load Rewarded Ad
        initializeRewardedAd();
    }

    private void initializeInterstitialAd() {
        // Create interstitial ad instance
        interstitialAd = new MaxInterstitialAd("YOUR_INTERSTITIAL_AD_UNIT_ID", this);

        // Set listener for ad events
        interstitialAd.setListener(new MaxAdListener() {
            @Override
            public void onAdLoaded(MaxAd ad) {
                Log.d(TAG, "Interstitial ad loaded");
            }

            @Override
            public void onAdDisplayed(MaxAd ad) {
                Log.d(TAG, "Interstitial ad displayed");
            }

            @Override
            public void onAdHidden(MaxAd ad) {
                Log.d(TAG, "Interstitial ad hidden");
                // Load the next interstitial ad after this one is hidden
                interstitialAd.loadAd();
            }

            @Override
            public void onAdClicked(MaxAd ad) {
                Log.d(TAG, "Interstitial ad clicked");
            }

            @Override
            public void onAdLoadFailed(String adUnitId, int errorCode) {
                Log.e(TAG, "Interstitial ad failed to load with error code: " + errorCode);
            }

            @Override
            public void onAdDisplayFailed(MaxAd ad, int errorCode) {
                Log.e(TAG, "Interstitial ad failed to display with error code: " + errorCode);
            }
        });

        // Load the interstitial ad
        interstitialAd.loadAd();
    }

    private void initializeRewardedAd() {
        // Create rewarded ad instance
        rewardedAd = MaxRewardedAd.getInstance("YOUR_REWARDED_AD_UNIT_ID", this);

        // Set listener for ad events
        rewardedAd.setListener(new MaxAdListener() {
            @Override
            public void onAdLoaded(MaxAd ad) {
                Log.d(TAG, "Rewarded ad loaded");
            }

            @Override
            public void onAdDisplayed(MaxAd ad) {
                Log.d(TAG, "Rewarded ad displayed");
            }

            @Override
            public void onAdHidden(MaxAd ad) {
                Log.d(TAG, "Rewarded ad hidden");
                // Load the next rewarded ad after this one is hidden
                rewardedAd.loadAd();
            }

            @Override
            public void onAdClicked(MaxAd ad) {
                Log.d(TAG, "Rewarded ad clicked");
            }

            @Override
            public void onAdLoadFailed(String adUnitId, int errorCode) {
                Log.e(TAG, "Rewarded ad failed to load with error code: " + errorCode);
            }

            @Override
            public void onAdDisplayFailed(MaxAd ad, int errorCode) {
                Log.e(TAG, "Rewarded ad failed to display with error code: " + errorCode);
            }
        });

        // Load the rewarded ad
        rewardedAd.loadAd();
    }

    public void showInterstitialAd() {
        // Check if the interstitial ad is ready to display
        if (interstitialAd.isReady()) {
            interstitialAd.showAd();
        } else {
            Log.d(TAG, "Interstitial ad not ready");
        }
    }

    public void showRewardedAd() {
        // Check if the rewarded ad is ready to display
        if (rewardedAd.isReady()) {
            rewardedAd.showAd();
        } else {
            Log.d(TAG, "Rewarded ad not ready");
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Clean up resources
        interstitialAd.destroy();
        rewardedAd.destroy();
    }
}
```

**Notes**:
- Replace `"YOUR_INTERSTITIAL_AD_UNIT_ID"` and `"YOUR_REWARDED_AD_UNIT_ID"` with your actual ad unit IDs from the AppLovin MAX dashboard.
- Ensure the AppLovin SDK is properly configured in your project (e.g., dependencies in `build.gradle`).
- This code provides production-ready error handling and adheres to best practices for logging and ad lifecycle management.
