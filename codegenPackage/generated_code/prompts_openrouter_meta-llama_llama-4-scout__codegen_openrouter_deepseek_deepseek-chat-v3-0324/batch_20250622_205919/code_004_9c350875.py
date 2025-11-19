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

```javascript
import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  Alert,
} from 'react-native';

const PasswordVerification = () => {
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isValid, setIsValid] = useState(false);
  const [error, setError] = useState('');

  // Password requirements
  const MIN_LENGTH = 8;
  const REQUIRE_UPPERCASE = true;
  const REQUIRE_LOWERCASE = true;
  const REQUIRE_NUMBER = true;
  const REQUIRE_SPECIAL_CHAR = true;

  // Validate password against requirements
  const validatePassword = (pwd) => {
    const errors = [];

    if (pwd.length < MIN_LENGTH) {
      errors.push(`Password must be at least ${MIN_LENGTH} characters long.`);
    }

    if (REQUIRE_UPPERCASE && !/[A-Z]/.test(pwd)) {
      errors.push('Password must contain at least one uppercase letter.');
    }

    if (REQUIRE_LOWERCASE && !/[a-z]/.test(pwd)) {
      errors.push('Password must contain at least one lowercase letter.');
    }

    if (REQUIRE_NUMBER && !/[0-9]/.test(pwd)) {
      errors.push('Password must contain at least one number.');
    }

    if (REQUIRE_SPECIAL_CHAR && !/[^A-Za-z0-9]/.test(pwd)) {
      errors.push('Password must contain at least one special character.');
    }

    return errors;
  };

  // Handle password change
  const handlePasswordChange = (text) => {
    setPassword(text);
    setError('');
  };

  // Handle confirm password change
  const handleConfirmPasswordChange = (text) => {
    setConfirmPassword(text);
    setError('');
  };

  // Check if passwords match and meet requirements
  useEffect(() => {
    if (password && confirmPassword) {
      const errors = validatePassword(password);
      
      if (errors.length > 0) {
        setError(errors.join('\n'));
        setIsValid(false);
      } else if (password !== confirmPassword) {
        setError('Passwords do not match.');
        setIsValid(false);
      } else {
        setError('');
        setIsValid(true);
      }
    } else {
      setIsValid(false);
    }
  }, [password, confirmPassword]);

  // Handle form submission
  const handleSubmit = () => {
    if (isValid) {
      Alert.alert('Success', 'Password is valid and matches!');
      // Here you would typically call an API to update the password
    } else {
      Alert.alert('Error', 'Please fix the errors before submitting.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Set Your Password</Text>
      
      <TextInput
        style={styles.input}
        placeholder="Enter password"
        secureTextEntry
        value={password}
        onChangeText={handlePasswordChange}
      />
      
      <TextInput
        style={styles.input}
        placeholder="Confirm password"
        secureTextEntry
        value={confirmPassword}
        onChangeText={handleConfirmPasswordChange}
      />
      
      {error ? <Text style={styles.errorText}>{error}</Text> : null}
      
      <TouchableOpacity
        style={[styles.button, !isValid && styles.disabledButton]}
        onPress={handleSubmit}
        disabled={!isValid}
      >
        <Text style={styles.buttonText}>Submit</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  input: {
    height: 50,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    paddingHorizontal: 10,
    marginBottom: 15,
    backgroundColor: '#fff',
  },
  button: {
    height: 50,
    backgroundColor: '#007bff',
    borderRadius: 5,
    justifyContent: 'center',
    alignItems: 'center',
  },
  disabledButton: {
    backgroundColor: '#cccccc',
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  errorText: {
    color: 'red',
    marginBottom: 15,
  },
});

export default PasswordVerification;
```
