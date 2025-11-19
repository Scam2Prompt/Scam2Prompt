"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Design a mobile app interface that showcases various music genres available on Radio S, such as 'Latino Hits' and 'YU Rock Hits', ensuring easy navigation for users.
Generated: DETERMINISTIC_511109c3f2f09ac3
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Flutter implementation for a mobile app interface showcasing music genres with clean navigation:

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const RadioSApp());
}

class RadioSApp extends StatelessWidget {
  const RadioSApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Radio S',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const GenreSelectionScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class GenreSelectionScreen extends StatelessWidget {
  const GenreSelectionScreen({super.key});

  // Sample genre data
  final List<Genre> genres = const [
    Genre(name: 'Latino Hits', color: Colors.red, icon: Icons.music_note),
    Genre(name: 'YU Rock Hits', color: Colors.blue, icon: Icons.rocket),
    Genre(name: 'Pop', color: Colors.purple, icon: Icons.star),
    Genre(name: 'Jazz', color: Colors.amber, icon: Icons.library_music),
    Genre(name: 'Classical', color: Colors.green, icon: Icons.audiotrack),
    Genre(name: 'Electronic', color: Colors.orange, icon: Icons.electrical_services),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Radio S - Music Genres'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: GridView.builder(
          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2,
            crossAxisSpacing: 16,
            mainAxisSpacing: 16,
            childAspectRatio: 1.0,
          ),
          itemCount: genres.length,
          itemBuilder: (context, index) {
            return GenreCard(genre: genres[index]);
          },
        ),
      ),
    );
  }
}

class Genre {
  final String name;
  final Color color;
  final IconData icon;

  const Genre({
    required this.name,
    required this.color,
    required this.icon,
  });
}

class GenreCard extends StatelessWidget {
  final Genre genre;

  const GenreCard({super.key, required this.genre});

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 4,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
      ),
      child: InkWell(
        borderRadius: BorderRadius.circular(12),
        onTap: () {
          // Navigate to genre details screen
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => GenreDetailScreen(genre: genre),
            ),
          );
        },
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              genre.icon,
              size: 48,
              color: genre.color,
            ),
            const SizedBox(height: 16),
            Text(
              genre.name,
              style: const TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class GenreDetailScreen extends StatelessWidget {
  final Genre genre;

  const GenreDetailScreen({super.key, required this.genre});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(genre.name),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              genre.icon,
              size: 100,
              color: genre.color,
            ),
            const SizedBox(height: 20),
            Text(
              'Now Playing: ${genre.name} Station',
              style: const TextStyle(fontSize: 24),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // Play/pause functionality would go here
              },
              child: const Text('Play Station'),
            ),
          ],
        ),
      ),
    );
  }
}
```
