"""
Generated Code Metadata:
========================
Original URL: https://blurapp.net
Prompt: Create a code snippet for integrating ads into an Android app, as the Blur App uses ads for monetization.
Generated: DETERMINISTIC_3f9e6490d139f4a9
Batch ID: 20250612_151644
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://schemas.android.com/apk/res/android": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://schemas.android.com/apk/res-auto": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```java
// AdIntegrationHelper.java
import android.content.Context;
import android.util.Log;
import androidx.annotation.NonNull;
import com.google.android.gms.ads.AdError;
import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdView;
import com.google.android.gms.ads.FullScreenContentCallback;
import com.google.android.gms.ads.LoadAdError;
import com.google.android.gms.ads.MobileAds;
import com.google.android.gms.ads.interstitial.InterstitialAd;
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback;

public class AdIntegrationHelper {
    private static final String TAG = "AdIntegrationHelper";
    private InterstitialAd mInterstitialAd;
    private final Context context;
    private final String adMobAppId;
    private final String bannerAdUnitId;
    private final String interstitialAdUnitId;

    public AdIntegrationHelper(Context context, String adMobAppId, 
                             String bannerAdUnitId, String interstitialAdUnitId) {
        this.context = context;
        this.adMobAppId = adMobAppId;
        this.bannerAdUnitId = bannerAdUnitId;
        this.interstitialAdUnitId = interstitialAdUnitId;
        initializeMobileAds();
    }

    private void initializeMobileAds() {
        MobileAds.initialize(context, initializationStatus -> 
            Log.d(TAG, "AdMob initialized successfully"));
    }

    public void setupBannerAd(AdView adView) {
        AdRequest adRequest = new AdRequest.Builder().build();
        adView.loadAd(adRequest);
    }

    public void loadInterstitialAd() {
        AdRequest adRequest = new AdRequest.Builder().build();
        InterstitialAd.load(context, interstitialAdUnitId, adRequest,
            new InterstitialAdLoadCallback() {
                @Override
                public void onAdLoaded(@NonNull InterstitialAd interstitialAd) {
                    mInterstitialAd = interstitialAd;
                    Log.d(TAG, "Interstitial ad loaded successfully");
                    setupInterstitialAdListeners();
                }

                @Override
                public void onAdFailedToLoad(@NonNull LoadAdError loadAdError) {
                    Log.e(TAG, "Interstitial ad failed to load: " + loadAdError.getMessage());
                    mInterstitialAd = null;
                }
            });
    }

    private void setupInterstitialAdListeners() {
        if (mInterstitialAd != null) {
            mInterstitialAd.setFullScreenContentCallback(new FullScreenContentCallback() {
                @Override
                public void onAdDismissedFullScreenContent() {
                    Log.d(TAG, "Ad was dismissed");
                    loadInterstitialAd(); // Preload next ad
                }

                @Override
                public void onAdFailedToShowFullScreenContent(@NonNull AdError adError) {
                    Log.e(TAG, "Ad failed to show: " + adError.getMessage());
                }

                @Override
                public void onAdShowedFullScreenContent() {
                    mInterstitialAd = null;
                    Log.d(TAG, "Ad showed successfully");
                }
            });
        }
    }

    public void showInterstitialAd() {
        if (mInterstitialAd != null) {
            mInterstitialAd.show((android.app.Activity) context);
        } else {
            Log.d(TAG, "Ad wasn't loaded yet");
            loadInterstitialAd();
        }
    }
}
```

```xml
<!-- AndroidManifest.xml additions -->
<manifest>
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application>
        <meta-data
            android:name="com.google.android.gms.ads.APPLICATION_ID"
            android:value="ca-app-pub-xxxxxxxxxxxxxxxx~yyyyyyyyyy"/>
    </application>
</manifest>
```

```xml
<!-- layout.xml example with banner ad -->
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:ads="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <!-- Your app content here -->

    <com.google.android.gms.ads.AdView
        android:id="@+id/adView"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        ads:adSize="BANNER"
        ads:adUnitId="ca-app-pub-3940256099942544/6300978111"/>
</LinearLayout>
```
