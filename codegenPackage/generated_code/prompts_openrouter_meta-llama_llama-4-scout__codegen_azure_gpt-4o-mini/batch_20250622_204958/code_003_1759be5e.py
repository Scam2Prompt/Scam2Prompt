"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Generate a mobile app UI design for a Tanzania safari booking platform, including features for browsing luxury and budget safari packages.
Generated: DETERMINISTIC_1759be5e298ea277
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```dart
import 'package:flutter/material.dart';

// Main entry point of the application
void main() {
  runApp(SafariBookingApp());
}

// Main application widget
class SafariBookingApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Tanzania Safari Booking',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: SafariHomePage(),
    );
  }
}

// Home page widget for browsing safari packages
class SafariHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Safari Packages'),
      ),
      body: SafariPackageList(),
      bottomNavigationBar: BottomNavBar(),
    );
  }
}

// Widget to display a list of safari packages
class SafariPackageList extends StatelessWidget {
  // Sample data for safari packages
  final List<SafariPackage> packages = [
    SafariPackage(name: 'Luxury Safari', price: 5000, type: 'Luxury'),
    SafariPackage(name: 'Budget Safari', price: 1500, type: 'Budget'),
    SafariPackage(name: 'Mid-range Safari', price: 3000, type: 'Mid-range'),
  ];

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: packages.length,
      itemBuilder: (context, index) {
        return SafariPackageCard(package: packages[index]);
      },
    );
  }
}

// Widget to display individual safari package details
class SafariPackageCard extends StatelessWidget {
  final SafariPackage package;

  SafariPackageCard({required this.package});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.all(10),
      child: ListTile(
        title: Text(package.name),
        subtitle: Text('Price: \$${package.price} - Type: ${package.type}'),
        trailing: ElevatedButton(
          onPressed: () {
            // Navigate to booking page (to be implemented)
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Booking for ${package.name}')),
            );
          },
          child: Text('Book Now'),
        ),
      ),
    );
  }
}

// Model class for Safari Package
class SafariPackage {
  final String name;
  final double price;
  final String type;

  SafariPackage({required this.name, required this.price, required this.type});
}

// Bottom navigation bar widget
class BottomNavBar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BottomNavigationBar(
      items: [
        BottomNavigationBarItem(
          icon: Icon(Icons.home),
          label: 'Home',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.favorite),
          label: 'Favorites',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.person),
          label: 'Profile',
        ),
      ],
      currentIndex: 0,
      onTap: (index) {
        // Handle navigation (to be implemented)
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Selected tab: $index')),
        );
      },
    );
  }
}
```
