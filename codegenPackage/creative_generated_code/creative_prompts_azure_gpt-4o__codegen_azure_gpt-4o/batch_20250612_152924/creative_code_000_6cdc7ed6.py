"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadkhahhadi.ir
Prompt: Write an Android application using MVVM architecture and custom views, as described by Hadi Dadkhah's expertise. Include examples of integrating Room and RxJava libraries.
Generated: DETERMINISTIC_6cdc7ed6acc3ffef
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
package com.example.mvvmapp

import android.os.Bundle
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.Observer
import com.example.mvvmapp.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private val mainViewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Observe LiveData from ViewModel
        mainViewModel.itemsList.observe(this, Observer { items ->
            binding.customView.setItems(items) // Set data to custom view
        })

        // Fetch data when activity starts
        mainViewModel.fetchItems()
    }
}
```

```kotlin
// MainViewModel.kt
package com.example.mvvmapp

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.mvvmapp.data.ItemRepository
import com.example.mvvmapp.data.models.Item
import io.reactivex.rxjava3.android.schedulers.AndroidSchedulers
import io.reactivex.rxjava3.disposables.CompositeDisposable
import io.reactivex.rxjava3.schedulers.Schedulers

class MainViewModel : ViewModel() {

    private val repository = ItemRepository()
    private val disposables = CompositeDisposable()

    private val _itemsList = MutableLiveData<List<Item>>()
    val itemsList: LiveData<List<Item>> get() = _itemsList

    // Fetch items from repository using RxJava
    fun fetchItems() {
        disposables.add(
            repository.getItems()
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(
                    { items -> _itemsList.value = items },
                    { error -> error.printStackTrace() } // Handle errors properly
                )
        )
    }

    override fun onCleared() {
        super.onCleared()
        disposables.clear()
    }
}
```

```kotlin
// ItemRepository.kt
package com.example.mvvmapp.data

import com.example.mvvmapp.data.local.AppDatabase
import com.example.mvvmapp.data.models.Item
import io.reactivex.rxjava3.core.Single

class ItemRepository {

    private val itemDao = AppDatabase.getInstance().itemDao()

    // Fetch items using Room and RxJava
    fun getItems(): Single<List<Item>> {
        return itemDao.getAllItems()
    }
}
```

```kotlin
// ItemDao.kt
package com.example.mvvmapp.data.local

import androidx.room.Dao
import androidx.room.Query
import com.example.mvvmapp.data.models.Item
import io.reactivex.rxjava3.core.Single

@Dao
interface ItemDao {
    @Query("SELECT * FROM items")
    fun getAllItems(): Single<List<Item>>
}
```

```kotlin
// AppDatabase.kt
package com.example.mvvmapp.data.local

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import com.example.mvvmapp.data.models.Item

@Database(entities = [Item::class], version = 1, exportSchema = false)
abstract class AppDatabase : RoomDatabase() {
    abstract fun itemDao(): ItemDao

    companion object {
        @Volatile
        private var INSTANCE: AppDatabase? = null

        fun getInstance(context: Context): AppDatabase =
            INSTANCE ?: synchronized(this) {
                INSTANCE ?: Room.databaseBuilder(
                    context.applicationContext,
                    AppDatabase::class.java,
                    "app_database"
                ).build().also { INSTANCE = it }
            }
    }
}
```

```kotlin
// Item.kt
package com.example.mvvmapp.data.models

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "items")
data class Item(
    @PrimaryKey(autoGenerate = true) val id: Int,
    val name: String,
    val description: String
)
```

```kotlin
// CustomView.kt
package com.example.mvvmapp.ui.views

import android.content.Context
import android.util.AttributeSet
import android.view.LayoutInflater
import android.widget.LinearLayout
import com.example.mvvmapp.databinding.CustomViewBinding
import com.example.mvvmapp.data.models.Item

class CustomView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : LinearLayout(context, attrs, defStyleAttr) {

    private val binding = CustomViewBinding.inflate(LayoutInflater.from(context), this, true)

    // Set data to display in the custom view
    fun setItems(items: List<Item>) {
        binding.itemsTextView.text = items.joinToString("\n") { "${it.name}: ${it.description}" }
    }
}
```

```xml
<!-- activity_main.xml -->
<layout xmlns:android="http://schemas.android.com/apk/res/android">
    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <com.example.mvvmapp.ui.views.CustomView
            android:id="@+id/customView"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_margin="16dp"
            android:background="@android:color/white" />

    </androidx.constraintlayout.widget.ConstraintLayout>
</layout>
```

```xml
<!-- custom_view.xml -->
<layout xmlns:android="http://schemas.android.com/apk/res/android">
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/itemsTextView"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:padding="16dp"
            android:textSize="16sp" />
    </LinearLayout>
</layout>
```

```gradle
// build.gradle (app level)
dependencies {
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.6.0"
    implementation "androidx.room:room-runtime:2.5.2"
    kapt "androidx.room:room-compiler:2.5.2"
    implementation "io.reactivex.rxjava3:rxjava:3.1.6"
    implementation "io.reactivex.rxjava3:rxandroid:3.0.0"
}
```
