"""
Generated Code Metadata:
========================
Original URL: https://turpymobileapps.com
Prompt: Generate a custom mobile app solution for a startup using the latest technologies discussed on Turpy Mobile Apps.
Generated: DETERMINISTIC_ba1d5e39b93cfaaa
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, Button, Alert } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Create a Stack Navigator
const Stack = createStackNavigator();

// Home Screen Component
const HomeScreen = ({ navigation }) => {
  const [data, setData] = useState(null);

  // Fetch data from AsyncStorage on component mount
  useEffect(() => {
    const fetchData = async () => {
      try {
        const storedData = await AsyncStorage.getItem('userData');
        if (storedData) {
          setData(JSON.parse(storedData));
        }
      } catch (error) {
        console.error('Error fetching data from AsyncStorage:', error);
      }
    };
    fetchData();
  }, []);

  // Function to handle data submission
  const handleSubmit = async () => {
    const userData = { name: 'John Doe', age: 30 }; // Example data
    try {
      await AsyncStorage.setItem('userData', JSON.stringify(userData));
      Alert.alert('Success', 'Data saved successfully!');
    } catch (error) {
      console.error('Error saving data to AsyncStorage:', error);
      Alert.alert('Error', 'Failed to save data.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to Turpy Mobile App!</Text>
      {data && (
        <Text style={styles.dataText}>
          Stored Data: {JSON.stringify(data)}
        </Text>
      )}
      <Button title="Save Data" onPress={handleSubmit} />
      <Button title="Go to Details" onPress={() => navigation.navigate('Details')} />
    </View>
  );
};

// Details Screen Component
const DetailsScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Details Screen</Text>
      <Text style={styles.dataText}>Here you can add more details about your app.</Text>
    </View>
  );
};

// Main App Component
const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
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
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  dataText: {
    fontSize: 16,
    marginBottom: 20,
  },
});

// Export the App component as the default export
export default App;
```
