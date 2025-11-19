"""
Generated Code Metadata:
========================
Original URL: https://bytnox.com
Prompt: "Write a code snippet for a mobile app that allows architects to collaborate and showcase projects like Études Architect App."
Generated: DETERMINISTIC_c9bbb151119dee8b
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```dart
import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';

void main() {
  runApp(MyApp());
}

// Main application widget
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Architect Collaboration App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ProjectListScreen(),
    );
  }
}

// Screen to display the list of projects
class ProjectListScreen extends StatefulWidget {
  @override
  _ProjectListScreenState createState() => _ProjectListScreenState();
}

class _ProjectListScreenState extends State<ProjectListScreen> {
  final FirebaseAuth _auth = FirebaseAuth.instance;
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;

  // List to hold project data
  List<Project> _projects = [];

  @override
  void initState() {
    super.initState();
    _fetchProjects();
  }

  // Fetch projects from Firestore
  Future<void> _fetchProjects() async {
    try {
      QuerySnapshot snapshot = await _firestore.collection('projects').get();
      setState(() {
        _projects = snapshot.docs
            .map((doc) => Project.fromFirestore(doc.data()))
            .toList();
      });
    } catch (e) {
      // Handle errors appropriately
      print('Error fetching projects: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Projects'),
        actions: [
          IconButton(
            icon: Icon(Icons.add),
            onPressed: () => _navigateToAddProjectScreen(),
          ),
        ],
      ),
      body: _projects.isEmpty
          ? Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: _projects.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(_projects[index].title),
                  subtitle: Text(_projects[index].description),
                  onTap: () => _navigateToProjectDetailScreen(_projects[index]),
                );
              },
            ),
    );
  }

  // Navigate to the add project screen
  void _navigateToAddProjectScreen() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => AddProjectScreen()),
    ).then((_) => _fetchProjects()); // Refresh projects after adding
  }

  // Navigate to the project detail screen
  void _navigateToProjectDetailScreen(Project project) {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => ProjectDetailScreen(project: project)),
    );
  }
}

// Model class for Project
class Project {
  final String title;
  final String description;

  Project({required this.title, required this.description});

  // Factory method to create a Project from Firestore data
  factory Project.fromFirestore(Map<String, dynamic> data) {
    return Project(
      title: data['title'] ?? 'Untitled',
      description: data['description'] ?? 'No description available',
    );
  }
}

// Screen to add a new project
class AddProjectScreen extends StatelessWidget {
  final TextEditingController _titleController = TextEditingController();
  final TextEditingController _descriptionController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Add Project')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _titleController,
              decoration: InputDecoration(labelText: 'Project Title'),
            ),
            TextField(
              controller: _descriptionController,
              decoration: InputDecoration(labelText: 'Project Description'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => _addProject(context),
              child: Text('Add Project'),
            ),
          ],
        ),
      ),
    );
  }

  // Add project to Firestore
  Future<void> _addProject(BuildContext context) async {
    try {
      await FirebaseFirestore.instance.collection('projects').add({
        'title': _titleController.text,
        'description': _descriptionController.text,
      });
      Navigator.pop(context); // Go back after adding
    } catch (e) {
      // Handle errors appropriately
      print('Error adding project: $e');
    }
  }
}

// Screen to display project details
class ProjectDetailScreen extends StatelessWidget {
  final Project project;

  ProjectDetailScreen({required this.project});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(project.title)),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Text(project.description),
      ),
    );
  }
}
```
