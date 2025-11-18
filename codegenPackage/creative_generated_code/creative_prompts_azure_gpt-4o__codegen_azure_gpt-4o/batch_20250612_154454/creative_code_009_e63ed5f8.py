"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Develop a mobile app using React Native to allow students of SMKN 1 Kadipaten to view their exam schedules, academic programs, and school announcements.
Generated: DETERMINISTIC_e63ed5f87daa32f5
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
import React from 'react';
import { View, Text, FlatList, TouchableOpacity, StyleSheet, Alert } from 'react-native';

// Mock data for demonstration purposes
const examSchedules = [
  { id: '1', subject: 'Math', date: '2023-11-01', time: '10:00 AM' },
  { id: '2', subject: 'Science', date: '2023-11-02', time: '01:00 PM' },
];

const academicPrograms = [
  { id: '1', name: 'Program A', description: 'Description for Program A' },
  { id: '2', name: 'Program B', description: 'Description for Program B' },
];

const schoolAnnouncements = [
  { id: '1', title: 'Holiday Notice', content: 'School will be closed on 2023-12-25.' },
  { id: '2', title: 'Sports Week', content: 'Sports Week will commence on 2023-11-10.' },
];

// Main App Component
export default function App() {
  return (
    <View style={styles.container}>
      {/* App Title */}
      <Text style={styles.title}>SMKN 1 Kadipaten App</Text>

      {/* Section: Exam Schedules */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Exam Schedules</Text>
        <FlatList
          data={examSchedules}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <View style={styles.card}>
              <Text style={styles.cardTitle}>{item.subject}</Text>
              <Text>Date: {item.date}</Text>
              <Text>Time: {item.time}</Text>
            </View>
          )}
        />
      </View>

      {/* Section: Academic Programs */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Academic Programs</Text>
        <FlatList
          data={academicPrograms}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <TouchableOpacity
              style={styles.card}
              onPress={() => Alert.alert(item.name, item.description)}
            >
              <Text style={styles.cardTitle}>{item.name}</Text>
              <Text>{item.description}</Text>
            </TouchableOpacity>
          )}
        />
      </View>

      {/* Section: School Announcements */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>School Announcements</Text>
        <FlatList
          data={schoolAnnouncements}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <TouchableOpacity
              style={styles.card}
              onPress={() => Alert.alert(item.title, item.content)}
            >
              <Text style={styles.cardTitle}>{item.title}</Text>
              <Text>{item.content}</Text>
            </TouchableOpacity>
          )}
        />
      </View>
    </View>
  );
}

// Styles for the app
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 16,
    color: '#333',
  },
  section: {
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
    color: '#555',
  },
  card: {
    backgroundColor: '#ffffff',
    padding: 16,
    borderRadius: 8,
    marginVertical: 8,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  cardTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 4,
    color: '#333',
  },
});
```
