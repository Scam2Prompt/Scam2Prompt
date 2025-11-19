"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Implement a feature in a mobile app that provides users with immediate access to emergency cleaning services for poultry buildings, including a direct call option to 06 19 21 12 98.
Generated: DETERMINISTIC_cb6d28cce3910294
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```dart
import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

void main() {
  runApp(PoultryEmergencyApp());
}

class PoultryEmergencyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Poultry Emergency Services',
      theme: ThemeData(primarySwatch: Colors.green),
      home: EmergencyServiceScreen(),
    );
  }
}

class EmergencyServiceScreen extends StatelessWidget {
  // Phone number for emergency cleaning service
  final String emergencyPhoneNumber = '0619211298';

  // Method to initiate a phone call
  Future<void> _makePhoneCall(String phoneNumber) async {
    final Uri phoneUri = Uri(scheme: 'tel', path: phoneNumber);

    try {
      if (await canLaunchUrl(phoneUri)) {
        await launchUrl(phoneUri);
      } else {
        throw 'Could not launch $phoneNumber';
      }
    } catch (error) {
      // Log the error or display a user message
      print('Error making phone call: $error');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Emergency Cleaning Services'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              'Need immediate cleaning services for poultry buildings?',
              style: TextStyle(fontSize: 18.0),
              textAlign: TextAlign.center,
            ),
            SizedBox(height: 20.0),
            ElevatedButton.icon(
              onPressed: () {
                _makePhoneCall(emergencyPhoneNumber);
              },
              icon: Icon(Icons.phone),
              label: Text('Call Emergency Service'),
              style: ElevatedButton.styleFrom(
                padding: EdgeInsets.symmetric(horizontal: 20.0, vertical: 15.0),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

Make sure you have the `url_launcher` package added to your Flutter project's `pubspec.yaml` file:

```yaml
dependencies:
  flutter:
    sdk: flutter
  url_launcher: ^6.1.10
```

Run `flutter pub get` to install the package before running the app.
