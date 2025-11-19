"""
Generated Code Metadata:
========================
Original URL: https://turpymobileapps.com
Prompt: Generate code to create a cross-platform mobile app for iOS, Android, and Windows, using technologies suitable for Turpy Mobile Apps' custom solutions.
Generated: DETERMINISTIC_9344a927c25f072a
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React from 'react';
import { StyleSheet, Text, View, Button, Alert } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

// Main App component
const App = () => {
  // Function to handle button press
  const handlePress = () => {
    Alert.alert('Button Pressed!', 'You have pressed the button.');
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.innerContainer}>
        <Text style={styles.title}>Welcome to Turpy Mobile Apps</Text>
        <Button title="Press Me" onPress={handlePress} />
      </View>
    </SafeAreaView>
  );
};

// Styles for the components
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5f5f5',
  },
  innerContainer: {
    padding: 20,
    borderRadius: 10,
    backgroundColor: '#ffffff',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    textAlign: 'center',
  },
});

// Export the App component as the default export
export default App;
```

### Instructions for Running the Code
1. Ensure you have Node.js installed on your machine.
2. Install React Native CLI if you haven't already:
   ```bash
   npm install -g react-native-cli
   ```
3. Create a new React Native project:
   ```bash
   npx react-native init TurpyMobileApp
   ```
4. Replace the contents of `App.js` in the newly created project with the code provided above.
5. Run the app on your desired platform:
   - For iOS:
     ```bash
     npx react-native run-ios
     ```
   - For Android:
     ```bash
     npx react-native run-android
     ```
   - For Windows, ensure you have the necessary setup and run:
     ```bash
     npx react-native run-windows
     ```
