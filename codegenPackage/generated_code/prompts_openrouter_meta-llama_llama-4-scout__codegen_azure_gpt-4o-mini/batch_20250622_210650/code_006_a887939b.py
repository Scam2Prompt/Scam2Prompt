"""
Generated Code Metadata:
========================
Original URL: https://canatechinstitute.ca
Prompt: "Develop a mobile application for a client using a suitable framework and programming language, considering factors such as user experience and usability."
Generated: DETERMINISTIC_a887939b8f2f5992
Batch ID: 20250622_210650
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
import { StyleSheet, View, Text, Button, Alert } from 'react-native';

// Main App component
const App = () => {
  // Function to handle button press
  const handlePress = () => {
    Alert.alert('Button Pressed!', 'You have pressed the button.');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to Our Mobile App</Text>
      <Button title="Press Me" onPress={handlePress} />
    </View>
  );
};

// Styles for the application
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    color: '#333',
  },
});

// Export the App component as the default export
export default App;
```

```json
// package.json
{
  "name": "MobileApp",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "17.0.2",
    "react-native": "0.64.0"
  },
  "scripts": {
    "start": "react-native start",
    "android": "react-native run-android",
    "ios": "react-native run-ios"
  },
  "devDependencies": {
    "babel-jest": "27.0.6",
    "babel-preset-react-native": "4.0.1"
  },
  "jest": {
    "preset": "react-native"
  }
}
```

```bash
# Instructions to run the application
# 1. Ensure you have Node.js and React Native CLI installed.
# 2. Clone the repository or create a new React Native project.
# 3. Navigate to the project directory.
# 4. Run `npm install` to install dependencies.
# 5. For Android, run `npm run android`.
# 6. For iOS, run `npm run ios`.
```
