"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiberahamlets.org
Prompt: Write code for a mobile app that tracks talent development activities such as spoken word, acrobatics, football, theatre, music, and dance, as described in the "Help me explore my talent" project.
Generated: DETERMINISTIC_3c34427bebd927c2
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

// Model for Talent Activity
class TalentActivity {
  final String title;
  final String category;
  final DateTime date;

  TalentActivity({
    required this.title,
    required this.category,
    required this.date,
  });
}

// Provider for managing activities
class ActivityProvider with ChangeNotifier {
  List<TalentActivity> _activities = [];

  List<TalentActivity> get activities => _activities;

  void addActivity(TalentActivity activity) {
    _activities.add(activity);
    notifyListeners();
  }

  void removeActivity(int index) {
    if (index >= 0 && index < _activities.length) {
      _activities.removeAt(index);
      notifyListeners();
    }
  }
}

// Main application widget
void main() {
  runApp(
    ChangeNotifierProvider(
      create: (context) => ActivityProvider(),
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Talent Development Tracker',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: ActivityListScreen(),
    );
  }
}

// Screen to display list of activities
class ActivityListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final activityProvider = Provider.of<ActivityProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('Talent Activities'),
        actions: [
          IconButton(
            icon: Icon(Icons.add),
            onPressed: () => _showAddActivityDialog(context),
          ),
        ],
      ),
      body: ListView.builder(
        itemCount: activityProvider.activities.length,
        itemBuilder: (context, index) {
          final activity = activityProvider.activities[index];
          return ListTile(
            title: Text(activity.title),
            subtitle: Text('${activity.category} - ${activity.date.toLocal()}'),
            trailing: IconButton(
              icon: Icon(Icons.delete),
              onPressed: () => activityProvider.removeActivity(index),
            ),
          );
        },
      ),
    );
  }

  void _showAddActivityDialog(BuildContext context) {
    final titleController = TextEditingController();
    final categoryController = TextEditingController();
    final dateController = TextEditingController();

    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text('Add Talent Activity'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              TextField(
                controller: titleController,
                decoration: InputDecoration(labelText: 'Activity Title'),
              ),
              TextField(
                controller: categoryController,
                decoration: InputDecoration(labelText: 'Category (e.g., spoken word, acrobatics)'),
              ),
              TextField(
                controller: dateController,
                decoration: InputDecoration(labelText: 'Date (YYYY-MM-DD)'),
                keyboardType: TextInputType.datetime,
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                // Basic input validation
                if (titleController.text.isNotEmpty &&
                    categoryController.text.isNotEmpty &&
                    dateController.text.isNotEmpty) {
                  try {
                    DateTime parsedDate = DateTime.parse(dateController.text);
                    TalentActivity newActivity = TalentActivity(
                      title: titleController.text,
                      category: categoryController.text,
                      date: parsedDate,
                    );

                    Provider.of<ActivityProvider>(context, listen: false)
                        .addActivity(newActivity);
                    Navigator.of(context).pop();
                  } catch (e) {
                    // Show error message for date parsing
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(content: Text('Invalid date format.')),
                    );
                  }
                }
              },
              child: Text('Add'),
            ),
          ],
        );
      },
    );
  }
}
```
