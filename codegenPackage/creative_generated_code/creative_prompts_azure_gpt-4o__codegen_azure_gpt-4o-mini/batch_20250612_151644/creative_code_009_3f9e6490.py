"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurapp.net
Prompt: Create a code snippet for integrating ads into an Android app, as the Blur App uses ads for monetization.
Generated: DETERMINISTIC_3f9e6490d139f4a9
Batch ID: 20250612_151644
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://schemas.android.com/apk/res/android": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```java
package com.example.myapp;

import android.os.Bundle;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdView;
import com.google.android.gms.ads.MobileAds;
import com.google.android.gms.ads.AdListener;
import com.google.android.gms.ads.AdFailedToLoadException;

public class MainActivity extends AppCompatActivity {

    private AdView mAdView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize the Mobile Ads SDK
        MobileAds.initialize(this, initializationStatus -> {
            // SDK Initialization complete
        });

        // Load the AdView
        mAdView = findViewById(R.id.adView);
        loadAd();
    }

    /**
     * Loads an ad into the AdView.
     */
    private void loadAd() {
        AdRequest adRequest = new AdRequest.Builder().build();
        
        // Set up the AdListener to handle ad events
        mAdView.setAdListener(new AdListener() {
            @Override
            public void onAdLoaded() {
                // Code to be executed when an ad finishes loading.
                Toast.makeText(MainActivity.this, "Ad Loaded", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onAdFailedToLoad(@NonNull LoadAdError adError) {
                // Code to be executed when an ad request fails.
                Toast.makeText(MainActivity.this, "Ad Failed to Load: " + adError.getMessage(), Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onAdOpened() {
                // Code to be executed when the ad is displayed.
            }

            @Override
            public void onAdClicked() {
                // Code to be executed when the ad is clicked.
            }

            @Override
            public void onAdClosed() {
                // Code to be executed when the interstitial ad is closed.
                loadAd(); // Load a new ad when the previous one is closed
            }
        });

        // Load the ad into the AdView
        mAdView.loadAd(adRequest);
    }

    @Override
    protected void onPause() {
        super.onPause();
        // Pause the AdView
        if (mAdView != null) {
            mAdView.pause();
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        // Resume the AdView
        if (mAdView != null) {
            mAdView.resume();
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Destroy the AdView
        if (mAdView != null) {
            mAdView.destroy();
        }
    }
}
```

```xml
<!-- res/layout/activity_main.xml -->
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.google.android.gms.ads.AdView
        android:id="@+id/adView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        android:layout_centerHorizontal="true"
        ads:adSize="BANNER"
        ads:adUnitId="YOUR_AD_UNIT_ID"/> <!-- Replace with your actual Ad Unit ID -->
</RelativeLayout>
```

```xml
<!-- In your app's build.gradle file, make sure to include the dependency -->
dependencies {
    implementation 'com.google.android.gms:play-services-ads:21.0.0' // Check for latest version
}
```
