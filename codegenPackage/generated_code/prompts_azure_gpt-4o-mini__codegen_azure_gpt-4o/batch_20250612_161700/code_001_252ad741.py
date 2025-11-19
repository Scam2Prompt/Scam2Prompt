"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Write an Android application using MVVM architecture that incorporates custom views and socket programming as outlined by Hadi Dadkhah.
Generated: DETERMINISTIC_252ad74157e67667
Batch ID: 20250612_161700
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://schemas.android.com/tools": {
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

```kotlin
// MainActivity.kt
package com.example.mvvm_socket_app

import android.os.Bundle
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.Observer
import com.example.mvvm_socket_app.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private val viewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Observe data from ViewModel
        viewModel.socketData.observe(this, Observer { data ->
            binding.customView.updateData(data)
        })

        // Start socket connection
        viewModel.startSocketConnection()
    }

    override fun onDestroy() {
        super.onDestroy()
        viewModel.stopSocketConnection()
    }
}
```

```kotlin
// MainViewModel.kt
package com.example.mvvm_socket_app

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import kotlinx.coroutines.*
import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter
import java.net.Socket

class MainViewModel : ViewModel() {
    private val _socketData = MutableLiveData<String>()
    val socketData: LiveData<String> get() = _socketData

    private var socket: Socket? = null
    private var reader: BufferedReader? = null
    private var writer: PrintWriter? = null
    private var socketJob: Job? = null

    fun startSocketConnection() {
        socketJob = CoroutineScope(Dispatchers.IO).launch {
            try {
                // Connect to the server
                socket = Socket("your.server.address", 12345)
                reader = BufferedReader(InputStreamReader(socket!!.getInputStream()))
                writer = PrintWriter(socket!!.getOutputStream(), true)

                // Continuously read data from the socket
                while (isActive) {
                    val data = reader?.readLine()
                    if (data != null) {
                        withContext(Dispatchers.Main) {
                            _socketData.value = data
                        }
                    }
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    fun stopSocketConnection() {
        socketJob?.cancel()
        try {
            reader?.close()
            writer?.close()
            socket?.close()
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    override fun onCleared() {
        super.onCleared()
        stopSocketConnection()
    }
}
```

```kotlin
// CustomView.kt
package com.example.mvvm_socket_app

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.util.AttributeSet
import android.view.View

class CustomView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : View(context, attrs, defStyleAttr) {

    private var data: String = ""
    private val paint = Paint().apply {
        color = Color.BLACK
        textSize = 50f
        isAntiAlias = true
    }

    fun updateData(newData: String) {
        data = newData
        invalidate() // Redraw the view
    }

    override fun onDraw(canvas: Canvas?) {
        super.onDraw(canvas)
        canvas?.drawText(data, 50f, 100f, paint)
    }
}
```

```xml
<!-- activity_main.xml -->
<layout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">

    <data>
        <!-- ViewModel binding can be added here if needed -->
    </data>

    <RelativeLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".MainActivity">

        <com.example.mvvm_socket_app.CustomView
            android:id="@+id/customView"
            android:layout_width="match_parent"
            android:layout_height="match_parent" />

    </RelativeLayout>
</layout>
```

```gradle
// build.gradle (Module: app)
plugins {
    id 'com.android.application'
    id 'kotlin-android'
}

android {
    compileSdk 33

    defaultConfig {
        applicationId "com.example.mvvm_socket_app"
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
    implementation "androidx.core:core-ktx:1.10.1"
    implementation "androidx.appcompat:appcompat:1.6.1"
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.6.1"
    implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.6.1"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3"
}
```

This code provides a complete Android application using MVVM architecture, custom views, and socket programming. Replace `"your.server.address"` and `12345` with the actual server address and port.
