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

Here is the code for a mobile app built using **Flutter** (Dart), as it supports cross-platform development and offline capabilities via packages like `sqflite` and `provider`. The app allows access to SKI Foundation's "Training & Coaching Bisnis" materials, enables offline access, and includes progress tracking.

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import 'dart:async';

// Main Entry Point
void main() {
  runApp(const SKIFoundationApp());
}

// App Initialization
class SKIFoundationApp extends StatelessWidget {
  const SKIFoundationApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => TrainingProvider(),
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'SKI Foundation',
        theme: ThemeData(primarySwatch: Colors.blue),
        home: const TrainingHomePage(),
      ),
    );
  }
}

// Training Provider for State Management
class TrainingProvider with ChangeNotifier {
  List<TrainingMaterial> _materials = [];
  late Database _db;

  List<TrainingMaterial> get materials => _materials;

  TrainingProvider() {
    _initializeDatabase();
  }

  Future<void> _initializeDatabase() async {
    try {
      // Open/create database
      _db = await openDatabase(
        join(await getDatabasesPath(), 'training_materials.db'),
        onCreate: (db, version) {
          return db.execute(
            'CREATE TABLE materials (id INTEGER PRIMARY KEY, title TEXT, content TEXT, progress INTEGER)',
          );
        },
        version: 1,
      );
      await _loadMaterials();
    } catch (e) {
      debugPrint('Error initializing database: $e');
    }
  }

  Future<void> _loadMaterials() async {
    try {
      final List<Map<String, dynamic>> maps = await _db.query('materials');
      _materials = List.generate(
        maps.length,
        (i) => TrainingMaterial(
          id: maps[i]['id'],
          title: maps[i]['title'],
          content: maps[i]['content'],
          progress: maps[i]['progress'],
        ),
      );
      notifyListeners();
    } catch (e) {
      debugPrint('Error loading materials: $e');
    }
  }

  Future<void> addMaterial(TrainingMaterial material) async {
    try {
      await _db.insert(
        'materials',
        material.toMap(),
        conflictAlgorithm: ConflictAlgorithm.replace,
      );
      _materials.add(material);
      notifyListeners();
    } catch (e) {
      debugPrint('Error adding material: $e');
    }
  }

  Future<void> updateProgress(int id, int progress) async {
    try {
      await _db.update(
        'materials',
        {'progress': progress},
        where: 'id = ?',
        whereArgs: [id],
      );
      final index = _materials.indexWhere((material) => material.id == id);
      if (index != -1) {
        _materials[index].progress = progress;
        notifyListeners();
      }
    } catch (e) {
      debugPrint('Error updating progress: $e');
    }
  }
}

// Training Material Model
class TrainingMaterial {
  final int id;
  final String title;
  final String content;
  int progress;

  TrainingMaterial({
    required this.id,
    required this.title,
    required this.content,
    this.progress = 0,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'title': title,
      'content': content,
      'progress': progress,
    };
  }
}

// Home Page
class TrainingHomePage extends StatelessWidget {
  const TrainingHomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final trainingProvider = Provider.of<TrainingProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('SKI Foundation Materials'),
      ),
      body: trainingProvider.materials.isEmpty
          ? const Center(child: Text('No materials available.'))
          : ListView.builder(
              itemCount: trainingProvider.materials.length,
              itemBuilder: (context, index) {
                final material = trainingProvider.materials[index];
                return ListTile(
                  title: Text(material.title),
                  subtitle: Text('Progress: ${material.progress}%'),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) =>
                            MaterialDetailsPage(material: material),
                      ),
                    );
                  },
                );
              },
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          final newMaterial = TrainingMaterial(
            id: DateTime.now().millisecondsSinceEpoch,
            title: 'New Training Material',
            content: 'Content of the new material',
          );
          trainingProvider.addMaterial(newMaterial);
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}

// Material Details Page
class MaterialDetailsPage extends StatelessWidget {
  final TrainingMaterial material;

  const MaterialDetailsPage({Key? key, required this.material})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    final trainingProvider = Provider.of<TrainingProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text(material.title),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              material.content,
              style: const TextStyle(fontSize: 18),
            ),
            const SizedBox(height: 20),
            Text(
              'Progress: ${material.progress}%',
              style: const TextStyle(fontSize: 16),
            ),
            const Spacer(),
            Slider(
              value: material.progress.toDouble(),
              min: 0,
              max: 100,
              divisions: 100,
              label: '${material.progress}%',
              onChanged: (value) {
                trainingProvider.updateProgress(material.id, value.toInt());
              },
            ),
          ],
        ),
      ),
    );
  }
}
```

### How to Run:
1. Install Flutter SDK.
2. Create a new Flutter project and replace the content of `main.dart` with the code above.
3. Run `flutter pub get` to fetch dependencies like `provider` and `sqflite`.
4. Run the app on an emulator or a physical device using `flutter run`.

This code covers offline access, progress tracking, and state management, with error handling for database operations.
