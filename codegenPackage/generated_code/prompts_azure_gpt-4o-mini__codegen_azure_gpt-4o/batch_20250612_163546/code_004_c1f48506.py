"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: Implement a feature in a mobile app that allows users to book a free consultation with Meezan Interior Solutions and select their preferred design services.
Generated: DETERMINISTIC_c1f48506606146cf
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is the code for implementing the requested feature in a mobile app using Flutter (Dart). This code assumes the app is already set up with Flutter and uses Firebase Firestore for backend data storage.

```dart
import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class ConsultationBookingScreen extends StatefulWidget {
  @override
  _ConsultationBookingScreenState createState() =>
      _ConsultationBookingScreenState();
}

class _ConsultationBookingScreenState extends State<ConsultationBookingScreen> {
  final _formKey = GlobalKey<FormState>();
  final _nameController = TextEditingController();
  final _emailController = TextEditingController();
  final _phoneController = TextEditingController();
  String? _selectedService;

  // List of design services offered
  final List<String> _designServices = [
    'Interior Design',
    'Furniture Design',
    'Space Planning',
    'Lighting Design',
    'Custom Decor'
  ];

  // Function to handle form submission
  Future<void> _submitForm() async {
    if (_formKey.currentState!.validate()) {
      try {
        // Save booking details to Firestore
        await FirebaseFirestore.instance.collection('consultations').add({
          'name': _nameController.text,
          'email': _emailController.text,
          'phone': _phoneController.text,
          'service': _selectedService,
          'timestamp': FieldValue.serverTimestamp(),
        });

        // Show success message
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Consultation booked successfully!')),
        );

        // Clear form fields
        _nameController.clear();
        _emailController.clear();
        _phoneController.clear();
        setState(() {
          _selectedService = null;
        });
      } catch (error) {
        // Handle errors gracefully
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Failed to book consultation. Please try again.')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Book a Free Consultation'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Name field
                TextFormField(
                  controller: _nameController,
                  decoration: InputDecoration(labelText: 'Name'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter your name';
                    }
                    return null;
                  },
                ),
                SizedBox(height: 16),

                // Email field
                TextFormField(
                  controller: _emailController,
                  decoration: InputDecoration(labelText: 'Email'),
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
                SizedBox(height: 16),

                // Phone field
                TextFormField(
                  controller: _phoneController,
                  decoration: InputDecoration(labelText: 'Phone'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter your phone number';
                    }
                    if (!RegExp(r'^\d{10}$').hasMatch(value)) {
                      return 'Please enter a valid 10-digit phone number';
                    }
                    return null;
                  },
                ),
                SizedBox(height: 16),

                // Dropdown for selecting design service
                DropdownButtonFormField<String>(
                  value: _selectedService,
                  decoration: InputDecoration(labelText: 'Select Design Service'),
                  items: _designServices.map((service) {
                    return DropdownMenuItem(
                      value: service,
                      child: Text(service),
                    );
                  }).toList(),
                  onChanged: (value) {
                    setState(() {
                      _selectedService = value;
                    });
                  },
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please select a design service';
                    }
                    return null;
                  },
                ),
                SizedBox(height: 32),

                // Submit button
                Center(
                  child: ElevatedButton(
                    onPressed: _submitForm,
                    child: Text('Book Consultation'),
                  ),
                ),
              ],
            ),
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
    _phoneController.dispose();
    super.dispose();
  }
}
```

### Notes:
- Ensure Firebase is properly configured in your Flutter project.
- Add the necessary dependencies (`cloud_firestore`) in your `pubspec.yaml` file.
- Replace the Firestore collection name (`consultations`) with the appropriate name for your database schema.
