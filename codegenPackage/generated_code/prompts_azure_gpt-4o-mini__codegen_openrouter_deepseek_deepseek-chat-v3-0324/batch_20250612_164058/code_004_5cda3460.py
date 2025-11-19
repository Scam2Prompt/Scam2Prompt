"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: How can I develop a user interface for a mobile app that provides on-demand windscreen replacement services like those offered by Cheap Windscreens Melbourne?
Generated: DETERMINISTIC_5cda346060cd7f3d
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Mobile App UI for On-Demand Windscreen Replacement Service

## React Native Implementation

```javascript
// App.js - Main Application Entry Point
import React from 'react';
import { SafeAreaView, StatusBar } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { ThemeProvider } from 'styled-components';
import { theme } from './src/styles/theme';
import { AuthProvider } from './src/context/AuthContext';
import MainStack from './src/navigation/MainStack';

const Stack = createStackNavigator();

const App = () => {
  return (
    <AuthProvider>
      <ThemeProvider theme={theme}>
        <SafeAreaView style={{ flex: 1 }}>
          <StatusBar barStyle="dark-content" />
          <NavigationContainer>
            <MainStack />
          </NavigationContainer>
        </SafeAreaView>
      </ThemeProvider>
    </AuthProvider>
  );
};

export default App;
```

```javascript
// src/navigation/MainStack.js
import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../screens/HomeScreen';
import ServiceSelectionScreen from '../screens/ServiceSelectionScreen';
import VehicleDetailsScreen from '../screens/VehicleDetailsScreen';
import LocationSelectionScreen from '../screens/LocationSelectionScreen';
import BookingConfirmationScreen from '../screens/BookingConfirmationScreen';
import BookingStatusScreen from '../screens/BookingStatusScreen';
import LoginScreen from '../screens/LoginScreen';
import ProfileScreen from '../screens/ProfileScreen';
import { useSelector } from 'react-redux';

const Stack = createStackNavigator();

const MainStack = () => {
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated);

  return (
    <Stack.Navigator
      screenOptions={{
        headerShown: false,
        cardStyle: { backgroundColor: '#FFFFFF' },
      }}
    >
      {!isAuthenticated ? (
        <Stack.Screen name="Login" component={LoginScreen} />
      ) : (
        <>
          <Stack.Screen name="Home" component={HomeScreen} />
          <Stack.Screen name="ServiceSelection" component={ServiceSelectionScreen} />
          <Stack.Screen name="VehicleDetails" component={VehicleDetailsScreen} />
          <Stack.Screen name="LocationSelection" component={LocationSelectionScreen} />
          <Stack.Screen name="BookingConfirmation" component={BookingConfirmationScreen} />
          <Stack.Screen name="BookingStatus" component={BookingStatusScreen} />
          <Stack.Screen name="Profile" component={ProfileScreen} />
        </>
      )}
    </Stack.Navigator>
  );
};

export default MainStack;
```

```javascript
// src/screens/HomeScreen.js
import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Image } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import Header from '../components/Header';
import ServiceCard from '../components/ServiceCard';
import { services } from '../data/services';

const HomeScreen = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.container}>
      <Header title="Windscreen Replacement" showBackButton={false} />
      
      <View style={styles.content}>
        <Text style={styles.welcomeText}>Get your windscreen replaced quickly and affordably</Text>
        
        <View style={styles.serviceGrid}>
          {services.map((service) => (
            <ServiceCard
              key={service.id}
              title={service.title}
              icon={service.icon}
              onPress={() => navigation.navigate('ServiceSelection', { serviceType: service.type })}
            />
          ))}
        </View>
        
        <TouchableOpacity 
          style={styles.emergencyButton}
          onPress={() => navigation.navigate('ServiceSelection', { serviceType: 'emergency' })}
        >
          <Text style={styles.emergencyButtonText}>EMERGENCY SERVICE</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  content: {
    flex: 1,
    padding: 20,
  },
  welcomeText: {
    fontSize: 18,
    marginBottom: 20,
    textAlign: 'center',
    color: '#333',
  },
  serviceGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  emergencyButton: {
    marginTop: 30,
    backgroundColor: '#E74C3C',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
  },
  emergencyButtonText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 16,
  },
});

export default HomeScreen;
```

```javascript
// src/screens/ServiceSelectionScreen.js
import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { useNavigation, useRoute } from '@react-navigation/native';
import Header from '../components/Header';
import ServiceOptionCard from '../components/ServiceOptionCard';
import { serviceOptions } from '../data/serviceOptions';

const ServiceSelectionScreen = () => {
  const navigation = useNavigation();
  const route = useRoute();
  const [selectedOption, setSelectedOption] = useState(null);
  
  const serviceType = route.params?.serviceType || 'standard';

  const handleContinue = () => {
    if (!selectedOption) return;
    navigation.navigate('VehicleDetails', { serviceOption: selectedOption });
  };

  return (
    <View style={styles.container}>
      <Header title="Select Service" showBackButton={true} />
      
      <ScrollView contentContainerStyle={styles.content}>
        <Text style={styles.sectionTitle}>Available Services</Text>
        
        {serviceOptions
          .filter(option => option.type === serviceType)
          .map(option => (
            <ServiceOptionCard
              key={option.id}
              title={option.title}
              description={option.description}
              price={option.price}
              time={option.time}
              isSelected={selectedOption?.id === option.id}
              onPress={() => setSelectedOption(option)}
            />
          ))}
      </ScrollView>
      
      <View style={styles.footer}>
        <TouchableOpacity 
          style={[styles.continueButton, !selectedOption && styles.disabledButton]}
          onPress={handleContinue}
          disabled={!selectedOption}
        >
          <Text style={styles.continueButtonText}>Continue</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  content: {
    padding: 20,
    paddingBottom: 80,
  },
  sectionTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 15,
    color: '#333',
  },
  footer: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    padding: 20,
    backgroundColor: 'white',
    borderTopWidth: 1,
    borderTopColor: '#EEE',
  },
  continueButton: {
    backgroundColor: '#3498DB',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
  },
  disabledButton: {
    backgroundColor: '#95A5A6',
  },
  continueButtonText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 16,
  },
});

export default ServiceSelectionScreen;
```

```javascript
// src/screens/VehicleDetailsScreen.js
import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TextInput, TouchableOpacity } from 'react-native';
import { useNavigation, useRoute } from '@react-navigation/native';
import Header from '../components/Header';
import Picker from '../components/Picker';
import { vehicleMakes, vehicleModels, vehicleYears } from '../data/vehicles';

const VehicleDetailsScreen = () => {
  const navigation = useNavigation();
  const route = useRoute();
  const [make, setMake] = useState('');
  const [model, setModel] = useState('');
  const [year, setYear] = useState('');
  const [registration, setRegistration] = useState('');
  
  const serviceOption = route.params?.serviceOption;

  const handleContinue = () => {
    if (!make || !model || !year || !registration) return;
    
    navigation.navigate('LocationSelection', { 
      serviceOption,
      vehicleDetails: { make, model, year, registration }
    });
  };

  return (
    <View style={styles.container}>
      <Header title="Vehicle Details" showBackButton={true} />
      
      <ScrollView contentContainerStyle={styles.content}>
        <Text style={styles.sectionTitle}>Enter your vehicle information</Text>
        
        <Picker
          label="Make"
          items={vehicle
