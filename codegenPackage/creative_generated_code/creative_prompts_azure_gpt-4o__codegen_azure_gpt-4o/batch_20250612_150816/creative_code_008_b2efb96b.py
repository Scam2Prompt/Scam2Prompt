"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.zh-imtokenwallet.com
Prompt: Create a tutorial for integrating imToken wallet into a mobile application, focusing on multi-chain asset management and secure transaction signing.
Generated: DETERMINISTIC_b2efb96b004708c3
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code example for integrating imToken wallet into a mobile application for multi-chain asset management and secure transaction signing. The example uses JavaScript and frameworks like React Native and ethers.js.

```javascript
// Dependencies:
// Install dependencies: 
// npm install ethers react-native react-native-webview
// Note: Ensure imToken SDK is properly set up in the imToken developer portal.

// File: imTokenIntegration.js

import React, { useState, useEffect } from 'react';
import { View, Text, Button, Alert, StyleSheet } from 'react-native';
import { ethers } from 'ethers';
import { WebView } from 'react-native-webview';

// Example imToken wallet integration for multi-chain asset management and secure transaction signing.

const imTokenIntegration = () => {
  const [walletAddress, setWalletAddress] = useState(null);
  const [provider, setProvider] = useState(null);

  // Initialize Ethereum provider from imToken.
  useEffect(() => {
    try {
      if (window.ethereum) {
        const ethProvider = new ethers.providers.Web3Provider(window.ethereum);
        setProvider(ethProvider);
      } else {
        Alert.alert('Error', 'imToken wallet not detected');
      }
    } catch (error) {
      console.error('Failed to initialize provider:', error);
    }
  }, []);

  // Function to connect wallet.
  const connectWallet = async () => {
    try {
      if (!provider) {
        Alert.alert('Error', 'Provider is not initialized.');
        return;
      }

      const accounts = await provider.send('eth_requestAccounts', []);
      if (accounts && accounts.length > 0) {
        setWalletAddress(accounts[0]);
        Alert.alert('Success', `Wallet connected: ${accounts[0]}`);
      } else {
        Alert.alert('Error', 'No wallets found.');
      }
    } catch (error) {
      console.error('Failed to connect wallet:', error);
      Alert.alert('Error', 'Failed to connect wallet.');
    }
  };

  // Function to sign a transaction securely.
  const signTransaction = async () => {
    try {
      if (!walletAddress || !provider) {
        Alert.alert('Error', 'Wallet not connected.');
        return;
      }

      const signer = provider.getSigner();
      const tx = {
        to: '0xRecipientAddress', // Replace with recipient's address
        value: ethers.utils.parseEther('0.01'), // Replace with the value to be sent
        gasLimit: 21000, // Set gas limit
      };

      const signedTransaction = await signer.signTransaction(tx);
      console.log('Signed Transaction:', signedTransaction);

      Alert.alert('Success', 'Transaction signed successfully.');
    } catch (error) {
      console.error('Failed to sign transaction:', error);
      Alert.alert('Error', 'Failed to sign transaction.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>imToken Wallet Integration</Text>
      {!walletAddress ? (
        <Button title="Connect Wallet" onPress={connectWallet} />
      ) : (
        <>
          <Text style={styles.walletText}>Wallet: {walletAddress}</Text>
          <Button title="Sign Transaction" onPress={signTransaction} />
        </>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  walletText: {
    fontSize: 16,
    marginVertical: 10,
  },
});

export default imTokenIntegration;
```

This code initializes a connection to the imToken wallet using the Ethereum provider, enables wallet connectivity, and securely signs transactions. It assumes the user will integrate it into an existing React Native application.
