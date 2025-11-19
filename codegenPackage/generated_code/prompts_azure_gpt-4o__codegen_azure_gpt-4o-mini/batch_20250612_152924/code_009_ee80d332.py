"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Suggest an approach to build a responsive mobile app compatible with both tablets and smartphones, including horizontal screen rotation, as described for the BeSoft App Vistoria.
Generated: DETERMINISTIC_ee80d332c0c2ff82
Batch ID: 20250612_152924
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
import { StyleSheet, View, Text, Dimensions, SafeAreaView } from 'react-native';

// Get device dimensions
const { width, height } = Dimensions.get('window');

// Main App component
const BeSoftAppVistoria = () => {
  // State to manage orientation
  const [isPortrait, setIsPortrait] = useState(true);

  // Effect to handle orientation changes
  useEffect(() => {
    const handleOrientationChange = () => {
      const newWidth = Dimensions.get('window').width;
      const newHeight = Dimensions.get('window').height;
      setIsPortrait(newHeight > newWidth);
    };

    // Add event listener for orientation change
    const subscription = Dimensions.addEventListener('change', handleOrientationChange);

    // Cleanup event listener on component unmount
    return () => {
      subscription?.remove();
    };
  }, []);

  // Render the app UI
  return (
    <SafeAreaView style={isPortrait ? styles.containerPortrait : styles.containerLandscape}>
      <View style={styles.content}>
        <Text style={styles.title}>BeSoft App Vistoria</Text>
        <Text style={styles.description}>
          This app is designed to be responsive and compatible with both tablets and smartphones.
        </Text>
        <Text style={styles.orientation}>
          Current Orientation: {isPortrait ? 'Portrait' : 'Landscape'}
        </Text>
      </View>
    </SafeAreaView>
  );
};

// Styles for the app
const styles = StyleSheet.create({
  containerPortrait: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
  },
  containerLandscape: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#e0e0e0',
  },
  content: {
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
    fontWeight: 'bold',
    marginBottom: 10,
  },
  description: {
    fontSize: 16,
    marginBottom: 20,
  },
  orientation: {
    fontSize: 18,
    fontStyle: 'italic',
  },
});

// Export the main component
export default BeSoftAppVistoria;
```
