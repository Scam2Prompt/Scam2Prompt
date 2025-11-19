"""
Generated Code Metadata:
========================
Original URL: https://förderohr.de
Prompt: Design a user interface for a mobile app that allows users to report drainage issues and request services, reflecting the customer service approach of ElbeRohr.
Generated: DETERMINISTIC_b95e4d16da42b2eb
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```dart
// Flutter code for a mobile app UI to report drainage issues and request services
import 'package:flutter/material.dart';

void main() {
  runApp(ElbeRohrApp());
}

class ElbeRohrApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ElbeRohr Customer Service',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ReportIssueScreen(),
    );
  }
}

class ReportIssueScreen extends StatefulWidget {
  @override
  _ReportIssueScreenState createState() => _ReportIssueScreenState();
}

class _ReportIssueScreenState extends State<ReportIssueScreen> {
  final _formKey = GlobalKey<FormState>();
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _descriptionController = TextEditingController();

  // Method to handle form submission
  void _submitForm() {
    if (_formKey.currentState!.validate()) {
      // Simulate form submission
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Issue reported successfully!')),
      );
      // Clear the form fields
      _nameController.clear();
      _emailController.clear();
      _descriptionController.clear();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Report Drainage Issue'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: ListView(
            children: [
              // Name input field
              TextFormField(
                controller: _nameController,
                decoration: InputDecoration(
                  labelText: 'Name',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your name';
                  }
                  return null;
                },
              ),
              SizedBox(height: 16.0),
              // Email input field
              TextFormField(
                controller: _emailController,
                decoration: InputDecoration(
                  labelText: 'Email',
                  border: OutlineInputBorder(),
                ),
                keyboardType: TextInputType.emailAddress,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your email';
                  }
                  if (!RegExp(r'^[^@]+@[^@]+\.[^@]+').hasMatch(value)) {
                    return 'Please enter a valid email address';
                  }
                  return null;
                },
              ),
              SizedBox(height: 16.0),
              // Description input field
              TextFormField(
                controller: _descriptionController,
                decoration: InputDecoration(
                  labelText: 'Issue Description',
                  border: OutlineInputBorder(),
                ),
                maxLines: 5,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please describe the issue';
                  }
                  return null;
                },
              ),
              SizedBox(height: 16.0),
              // Submit button
              ElevatedButton(
                onPressed: _submitForm,
                child: Text('Submit'),
              ),
            ],
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    // Dispose controllers to free resources
    _nameController.dispose();
    _emailController.dispose();
    _descriptionController.dispose();
    super.dispose();
  }
}
```
