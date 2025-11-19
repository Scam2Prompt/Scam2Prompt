"""
Generated Code Metadata:
========================
Original URL: https://globaljournalpress.com
Prompt: Create a tutorial on how to install Base.Apk on an Android device, including troubleshooting tips and common issues.
Generated: DETERMINISTIC_b5cb0d1169b9f712
Batch ID: 20250622_210655
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://schemas.android.com/tools": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

```java
// MainActivity.java
package com.example.baseapkinstaller;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.Settings;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import java.io.File;

public class MainActivity extends AppCompatActivity {
    private static final int REQUEST_CODE_PERMISSIONS = 1001;
    private static final int REQUEST_CODE_INSTALL_UNKNOWN_APK = 1002;
    private static final String APK_NAME = "base.apk";
    
    private TextView statusTextView;
    private Button installButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        statusTextView = findViewById(R.id.statusTextView);
        installButton = findViewById(R.id.installButton);

        installButton.setOnClickListener(v -> checkPermissionsAndInstall());
        
        updateStatus("Ready to install " + APK_NAME);
    }

    private void checkPermissionsAndInstall() {
        // Check for storage permission first
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.READ_EXTERNAL_STORAGE) 
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, 
                    new String[]{Manifest.permission.READ_EXTERNAL_STORAGE}, 
                    REQUEST_CODE_PERMISSIONS);
        } else {
            checkForUnknownSourcesPermission();
        }
    }

    private void checkForUnknownSourcesPermission() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            if (!getPackageManager().canRequestPackageInstalls()) {
                // Request the permission to install unknown APKs
                Intent intent = new Intent(Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES)
                        .setData(Uri.parse(String.format("package:%s", getPackageName())));
                startActivityForResult(intent, REQUEST_CODE_INSTALL_UNKNOWN_APK);
            } else {
                installApk();
            }
        } else {
            installApk();
        }
    }

    private void installApk() {
        File apkFile = new File(Environment.getExternalStorageDirectory(), APK_NAME);
        
        if (!apkFile.exists()) {
            updateStatus("Error: " + APK_NAME + " not found in root directory");
            Toast.makeText(this, APK_NAME + " not found", Toast.LENGTH_LONG).show();
            return;
        }

        Intent intent = new Intent(Intent.ACTION_VIEW);
        intent.setDataAndType(Uri.fromFile(apkFile), "application/vnd.android.package-archive");
        intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        
        try {
            startActivity(intent);
            updateStatus("Installing " + APK_NAME + "...");
        } catch (Exception e) {
            updateStatus("Error: Could not start installation");
            Toast.makeText(this, "Installation failed: " + e.getMessage(), Toast.LENGTH_LONG).show();
        }
    }

    private void updateStatus(String message) {
        statusTextView.setText(message);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == REQUEST_CODE_PERMISSIONS) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                checkForUnknownSourcesPermission();
            } else {
                updateStatus("Permission denied. Cannot access storage.");
                Toast.makeText(this, "Storage permission required", Toast.LENGTH_LONG).show();
            }
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQUEST_CODE_INSTALL_UNKNOWN_APK) {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O && 
                    getPackageManager().canRequestPackageInstalls()) {
                installApk();
            } else {
                updateStatus("Installation blocked. Please enable 'Unknown Sources'.");
                Toast.makeText(this, "Unknown Sources permission required", Toast.LENGTH_LONG).show();
            }
        }
    }
}
```

```xml
<!-- activity_main.xml -->
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/statusTextView"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:textSize="18sp"
        android:text="Preparing installation..."
        android:layout_marginBottom="16dp"/>

    <Button
        android:id="@+id/installButton"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Install Base.APK"/>

</LinearLayout>
```

```xml
<!-- AndroidManifest.xml -->
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.baseapkinstaller">

    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.REQUEST_INSTALL_PACKAGES" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.BaseAPKInstaller">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```
