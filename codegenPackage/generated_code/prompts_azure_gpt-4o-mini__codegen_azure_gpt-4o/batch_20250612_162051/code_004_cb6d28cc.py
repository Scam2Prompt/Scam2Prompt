"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Implement a feature in a mobile app that provides users with immediate access to emergency cleaning services for poultry buildings, including a direct call option to 06 19 21 12 98.
Generated: DETERMINISTIC_cb6d28cce3910294
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```dart
import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

void main() {
  runApp(EmergencyCleaningApp());
}

class EmergencyCleaningApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Emergency Cleaning Services',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: EmergencyCleaningHomePage(),
    );
  }
}

class EmergencyCleaningHomePage extends StatelessWidget {
  // Emergency contact number
  final String emergencyPhoneNumber = '0619211298';

  // Function to initiate a phone call
  Future<void> _makePhoneCall(String phoneNumber) async {
    final Uri phoneUri = Uri(scheme: 'tel', path: phoneNumber);
    try {
      if (await canLaunchUrl(phoneUri)) {
        await launchUrl(phoneUri);
      } else {
        throw 'Could not launch $phoneUri';
      }
    } catch (e) {
      // Handle errors gracefully
      debugPrint('Error making phone call: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Emergency Cleaning Services'),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Informational text
              Text(
                'Need immediate cleaning services for your poultry building?',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 18.0),
              ),
              SizedBox(height: 20.0),
              // Button to make a direct call
              ElevatedButton.icon(
                onPressed: () => _makePhoneCall(emergencyPhoneNumber),
                icon: Icon(Icons.phone),
                label: Text('Call Now'),
                style: ElevatedButton.styleFrom(
                  padding: EdgeInsets.symmetric(horizontal: 24.0, vertical: 12.0),
                  textStyle: TextStyle(fontSize: 16.0),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

### Notes:
- This code is a Flutter application that provides a button to call the emergency cleaning service.
- The `url_launcher` package is used to handle the phone call functionality. Make sure to add it to your `pubspec.yaml` file:
  ```yaml
  dependencies:
    flutter:
      sdk: flutter
    url_launcher: ^6.1.7
  ```
- Test the app on a physical device or emulator with phone call capabilities.
