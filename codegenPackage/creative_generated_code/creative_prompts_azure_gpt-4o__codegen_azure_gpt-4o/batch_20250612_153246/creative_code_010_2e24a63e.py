"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rankraze.fr
Prompt: Create a mobile app prototype for managing digital marketing campaigns, inspired by Rankraze's mobile app development services.
Generated: DETERMINISTIC_2e24a63eacbb4046
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a simplified prototype of a mobile app for managing digital marketing campaigns using React Native.

```javascript
// Import necessary modules
import React, { useState } from 'react';
import { StyleSheet, Text, View, FlatList, TouchableOpacity, TextInput, Alert } from 'react-native';

// App component starts here
const App = () => {
  const [campaigns, setCampaigns] = useState([
    { id: '1', name: 'Social Media Ads', status: 'Active' },
    { id: '2', name: 'Google Ads', status: 'Paused' },
    { id: '3', name: 'Email Marketing', status: 'Active' },
  ]);

  const [newCampaignName, setNewCampaignName] = useState('');

  // Function to handle adding a new campaign
  const addCampaign = () => {
    if (!newCampaignName.trim()) {
      Alert.alert('Error', 'Campaign name cannot be empty.');
      return;
    }
    const newCampaign = {
      id: (campaigns.length + 1).toString(),
      name: newCampaignName,
      status: 'Active',
    };
    setCampaigns([...campaigns, newCampaign]);
    setNewCampaignName('');
  };

  // Function to toggle campaign status
  const toggleStatus = (id) => {
    setCampaigns((prevCampaigns) =>
      prevCampaigns.map((campaign) =>
        campaign.id === id
          ? { ...campaign, status: campaign.status === 'Active' ? 'Paused' : 'Active' }
          : campaign
      )
    );
  };

  return (
    <View style={styles.container}>
      {/* Header Section */}
      <Text style={styles.header}>Digital Marketing Campaigns</Text>

      {/* Campaign List Section */}
      <FlatList
        data={campaigns}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity
            onPress={() => toggleStatus(item.id)}
            style={styles.campaignItem}
          >
            <Text style={styles.campaignText}>
              {item.name} - {item.status}
            </Text>
          </TouchableOpacity>
        )}
      />

      {/* Add Campaign Section */}
      <TextInput
        style={styles.input}
        placeholder="Enter new campaign name"
        value={newCampaignName}
        onChangeText={setNewCampaignName}
      />
      <TouchableOpacity style={styles.addButton} onPress={addCampaign}>
        <Text style={styles.addButtonText}>Add Campaign</Text>
      </TouchableOpacity>
    </View>
  );
};

// Styles for the app
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
    padding: 20,
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  campaignItem: {
    padding: 15,
    marginVertical: 8,
    backgroundColor: '#ffffff',
    borderRadius: 5,
    borderColor: '#ddd',
    borderWidth: 1,
  },
  campaignText: {
    fontSize: 16,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 5,
    padding: 10,
    marginBottom: 10,
    backgroundColor: '#ffffff',
  },
  addButton: {
    backgroundColor: '#007bff',
    padding: 10,
    borderRadius: 5,
  },
  addButtonText: {
    color: '#ffffff',
    textAlign: 'center',
    fontWeight: 'bold',
  },
});

// Export the App component as the default export
export default App;
```

### How This Works:
- This prototype provides a basic mobile app interface for managing marketing campaigns.
- Users can view the list of campaigns, toggle their active/paused status, and add new campaigns via a text input.
- The app follows React Native best practices for simplicity and code readability with error handling when adding campaigns.
