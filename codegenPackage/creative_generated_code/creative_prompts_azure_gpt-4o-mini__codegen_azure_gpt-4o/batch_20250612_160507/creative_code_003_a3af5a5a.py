"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Develop a mobile app feature that allows users to track their volunteer hours, reflecting the NICER Foundation's mission of community involvement and support.
Generated: DETERMINISTIC_a3af5a5a6bdf88c0
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for the mobile app feature to track volunteer hours. This example is written in Flutter (Dart) since it's a popular framework for mobile app development and supports both Android and iOS.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(VolunteerHoursTrackerApp());
}

// Main Application Widget
class VolunteerHoursTrackerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Volunteer Hours Tracker',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: VolunteerHoursTracker(),
    );
  }
}

// Volunteer Hours Tracker Screen
class VolunteerHoursTracker extends StatefulWidget {
  @override
  _VolunteerHoursTrackerState createState() => _VolunteerHoursTrackerState();
}

class _VolunteerHoursTrackerState extends State<VolunteerHoursTracker> {
  final List<Map<String, dynamic>> _entries = []; // List to store volunteer hours data
  final _formKey = GlobalKey<FormState>(); // Key for the form
  String _activityName = ''; // Activity name input
  double _hours = 0; // Hours input

  // Function to add an entry
  void _addEntry() {
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save(); // Save form inputs
      setState(() {
        _entries.add({'activity': _activityName, 'hours': _hours});
      });
    }
  }

  // Function to calculate total hours
  double _calculateTotalHours() {
    return _entries.fold(0, (sum, entry) => sum + entry['hours']);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Volunteer Hours Tracker'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            // Form to input activity and hours
            Form(
              key: _formKey,
              child: Column(
                children: [
                  TextFormField(
                    decoration: const InputDecoration(
                      labelText: 'Activity Name',
                      border: OutlineInputBorder(),
                    ),
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter an activity name';
                      }
                      return null;
                    },
                    onSaved: (value) {
                      _activityName = value!;
                    },
                  ),
                  const SizedBox(height: 16),
                  TextFormField(
                    decoration: const InputDecoration(
                      labelText: 'Hours',
                      border: OutlineInputBorder(),
                    ),
                    keyboardType: TextInputType.number,
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter the number of hours';
                      }
                      final hours = double.tryParse(value);
                      if (hours == null || hours <= 0) {
                        return 'Please enter a valid number of hours';
                      }
                      return null;
                    },
                    onSaved: (value) {
                      _hours = double.parse(value!);
                    },
                  ),
                  const SizedBox(height: 16),
                  ElevatedButton(
                    onPressed: _addEntry,
                    child: const Text('Add Entry'),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),
            // Display total hours
            Text(
              'Total Volunteer Hours: ${_calculateTotalHours()}',
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 16),
            // List of entries
            Expanded(
              child: ListView.builder(
                itemCount: _entries.length,
                itemBuilder: (context, index) {
                  final entry = _entries[index];
                  return ListTile(
                    title: Text(entry['activity']),
                    subtitle: Text('${entry['hours']} hours'),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```
