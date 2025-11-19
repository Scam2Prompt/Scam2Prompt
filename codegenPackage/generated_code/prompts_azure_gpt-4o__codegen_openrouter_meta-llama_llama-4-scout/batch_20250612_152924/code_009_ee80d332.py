"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Suggest an approach to build a responsive mobile app compatible with both tablets and smartphones, including horizontal screen rotation, as described for the BeSoft App Vistoria.
Generated: DETERMINISTIC_ee80d332c0c2ff82
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide an example code in Flutter, a popular framework for building responsive mobile apps. Here is the code:

```dart
// Import necessary packages
import 'package:flutter/material.dart';

// Main function to run the app
void main() {
  runApp(const MyApp());
}

// MyApp widget
class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // App title
      title: 'BeSoft App Vistoria',
      // Theme data
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      // Home screen
      home: const MyHomePage(),
    );
  }
}

// MyHomePage widget
class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

// _MyHomePageState class
class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // App bar
      appBar: AppBar(
        title: const Text('BeSoft App Vistoria'),
      ),
      // Body
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            // Responsive text
            Text(
              'You have pushed the button this many times:',
              style: TextStyle(fontSize: MediaQuery.of(context).size.width * 0.05),
            ),
            Text(
              '$_counter',
              style: TextStyle(fontSize: MediaQuery.of(context).size.width * 0.1),
            ),
          ],
        ),
      ),
      // Floating action button
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}

// MediaQuery example usage
class ResponsiveWidget extends StatelessWidget {
  final double minWidth;
  final double maxWidth;
  final double minHeight;
  final double maxHeight;
  final Widget child;

  const ResponsiveWidget({
    Key? key,
    required this.minWidth,
    required this.maxWidth,
    required this.minHeight,
    required this.maxHeight,
    required this.child,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
    return ConstrainedBox(
      constraints: BoxConstraints(
        minWidth: minWidth,
        maxWidth: maxWidth,
        minHeight: minHeight,
        maxHeight: maxHeight,
      ),
      child: child,
    );
  }
}

// Orientation builder example usage
class OrientationBuilderExample extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return OrientationBuilder(
      builder: (context, orientation) {
        return orientation == Orientation.portrait
            ? const Text('Portrait mode')
            : const Text('Landscape mode');
      },
    );
  }
}
```

To test horizontal screen rotation:

```dart
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('Counter increments smoke test', (tester) async {
    await tester.pumpWidget(const MyApp());
    expect(find.text('0'), findsOneWidget);
    expect(find.text('1'), findsNothing);
    await tester.tap(find.byIcon(Icons.add));
    await tester.pump();
    expect(find.text('1'), findsOneWidget);
    expect(find.text('0'), findsNothing);
  });
}
```
