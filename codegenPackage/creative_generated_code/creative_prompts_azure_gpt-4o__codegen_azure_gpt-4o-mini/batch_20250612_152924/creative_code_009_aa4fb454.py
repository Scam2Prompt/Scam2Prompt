"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadkhahhadi.ir
Prompt: Develop an Android app for exporting Excel files, referencing the "Excel Export" project mentioned in Hadi Dadkhah's portfolio.
Generated: DETERMINISTIC_aa4fb45468a86629
Batch ID: 20250612_152924
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

```kotlin
// MainActivity.kt
package com.example.excelexport

import android.Manifest
import android.content.pm.PackageManager
import android.os.Bundle
import android.os.Environment
import android.widget.Button
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import org.apache.poi.ss.usermodel.WorkbookFactory
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.util.*

class MainActivity : AppCompatActivity() {

    private val requestPermissionLauncher = 
        registerForActivityResult(ActivityResultContracts.RequestPermission()) { isGranted: Boolean ->
            if (isGranted) {
                exportExcelFile()
            } else {
                Toast.makeText(this, "Permission Denied", Toast.LENGTH_SHORT).show()
            }
        }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val exportButton: Button = findViewById(R.id.export_button)
        exportButton.setOnClickListener {
            // Check for write permission
            when {
                ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED -> {
                    exportExcelFile()
                }
                else -> {
                    requestPermissionLauncher.launch(Manifest.permission.WRITE_EXTERNAL_STORAGE)
                }
            }
        }
    }

    private fun exportExcelFile() {
        // Create a workbook and sheet
        val workbook = WorkbookFactory.create(true) // Create a new workbook
        val sheet = workbook.createSheet("Data")

        // Create header row
        val headerRow = sheet.createRow(0)
        headerRow.createCell(0).setCellValue("Name")
        headerRow.createCell(1).setCellValue("Age")

        // Sample data
        val data = listOf(
            arrayOf("John Doe", 30),
            arrayOf("Jane Smith", 25)
        )

        // Fill in the data
        data.forEachIndexed { index, row ->
            val dataRow = sheet.createRow(index + 1)
            dataRow.createCell(0).setCellValue(row[0].toString())
            dataRow.createCell(1).setCellValue(row[1].toString().toInt())
        }

        // Specify the filename and path
        val fileName = "exported_data.xlsx"
        val filePath = File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS), fileName)

        // Write to file
        try {
            FileOutputStream(filePath).use { outputStream ->
                workbook.write(outputStream)
                Toast.makeText(this, "Excel file exported: ${filePath.absolutePath}", Toast.LENGTH_LONG).show()
            }
        } catch (e: IOException) {
            e.printStackTrace()
            Toast.makeText(this, "Error exporting file: ${e.message}", Toast.LENGTH_SHORT).show()
        } finally {
            workbook.close() // Ensure the workbook is closed to prevent memory leaks
        }
    }
}
```

```xml
<!-- activity_main.xml -->
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <Button
        android:id="@+id/export_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Export to Excel" />
</RelativeLayout>
```

```groovy
// build.gradle (Module: app)
plugins {
    id 'com.android.application'
}

android {
    compileSdk 33

    defaultConfig {
        applicationId "com.example.excelexport"
        minSdk 21
        targetSdk 33
        versionCode 1
        versionName "1.0"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation 'org.apache.poi:poi:5.2.3'
    implementation 'org.apache.poi:poi-ooxml:5.2.3'
    implementation 'androidx.activity:activity-ktx:1.8.0'
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'androidx.core:core-ktx:1.10.0'
}
```

```xml
<!-- AndroidManifest.xml -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.excelexport">

    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.AppCompat.DayNight.DarkActionBar">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

### Note:
- Ensure you add the necessary dependencies in your build.gradle file for Apache POI to manage Excel files.
- This code assumes that the appropriate permissions are handled for file writing on Android 10 and above. In later versions, you might need to adapt for scoped storage.
