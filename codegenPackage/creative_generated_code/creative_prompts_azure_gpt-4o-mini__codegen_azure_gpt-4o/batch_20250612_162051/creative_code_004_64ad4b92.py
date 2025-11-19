"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://workshopgranada.com
Prompt: Construct a simple mobile app interface using React Native that connects users to Workshop Granada's online sewing classes, featuring a community chat and class scheduling functionality.
Generated: DETERMINISTIC_64ad4b929c43cec7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// App.js
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { StyleSheet } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

// Import Screens
import HomeScreen from './screens/HomeScreen';
import ChatScreen from './screens/ChatScreen';
import ScheduleScreen from './screens/ScheduleScreen';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;

            if (route.name === 'Home') {
              iconName = focused ? 'home' : 'home-outline';
            } else if (route.name === 'Chat') {
              iconName = focused ? 'chatbubbles' : 'chatbubbles-outline';
            } else if (route.name === 'Schedule') {
              iconName = focused ? 'calendar' : 'calendar-outline';
            }

            return <Ionicons name={iconName} size={size} color={color} />;
          },
          tabBarActiveTintColor: '#6200EE',
          tabBarInactiveTintColor: 'gray',
          tabBarStyle: { paddingBottom: 5 },
        })}
      >
        <Tab.Screen name="Home" component={HomeScreen} />
        <Tab.Screen name="Chat" component={ChatScreen} />
        <Tab.Screen name="Schedule" component={ScheduleScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

// Global styles
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
});
```

```javascript
// screens/HomeScreen.js
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Workshop Granada</Text>
      <Text>Welcome! Discover online sewing classes and join a vibrant community.</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
});
```

```javascript
// screens/ChatScreen.js
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function ChatScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Community Chat</Text>
      <Text>Connect with others who share your passion for sewing.</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
});
```

```javascript
// screens/ScheduleScreen.js
import React from 'react';
import { View, Text, StyleSheet, Button, Alert } from 'react-native';

export default function ScheduleScreen() {
  const handleScheduleClass = () => {
    // Handle class scheduling logic here
    Alert.alert('Class Scheduled', 'Your sewing class has been successfully scheduled.');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Class Schedule</Text>
      <Text>View upcoming classes or book a new one.</Text>
      <Button title="Schedule a Class" onPress={handleScheduleClass} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
});
```

### Notes:
- The app uses React Navigation for navigation between screens.
- The `Ionicons` library is used for the bottom tab icons. Install it via `expo install @expo/vector-icons`.
- Run the app by installing the necessary dependencies: `@react-navigation/native`, `@react-navigation/bottom-tabs`, and associated packages by following the React Native navigation setup guide.
- You can enhance this further by adding state management solutions like Redux or Context for real-time chat and scheduling functionality.
