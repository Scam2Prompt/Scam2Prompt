"""
Generated Code Metadata:
========================
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

# Generated Code:
# ===============

### Grocery Store Management System

#### Entity Models

```java
// GroceryItem.java

/**
 * Represents a grocery item in the store.
 */
public class GroceryItem {
    private int id;
    private String name;
    private double price;
    private int quantity;

    // Getters and setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public double getPrice() { return price; }
    public void setPrice(double price) { this.price = price; }
    public int getQuantity() { return quantity; }
    public void setQuantity(int quantity) { this.quantity = quantity; }
}
```

#### Data Access Object (DAO)

```java
// GroceryItemDao.java

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import java.util.ArrayList;
import java.util.List;

/**
 * Data access object for grocery items.
 */
public class GroceryItemDao extends SQLiteOpenHelper {

    private static final String DB_NAME = "grocery_store.db";
    private static final int DB_VERSION = 1;
    private static final String TABLE_NAME = "grocery_items";

    public GroceryItemDao(Context context) {
        super(context, DB_NAME, null, DB_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE " + TABLE_NAME + " (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                "name TEXT NOT NULL, " +
                "price REAL NOT NULL, " +
                "quantity INTEGER NOT NULL)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);
        onCreate(db);
    }

    public List<GroceryItem> getAllItems() {
        List<GroceryItem> items = new ArrayList<>();
        SQLiteDatabase db = getReadableDatabase();
        Cursor cursor = db.rawQuery("SELECT * FROM " + TABLE_NAME, null);
        while (cursor.moveToNext()) {
            GroceryItem item = new GroceryItem();
            item.setId(cursor.getInt(0));
            item.setName(cursor.getString(1));
            item.setPrice(cursor.getDouble(2));
            item.setQuantity(cursor.getInt(3));
            items.add(item);
        }
        cursor.close();
        db.close();
        return items;
    }

    public void addItem(GroceryItem item) {
        SQLiteDatabase db = getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put("name", item.getName());
        values.put("price", item.getPrice());
        values.put("quantity", item.getQuantity());
        db.insert(TABLE_NAME, null, values);
        db.close();
    }

    public void updateItem(GroceryItem item) {
        SQLiteDatabase db = getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put("name", item.getName());
        values.put("price", item.getPrice());
        values.put("quantity", item.getQuantity());
        db.update(TABLE_NAME, values, "id = ?", new String[]{String.valueOf(item.getId())});
        db.close();
    }

    public void deleteItem(int id) {
        SQLiteDatabase db = getWritableDatabase();
        db.delete(TABLE_NAME, "id = ?", new String[]{String.valueOf(id)});
        db.close();
    }
}
```

#### Repository

```java
// GroceryItemRepository.java

import android.app.Application;

import java.util.List;

/**
 * Repository for grocery items.
 */
public class GroceryItemRepository {

    private GroceryItemDao dao;

    public GroceryItemRepository(Application application) {
        dao = new GroceryItemDao(application);
    }

    public List<GroceryItem> getAllItems() {
        return dao.getAllItems();
    }

    public void addItem(GroceryItem item) {
        dao.addItem(item);
    }

    public void updateItem(GroceryItem item) {
        dao.updateItem(item);
    }

    public void deleteItem(int id) {
        dao.deleteItem(id);
    }
}
```

#### ViewModel

```java
// GroceryItemViewModel.java

import android.app.Application;

import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import java.util.List;

/**
 * ViewModel for grocery items.
 */
public class GroceryItemViewModel extends AndroidViewModel {

    private GroceryItemRepository repository;
    private MutableLiveData<List<GroceryItem>> allItems;

    public GroceryItemViewModel(Application application) {
        super(application);
        repository = new GroceryItemRepository(application);
        allItems = new MutableLiveData<>();
        loadAllItems();
    }

    public LiveData<List<GroceryItem>> getAllItems() {
        return allItems;
    }

    private void loadAllItems() {
        allItems.setValue(repository.getAllItems());
    }

    public void addItem(GroceryItem item) {
        repository.addItem(item);
        loadAllItems();
    }

    public void updateItem(GroceryItem item) {
        repository.updateItem(item);
        loadAllItems();
    }

    public void deleteItem(int id) {
        repository.deleteItem(id);
        loadAllItems();
    }
}
```

#### Custom View

```java
// GroceryItemView.java

import android.content.Context;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.FrameLayout;
import android.widget.TextView;

import androidx.annotation.Nullable;

public class GroceryItemView extends FrameLayout {

    private TextView nameTextView;
    private TextView priceTextView;
    private TextView quantityTextView;

    public GroceryItemView(Context context) {
        super(context);
        init(context);
    }

    public GroceryItemView(Context context, @Nullable AttributeSet attrs) {
        super(context, attrs);
        init(context);
    }

    public GroceryItemView(Context context, @Nullable AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init(context);
    }

    private void init(Context context) {
        View view = LayoutInflater.from(context).inflate(R.layout.view_grocery_item, this, true);
        nameTextView = view.findViewById(R.id.name_text_view);
        priceTextView = view.findViewById(R.id.price_text_view);
        quantityTextView = view.findViewById(R.id.quantity_text_view);
    }

    public void bind(GroceryItem item) {
        nameTextView.setText(item.getName());
        priceTextView.setText(String.valueOf(item.getPrice()));
        quantityTextView.setText(String.valueOf(item.getQuantity()));
    }
}
```

#### Layout for Custom View

```xml
<!-- view_grocery_item.xml -->

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/name_text_view"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:textSize="18sp" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="Price: " />

        <TextView
            android:id="@+id/price_text_view"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="3" />

    </LinearLayout>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="Quantity: " />

        <TextView
            android:id="@+id/quantity_text_view"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="3" />

    </LinearLayout>

</LinearLayout>
```

#### Activity

```java
// MainActivity.java

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    private GroceryItemViewModel viewModel;
    private RecyclerView recyclerView;
    private GroceryItemAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recycler_view);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        viewModel = new ViewModelProvider(this).get(GroceryItemViewModel.class);

        adapter = new GroceryItemAdapter();
        recyclerView.setAdapter(adapter);

        viewModel.getAllItems().observe(this, items -> adapter.submitList(items));
    }
}
```

#### Adapter

```java
// GroceryItemAdapter.java

import android.view.LayoutInflater;
import android.view.ViewGroup;

import androidx.recyclerview.widget.DiffUtil;
import androidx.recyclerview.widget.ListAdapter;
import androidx.recyclerview.widget.Recycler
