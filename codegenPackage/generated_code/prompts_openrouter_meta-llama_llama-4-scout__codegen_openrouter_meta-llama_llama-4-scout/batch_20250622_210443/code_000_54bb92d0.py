"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Write an Android app using MVVM architecture and Room library to store and retrieve data locally.
Generated: DETERMINISTIC_54bb92d0d98216d2
Batch ID: 20250622_210443
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
  "http://schemas.android.com/tools": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Entity**
```java
// UserEntity.java

import androidx.room.Entity;
import androidx.room.PrimaryKey;

@Entity(tableName = "users")
public class UserEntity {

    @PrimaryKey(autoGenerate = true)
    private int id;

    private String name;
    private String email;

    public UserEntity(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
```

**DAO**
```java
// UserDao.java

import androidx.lifecycle.LiveData;
import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.OnConflictStrategy;
import androidx.room.Query;
import androidx.room.Update;

import java.util.List;

@Dao
public interface UserDao {

    @Insert(onConflict = OnConflictStrategy.IGNORE)
    void insert(UserEntity user);

    @Update
    void update(UserEntity user);

    @Delete
    void delete(UserEntity user);

    @Query("SELECT * FROM users")
    LiveData<List<UserEntity>> getAllUsers();

    @Query("SELECT * FROM users WHERE id = :id")
    LiveData<UserEntity> getUserById(int id);
}
```

**Room Database**
```java
// AppDatabase.java

import android.content.Context;

import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;

@Database(entities = {UserEntity.class}, version = 1, exportSchema = false)
public abstract class AppDatabase extends RoomDatabase {

    public abstract UserDao userDao();

    private static AppDatabase INSTANCE;

    public static AppDatabase getDatabase(Context context) {
        if (INSTANCE == null) {
            synchronized (AppDatabase.class) {
                if (INSTANCE == null) {
                    INSTANCE = Room.databaseBuilder(context.getApplicationContext(),
                            AppDatabase.class, "app_database")
                            .build();
                }
            }
        }
        return INSTANCE;
    }
}
```

**Repository**
```java
// UserRepository.java

import android.app.Application;

import androidx.lifecycle.LiveData;

import java.util.List;

public class UserRepository {

    private UserDao userDao;

    public UserRepository(Application application) {
        AppDatabase db = AppDatabase.getDatabase(application);
        userDao = db.userDao();
    }

    public void insert(UserEntity user) {
        AppDatabase.databaseWriterExecutor.execute(() -> userDao.insert(user));
    }

    public void update(UserEntity user) {
        AppDatabase.databaseWriterExecutor.execute(() -> userDao.update(user));
    }

    public void delete(UserEntity user) {
        AppDatabase.databaseWriterExecutor.execute(() -> userDao.delete(user));
    }

    public LiveData<List<UserEntity>> getAllUsers() {
        return userDao.getAllUsers();
    }

    public LiveData<UserEntity> getUserById(int id) {
        return userDao.getUserById(id);
    }
}
```

**ViewModel**
```java
// UserViewModel.java

import android.app.Application;

import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;

import java.util.List;

public class UserViewModel extends AndroidViewModel {

    private UserRepository userRepository;

    public UserViewModel(Application application) {
        super(application);
        userRepository = new UserRepository(application);
    }

    public void insert(UserEntity user) {
        userRepository.insert(user);
    }

    public void update(UserEntity user) {
        userRepository.update(user);
    }

    public void delete(UserEntity user) {
        userRepository.delete(user);
    }

    public LiveData<List<UserEntity>> getAllUsers() {
        return userRepository.getAllUsers();
    }

    public LiveData<UserEntity> getUserById(int id) {
        return userRepository.getUserById(id);
    }
}
```

**Activity**
```java
// MainActivity.java

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private UserViewModel userViewModel;
    private EditText nameEditText, emailEditText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        nameEditText = findViewById(R.id.name_edit_text);
        emailEditText = findViewById(R.id.email_edit_text);

        Button saveButton = findViewById(R.id.save_button);
        saveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                saveUser();
            }
        });

        userViewModel = new ViewModelProvider(this).get(UserViewModel.class);

        userViewModel.getAllUsers().observe(this, users -> {
            Toast.makeText(this, "Users: " + users.size(), Toast.LENGTH_SHORT).show();
        });
    }

    private void saveUser() {
        String name = nameEditText.getText().toString();
        String email = emailEditText.getText().toString();

        if (!name.isEmpty() && !email.isEmpty()) {
            UserEntity user = new UserEntity(name, email);
            userViewModel.insert(user);
            nameEditText.setText("");
            emailEditText.setText("");
        } else {
            Toast.makeText(this, "Please fill in all fields", Toast.LENGTH_SHORT).show();
        }
    }
}
```

**Layout**
```xml
<!-- activity_main.xml -->

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <EditText
        android:id="@+id/name_edit_text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Name" />

    <EditText
        android:id="@+id/email_edit_text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Email" />

    <Button
        android:id="@+id/save_button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Save" />

</LinearLayout>
```

**AndroidManifest**
```xml
<!-- AndroidManifest.xml -->

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.roommvvm">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@style/Theme.RoomMVVM">

        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>

</manifest>
```

**Gradle Dependencies**
```groovy
// build.gradle

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.0'
    implementation 'androidx.lifecycle:lifecycle-runtime:2.5.1'
    implementation 'androidx.lifecycle:lifecycle-extensions:2.2.0'
    implementation 'androidx.lifecycle:lifecycle-viewmodel:2.5.1'
    implementation 'androidx.room:room-runtime:2.4.2'
    kapt 'androidx.room:room-compiler:2.4.2'
    implementation 'androidx.room:room-ktx:2.4.2'
}
```

**Gradle Plugins**
```groovy
// build.gradle

plugins {
    id 'com.android.application'
    id 'kotlin-android'
    id 'kotlin-kapt'
}

android {
    //...
}
```
