"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Generate code for a mobile app that connects to AI-powered CCTV cameras for real-time monitoring and analytics, inspired by Donture Systems Ltd's solutions.
Generated: DETERMINISTIC_07a02caf1f326baf
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/cctv-cameras": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/cctv-cameras`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here’s the clean, production-ready code for a mobile app using Flutter (Dart) to connect to AI-powered CCTV cameras for real-time monitoring and analytics. This implementation assumes the backend AI system provides RESTful APIs for connecting to and retrieving data from the cameras.

```dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

// Entry point of the app
void main() {
  runApp(CCTVMonitoringApp());
}

// Main application widget
class CCTVMonitoringApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AI CCTV Monitoring',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: CCTVMonitoringScreen(),
    );
  }
}

// Home screen for monitoring AI-powered CCTV cameras
class CCTVMonitoringScreen extends StatefulWidget {
  @override
  _CCTVMonitoringScreenState createState() => _CCTVMonitoringScreenState();
}

class _CCTVMonitoringScreenState extends State<CCTVMonitoringScreen> {
  List<dynamic> cameraData = [];
  bool isLoading = false;
  String errorMessage = "";

  // Replace this URL with your backend endpoint
  final String apiEndpoint = "https://api.example.com/cctv-cameras";

  @override
  void initState() {
    super.initState();
    fetchCameraData();
  }

  // Function to fetch camera data from the backend
  Future<void> fetchCameraData() async {
    setState(() {
      isLoading = true;
      errorMessage = "";
    });

    try {
      final response = await http.get(Uri.parse(apiEndpoint));
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        setState(() {
          cameraData = data['cameras']; // Adjust the key as per API response
        });
      } else {
        setState(() {
          errorMessage = "Failed to fetch camera data: ${response.statusCode}";
        });
      }
    } catch (e) {
      setState(() {
        errorMessage = "An error occurred while fetching data: $e";
      });
    } finally {
      setState(() {
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('AI CCTV Monitoring'),
      ),
      body: isLoading
          ? Center(child: CircularProgressIndicator())
          : errorMessage.isNotEmpty
              ? Center(child: Text(errorMessage, style: TextStyle(color: Colors.red)))
              : ListView.builder(
                  itemCount: cameraData.length,
                  itemBuilder: (context, index) {
                    final camera = cameraData[index];
                    return ListTile(
                      leading: Icon(Icons.videocam),
                      title: Text(camera['name'] ?? 'Unknown Camera'),
                      subtitle: Text('Status: ${camera['status'] ?? 'Unknown'}'),
                      onTap: () {
                        // Navigate to detailed view (implementation needed)
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => CameraDetailScreen(camera: camera),
                          ),
                        );
                      },
                    );
                  },
                ),
      floatingActionButton: FloatingActionButton(
        onPressed: fetchCameraData,
        child: Icon(Icons.refresh),
        tooltip: 'Refresh Cameras',
      ),
    );
  }
}

// Screen for displaying detailed camera analytics
class CameraDetailScreen extends StatelessWidget {
  final dynamic camera;

  CameraDetailScreen({required this.camera});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(camera['name'] ?? 'Camera Details'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Camera Name: ${camera['name'] ?? 'Unknown'}',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text('Status: ${camera['status'] ?? 'Unknown'}'),
            SizedBox(height: 8),
            Text('Analytics:', style: TextStyle(fontWeight: FontWeight.bold)),
            SizedBox(height: 8),
            Expanded(
              child: camera['analytics'] != null
                  ? ListView.builder(
                      itemCount: camera['analytics'].length,
                      itemBuilder: (context, index) {
                        final analytic = camera['analytics'][index];
                        return ListTile(
                          title: Text(analytic['type'] ?? 'Unknown Analytic'),
                          subtitle: Text(analytic['data'] ?? 'No data available'),
                        );
                      },
                    )
                  : Center(child: Text('No analytics available')),
            ),
          ],
        ),
      ),
    );
  }
}
```

### Notes:
1. Replace `https://api.example.com/cctv-cameras` with your actual backend URL for fetching data from the AI-powered CCTV cameras.
2. Ensure the backend API response format matches the code structure (e.g., `cameras`, `name`, `status`, `analytics` keys).
3. You might need to expand the app to handle authentication, live video streams, and additional analytics from the cameras, depending on the backend capabilities.
