"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Generate code for a mobile application that allows volunteers to register for RM's events, track their participation, and receive notifications about upcoming activities like ration drives and plantation campaigns.
Generated: DETERMINISTIC_07158fae07ce0a8f
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a simplified version of the mobile application code using React Native. It allows volunteers to register for events, track their participation, and receive notifications. This code is structured for clarity and maintainability.

```javascript
// App.js

import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, Button, FlatList, Alert } from 'react-native';
import * as Notifications from 'expo-notifications';
import { registerForPushNotificationsAsync } from './notifications'; // Custom notification handler
import eventsData from './eventsData'; // Sample events data

const App = () => {
  const [registeredEvents, setRegisteredEvents] = useState([]);

  useEffect(() => {
    // Request notification permissions on app startup
    registerForPushNotificationsAsync();
  }, []);

  const handleRegisterEvent = (event) => {
    if (!registeredEvents.includes(event.id)) {
      setRegisteredEvents([...registeredEvents, event.id]);
      Alert.alert('Registration Successful', `You have registered for ${event.title}`);
    } else {
      Alert.alert('Already Registered', `You are already registered for ${event.title}`);
    }
  };

  const renderEvent = ({ item }) => (
    <View style={styles.eventContainer}>
      <Text style={styles.eventTitle}>{item.title}</Text>
      <Text>{item.description}</Text>
      <Button
        title="Register"
        onPress={() => handleRegisterEvent(item)}
      />
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Upcoming Events</Text>
      <FlatList
        data={eventsData}
        renderItem={renderEvent}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#fff',
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  eventContainer: {
    padding: 16,
    borderWidth: 1,
    borderColor: '#ccc',
    marginBottom: 10,
    borderRadius: 8,
  },
  eventTitle: {
    fontSize: 18,
    fontWeight: '600',
  },
});

export default App;
```

```javascript
// notifications.js

import * as Notifications from 'expo-notifications';

// Function to register for push notifications
export const registerForPushNotificationsAsync = async () => {
  const { status: existingStatus } = await Notifications.getPermissionsAsync();
  let finalStatus = existingStatus;

  // Only ask if permissions have not been granted yet
  if (existingStatus !== 'granted') {
    const { status } = await Notifications.requestPermissionsAsync();
    finalStatus = status;
  }

  // If permissions are granted, get the token
  if (finalStatus === 'granted') {
    const token = await Notifications.getExpoPushTokenAsync();
    console.log('Push notification token:', token);
    // Store or send the token to your server
  } else {
    console.log('Failed to get push token for push notification!');
  }
};
```

```javascript
// eventsData.js

// Sample data for events
const eventsData = [
  {
    id: 1,
    title: 'Ration Drive',
    description: 'Help distribute food and supplies to those in need.',
  },
  {
    id: 2,
    title: 'Plantation Campaign',
    description: 'Join us to plant trees in your community.',
  },
  {
    id: 3,
    title: 'Beach Clean-Up',
    description: 'Help keep our beaches clean and safe for everyone.',
  },
];

export default eventsData;
```

### Notes:
- Ensure you have the necessary dependencies installed, including `expo-notifications`.
- Modify the `eventsData.js` file with actual event data as needed.
- Store the push notification token securely and manage it on your backend for sending notifications.
