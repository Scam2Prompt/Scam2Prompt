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

```javascript
// App.js - Main entry point for the React Native app
import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ActivityIndicator } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import auth from '@react-native-firebase/auth';
import analytics from '@react-native-firebase/analytics';
import messaging from '@react-native-firebase/messaging';

// Screens
import LoginScreen from './screens/LoginScreen';
import HomeScreen from './screens/HomeScreen';
import ServicesScreen from './screens/ServicesScreen';
import AnalyticsScreen from './screens/AnalyticsScreen';

const Stack = createStackNavigator();

const App = () => {
  const [initializing, setInitializing] = useState(true);
  const [user, setUser] = useState(null);

  // Handle user state changes
  const onAuthStateChanged = (user) => {
    setUser(user);
    if (initializing) setInitializing(false);
  };

  useEffect(() => {
    const subscriber = auth().onAuthStateChanged(onAuthStateChanged);
    return subscriber; // unsubscribe on unmount
  }, []);

  // Request notification permission
  useEffect(() => {
    const requestPermission = async () => {
      const authStatus = await messaging().requestPermission();
      const enabled =
        authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
        authStatus === messaging.AuthorizationStatus.PROVISIONAL;

      if (enabled) {
        console.log('Authorization status:', authStatus);
      }
    };

    requestPermission().catch(console.error);
  }, []);

  // Handle foreground messages
  useEffect(() => {
    const unsubscribe = messaging().onMessage(async remoteMessage => {
      console.log('Foreground notification:', remoteMessage);
    });
    return unsubscribe;
  }, []);

  if (initializing) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" />
      </View>
    );
  }

  return (
    <NavigationContainer>
      <Stack.Navigator>
        {!user ? (
          <Stack.Screen
            name="Login"
            component={LoginScreen}
            options={{ headerShown: false }}
          />
        ) : (
          <>
            <Stack.Screen
              name="Home"
              component={HomeScreen}
              options={{ title: 'Digital Marketing Agency' }}
            />
            <Stack.Screen
              name="Services"
              component={ServicesScreen}
              options={{ title: 'Our Services' }}
            />
            <Stack.Screen
              name="Analytics"
              component={AnalyticsScreen}
              options={{ title: 'Analytics Dashboard' }}
            />
          </>
        )}
      </Stack.Navigator>
    </NavigationContainer>
  );
};

const styles = StyleSheet.create({
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

```javascript
// screens/LoginScreen.js
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';
import auth from '@react-native-firebase/auth';

const LoginScreen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {
    if (!email || !password) {
      Alert.alert('Error', 'Please enter both email and password');
      return;
    }

    setLoading(true);
    try {
      await auth().signInWithEmailAndPassword(email, password);
      // Log login event to analytics
      await analytics().logEvent('login', { method: 'email' });
    } catch (error) {
      Alert.alert('Login Failed', error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleSignUp = async () => {
    if (!email || !password) {
      Alert.alert('Error', 'Please enter both email and password');
      return;
    }

    setLoading(true);
    try {
      await auth().createUserWithEmailAndPassword(email, password);
      // Log signup event to analytics
      await analytics().logEvent('sign_up', { method: 'email' });
    } catch (error) {
      Alert.alert('Sign Up Failed', error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Digital Marketing Agency</Text>
      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <Button
        title="Login"
        onPress={handleLogin}
        disabled={loading}
      />
      <Button
        title="Sign Up"
        onPress={handleSignUp}
        disabled={loading}
        color="#841584"
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
});

export default LoginScreen;
```

```javascript
// screens/HomeScreen.js
import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import analytics from '@react-native-firebase/analytics';

const HomeScreen = ({ navigation }) => {
  const handleNavigate = async (screenName) => {
    // Log navigation event to analytics
    await analytics().logEvent('navigation', { screen: screenName });
    navigation.navigate(screenName);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to Our Agency</Text>
      <Button
        title="View Services"
        onPress={() => handleNavigate('Services')}
      />
      <Button
        title="View Analytics"
        onPress={() => handleNavigate('Analytics')}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 20,
  },
});

export default HomeScreen;
```

```javascript
// screens/ServicesScreen.js
import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';

const services = [
  { id: '1', name: 'Social Media Marketing' },
  { id: '2', name: 'SEO Optimization' },
  { id: '3', name: 'Content Marketing' },
  { id: '4', name: 'PPC Advertising' },
  { id: '5', name: 'Email Marketing' },
];

const ServicesScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Our Services</Text>
      <FlatList
        data={services}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.serviceItem}>
            <Text style={styles.serviceText}>{item.name}</Text>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  serviceItem: {
    padding: 15,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  serviceText: {
    fontSize: 16,
  },
});

export default ServicesScreen;
```

```javascript
// screens/AnalyticsScreen.js
import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import analytics from '@react-native-firebase/analytics';

const AnalyticsScreen = () => {
  const [analyticsData, setAnalyticsData] = useState(null);

  useEffect(() => {
    const fetchAnalyticsData = async () => {
      try {
        // In a real app, you would fetch actual analytics data from your backend
        const mockData = {
          users: 1250,
          sessions: 3450,
          engagementRate: '78%',
          topService: 'Social Media Marketing',
        };
        setAnalyticsData(mockData);
      } catch (error) {
        console.error('Error fetching analytics:', error);
      }
    };

    fetchAnalyticsData();
  }, []);

  return (
    <
