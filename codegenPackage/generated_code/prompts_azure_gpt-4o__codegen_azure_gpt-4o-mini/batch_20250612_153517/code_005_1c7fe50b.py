"""
Generated Code Metadata:
========================
Original URL: https://kvtech.ae
Prompt: Write code to develop a mobile application compatible with both Android and iOS platforms, following KEVI Technologies' mobile app development services.
Generated: DETERMINISTIC_1c7fe50b35ea5e7b
Batch ID: 20250612_153517
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
import { StatusBar } from 'expo-status-bar';

// Main App component
export default function App() {
  // Function to handle button press
  const handlePress = () => {
    Alert.alert("Button Pressed", "You have pressed the button!");
  };

  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      <Text style={styles.title}>Welcome to KEVI Technologies Mobile App</Text>
      <Button title="Press Me" onPress={handlePress} />
    </View>
  );
}

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

// Error boundary component for handling errors in the app
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render shows the fallback UI
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // Log the error to an error reporting service
    console.error("Error caught in ErrorBoundary: ", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // Fallback UI
      return <Text style={styles.errorText}>Something went wrong.</Text>;
    }

    return this.props.children; 
  }
}

// Wrap the App component with ErrorBoundary for error handling
export default function Main() {
  return (
    <ErrorBoundary>
      <App />
    </ErrorBoundary>
  );
}
```

### Notes:
- This code is a simple React Native application that is compatible with both Android and iOS.
- It includes an error boundary to catch and handle errors gracefully.
- The code is structured to follow best practices, including separation of concerns and proper error handling.
