"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Generate code for a mobile app that provides access to SKI Foundation's "Training & Coaching Bisnis" materials, with offline access and progress tracking features.
Generated: DETERMINISTIC_d285a1294061c0db
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```dart
// Import necessary packages
import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';
import 'package:sqflite/sqflite.dart';
import 'dart:io';

// Main function to run the application
void main() {
  runApp(SKIApp());
}

// The main application widget
class SKIApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SKI Foundation Training & Coaching',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: TrainingHome(),
    );
  }
}

// Home screen for the training materials
class TrainingHome extends StatefulWidget {
  @override
  _TrainingHomeState createState() => _TrainingHomeState();
}

class _TrainingHomeState extends State<TrainingHome> {
  // Database instance
  Database? _database;
  List<TrainingMaterial> _materials = [];

  @override
  void initState() {
    super.initState();
    _initializeDatabase();
    _loadTrainingMaterials();
  }

  // Initialize the SQLite database
  Future<void> _initializeDatabase() async {
    Directory documentsDirectory = await getApplicationDocumentsDirectory();
    String path = '${documentsDirectory.path}/training_materials.db';

    _database = await openDatabase(
      path,
      version: 1,
      onCreate: (Database db, int version) async {
        await db.execute('''
          CREATE TABLE materials (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            progress INTEGER DEFAULT 0
          )
        ''');
      },
    );
  }

  // Load training materials from the database
  Future<void> _loadTrainingMaterials() async {
    if (_database != null) {
      List<Map<String, dynamic>> maps = await _database!.query('materials');
      setState(() {
        _materials = maps.map((m) => TrainingMaterial.fromMap(m)).toList();
      });
    }
  }

  // Display a list of training materials
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Training Materials'),
      ),
      body: ListView.builder(
        itemCount: _materials.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(_materials[index].title),
            subtitle: Text('Progress: ${_materials[index].progress}%'),
            onTap: () => _navigateToMaterialDetail(_materials[index]),
          );
        },
      ),
    );
  }

  // Navigate to the material detail page
  void _navigateToMaterialDetail(TrainingMaterial material) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => TrainingDetail(material: material, onProgressUpdate: _updateProgress),
      ),
    );
  }

  // Update the progress of a training material
  Future<void> _updateProgress(int id, int progress) async {
    await _database!.update(
      'materials',
      {'progress': progress},
      where: 'id = ?',
      whereArgs: [id],
    );
    _loadTrainingMaterials();
  }
}

// Model class for Training Material
class TrainingMaterial {
  final int? id;
  final String title;
  final String content;
  final int progress;

  TrainingMaterial({this.id, required this.title, required this.content, this.progress = 0});

  factory TrainingMaterial.fromMap(Map<String, dynamic> map) {
    return TrainingMaterial(
      id: map['id'],
      title: map['title'],
      content: map['content'],
      progress: map['progress'],
    );
  }
}

// Detail page for each training material
class TrainingDetail extends StatelessWidget {
  final TrainingMaterial material;
  final Future<void> Function(int, int) onProgressUpdate;

  TrainingDetail({required this.material, required this.onProgressUpdate});

  @override
  Widget build(BuildContext context) {
    int progress = material.progress;

    return Scaffold(
      appBar: AppBar(
        title: Text(material.title),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Text(material.content),
            SizedBox(height: 20),
            Text('Progress: $progress%'),
            Slider(
              value: progress.toDouble(),
              min: 0,
              max: 100,
              divisions: 100,
              label: '$progress%',
              onChanged: (value) {
                progress = value.toInt();
                onProgressUpdate(material.id!, progress);
              },
            ),
          ],
        ),
      ),
    );
  }
}
```
