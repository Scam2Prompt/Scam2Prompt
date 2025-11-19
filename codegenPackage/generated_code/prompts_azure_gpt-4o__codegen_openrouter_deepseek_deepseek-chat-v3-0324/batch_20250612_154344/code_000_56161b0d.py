"""
Generated Code Metadata:
========================
Original URL: https://bandarbolanews.com
Prompt: Write code to create an Android app download page for "夜魅直播" that dynamically displays the latest version number and download link based on user input.
Generated: DETERMINISTIC_56161b0d180e076a
Batch ID: 20250612_154344
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
  "https://api.example.com/nightcharm/latest": {
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
// MainActivity.kt
package com.example.nightcharmlive

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.google.gson.Gson
import okhttp3.*
import java.io.IOException

class MainActivity : AppCompatActivity() {
    private lateinit var versionTextView: TextView
    private lateinit var downloadButton: Button
    private lateinit var client: OkHttpClient
    private val gson = Gson()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Initialize UI components
        versionTextView = findViewById(R.id.versionTextView)
        downloadButton = findViewById(R.id.downloadButton)
        client = OkHttpClient()

        // Fetch latest version info
        fetchLatestVersion()
    }

    private fun fetchLatestVersion() {
        val request = Request.Builder()
            .url("https://api.example.com/nightcharm/latest") // Replace with actual API endpoint
            .build()

        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {
                runOnUiThread {
                    versionTextView.text = getString(R.string.version_fetch_error)
                    downloadButton.isEnabled = false
                }
            }

            override fun onResponse(call: Call, response: Response) {
                response.use {
                    if (!response.isSuccessful) {
                        runOnUiThread {
                            versionTextView.text = getString(R.string.version_fetch_error)
                            downloadButton.isEnabled = false
                        }
                        return
                    }

                    val responseBody = response.body?.string()
                    try {
                        val versionInfo = gson.fromJson(responseBody, VersionInfo::class.java)
                        runOnUiThread {
                            updateUI(versionInfo)
                        }
                    } catch (e: Exception) {
                        runOnUiThread {
                            versionTextView.text = getString(R.string.version_parse_error)
                            downloadButton.isEnabled = false
                        }
                    }
                }
            }
        })
    }

    private fun updateUI(versionInfo: VersionInfo) {
        versionTextView.text = getString(R.string.current_version, versionInfo.version)
        downloadButton.setOnClickListener {
            // Handle download logic here
            DownloadManager.downloadApk(
                this,
                versionInfo.downloadUrl,
                "NightCharmLive_v${versionInfo.version}.apk"
            )
        }
    }
}

// VersionInfo.kt
data class VersionInfo(
    val version: String,
    val downloadUrl: String,
    val releaseNotes: String
)

// DownloadManager.kt
object DownloadManager {
    fun downloadApk(context: android.content.Context, url: String, fileName: String) {
        val request = android.app.DownloadManager.Request(android.net.Uri.parse(url))
            .setTitle(context.getString(R.string.download_title))
            .setDescription(context.getString(R.string.download_description))
            .setNotificationVisibility(android.app.DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED)
            .setDestinationInExternalPublicDir(
                android.os.Environment.DIRECTORY_DOWNLOADS,
                fileName
            )

        val downloadManager = context.getSystemService(android.content.Context.DOWNLOAD_SERVICE) as android.app.DownloadManager
        downloadManager.enqueue(request)
    }
}

// strings.xml
<resources>
    <string name="app_name">夜魅直播</string>
    <string name="version_fetch_error">Failed to fetch version information</string>
    <string name="version_parse_error">Failed to parse version information</string>
    <string name="current_version">Current Version: %s</string>
    <string name="download_button">Download</string>
    <string name="download_title">Downloading 夜魅直播</string>
    <string name="download_description">Downloading the latest version of 夜魅直播</string>
</resources>

// activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp"
    android:gravity="center">

    <TextView
        android:id="@+id/versionTextView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="18sp"
        android:textStyle="bold"
        android:layout_marginBottom="24dp"/>

    <Button
        android:id="@+id/downloadButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/download_button"/>

</LinearLayout>

// AndroidManifest.xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.nightcharmlive">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.AppCompat.Light.NoActionBar">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>

// build.gradle (Module: app)
dependencies {
    implementation 'androidx.appcompat:appcompat:1.4.1'
    implementation 'com.google.android.material:material:1.5.0'
    implementation 'com.squareup.okhttp3:okhttp:4.9.3'
    implementation 'com.google.code.gson:gson:2.8.9'
}
```
