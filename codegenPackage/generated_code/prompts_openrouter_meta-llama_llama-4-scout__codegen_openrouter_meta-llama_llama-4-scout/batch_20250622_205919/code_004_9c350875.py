"""
Generated Code Metadata:
========================
Original URL: https://www.solcialapp.com
Prompt: Implement a password verification system in React Native for a mobile app, inspired by the access control of Solcial.
Generated: DETERMINISTIC_9c3508755e6d001b
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// PasswordVerificationScreen.js
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';
import { validatePassword } from '../utils/validation';

/**
 * Password Verification Screen
 * 
 * This screen handles password verification for the mobile app.
 * 
 * @returns {JSX.Element}
 */
const PasswordVerificationScreen = () => {
  const [password, setPassword] = useState('');
  const [isValid, setIsValid] = useState(false);
  const [errorMessage, setErrorMessage] = useState(null);

  /**
   * Handle password input change
   * 
   * @param {string} text
   */
  const handlePasswordChange = (text) => {
    setPassword(text);
    const validation = validatePassword(text);
    setIsValid(validation.isValid);
    setErrorMessage(validation.errorMessage);
  };

  /**
   * Handle password verification
   */
  const handleVerifyPassword = () => {
    if (isValid) {
      // Call API or perform verification logic here
      Alert.alert('Password Verified', 'Password is valid');
    } else {
      Alert.alert('Invalid Password', errorMessage);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Verify Password</Text>
      <TextInput
        style={styles.input}
        secureTextEntry
        value={password}
        onChangeText={handlePasswordChange}
        placeholder="Enter password"
      />
      {errorMessage && (
        <Text style={styles.error}>{errorMessage}</Text>
      )}
      <Button
        title="Verify Password"
        onPress={handleVerifyPassword}
        disabled={!isValid}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    padding: 10,
    marginBottom: 20,
  },
  error: {
    color: 'red',
    marginBottom: 20,
  },
});

export default PasswordVerificationScreen;
```

```javascript
// utils/validation.js
/**
 * Validate password
 * 
 * @param {string} password
 * @returns {{isValid: boolean, errorMessage: string}}
 */
export const validatePassword = (password) => {
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  if (!passwordRegex.test(password)) {
    return {
      isValid: false,
      errorMessage: 'Password must be at least 8 characters, contain uppercase and lowercase letters, numbers, and special characters',
    };
  }
  return { isValid: true, errorMessage: null };
};
```

```javascript
// App.js
import React from 'react';
import PasswordVerificationScreen from './PasswordVerificationScreen';

const App = () => {
  return (
    <PasswordVerificationScreen />
  );
};

export default App;
```
