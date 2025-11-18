"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pisapopa.pages.dev
Prompt: Write code to create a notification system for a mobile app, similar to the TonPlace app, using Flutter or React Native.
Generated: DETERMINISTIC_96c9e187a58f211b
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Flutter Implementation

```dart
import 'package:flutter/material.dart';
import 'package:firebase_messaging/firebase_messaging.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Notification System',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: NotificationScreen(),
    );
  }
}

class NotificationScreen extends StatefulWidget {
  @override
  _NotificationScreenState createState() => _NotificationScreenState();
}

class _NotificationScreenState extends State<NotificationScreen> {
  late FirebaseMessaging _firebaseMessaging;

  @override
  void initState() {
    super.initState();

    _firebaseMessaging = FirebaseMessaging.instance;

    // Request Notification Permissions
    _firebaseMessaging.requestPermission();

    // Configure Notification Settings
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      if (message.notification != null) {
        _showNotificationDialog(message.notification!.title, message.notification!.body);
      }
    });

    FirebaseMessaging.onMessageOpenedApp.listen((RemoteMessage message) {
      if (message.notification != null) {
        _navigateToDetailsScreen(message.data);
      }
    });

    _firebaseMessaging.getToken().then((String? token) {
      if (token != null) {
        print("FCM Token: $token"); // Save this token to your backend server
      }
    });
  }

  void _showNotificationDialog(String? title, String? body) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(title ?? "New Notification"),
        content: Text(body ?? "You have received a new message."),
        actions: [
          TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text("OK")),
        ],
      ),
    );
  }

  void _navigateToDetailsScreen(Map<String, dynamic> data) {
    // Handle navigation to a specific screen based on the notification data
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => NotificationDetailsScreen(data: data),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Notifications")),
      body: Center(child: Text("Waiting for notifications...")),
    );
  }
}

class NotificationDetailsScreen extends StatelessWidget {
  final Map<String, dynamic> data;

  NotificationDetailsScreen({required this.data});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Notification Details")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Text("Notification Data: ${data.toString()}"),
      ),
    );
  }
}
```

---

### React Native Implementation

```javascript
import React, { useEffect } from 'react';
import { View, Text, Alert, Button } from 'react-native';
import messaging from '@react-native-firebase/messaging';

const NotificationSystem = ({ navigation }) => {
  useEffect(() => {
    // Request Notification Permissions
    const requestPermission = async () => {
      const authStatus = await messaging().requestPermission();
      console.log('Notification Permission Status:', authStatus);
    };

    requestPermission();

    // Get FCM Token
    messaging()
      .getToken()
      .then((token) => {
        console.log('FCM Token:', token); // Save this token to your backend server
      });

    // Handle Notifications while app is in foreground
    const unsubscribeOnMessage = messaging().onMessage(async (remoteMessage) => {
      Alert.alert(
        remoteMessage.notification.title || 'New Notification',
        remoteMessage.notification.body || 'You have received a new message.',
        [{ text: 'OK' }]
      );
    });

    // Handle Notifications when app is opened via notification
    const unsubscribeOnNotificationOpened = messaging().onNotificationOpenedApp((remoteMessage) => {
      if (remoteMessage?.data) {
        navigation.navigate('NotificationDetails', { data: remoteMessage.data });
      }
    });

    // Check initial notification (when app launches via notification)
    messaging()
      .getInitialNotification()
      .then((remoteMessage) => {
        if (remoteMessage?.data) {
          navigation.navigate('NotificationDetails', { data: remoteMessage.data });
        }
      });

    return () => {
      unsubscribeOnMessage();
      unsubscribeOnNotificationOpened();
    };
  }, [navigation]);

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Waiting for notifications...</Text>
    </View>
  );
};

const NotificationDetailsScreen = ({ route }) => {
  const { data } = route.params;

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 18, fontWeight: 'bold' }}>Notification Details</Text>
      <Text style={{ marginTop: 8 }}>{JSON.stringify(data)}</Text>
    </View>
  );
};

// App Navigation (using React Navigation)
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="NotificationSystem">
        <Stack.Screen name="NotificationSystem" component={NotificationSystem} />
        <Stack.Screen name="NotificationDetails" component={NotificationDetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
```
