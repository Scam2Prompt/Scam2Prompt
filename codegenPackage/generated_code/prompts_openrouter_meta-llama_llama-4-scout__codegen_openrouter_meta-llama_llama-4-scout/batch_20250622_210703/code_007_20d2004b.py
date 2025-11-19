"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: "Design a mobile app for a digital marketing agency in Dubai, UAE, using a framework such as React Native or Flutter, including features such as user authentication, push notifications, and in-app analytics."
Generated: DETERMINISTIC_20d2004baa8c522e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide a basic implementation using React Native. Please note that a complete mobile app would require more features, screens, and functionality.

**package.json**
```json
{
  "name": "digital-marketing-agency-app",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "npx react-native start",
    "android": "npx react-native run-android",
    "ios": "npx react-native run-ios"
  },
  "dependencies": {
    "@react-native-community/netinfo": "^6.0.0",
    "@react-native-firebase/app": "^14.3.1",
    "@react-native-firebase/auth": "^14.3.1",
    "@react-native-firebase/messaging": "^14.3.1",
    "@react-native-firebase/perf": "^14.3.1",
    "react": "18.2.0",
    "react-native": "0.71.11",
    "react-navigation": "^6.0.13"
  },
  "devDependencies": {
    "@babel/core": "^7.12.10",
    "@babel/preset-env": "^7.12.11",
    "@babel/preset-react": "^7.12.10",
    "babel-jest": "^27.0.6",
    "jest": "^27.4.5",
    "react-test-renderer": "^18.2.0"
  }
}
```

**App.js**
```jsx
import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { firebase } from './firebaseConfig';
import LoginScreen from './screens/LoginScreen';
import HomeScreen from './screens/HomeScreen';
import { messaging } from '@react-native-firebase/messaging';

const Stack = createStackNavigator();

const App = () => {
  const [user, setUser] = useState(null);
  const [ messagingToken, setMessagingToken] = useState(null);

  useEffect(() => {
    const unsubscribe = firebase.auth().onAuthStateChanged((user) => {
      setUser(user);
    });
    return unsubscribe;
  }, []);

  useEffect(() => {
    const messagingConfig = async () => {
      const token = await messaging().getToken();
      setMessagingToken(token);
    };
    messagingConfig();
  }, []);

  return (
    <NavigationContainer>
      <Stack.Navigator>
        {!user ? (
          <Stack.Screen name="Login" component={LoginScreen} />
        ) : (
          <>
            <Stack.Screen name="Home" component={HomeScreen} />
          </>
        )}
      </Stack.Navigator>
    </NavigationContainer>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

**firebaseConfig.js**
```javascript
import { initializeApp } from '@react-native-firebase/app';
import { getFirestore } from '@react-native-firebase/firestore';
import { getAuth } from '@react-native-firebase/auth';
import { getMessaging } from '@react-native-firebase/messaging';

const firebaseConfig = {
  apiKey: 'YOUR_API_KEY',
  authDomain: 'YOUR_AUTH_DOMAIN',
  projectId: 'YOUR_PROJECT_ID',
  storageBucket: 'YOUR_STORAGE_BUCKET',
  messagingSenderId: 'YOUR_MESSAGING_SENDER_ID',
  appId: 'YOUR_APP_ID',
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);
const messaging = getMessaging(app);

export { db, auth, messaging };
```

**screens/LoginScreen.js**
```jsx
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import { auth } from '../firebaseConfig';

const LoginScreen = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      await auth.signInWithEmailAndPassword(email, password);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={(text) => setEmail(text)}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={(text) => setPassword(text)}
      />
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  input: {
    width: 300,
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 20,
    padding: 10,
  },
});

export default LoginScreen;
```

**screens/HomeScreen.js**
```jsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { auth } from '../firebaseConfig';

const HomeScreen = () => {
  const handleLogout = async () => {
    try {
      await auth.signOut();
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <View style={styles.container}>
      <Text>Welcome to the Home Screen!</Text>
      <Button title="Logout" onPress={handleLogout} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default HomeScreen;
```

**Messaging.js**
```javascript
import { messaging } from '@react-native-firebase/messaging';

const messagingConfig = async () => {
  try {
    const token = await messaging().getToken();
    console.log('Messaging token:', token);
  } catch (error) {
    console.log(error);
  }
};

export default messagingConfig;
```

**android/app/src/main/java/com/digitalmarketingagencyapp/MainActivity.java**
```java
package com.digitalmarketingagencyapp;

import android.os.Bundle;
import com.facebook.react.ReactActivity;
import com.facebook.react.ReactPackage;
import com.facebook.react.shell.MainReactPackage;
import com.facebook.react.uimanager.UIManagerModule;
import com.google.firebase.messaging.FirebaseMessaging;

import java.util.Arrays;
import java.util.List;

public class MainActivity extends ReactActivity {
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    FirebaseMessaging.getInstance().getToken()
      .addOnCompleteListener(task -> {
        if (!task.isSuccessful()) {
          Log.w(TAG, "Fetching FCM registration token failed", task.getException());
          return;
        }

        // Get new FCM registration token
        String token = task.getResult();

        // Log and toast
        Log.d(TAG, "FCM token: " + token);
      });
  }
}
```

**ios/DigitalMarketingAgencyApp/AppDelegate.m**
```objectivec
#import <Firebase/Firebase.h>
#import <React/RCTBridgeModule.h>

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [FIRApp configure];
  [self registerForRemoteNotifications];
  return YES;
}

- (void)registerForRemoteNotifications {
  [[UIApplication sharedApplication] registerForRemoteNotifications];
}

- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  [[FIRMessaging messaging] tokenWithCompletion:^(NSString *token, NSError *error) {
    if (error) {
      NSLog(@"Error getting FCM token: %@", error);
    } else {
      NSLog(@"FCM token: %@", token);
    }
  }];
}

@end
```
