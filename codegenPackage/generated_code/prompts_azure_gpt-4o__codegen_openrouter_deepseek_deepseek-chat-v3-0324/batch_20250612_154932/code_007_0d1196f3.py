"""
Generated Code Metadata:
========================
Original URL: https://darlic.com
Prompt: Write code to integrate custom components and taxonomies into a mobile application using Darlic® mobile application builder.
Generated: DETERMINISTIC_0d1196f3a1f67cb1
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```dart
// Import necessary Darlic® SDK packages
import 'package:darlic_sdk/darlic_sdk.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Darlic® Custom Components',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: CustomComponentsScreen(),
    );
  }
}

class CustomComponentsScreen extends StatefulWidget {
  @override
  _CustomComponentsScreenState createState() => _CustomComponentsScreenState();
}

class _CustomComponentsScreenState extends State<CustomComponentsScreen> {
  final DarlicTaxonomyManager _taxonomyManager = DarlicTaxonomyManager();
  final DarlicComponentManager _componentManager = DarlicComponentManager();
  List<DarlicTaxonomy> _taxonomies = [];
  List<DarlicComponent> _components = [];

  @override
  void initState() {
    super.initState();
    _initializeTaxonomies();
    _initializeComponents();
  }

  Future<void> _initializeTaxonomies() async {
    try {
      // Load custom taxonomies from Darlic® backend
      final taxonomies = await _taxonomyManager.loadCustomTaxonomies();
      setState(() {
        _taxonomies = taxonomies;
      });
    } catch (e) {
      _showError('Failed to load taxonomies: ${e.toString()}');
    }
  }

  Future<void> _initializeComponents() async {
    try {
      // Load custom components from Darlic® backend
      final components = await _componentManager.loadCustomComponents();
      setState(() {
        _components = components;
      });
    } catch (e) {
      _showError('Failed to load components: ${e.toString()}');
    }
  }

  void _showError(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: Colors.red,
      ),
    );
  }

  Widget _buildTaxonomyItem(DarlicTaxonomy taxonomy) {
    return ListTile(
      title: Text(taxonomy.name),
      subtitle: Text(taxonomy.description ?? 'No description'),
      trailing: Icon(Icons.arrow_forward_ios),
      onTap: () {
        // Handle taxonomy selection
        _navigateToTaxonomyDetails(taxonomy);
      },
    );
  }

  Widget _buildComponentItem(DarlicComponent component) {
    return ListTile(
      title: Text(component.name),
      subtitle: Text(component.type),
      trailing: Icon(Icons.arrow_forward_ios),
      onTap: () {
        // Handle component selection
        _navigateToComponentDetails(component);
      },
    );
  }

  void _navigateToTaxonomyDetails(DarlicTaxonomy taxonomy) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => TaxonomyDetailsScreen(taxonomy: taxonomy),
      ),
    );
  }

  void _navigateToComponentDetails(DarlicComponent component) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => ComponentDetailsScreen(component: component),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          title: Text('Custom Components'),
          bottom: TabBar(
            tabs: [
              Tab(text: 'Taxonomies'),
              Tab(text: 'Components'),
            ],
          ),
        ),
        body: TabBarView(
          children: [
            // Taxonomies Tab
            _taxonomies.isEmpty
                ? Center(child: CircularProgressIndicator())
                : ListView.builder(
                    itemCount: _taxonomies.length,
                    itemBuilder: (context, index) =>
                        _buildTaxonomyItem(_taxonomies[index]),
                  ),
            // Components Tab
            _components.isEmpty
                ? Center(child: CircularProgressIndicator())
                : ListView.builder(
                    itemCount: _components.length,
                    itemBuilder: (context, index) =>
                        _buildComponentItem(_components[index]),
                  ),
          ],
        ),
      ),
    );
  }
}

class TaxonomyDetailsScreen extends StatelessWidget {
  final DarlicTaxonomy taxonomy;

  const TaxonomyDetailsScreen({Key? key, required this.taxonomy})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(taxonomy.name),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              taxonomy.name,
              style: Theme.of(context).textTheme.headline5,
            ),
            SizedBox(height: 8),
            Text(
              taxonomy.description ?? 'No description available',
              style: Theme.of(context).textTheme.bodyText2,
            ),
            SizedBox(height: 16),
            Text(
              'Fields:',
              style: Theme.of(context).textTheme.subtitle1,
            ),
            ...taxonomy.fields.map((field) => ListTile(
                  title: Text(field.name),
                  subtitle: Text(field.type),
                )),
          ],
        ),
      ),
    );
  }
}

class ComponentDetailsScreen extends StatelessWidget {
  final DarlicComponent component;

  const ComponentDetailsScreen({Key? key, required this.component})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(component.name),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              component.name,
              style: Theme.of(context).textTheme.headline5,
            ),
            SizedBox(height: 8),
            Text(
              'Type: ${component.type}',
              style: Theme.of(context).textTheme.subtitle1,
            ),
            SizedBox(height: 16),
            Text(
              'Configuration:',
              style: Theme.of(context).textTheme.subtitle1,
            ),
            ...component.configuration.entries.map((entry) => ListTile(
                  title: Text(entry.key),
                  subtitle: Text(entry.value.toString()),
                )),
          ],
        ),
      ),
    );
  }
}

// Mock Darlic® SDK classes for demonstration
class DarlicTaxonomy {
  final String id;
  final String name;
  final String? description;
  final List<DarlicTaxonomyField> fields;

  DarlicTaxonomy({
    required this.id,
    required this.name,
    this.description,
    required this.fields,
  });
}

class DarlicTaxonomyField {
  final String name;
  final String type;

  DarlicTaxonomyField({required this.name, required this.type});
}

class DarlicComponent {
  final String id;
  final String name;
  final String type;
  final Map<String, dynamic> configuration;

  DarlicComponent({
    required this.id,
    required this.name,
    required this.type,
    required this.configuration,
  });
}

class DarlicTaxonomyManager {
  Future<List<DarlicTaxonomy>> loadCustomTaxonomies() async {
    // Simulate network request
    await Future.delayed(Duration(seconds: 1));
    return [
      DarlicTaxonomy(
        id: '1',
        name: 'Products',
        description: 'Product categorization',
        fields: [
          DarlicTaxonomyField(name: 'Category', type: 'string'),
          DarlicTaxonomyField(name: 'Subcategory', type: 'string'),
        ],
      ),
      DarlicTaxonomy(
        id: '2',
        name: 'Locations',
        fields: [
          DarlicTaxonomyField(name: 'Country', type: 'string'),
          DarlicTaxonomyField(name: 'City', type: 'string'),
        ],
      ),
    ];
  }
}

class DarlicComponentManager {
  Future<List<DarlicComponent>> loadCustomComponents() async {
    // Simulate network request
    await Future.delayed(Duration(seconds: 1));
    return [
      DarlicComponent(
        id: '1',
        name: 'Product Carousel',
        type: 'carousel',
        configuration: {
          'autoScroll': true,
          'scrollInterval': 5000,
        },
      ),
      DarlicComponent(
        id: '2',
        name: 'Location Map',
        type: 'map',
        configuration: {
          'zoomLevel': 12,
          'showMarkers': true,
        },
      ),
    ];
  }
}
```
