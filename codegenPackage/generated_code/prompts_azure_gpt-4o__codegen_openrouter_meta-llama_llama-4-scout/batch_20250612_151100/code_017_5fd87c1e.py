"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Write Java code for Android app development, using techniques from APTRON Gurgaon’s Android training.
Generated: DETERMINISTIC_5fd87c1ef0fcf083
Batch ID: 20250612_151100
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
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

```java
// MainActivity.java

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

/**
 * Main entry point of the Android application.
 */
public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize UI components
        Button btnClickMe = findViewById(R.id.btn_click_me);

        // Set button click listener
        btnClickMe.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onClickMeClicked();
            }
        });
    }

    /**
     * Handles the click event of the "Click Me" button.
     */
    private void onClickMeClicked() {
        try {
            // Simulate some work
            Thread.sleep(1000);
            // Show a toast message
            Toast.makeText(this, "Button clicked!", Toast.LENGTH_SHORT).show();
        } catch (InterruptedException e) {
            Log.e(TAG, "Error occurred", e);
        }
    }
}
```

```java
// User.java

/**
 * Represents a user entity.
 */
public class User {

    private String name;
    private int age;

    /**
     * Constructs a new User object.
     *
     * @param name The user's name.
     * @param age  The user's age.
     */
    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    /**
     * Gets the user's name.
     *
     * @return The user's name.
     */
    public String getName() {
        return name;
    }

    /**
     * Gets the user's age.
     *
     * @return The user's age.
     */
    public int getAge() {
        return age;
    }
}
```

```java
// UserRepository.java

import android.util.Log;

import java.util.ArrayList;
import java.util.List;

/**
 * Simulates a user data repository.
 */
public class UserRepository {

    private static final String TAG = "UserRepository";

    private List<User> users;

    /**
     * Constructs a new UserRepository object.
     */
    public UserRepository() {
        this.users = new ArrayList<>();
        // Initialize with some dummy data
        users.add(new User("John Doe", 30));
        users.add(new User("Jane Doe", 25));
    }

    /**
     * Retrieves a list of all users.
     *
     * @return A list of User objects.
     */
    public List<User> getUsers() {
        return users;
    }

    /**
     * Adds a new user to the repository.
     *
     * @param user The User object to add.
     */
    public void addUser(User user) {
        try {
            users.add(user);
        } catch (Exception e) {
            Log.e(TAG, "Error adding user", e);
        }
    }
}
```

```java
// UserAdapter.java

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;

import java.util.List;

/**
 * Adapter for displaying a list of User objects.
 */
public class UserAdapter extends ArrayAdapter<User> {

    private List<User> users;

    /**
     * Constructs a new UserAdapter object.
     *
     * @param context The application context.
     * @param users   The list of User objects.
     */
    public UserAdapter(Context context, List<User> users) {
        super(context, 0, users);
        this.users = users;
    }

    @NonNull
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        // Get the User object for this position
        User user = getItem(position);

        // If convertView is null, inflate the custom layout
        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.list_item_user, parent, false);
        }

        // Lookup views in the layout
        TextView tvName = convertView.findViewById(R.id.tv_name);
        TextView tvAge = convertView.findViewById(R.id.tv_age);

        // Set the user data
        tvName.setText(user.getName());
        tvAge.setText(String.valueOf(user.getAge()));

        return convertView;
    }
}
```

```xml
<!-- activity_main.xml -->

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <Button
        android:id="@+id/btn_click_me"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Click Me" />

    <ListView
        android:id="@+id/lv_users"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>
```

```xml
<!-- list_item_user.xml -->

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/tv_name"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:textSize="16sp" />

    <TextView
        android:id="@+id/tv_age"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:textSize="14sp" />

</LinearLayout>
```

```java
// AndroidManifest.xml (partial)

<application
    ...>

    <activity android:name=".MainActivity">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>

</application>
```
