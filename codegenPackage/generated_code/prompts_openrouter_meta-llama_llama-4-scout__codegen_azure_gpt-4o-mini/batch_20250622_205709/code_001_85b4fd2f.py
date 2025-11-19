"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: "Recommend a suitable JavaScript library for building a responsive and interactive mobile application, and provide an example code for a basic mobile app using React Native."
Generated: DETERMINISTIC_85b4fd2f352b29ce
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from React and React Native
import React from 'react';
import { StyleSheet, Text, View, Button, Alert } from 'react-native';

// Define the main App component
const App = () => {
  // Function to handle button press
  const handlePress = () => {
    Alert.alert('Button Pressed!', 'You have pressed the button.');
  };

  // Render the UI
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to My Mobile App</Text>
      <Button title="Press Me" onPress={handlePress} />
    </View>
  );
};

// Define styles for the components
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5fcff',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
});

// Export the App component as the default export
export default App;
```

### Instructions to Run the Code:
1. Ensure you have Node.js installed on your machine.
2. Install React Native CLI by running `npm install -g react-native-cli`.
3. Create a new React Native project using `npx react-native init MyApp`.
4. Replace the contents of `App.js` in the newly created project with the code above.
5. Run the application using `npx react-native run-android` or `npx react-native run-ios` depending on your target platform.
