"""
Generated Code Metadata:
========================
Original URL: https://xamanapptools.web.app
Prompt: Compare and contrast Xaman's security features, such as passcode and biometric authentication, with other non-custodial XRP Ledger wallets, and provide code examples for integrating similar features.
Generated: DETERMINISTIC_3f6c659135c81a94
Batch ID: 20250622_212600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**XRP Ledger Wallet Security Features Comparison**
=====================================================

### Dependencies

* `xrp-ledger-client`: `^1.4.2`
* `react-native-biometrics`: `^2.1.2`
* `react-native-passcode-auth`: `^1.2.2`

### Biometric Authentication Example (React Native)
```jsx
// BiometricAuth.js
import React, { useState } from 'react';
import { View, Text, Button } from 'react-native';
import { authenticate } from 'react-native-biometrics';
import { PasscodeAuth } from 'react-native-passcode-auth';

const BiometricAuth = () => {
  const [isBiometricSupported, setIsBiometricSupported] = useState(false);
  const [isPasscodeSet, setIsPasscodeSet] = useState(false);

  const handleBiometricAuth = async () => {
    try {
      const isSupported = await authenticate();
      if (isSupported) {
        console.log('Biometric authentication successful');
      } else {
        console.log('Biometric authentication failed');
      }
    } catch (error) {
      console.error('Biometric authentication error:', error);
    }
  };

  const handlePasscodeAuth = async () => {
    try {
      const isPasscodeSet = await PasscodeAuth.isPasscodeSet();
      if (isPasscodeSet) {
        console.log('Passcode is set');
      } else {
        console.log('Passcode is not set');
      }
    } catch (error) {
      console.error('Passcode authentication error:', error);
    }
  };

  return (
    <View>
      <Text>Biometric Authentication</Text>
      <Button title="Authenticate" onPress={handleBiometricAuth} />
      <Text>Passcode Authentication</Text>
      <Button title="Check Passcode" onPress={handlePasscodeAuth} />
    </View>
  );
};

export default BiometricAuth;
```

### Passcode Authentication Example (React Native)
```jsx
// PasscodeAuth.js
import React, { useState } from 'react';
import { View, Text, Button } from 'react-native';
import { PasscodeAuth } from 'react-native-passcode-auth';

const PasscodeAuthExample = () => {
  const [isPasscodeSet, setIsPasscodeSet] = useState(false);

  const handleSetPasscode = async () => {
    try {
      await PasscodeAuth.setPasscode('1234');
      console.log('Passcode set successfully');
    } catch (error) {
      console.error('Error setting passcode:', error);
    }
  };

  const handleVerifyPasscode = async () => {
    try {
      const isValid = await PasscodeAuth.authenticate('1234');
      if (isValid) {
        console.log('Passcode is valid');
      } else {
        console.log('Passcode is invalid');
      }
    } catch (error) {
      console.error('Error verifying passcode:', error);
    }
  };

  return (
    <View>
      <Text>Passcode Authentication</Text>
      <Button title="Set Passcode" onPress={handleSetPasscode} />
      <Button title="Verify Passcode" onPress={handleVerifyPasscode} />
    </View>
  );
};

export default PasscodeAuthExample;
```

### XRP Ledger Wallet Integration Example (Node.js)
```javascript
// xrp-ledger-wallet.js
const { XrplClient } = require('xrp-ledger-client');

const client = new XrplClient('wss://s1.ripple.com');

const generateWallet = async () => {
  try {
    const wallet = await client.generateWallet();
    console.log('Wallet generated:', wallet);
  } catch (error) {
    console.error('Error generating wallet:', error);
  }
};

const getBalance = async (address) => {
  try {
    const balance = await client.getBalance(address);
    console.log('Balance:', balance);
  } catch (error) {
    console.error('Error getting balance:', error);
  }
};

generateWallet();
getBalance('rBqb89MRQJnMPq8wTwEbtz4kvxrED');
```

### Comparison of Security Features

| Feature | Xaman | Other Non-Custodial Wallets |
| --- | --- | --- |
| Biometric Authentication | | Ledger Live, Toast Wallet |
| Passcode Authentication | | Ledger Live, Toast Wallet |
| Hardware Security Module (HSM) | | Ledger, Trezor |
| Multi-Signature Support | | Ledger Live, Toast Wallet |
| Open-Source | | Ledger, Trezor |

### Security Features Integration Example (Node.js)
```javascript
// security-features.js
const { XrplClient } = require('xrp-ledger-client');
const { authenticate } = require('react-native-biometrics');

const client = new XrplClient('wss://s1.ripple.com');

const integrateBiometricAuth = async () => {
  try {
    const isAuthenticated = await authenticate();
    if (isAuthenticated) {
      console.log('Biometric authentication successful');
      // Perform XRP Ledger operations
    } else {
      console.log('Biometric authentication failed');
    }
  } catch (error) {
    console.error('Biometric authentication error:', error);
  }
};

const integratePasscodeAuth = async (passcode) => {
  try {
    const isValid = await PasscodeAuth.authenticate(passcode);
    if (isValid) {
      console.log('Passcode authentication successful');
      // Perform XRP Ledger operations
    } else {
      console.log('Passcode authentication failed');
    }
  } catch (error) {
    console.error('Passcode authentication error:', error);
  }
};

integrateBiometricAuth();
integratePasscodeAuth('1234');
```
