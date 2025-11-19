"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canatechinstitute.ca
Prompt: Write a code snippet for a mobile app that tracks user preferences and integrates with a backend service, inspired by the app development services of the Canadian Tech-Institute.
Generated: DETERMINISTIC_4bbcd8d544dd1bd2
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/user/preferences": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

// Entry point for the application
void main() {
  runApp(UserPreferencesApp());
}

// Main Widget for the app
class UserPreferencesApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'User Preferences Tracker',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: PreferencesScreen(),
    );
  }
}

// Screen to display and manage user preferences
class PreferencesScreen extends StatefulWidget {
  @override
  _PreferencesScreenState createState() => _PreferencesScreenState();
}

class _PreferencesScreenState extends State<PreferencesScreen> {
  final Map<String, bool> _preferences = {
    'Receive Notifications': true,
    'Dark Mode': false,
    'Enable Location Tracking': true,
  };

  // Backend API URL
  final String _apiUrl = 'https://api.example.com/user/preferences';

  bool _isLoading = false;

  // Function to send preferences to the backend
  Future<void> _savePreferences() async {
    setState(() {
      _isLoading = true;
    });

    try {
      final response = await http.post(
        Uri.parse(_apiUrl),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({'preferences': _preferences}),
      );

      // Handle the response
      if (response.statusCode == 200) {
        final responseData = json.decode(response.body);
        // Success response handling
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(
          content: Text('Preferences saved successfully!'),
        ));
      } else {
        // Error handling for non-200 response
        throw Exception('Failed to save preferences. Status code: ${response.statusCode}');
      }
    } catch (error) {
      // Handle errors (e.g., network issues, parsing errors)
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
        content: Text('Error saving preferences: ${error.toString()}'),
      ));
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('User Preferences'),
      ),
      body: _isLoading
          ? Center(child: CircularProgressIndicator())
          : ListView(
              children: _preferences.keys.map((key) {
                return SwitchListTile(
                  title: Text(key),
                  value: _preferences[key]!,
                  onChanged: (value) {
                    setState(() {
                      _preferences[key] = value;
                    });
                  },
                );
              }).toList(),
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: _savePreferences,
        child: Icon(Icons.save),
        tooltip: 'Save Preferences',
      ),
    );
  }
}
```
