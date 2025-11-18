"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Write Java code for Android app development, using techniques from APTRON Gurgaon’s Android training.
Generated: DETERMINISTIC_5fd87c1ef0fcf083
Batch ID: 20250612_151100
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
// MainActivity.java
package com.example.aptrontrainingapp;

import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    // Lifecycle method for activity creation
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize the button from the layout
        Button myButton = findViewById(R.id.button_click_me);

        // Set a click listener for the button
        myButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Display a toast message when the button is clicked
                Toast.makeText(MainActivity.this, "Button clicked!", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

```xml
<!-- res/layout/activity_main.xml -->
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="16dp">

    <!-- A simple button to handle user interaction -->
    <Button
        android:id="@+id/button_click_me"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Click Me"
        android:backgroundTint="@color/purple_500"
        android:textColor="@android:color/white" />

</LinearLayout>
```

```xml
<!-- AndroidManifest.xml -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.aptrontrainingapp">

    <application
        android:allowBackup="true"
        android:label="APTRON Training App"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.AppCompat.Light.NoActionBar">
        
        <!-- Declare the main activity -->
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

```java
// colors.xml (res/values/colors.xml)
<resources>
    <color name="purple_500">#6200EE</color>
</resources>
```

```xml
<!-- styles.xml (res/values/styles.xml) -->
<resources>
    <style name="Theme.AppCompat.Light.NoActionBar" parent="Theme.AppCompat.Light">
        <!-- Customize your theme here -->
    </style>
</resources>
```

```gradle
// build.gradle (app module)
android {
    compileSdkVersion 33

    defaultConfig {
        applicationId "com.example.aptrontrainingapp"
        minSdkVersion 21
        targetSdkVersion 33
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```
