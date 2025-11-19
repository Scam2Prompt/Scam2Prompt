"""
Generated Code Metadata:
========================
Original URL: https://mayayogaofficial.com
Prompt: Develop a mobile app feature that allows users to track their yoga practice, inspired by the training programs offered at Maya Yoga.
Generated: DETERMINISTIC_4f94fd599e33f4f5
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```dart
// Flutter code for a Yoga Practice Tracker feature inspired by Maya Yoga training programs.

import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

void main() {
  runApp(YogaTrackerApp());
}

// Main application widget
class YogaTrackerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Yoga Practice Tracker',
      theme: ThemeData(
        primarySwatch: Colors.teal,
      ),
      home: YogaTrackerHomePage(),
    );
  }
}

// Home page for the Yoga Practice Tracker
class YogaTrackerHomePage extends StatefulWidget {
  @override
  _YogaTrackerHomePageState createState() => _YogaTrackerHomePageState();
}

class _YogaTrackerHomePageState extends State<YogaTrackerHomePage> {
  // List to store yoga practice sessions
  final List<YogaSession> _sessions = [];

  // Controller for the duration input
  final TextEditingController _durationController = TextEditingController();

  // Method to add a new yoga session
  void _addSession(String duration) {
    if (duration.isEmpty) return;

    try {
      final int parsedDuration = int.parse(duration);
      if (parsedDuration <= 0) throw FormatException();

      setState(() {
        _sessions.add(YogaSession(
          date: DateTime.now(),
          duration: parsedDuration,
        ));
      });

      _durationController.clear();
    } catch (e) {
      // Show error if input is invalid
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Please enter a valid duration in minutes.')),
      );
    }
  }

  // Method to delete a session
  void _deleteSession(int index) {
    setState(() {
      _sessions.removeAt(index);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Yoga Practice Tracker'),
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _durationController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      labelText: 'Duration (minutes)',
                      border: OutlineInputBorder(),
                    ),
                  ),
                ),
                SizedBox(width: 10),
                ElevatedButton(
                  onPressed: () => _addSession(_durationController.text),
                  child: Text('Add Session'),
                ),
              ],
            ),
          ),
          Expanded(
            child: _sessions.isEmpty
                ? Center(
                    child: Text(
                      'No sessions recorded yet. Start tracking your yoga practice!',
                      textAlign: TextAlign.center,
                      style: TextStyle(fontSize: 16),
                    ),
                  )
                : ListView.builder(
                    itemCount: _sessions.length,
                    itemBuilder: (context, index) {
                      final session = _sessions[index];
                      return Card(
                        margin: EdgeInsets.symmetric(vertical: 8, horizontal: 16),
                        child: ListTile(
                          title: Text(
                            '${session.duration} minutes',
                            style: TextStyle(fontWeight: FontWeight.bold),
                          ),
                          subtitle: Text(
                            'Date: ${DateFormat.yMMMd().format(session.date)}',
                          ),
                          trailing: IconButton(
                            icon: Icon(Icons.delete, color: Colors.red),
                            onPressed: () => _deleteSession(index),
                          ),
                        ),
                      );
                    },
                  ),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    _durationController.dispose();
    super.dispose();
  }
}

// Model class for a Yoga Session
class YogaSession {
  final DateTime date;
  final int duration;

  YogaSession({required this.date, required this.duration});
}
```
