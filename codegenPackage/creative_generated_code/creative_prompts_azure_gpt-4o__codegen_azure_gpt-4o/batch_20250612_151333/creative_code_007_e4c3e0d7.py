"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otherside-lb1.pages.dev
Prompt: Write code to implement mobile app functionality for scanning QR codes to connect with dapps, ensuring compatibility with Coinbase Wallet, as described on the Otherside event registration page.
Generated: DETERMINISTIC_e4c3e0d7e8092b2e
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation in **JavaScript** using the **React Native** framework with the **Expo** SDK (which simplifies access to the device's camera for QR code scanning). The code integrates with dApp connections, ensuring compatibility with Coinbase Wallet.

```javascript
import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Alert } from 'react-native';
import { BarCodeScanner } from 'expo-barcode-scanner';
import Linking from 'expo-linking';

const QRScanner = () => {
  const [hasPermission, setHasPermission] = useState(null);
  const [scanned, setScanned] = useState(false);

  // Request camera permission when component mounts
  useEffect(() => {
    const requestPermission = async () => {
      const { status } = await BarCodeScanner.requestPermissionsAsync();
      setHasPermission(status === 'granted');
    };

    requestPermission();
  }, []);

  // Function to handle scanned QR code
  const handleBarCodeScanned = ({ data }) => {
    setScanned(true);

    try {
      // Assuming the scanned QR code contains a URL for the dApp connection
      if (Linking.canOpenURL(data)) {
        // Open URL using deep linking (Coinbase Wallet compatibility)
        Linking.openURL(data);
      } else {
        throw new Error('Invalid QR code format');
      }
    } catch (error) {
      Alert.alert('Error', error.message);
    }
  };

  // Handle missing camera permissions
  if (hasPermission === null) {
    return <Text>Requesting for camera permission...</Text>;
  }
  if (hasPermission === false) {
    return <Text>No access to camera. Please enable camera permissions in settings.</Text>;
  }

  return (
    <View style={styles.container}>
      <BarCodeScanner
        onBarCodeScanned={scanned ? undefined : handleBarCodeScanned}
        style={StyleSheet.absoluteFillObject}
      />
      {scanned && (
        <Text style={styles.rescanText} onPress={() => setScanned(false)}>
          Tap to scan again
        </Text>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  rescanText: {
    position: 'absolute',
    bottom: 50,
    fontSize: 18,
    color: 'blue',
    textDecorationLine: 'underline',
  },
});

export default QRScanner;
```

### Key Features:
1. **QR Code Scanning**: Uses `expo-barcode-scanner` for scanning QR codes.
2. **Coinbase Wallet Compatibility**: Opens URLs with `expo-linking`, supporting dApp connection via deep links.
3. **Error Handling**: Alerts users when the QR code format is invalid.
4. **Camera Permission Handling**: Handles permission requests gracefully.
5. **Production-Ready Design**: Clean and modular, ensuring ease of maintenance.

To run this code, ensure you're using an Expo-based React Native setup. Install the required dependencies with the following:

```bash
npm install expo-barcode-scanner expo-linking
```

This code assumes the QR code contains a URL compatible with Coinbase Wallet's deep linking protocols.
