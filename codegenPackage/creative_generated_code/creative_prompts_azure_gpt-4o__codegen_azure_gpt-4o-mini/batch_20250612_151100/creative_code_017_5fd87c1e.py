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
package com.example.myapp;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

/**
 * MainActivity class is the entry point of the Android application.
 * It handles user input and displays a greeting message.
 */
public class MainActivity extends AppCompatActivity {

    // Declare UI components
    private EditText nameInput;
    private Button greetButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize UI components
        nameInput = findViewById(R.id.nameInput);
        greetButton = findViewById(R.id.greetButton);

        // Set up a click listener for the greet button
        greetButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                greetUser();
            }
        });
    }

    /**
     * Retrieves the user's input and displays a greeting message.
     */
    private void greetUser() {
        String name = nameInput.getText().toString().trim();

        // Basic error handling for empty input
        if (name.isEmpty()) {
            Toast.makeText(this, "Please enter your name", Toast.LENGTH_SHORT).show();
            return;
        }

        // Construct and display greeting message
        String greetingMessage = "Hello, " + name + "!";
        Toast.makeText(this, greetingMessage, Toast.LENGTH_LONG).show();
    }
}
```

**activity_main.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <EditText
        android:id="@+id/nameInput"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter your name" />

    <Button
        android:id="@+id/greetButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Greet Me" />
</LinearLayout>
```

**AndroidManifest.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.myapp">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.MyApp">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```
