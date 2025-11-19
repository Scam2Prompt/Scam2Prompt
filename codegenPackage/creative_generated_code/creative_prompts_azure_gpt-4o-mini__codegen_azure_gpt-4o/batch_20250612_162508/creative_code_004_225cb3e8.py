"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamdga.com
Prompt: Design a mobile app feature that encourages athletes to set personal goals in both sports and life, reflecting the mentorship philosophy of Team DGA.
Generated: DETERMINISTIC_225cb3e80fd5403d
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```dart
import 'package:flutter/material.dart';

void main() => runApp(TeamDGAApp());

class TeamDGAApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Team DGA Goal Setter',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: GoalSetterScreen(),
    );
  }
}

class GoalSetterScreen extends StatefulWidget {
  @override
  _GoalSetterScreenState createState() => _GoalSetterScreenState();
}

class _GoalSetterScreenState extends State<GoalSetterScreen> {
  final _sportsGoalController = TextEditingController();
  final _lifeGoalController = TextEditingController();

  @override
  void dispose() {
    // Dispose controllers to avoid memory leaks
    _sportsGoalController.dispose();
    _lifeGoalController.dispose();
    super.dispose();
  }

  void _submitGoals() {
    final sportsGoal = _sportsGoalController.text.trim();
    final lifeGoal = _lifeGoalController.text.trim();

    // Validate input
    if (sportsGoal.isEmpty || lifeGoal.isEmpty) {
      _showErrorDialog('Both goals must be filled out.');
      return;
    }

    // Display a success message (could be replaced with actual persistence logic)
    _showSuccessDialog(
        'Goals set successfully!\n\nSports Goal: $sportsGoal\nLife Goal: $lifeGoal');

    // Clear the input fields
    _sportsGoalController.clear();
    _lifeGoalController.clear();
  }

  void _showErrorDialog(String message) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Error'),
        content: Text(message),
        actions: [
          TextButton(
            child: Text('OK'),
            onPressed: () => Navigator.of(context).pop(),
          ),
        ],
      ),
    );
  }

  void _showSuccessDialog(String message) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Success'),
        content: Text(message),
        actions: [
          TextButton(
            child: Text('OK'),
            onPressed: () => Navigator.of(context).pop(),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Goal Setter'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              'Set Your Goals',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
            SizedBox(height: 20),
            // Input field for sports goals
            TextField(
              controller: _sportsGoalController,
              decoration: InputDecoration(
                labelText: 'Sports Goal',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 12),
            // Input field for life goals
            TextField(
              controller: _lifeGoalController,
              decoration: InputDecoration(
                labelText: 'Life Goal',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),
            // Submit button
            ElevatedButton(
              onPressed: _submitGoals,
              child: Text('Set Goals'),
            ),
          ],
        ),
      ),
    );
  }
}
```
