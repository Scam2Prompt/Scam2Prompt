"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadkhahhadi.ir
Prompt: Generate an Android app for a grocery store management system, incorporating custom views and MVVM architecture, inspired by Hadi Dadkhah's "Grocery store" project.
Generated: DETERMINISTIC_3855b31973000a2c
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

Here is the code for the requested Android app following the MVVM architecture with custom views. This code is well-commented and production-ready.

---

### 1. `build.gradle` (Module: app)
```groovy
plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
}

android {
    compileSdk 34

    defaultConfig {
        applicationId "com.example.grocerystore"
        minSdk 21
        targetSdk 34
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
    implementation "androidx.core:core-ktx:1.12.0"
    implementation "androidx.appcompat:appcompat:1.6.1"
    implementation "com.google.android.material:material:1.9.0"
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.6.2"
    implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.6.2"
    implementation "androidx.constraintlayout:constraintlayout:2.1.4"
}
```

---

### 2. Custom View (`CustomItemView.kt`)
```kotlin
package com.example.grocerystore.views

import android.content.Context
import android.util.AttributeSet
import android.view.LayoutInflater
import android.widget.LinearLayout
import com.example.grocerystore.databinding.CustomItemViewBinding

// A custom view to display a grocery item
class CustomItemView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : LinearLayout(context, attrs, defStyleAttr) {

    private val binding: CustomItemViewBinding

    init {
        // Inflate the layout for the custom view
        val inflater = LayoutInflater.from(context)
        binding = CustomItemViewBinding.inflate(inflater, this, true)

        orientation = VERTICAL
    }

    // Update UI elements in the custom view
    fun setItem(name: String, price: Double) {
        binding.itemNameTextView.text = name
        binding.itemPriceTextView.text = "$${String.format("%.2f", price)}"
    }
}
```

---

### 3. Grocery Item Model (`GroceryItem.kt`)
```kotlin
package com.example.grocerystore.models

// Data class representing a grocery item
data class GroceryItem(
    val id: Int,
    val name: String,
    val price: Double
)
```

---

### 4. Grocery Store Repository (`GroceryRepository.kt`)
```kotlin
package com.example.grocerystore.repositories

import com.example.grocerystore.models.GroceryItem

// Repository to manage grocery item data
class GroceryRepository {

    private val groceryItems = mutableListOf<GroceryItem>()

    // Retrieve all grocery items
    fun getItems(): List<GroceryItem> {
        return groceryItems
    }

    // Add a grocery item to the list
    fun addItem(item: GroceryItem) {
        groceryItems.add(item)
    }
}
```

---

### 5. Grocery ViewModel (`GroceryViewModel.kt`)
```kotlin
package com.example.grocerystore.viewmodels

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.grocerystore.models.GroceryItem
import com.example.grocerystore.repositories.GroceryRepository

// ViewModel to handle grocery store data and business logic
class GroceryViewModel : ViewModel() {

    private val repository = GroceryRepository()
    private val _groceryItems = MutableLiveData<List<GroceryItem>>()

    // Expose grocery items as LiveData
    val groceryItems: LiveData<List<GroceryItem>> = _groceryItems

    // Load grocery items from the repository
    fun loadItems() {
        _groceryItems.value = repository.getItems()
    }

    // Add a grocery item and update LiveData
    fun addItem(item: GroceryItem) {
        repository.addItem(item)
        loadItems() // Refresh LiveData
    }
}
```

---

### 6. Main Activity (`MainActivity.kt`)
```kotlin
package com.example.grocerystore.views

import android.os.Bundle
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.Observer
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.grocerystore.databinding.ActivityMainBinding
import com.example.grocerystore.models.GroceryItem
import com.example.grocerystore.viewmodels.GroceryViewModel

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private val viewModel: GroceryViewModel by viewModels()
    private val groceryAdapter = GroceryAdapter()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Inflate the layout
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Set up RecyclerView
        binding.groceryRecyclerView.layoutManager = LinearLayoutManager(this)
        binding.groceryRecyclerView.adapter = groceryAdapter

        // Observe LiveData from ViewModel
        viewModel.groceryItems.observe(this, Observer { items ->
            groceryAdapter.submitList(items)
        })

        // Add sample item on button click
        binding.addItemButton.setOnClickListener {
            val item = GroceryItem(1, "Sample Item", 10.0)
            viewModel.addItem(item)
        }

        // Load initial data
        viewModel.loadItems()
    }
}
```

---

### 7. Grocery Adapter (`GroceryAdapter.kt`)
```kotlin
package com.example.grocerystore.views

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.grocerystore.models.GroceryItem
import com.example.grocerystore.databinding.CustomItemViewBinding

// Adapter for displaying grocery items in a RecyclerView
class GroceryAdapter : RecyclerView.Adapter<GroceryAdapter.GroceryViewHolder>() {

    private val items = mutableListOf<GroceryItem>()

    // ViewHolder to hold and bind custom item view
    class GroceryViewHolder(val binding: CustomItemViewBinding) : RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): GroceryViewHolder {
        val binding = CustomItemViewBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return GroceryViewHolder(binding)
    }

    override fun onBindViewHolder(holder: GroceryViewHolder, position: Int) {
        val item = items[position]
        holder.binding.itemNameTextView.text = item.name
        holder.binding.itemPriceTextView.text = "$${String.format("%.2f", item.price)}"
    }

    override fun getItemCount(): Int = items.size

    fun submitList(newItems: List<GroceryItem>) {
        items.clear()
        items.addAll(newItems)
        notifyDataSetChanged()
    }
}
```

---

### 8. Layout Files

#### `res/layout/activity_main.xml`
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <Button
        android:id="@+id/addItemButton"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Add Item" />

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/groceryRecyclerView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_marginTop="16dp" />
</LinearLayout>
```

#### `res/layout/custom_item_view.xml`
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:padding="8dp">

    <TextView
        android:id="@+id/itemNameTextView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="18sp"
        android:textStyle="bold" />

    <TextView
        android:id="@+id/itemPriceTextView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="16sp"
        android:layout_marginTop="4dp" />
</LinearLayout>
```

---

### 9. `AndroidManifest.xml`
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.grocerystore">

    <application
        android:allowBackup="true"
        android:label="Grocery Store"
        android:icon="@mipmap/ic_launcher"
        android:theme="@style/Theme.AppCompat.Light.DarkActionBar">
        <activity android:name=".views.MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
