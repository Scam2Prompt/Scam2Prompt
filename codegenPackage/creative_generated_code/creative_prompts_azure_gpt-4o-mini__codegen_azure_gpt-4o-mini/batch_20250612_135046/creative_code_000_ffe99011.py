"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://example.walletconnect.org
Prompt: How can I create a React app using WalletConnect v2.8.6 to connect to testnets only?
Generated: DETERMINISTIC_ffe990119895f02a
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { useWalletConnect } from '@walletconnect/react-native-dapp';
import { View, Text, Button, Alert } from 'react-native';
import { ethers } from 'ethers';

// Define the App component
const App = () => {
  // Initialize WalletConnect
  const connector = useWalletConnect();
  
  // State to manage account and chain ID
  const [account, setAccount] = useState(null);
  const [chainId, setChainId] = useState(null);

  // Effect to handle connection
  useEffect(() => {
    if (connector.connected) {
      getAccountDetails();
    }
    // Subscribe to connection events
    connector.on("connect", (error, payload) => {
      if (error) {
        return console.error(error);
      }
      getAccountDetails();
    });

    return () => {
      // Cleanup the event listener
      connector.off("connect");
      connector.off("disconnect");
    };
  }, [connector]);

  // Fetch account details from the connected wallet
  const getAccountDetails = async () => {
    try {
      const accounts = await connector.getAccounts();
      const network = await connector.getChainId();
      setAccount(accounts[0]);
      setChainId(network);
    } catch (error) {
      console.error("Error fetching account details:", error);
      Alert.alert("Error", "Failed to fetch account details. Please try again.");
    }
  };

  // Connect to the wallet
  const connectWallet = async () => {
    try {
      await connector.connect();
    } catch (error) {
      console.error("Connection error:", error);
      Alert.alert("Error", "Failed to connect to wallet. Please try again.");
    }
  };

  // Disconnect from the wallet
  const disconnectWallet = async () => {
    try {
      await connector.killSession();
      setAccount(null);
      setChainId(null);
    } catch (error) {
      console.error("Disconnection error:", error);
      Alert.alert("Error", "Failed to disconnect from wallet. Please try again.");
    }
  };

  // Check if connected to testnets only
  const isTestnet = (chainId) => {
    // Define testnet chain IDs (e.g., Rinkeby, Goerli, etc.)
    const testnets = [4, 5, 42]; // Example: Rinkeby: 4, Goerli: 5, Kovan: 42
    return testnets.includes(chainId);
  };

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 20 }}>WalletConnect Example</Text>
      {account ? (
        <View>
          <Text>Connected Account: {account}</Text>
          <Text>Chain ID: {chainId}</Text>
          {isTestnet(chainId) ? (
            <Text style={{ color: 'green' }}>Connected to a testnet</Text>
          ) : (
            <Text style={{ color: 'red' }}>Not connected to a testnet</Text>
          )}
          <Button title="Disconnect" onPress={disconnectWallet} />
        </View>
      ) : (
        <Button title="Connect Wallet" onPress={connectWallet} />
      )}
    </View>
  );
};

export default App;
```
