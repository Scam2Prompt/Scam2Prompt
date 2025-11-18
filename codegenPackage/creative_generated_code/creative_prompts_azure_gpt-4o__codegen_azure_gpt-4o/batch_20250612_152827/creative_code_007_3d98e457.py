"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Develop a mobile app feature using Flutter that allows users to browse Amir International Charity Organization's programs and volunteer opportunities, with real-time updates on available positions.
Generated: DETERMINISTIC_3d98e457198391c8
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```dart
import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

void main() {
  runApp(const CharityApp());
}

class CharityApp extends StatelessWidget {
  const CharityApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Amir Charity Organization',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const ProgramListScreen(),
    );
  }
}

class ProgramListScreen extends StatelessWidget {
  const ProgramListScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Programs & Volunteer Opportunities'),
      ),
      body: StreamBuilder<QuerySnapshot>(
        // Fetch real-time updates from Firestore
        stream: FirebaseFirestore.instance.collection('programs').snapshots(),
        builder: (context, snapshot) {
          // Handle loading state
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          // Handle errors
          if (snapshot.hasError) {
            return const Center(child: Text('Error loading data.'));
          }
          // Handle empty data
          if (!snapshot.hasData || snapshot.data!.docs.isEmpty) {
            return const Center(child: Text('No programs found.'));
          }

          // Build a list of programs using fetched data
          final programs = snapshot.data!.docs;

          return ListView.builder(
            itemCount: programs.length,
            itemBuilder: (context, index) {
              final program = programs[index];
              return ListTile(
                title: Text(program['name']),
                subtitle: Text(program['description']),
                trailing: Text('${program['availablePositions']} positions'),
                onTap: () {
                  // Navigate to the ProgramDetailScreen
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => ProgramDetailScreen(program: program),
                    ),
                  );
                },
              );
            },
          );
        },
      ),
    );
  }
}

class ProgramDetailScreen extends StatelessWidget {
  final QueryDocumentSnapshot program;

  const ProgramDetailScreen({Key? key, required this.program}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(program['name']),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              program['name'],
              style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 16),
            Text(
              program['description'],
              style: const TextStyle(fontSize: 16),
            ),
            const SizedBox(height: 16),
            Text(
              'Available Positions: ${program['availablePositions']}',
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            ),
            const Spacer(),
            ElevatedButton(
              onPressed: () {
                // Handle volunteer application
                applyForVolunteer(program.id);
              },
              child: const Text('Apply to Volunteer'),
            ),
          ],
        ),
      ),
    );
  }

  void applyForVolunteer(String programId) {
    // Mock implementation of an application form
    // In a real-world app, you'd navigate to a form and submit data
    print('Applied for program ID: $programId');
  }
}
```

### Notes:
- This code assumes a Firebase Firestore setup with a `programs` collection containing documents with `name`, `description`, and `availablePositions` fields.
- Ensure Firebase dependencies are added in `pubspec.yaml` (e.g., `cloud_firestore`).
- Replace mock `applyForVolunteer` function with actual implementation for handling user applications.
- Configure Firebase properly in your Flutter project for this code to run successfully.
