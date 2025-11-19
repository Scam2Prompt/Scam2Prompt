"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Illustrate how to integrate Ambro Contables' loan application process into a mobile app using React Native.
Generated: DETERMINISTIC_e874177fd63178e3
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import { View, Text, TextInput, Button, Alert, StyleSheet, ScrollView } from 'react-native';

// Loan Application Component
const LoanApplication = () => {
  // State variables to hold form data
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [loanAmount, setLoanAmount] = useState('');
  const [income, setIncome] = useState('');

  // Function to validate form input
  const validateInputs = () => {
    if (!fullName || !email || !phone || !loanAmount || !income) {
      Alert.alert('Error', 'All fields are required.');
      return false;
    }
    if (!/^\d+$/.test(phone)) {
      Alert.alert('Error', 'Phone number must be numeric.');
      return false;
    }
    if (!/^\d+$/.test(loanAmount) || parseFloat(loanAmount) <= 0) {
      Alert.alert('Error', 'Loan amount must be a positive number.');
      return false;
    }
    if (!/^\d+$/.test(income) || parseFloat(income) <= 0) {
      Alert.alert('Error', 'Income must be a positive number.');
      return false;
    }
    return true;
  };

  // Function to handle form submission
  const handleSubmit = () => {
    if (validateInputs()) {
      const applicationData = {
        fullName,
        email,
        phone,
        loanAmount,
        income,
      };

      // Mock submission process
      Alert.alert(
        'Success',
        'Your application has been successfully submitted.',
        [{ text: 'OK' }]
      );

      console.log('Loan Application Submitted:', applicationData);

      // Reset form fields
      setFullName('');
      setEmail('');
      setPhone('');
      setLoanAmount('');
      setIncome('');
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Ambro Contables Loan Application</Text>
      
      {/* Form Fields */}
      <Text style={styles.label}>Full Name:</Text>
      <TextInput
        style={styles.input}
        value={fullName}
        onChangeText={setFullName}
        placeholder="Enter your full name"
      />

      <Text style={styles.label}>Email:</Text>
      <TextInput
        style={styles.input}
        value={email}
        onChangeText={setEmail}
        placeholder="Enter your email"
        keyboardType="email-address"
      />

      <Text style={styles.label}>Phone Number:</Text>
      <TextInput
        style={styles.input}
        value={phone}
        onChangeText={setPhone}
        placeholder="Enter your phone number"
        keyboardType="numeric"
      />

      <Text style={styles.label}>Loan Amount:</Text>
      <TextInput
        style={styles.input}
        value={loanAmount}
        onChangeText={setLoanAmount}
        placeholder="Enter the loan amount"
        keyboardType="numeric"
      />

      <Text style={styles.label}>Monthly Income:</Text>
      <TextInput
        style={styles.input}
        value={income}
        onChangeText={setIncome}
        placeholder="Enter your monthly income"
        keyboardType="numeric"
      />

      {/* Submit Button */}
      <Button title="Submit Application" onPress={handleSubmit} />
    </ScrollView>
  );
};

// Styles for the component
const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    padding: 20,
    backgroundColor: '#f9f9f9',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  label: {
    fontSize: 16,
    marginBottom: 5,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    padding: 10,
    marginBottom: 15,
    backgroundColor: '#fff',
  },
});

export default LoanApplication;
```
