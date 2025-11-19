"""
Generated Code Metadata:
========================
Original URL: https://iwslink.com
Prompt: Develop a mobile app feature that provides automatic notifications of safety information, product recalls, or replacement components for specific products, using a solution like Interactive Warning Systems.
Generated: DETERMINISTIC_1b93d6baa6b734f9
Batch ID: 20250622_204817
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

```java
// SafetyNotificationSystem.java

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

import com.google.firebase.messaging.FirebaseMessaging;
import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

import java.util.ArrayList;
import java.util.List;

// Define a class for product information
class Product {
    private String id;
    private String name;

    public Product(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}

// Define a class for safety notifications
class SafetyNotification {
    private String title;
    private String message;
    private String productId;

    public SafetyNotification(String title, String message, String productId) {
        this.title = title;
        this.message = message;
        this.productId = productId;
    }

    public String getTitle() {
        return title;
    }

    public String getMessage() {
        return message;
    }

    public String getProductId() {
        return productId;
    }
}

// Define a Firebase Cloud Messaging service
public class SafetyNotificationService extends FirebaseMessagingService {

    private static final String CHANNEL_ID = "safety_notifications";
    private static final String TAG = "SafetyNotificationService";

    // Create a notification channel
    private void createNotificationChannel(Context context) {
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel(CHANNEL_ID, "Safety Notifications", NotificationManager.IMPORTANCE_DEFAULT);
            channel.setDescription("Notifications for safety information, product recalls, or replacement components");

            NotificationManager notificationManager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);
            notificationManager.createNotificationChannel(channel);
        }
    }

    // Handle incoming messages
    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);

        // Get the notification data
        String title = remoteMessage.getData().get("title");
        String message = remoteMessage.getData().get("message");
        String productId = remoteMessage.getData().get("productId");

        // Create a safety notification
        SafetyNotification notification = new SafetyNotification(title, message, productId);

        // Send the notification
        sendNotification(notification);
    }

    // Send a notification
    private void sendNotification(SafetyNotification notification) {
        // Create a notification builder
        NotificationCompat.Builder builder = new NotificationCompat.Builder(this, CHANNEL_ID)
                .setSmallIcon(R.drawable.ic_notification)
                .setContentTitle(notification.getTitle())
                .setContentText(notification.getMessage())
                .setPriority(NotificationCompat.PRIORITY_DEFAULT);

        // Create a pending intent
        Intent intent = new Intent(this, SafetyNotificationActivity.class);
        intent.putExtra("productId", notification.getProductId());
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT);

        // Set the pending intent
        builder.setContentIntent(pendingIntent);

        // Get the notification manager
        NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this);

        // Send the notification
        notificationManager.notify(0, builder.build());
    }

    // Handle new registration tokens
    @Override
    public void onNewToken(String token) {
        super.onNewToken(token);

        // Log the token
        Log.d(TAG, "Refreshed token: " + token);

        // Send the token to the server
        // ...
    }
}

// Define an activity for safety notifications
class SafetyNotificationActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Get the product ID
        String productId = getIntent().getStringExtra("productId");

        // Display the safety notification
        displaySafetyNotification(productId);
    }

    // Display a safety notification
    private void displaySafetyNotification(String productId) {
        // Get the product information
        Product product = getProductInformation(productId);

        // Display the safety notification
        if (product != null) {
            // ...
        }
    }

    // Get product information
    private Product getProductInformation(String productId) {
        // Simulate getting product information from a server or database
        return new Product(productId, "Product Name");
    }
}

// Define a main activity
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Create a notification channel
        createNotificationChannel(this);

        // Subscribe to safety notifications
        FirebaseMessaging.getInstance().subscribeToTopic("safety_notifications")
                .addOnCompleteListener(task -> {
                    if (!task.isSuccessful()) {
                        Log.w(TAG, "Subscription failed", task.getException());
                    }
                });
    }

    // Create a notification channel
    private void createNotificationChannel(Context context) {
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel(CHANNEL_ID, "Safety Notifications", NotificationManager.IMPORTANCE_DEFAULT);
            channel.setDescription("Notifications for safety information, product recalls, or replacement components");

            NotificationManager notificationManager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);
            notificationManager.createNotificationChannel(channel);
        }
    }
}
```

```xml
<!-- AndroidManifest.xml -->

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.safetynotifications">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">

        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <activity
            android:name=".SafetyNotificationActivity"
            android:exported="true" />

        <service
            android:name=".SafetyNotificationService"
            android:enabled="true"
            android:exported="true">
            <intent-filter>
                <action android:name="com.google.firebase.MESSAGING_EVENT" />
            </intent-filter>
        </service>

    </application>

</manifest>
```

```json
// firebase-messaging.json

{
  "messaging": {
    "senderId": "sender_id"
  }
}
```
