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

```java
import android.app.Activity;
import android.content.Context;
import android.os.Handler;
import android.os.Looper;
import android.util.Log;

import com.applovin.mediation.MaxAd;
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

import java.util.concurrent.TimeUnit;

/**
 * AppLovin MAX SDK Manager for utility apps
 * Handles initialization and ad loading for banner, interstitial, and rewarded ads
 */
public class AppLovinManager {
    private static final String TAG = "AppLovinManager";
    
    // Ad unit IDs - replace with your actual IDs
    private static final String BANNER_AD_UNIT_ID = "YOUR_BANNER_AD_UNIT_ID";
    private static final String INTERSTITIAL_AD_UNIT_ID = "YOUR_INTERSTITIAL_AD_UNIT_ID";
    private static final String REWARDED_AD_UNIT_ID = "YOUR_REWARDED_AD_UNIT_ID";
    
    private static AppLovinManager instance;
    private final Context context;
    
    private MaxAdView bannerAd;
    private MaxInterstitialAd interstitialAd;
    private MaxRewardedAd rewardedAd;
    
    private int interstitialRetryAttempt;
    private int rewardedRetryAttempt;
    
    private AppLovinManager(Context context) {
        this.context = context.getApplicationContext();
    }
    
    public static synchronized AppLovinManager getInstance(Context context) {
        if (instance == null) {
            instance = new AppLovinManager(context);
        }
        return instance;
    }
    
    /**
     * Initialize the AppLovin SDK
     */
    public void initializeSdk(final InitializationListener listener) {
        AppLovinSdk.getInstance(context).setMediationProvider("max");
        AppLovinSdk.initializeSdk(context, new AppLovinSdk.SdkInitializationListener() {
            @Override
            public void onSdkInitialized(final AppLovinSdkConfiguration configuration) {
                Log.d(TAG, "AppLovin SDK initialized");
                
                // Create ads after SDK is initialized
                createBannerAd();
                createInterstitialAd();
                createRewardedAd();
                
                if (listener != null) {
                    new Handler(Looper.getMainLooper()).post(() -> listener.onInitialized());
                }
            }
        });
    }
    
    /**
     * Create and load banner ad
     */
    private void createBannerAd() {
        bannerAd = new MaxAdView(BANNER_AD_UNIT_ID, context);
        bannerAd.setListener(new MaxAdViewAdListener() {
            @Override
            public void onAdExpanded(MaxAd ad) {}
            
            @Override
            public void onAdCollapsed(MaxAd ad) {}
            
            @Override
            public void onAdLoaded(MaxAd ad) {
                Log.d(TAG, "Banner ad loaded");
            }
            
            @Override
            public void onAdDisplayed(MaxAd ad) {}
            
            @Override
            public void onAdHidden(MaxAd ad) {}
            
            @Override
            public void onAdClicked(MaxAd ad) {}
            
            @Override
            public void onAdLoadFailed(String adUnitId, MaxError error) {
                Log.e(TAG, "Banner ad failed to load: " + error.getMessage());
            }
            
            @Override
            public void onAdDisplayFailed(MaxAd ad, MaxError error) {
                Log.e(TAG, "Banner ad failed to display: " + error.getMessage());
            }
        });
        
        // Set banner ad position and size
        bannerAd.setLayoutParams(new android.view.ViewGroup.LayoutParams(
                android.view.ViewGroup.LayoutParams.MATCH_PARENT,
                context.getResources().getDimensionPixelSize(com.applovin.sdk.R.dimen.max_banner_height)
        ));
        
        // Load the banner ad
        bannerAd.loadAd();
    }
    
    /**
     * Get banner ad view
     */
    public MaxAdView getBannerAd() {
        return bannerAd;
    }
    
    /**
     * Create and load interstitial ad
     */
    private void createInterstitialAd() {
        interstitialAd = new MaxInterstitialAd(INTERSTITIAL_AD_UNIT_ID, (Activity) context);
        interstitialAd.setListener(new MaxAdListener() {
            @Override
            public void onAdLoaded(MaxAd ad) {
                Log.d(TAG, "Interstitial ad loaded");
                interstitialRetryAttempt = 0;
            }
            
            @Override
            public void onAdDisplayed(MaxAd ad) {}
            
            @Override
            public void onAdHidden(MaxAd ad) {
                // Interstitial ad is hidden. Pre-load the next ad
                interstitialAd.loadAd();
            }
            
            @Override
            public void onAdClicked(MaxAd ad) {}
            
            @Override
            public void onAdLoadFailed(String adUnitId, MaxError error) {
                Log.e(TAG, "Interstitial ad failed to load: " + error.getMessage());
                interstitialRetryAttempt++;
                
                long delayMillis = TimeUnit.SECONDS.toMillis((long) Math.pow(2, Math.min(6, interstitialRetryAttempt)));
                new Handler().postDelayed(() -> interstitialAd.loadAd(), delayMillis);
            }
            
            @Override
            public void onAdDisplayFailed(MaxAd ad, MaxError error) {
                Log.e(TAG, "Interstitial ad failed to display: " + error.getMessage());
                interstitialAd.loadAd();
            }
        });
        
        // Load the first interstitial ad
        interstitialAd.loadAd();
    }
    
    /**
     * Show interstitial ad if ready
     */
    public void showInterstitialAd() {
        if (interstitialAd != null && interstitialAd.isReady()) {
            interstitialAd.showAd();
        } else {
            Log.d(TAG, "Interstitial ad not ready yet");
        }
    }
    
    /**
     * Create and load rewarded ad
     */
    private void createRewardedAd() {
        rewardedAd = MaxRewardedAd.getInstance(REWARDED_AD_UNIT_ID, (Activity) context);
        rewardedAd.setListener(new MaxRewardedAdListener() {
            @Override
            public void onAdLoaded(MaxAd ad) {
                Log.d(TAG, "Rewarded ad loaded");
                rewardedRetryAttempt = 0;
            }
            
            @Override
            public void onAdDisplayed(MaxAd ad) {}
            
            @Override
            public void onAdHidden(MaxAd ad) {
                // Rewarded ad is hidden. Pre-load the next ad
                rewardedAd.loadAd();
            }
            
            @Override
            public void onAdClicked(MaxAd ad) {}
            
            @Override
            public void onAdLoadFailed(String adUnitId, MaxError error) {
                Log.e(TAG, "Rewarded ad failed to load: " + error.getMessage());
                rewardedRetryAttempt++;
                
                long delayMillis = TimeUnit.SECONDS.toMillis((long) Math.pow(2, Math.min(6, rewardedRetryAttempt)));
                new Handler().postDelayed(() -> rewardedAd.loadAd(), delayMillis);
            }
            
            @Override
            public void onAdDisplayFailed(MaxAd ad, MaxError error) {
                Log.e(TAG, "Rewarded ad failed to display: " + error.getMessage());
                rewardedAd.loadAd();
            }
            
            @Override
            public void onUserRewarded(MaxAd ad, MaxReward reward) {
                Log.d(TAG, "User earned reward: " + reward);
            }
        });
        
        // Load the first rewarded ad
        rewardedAd.loadAd();
    }
    
    /**
     * Show rewarded ad if ready
     */
    public void showRewardedAd() {
        if (rewardedAd != null && rewardedAd.isReady()) {
            rewardedAd.showAd();
        } else {
            Log.d(TAG, "Rewarded ad not ready yet");
        }
    }
    
    public interface InitializationListener {
        void onInitialized();
    }
}
```
