"""
Generated Code Metadata:
========================
Original URL: https://thuthuatxiaomi.com
Prompt: "Generate code snippets for enabling dynamic themes on MIUI 11 based on Google Pixel 5's Conveyor Belt live wallpapers."
Generated: DETERMINISTIC_abeff777900dd433
Batch ID: 20250622_211816
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

# Generated Code:
# ===============

```kotlin
// ThemeManager.kt
package com.example.dynamicthemes

import android.app.WallpaperManager
import android.content.Context
import android.graphics.Bitmap
import android.graphics.Color
import android.os.Handler
import android.os.Looper
import androidx.palette.graphics.Palette

/**
 * Manages dynamic theming based on live wallpaper colors
 */
class ThemeManager(private val context: Context) {

    private val wallpaperManager: WallpaperManager = WallpaperManager.getInstance(context)
    private val handler = Handler(Looper.getMainLooper())
    private var themeUpdateRunnable: Runnable? = null
    private var updateInterval: Long = 5000 // 5 seconds

    interface ThemeChangeListener {
        fun onThemeChanged(primaryColor: Int, secondaryColor: Int, textColor: Int)
    }

    private var listener: ThemeChangeListener? = null

    /**
     * Starts monitoring wallpaper changes and updating theme colors
     */
    fun startThemeUpdates(listener: ThemeChangeListener) {
        this.listener = listener
        stopThemeUpdates() // Stop any existing updates
        
        themeUpdateRunnable = object : Runnable {
            override fun run() {
                updateThemeFromWallpaper()
                handler.postDelayed(this, updateInterval)
            }
        }
        handler.post(themeUpdateRunnable!!)
    }

    /**
     * Stops monitoring wallpaper changes
     */
    fun stopThemeUpdates() {
        themeUpdateRunnable?.let {
            handler.removeCallbacks(it)
            themeUpdateRunnable = null
        }
    }

    /**
     * Extracts colors from current wallpaper and updates theme
     */
    private fun updateThemeFromWallpaper() {
        try {
            val wallpaperDrawable = wallpaperManager.drawable ?: return
            val bitmap = Bitmap.createBitmap(
                wallpaperDrawable.intrinsicWidth,
                wallpaperDrawable.intrinsicHeight,
                Bitmap.Config.ARGB_8888
            )
            
            val canvas = android.graphics.Canvas(bitmap)
            wallpaperDrawable.setBounds(0, 0, canvas.width, canvas.height)
            wallpaperDrawable.draw(canvas)

            Palette.from(bitmap).generate { palette ->
                palette?.let {
                    val dominantSwatch = it.dominantSwatch
                    val vibrantSwatch = it.vibrantSwatch
                    val darkMutedSwatch = it.darkMutedSwatch

                    val primaryColor = dominantSwatch?.rgb ?: Color.parseColor("#6200EE")
                    val secondaryColor = vibrantSwatch?.rgb ?: Color.parseColor("#03DAC6")
                    val textColor = darkMutedSwatch?.bodyTextColor ?: Color.WHITE

                    listener?.onThemeChanged(primaryColor, secondaryColor, textColor)
                }
            }
        } catch (e: Exception) {
            // Fallback colors if extraction fails
            listener?.onThemeChanged(
                Color.parseColor("#6200EE"),
                Color.parseColor("#03DAC6"),
                Color.WHITE
            )
        }
    }

    /**
     * Sets the interval for theme updates
     * @param intervalMs Update interval in milliseconds
     */
    fun setUpdateInterval(intervalMs: Long) {
        updateInterval = intervalMs
    }
}
```

```xml
<!-- themes.xml -->
<resources>
    <!-- Base application theme -->
    <style name="AppTheme" parent="Theme.MaterialComponents.DayNight">
        <!-- Customize your theme here -->
        <item name="colorPrimary">@color/colorPrimary</item>
        <item name="colorPrimaryVariant">@color/colorPrimaryVariant</item>
        <item name="colorOnPrimary">@color/colorOnPrimary</item>
        <item name="colorSecondary">@color/colorSecondary</item>
        <item name="colorSecondaryVariant">@color/colorSecondaryVariant</item>
        <item name="colorOnSecondary">@color/colorOnSecondary</item>
        <item name="android:statusBarColor">?attr/colorPrimaryVariant</item>
    </style>

    <!-- Dynamic theme overlay -->
    <style name="DynamicThemeOverlay">
        <item name="colorPrimary">@color/dynamic_primary</item>
        <item name="colorPrimaryVariant">@color/dynamic_primary_variant</item>
        <item name="colorOnPrimary">@color/dynamic_on_primary</item>
        <item name="colorSecondary">@color/dynamic_secondary</item>
        <item name="colorSecondaryVariant">@color/dynamic_secondary_variant</item>
        <item name="colorOnSecondary">@color/dynamic_on_secondary</item>
    </style>
</resources>
```

```kotlin
// MainActivity.kt
package com.example.dynamicthemes

import android.graphics.Color
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat

class MainActivity : AppCompatActivity(), ThemeManager.ThemeChangeListener {

    private lateinit var themeManager: ThemeManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        themeManager = ThemeManager(this)
    }

    override fun onResume() {
        super.onResume()
        themeManager.startThemeUpdates(this)
    }

    override fun onPause() {
        super.onPause()
        themeManager.stopThemeUpdates()
    }

    override fun onThemeChanged(primaryColor: Int, secondaryColor: Int, textColor: Int) {
        runOnUiThread {
            // Update theme colors
            window.statusBarColor = primaryColor
            window.navigationBarColor = primaryColor
            
            // You would typically update your theme here
            // This is a simplified example - in production you'd use ThemeOverlay
            // or similar mechanism to apply colors throughout the app
        }
    }

    private fun applyDynamicColors(primary: Int, secondary: Int, text: Int) {
        // In a real implementation, you would:
        // 1. Create a new ContextThemeWrapper with DynamicThemeOverlay
        // 2. Set the colors in your theme overlay
        // 3. Recreate activities or apply the theme to views
    }
}
```

```xml
<!-- AndroidManifest.xml -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.dynamicthemes">

    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```
