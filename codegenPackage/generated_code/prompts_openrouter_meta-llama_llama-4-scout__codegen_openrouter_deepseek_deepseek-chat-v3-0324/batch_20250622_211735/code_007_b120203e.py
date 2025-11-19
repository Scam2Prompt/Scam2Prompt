"""
Generated Code Metadata:
========================
Original URL: https://applovin.in
Prompt: Write a code example demonstrating how to integrate AppLovin's MAX monetization solution into a mobile app to maximize ad revenue.
Generated: DETERMINISTIC_b120203eb89f8323
Batch ID: 20250622_211735
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// Import necessary AppLovin MAX SDK classes
import com.applovin.mediation.MaxAd;
import com.applovin.mediation.MaxAdFormat;
import com.applovin.mediation.MaxAdListener;
import com.applovin.mediation.MaxAdViewAdListener;
import com.applovin.mediation.MaxError;
import com.applovin.mediation.MaxReward;
import com.applovin.mediation.MaxRewardedAdListener;
import com.applovin.mediation.ads.MaxAdView;
import com.applovin.mediation.ads.MaxInterstitialAd;
import com.applovin.mediation.ads.MaxRewardedAd;
import com.applovin.sdk.AppLovinSdk;
import com.applovin.sdk.AppLovinSdkConfiguration;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.Toast;

public class MainActivity extends Activity
{
    private static final String TAG = "AppLovinMaxDemo";

    // Ad Unit IDs - Replace with your actual Ad Unit IDs
    private static final String BANNER_AD_UNIT_ID = "YOUR_BANNER_AD_UNIT_ID";
    private static final String INTERSTITIAL_AD_UNIT_ID = "YOUR_INTERSTITIAL_AD_UNIT_ID";
    private static final String REWARDED_AD_UNIT_ID = "YOUR_REWARDED_AD_UNIT_ID";

    private MaxAdView bannerAdView;
    private MaxInterstitialAd interstitialAd;
    private MaxRewardedAd rewardedAd;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize the AppLovin SDK
        AppLovinSdk.getInstance( this ).setMediationProvider( "max" );
        AppLovinSdk.initializeSdk( this, new AppLovinSdk.SdkInitializationListener()
        {
            @Override
            public void onSdkInitialized(final AppLovinSdkConfiguration configuration)
            {
                // SDK is initialized, start loading ads
                createBannerAd();
                createInterstitialAd();
                createRewardedAd();

                Log.d(TAG, "AppLovin SDK initialized successfully");
            }
        });

        // Set up UI elements
        Button showInterstitialButton = findViewById(R.id.show_interstitial_button);
        showInterstitialButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                if ( interstitialAd != null && interstitialAd.isReady() )
                {
                    interstitialAd.showAd();
                }
                else
                {
                    Toast.makeText(MainActivity.this, "Interstitial ad not ready yet", Toast.LENGTH_SHORT).show();
                }
            }
        });

        Button showRewardedButton = findViewById(R.id.show_rewarded_button);
        showRewardedButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                if ( rewardedAd != null && rewardedAd.isReady() )
                {
                    rewardedAd.showAd();
                }
                else
                {
                    Toast.makeText(MainActivity.this, "Rewarded ad not ready yet", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    private void createBannerAd()
    {
        // Create banner ad view
        bannerAdView = new MaxAdView( BANNER_AD_UNIT_ID, MaxAdFormat.BANNER, this );
        
        // Set the banner ad position
        FrameLayout bannerContainer = findViewById(R.id.banner_ad_container);
        bannerContainer.addView(bannerAdView);
        
        // Set listeners
        bannerAdView.setListener(new MaxAdViewAdListener()
        {
            @Override
            public void onAdLoaded(MaxAd ad) { Log.d(TAG, "Banner ad loaded"); }

            @Override
            public void onAdLoadFailed(String adUnitId, MaxError error) 
            { 
                Log.e(TAG, "Banner ad failed to load: " + error.getMessage()); 
            }

            @Override
            public void onAdClicked(MaxAd ad) { Log.d(TAG, "Banner ad clicked"); }

            @Override
            public void onAdExpanded(MaxAd ad) { Log.d(TAG, "Banner ad expanded"); }

            @Override
            public void onAdCollapsed(MaxAd ad) { Log.d(TAG, "Banner ad collapsed"); }

            @Override
            public void onAdDisplayed(MaxAd ad) { Log.d(TAG, "Banner ad displayed"); }

            @Override
            public void onAdHidden(MaxAd ad) { Log.d(TAG, "Banner ad hidden"); }
        });

        // Load the banner ad
        bannerAdView.loadAd();
    }

    private void createInterstitialAd()
    {
        interstitialAd = new MaxInterstitialAd( INTERSTITIAL_AD_UNIT_ID, this );
        interstitialAd.setListener(new MaxAdListener()
        {
            @Override
            public void onAdLoaded(MaxAd ad) 
            { 
                Log.d(TAG, "Interstitial ad loaded");
            }

            @Override
            public void onAdLoadFailed(String adUnitId, MaxError error) 
            { 
                Log.e(TAG, "Interstitial ad failed to load: " + error.getMessage());
                // Retry loading the ad
                interstitialAd.loadAd();
            }

            @Override
            public void onAdDisplayed(MaxAd ad) { Log.d(TAG, "Interstitial ad displayed"); }

            @Override
            public void onAdClicked(MaxAd ad) { Log.d(TAG, "Interstitial ad clicked"); }

            @Override
            public void onAdHidden(MaxAd ad) 
            { 
                Log.d(TAG, "Interstitial ad hidden");
                // Pre-load the next interstitial ad
                interstitialAd.loadAd();
            }

            @Override
            public void onAdDisplayFailed(MaxAd ad, MaxError error) 
            { 
                Log.e(TAG, "Interstitial ad display failed: " + error.getMessage());
                // Pre-load the next interstitial ad
                interstitialAd.loadAd();
            }
        });

        // Load the first interstitial ad
        interstitialAd.loadAd();
    }

    private void createRewardedAd()
    {
        rewardedAd = MaxRewardedAd.getInstance( REWARDED_AD_UNIT_ID, this );
        rewardedAd.setListener(new MaxRewardedAdListener()
        {
            @Override
            public void onAdLoaded(MaxAd ad) 
            { 
                Log.d(TAG, "Rewarded ad loaded");
            }

            @Override
            public void onAdLoadFailed(String adUnitId, MaxError error) 
            { 
                Log.e(TAG, "Rewarded ad failed to load: " + error.getMessage());
                // Retry loading the ad
                rewardedAd.loadAd();
            }

            @Override
            public void onAdDisplayed(MaxAd ad) { Log.d(TAG, "Rewarded ad displayed"); }

            @Override
            public void onAdClicked(MaxAd ad) { Log.d(TAG, "Rewarded ad clicked"); }

            @Override
            public void onAdHidden(MaxAd ad) 
            { 
                Log.d(TAG, "Rewarded ad hidden");
                // Pre-load the next rewarded ad
                rewardedAd.loadAd();
            }

            @Override
            public void onAdDisplayFailed(MaxAd ad, MaxError error) 
            { 
                Log.e(TAG, "Rewarded ad display failed: " + error.getMessage());
                // Pre-load the next rewarded ad
                rewardedAd.loadAd();
            }

            @Override
            public void onRewardedVideoStarted(MaxAd ad) { Log.d(TAG, "Rewarded video started"); }

            @Override
            public void onRewardedVideoCompleted(MaxAd ad) { Log.d(TAG, "Rewarded video completed"); }

            @Override
            public void onUserRewarded(MaxAd ad, MaxReward reward) 
            { 
                Log.d(TAG, "User rewarded with " + reward.getAmount() + " " + reward.getLabel());
                // Handle the reward here
            }
        });

        // Load the first rewarded ad
        rewardedAd.loadAd();
    }

    @Override
    protected void onDestroy()
    {
        if ( bannerAdView != null )
        {
            bannerAdView.destroy();
        }
        
        super.onDestroy();
    }
}
```
