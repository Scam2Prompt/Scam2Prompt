"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Develop a mobile app feature that allows users to track their volunteer hours, reflecting the NICER Foundation's mission of community involvement and support.
Generated: DETERMINISTIC_a3af5a5a6bdf88c0
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```dart
// main.dart
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (context) => VolunteerHoursProvider(),
      child: const NicerVolunteerApp(),
    ),
  );
}

class NicerVolunteerApp extends StatelessWidget {
  const NicerVolunteerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'NICER Volunteer Tracker',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const VolunteerHoursScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class VolunteerHoursScreen extends StatefulWidget {
  const VolunteerHoursScreen({super.key});

  @override
  State<VolunteerHoursScreen> createState() => _VolunteerHoursScreenState();
}

class _VolunteerHoursScreenState extends State<VolunteerHoursScreen> {
  final _formKey = GlobalKey<FormState>();
  final _activityController = TextEditingController();
  final _organizationController = TextEditingController();
  DateTime _selectedDate = DateTime.now();
  double _hours = 1.0;

  Future<void> _selectDate(BuildContext context) async {
    final DateTime? picked = await showDatePicker(
      context: context,
      initialDate: _selectedDate,
      firstDate: DateTime(2000),
      lastDate: DateTime.now(),
    );
    if (picked != null && picked != _selectedDate) {
      setState(() {
        _selectedDate = picked;
      });
    }
  }

  @override
  void dispose() {
    _activityController.dispose();
    _organizationController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('NICER Volunteer Hours'),
        actions: [
          IconButton(
            icon: const Icon(Icons.bar_chart),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => const VolunteerStatsScreen(),
                ),
              );
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            _buildVolunteerForm(),
            const SizedBox(height: 20),
            _buildVolunteerHistory(),
          ],
        ),
      ),
    );
  }

  Widget _buildVolunteerForm() {
    return Card(
      elevation: 4,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'Log Volunteer Hours',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: _activityController,
                decoration: const InputDecoration(
                  labelText: 'Activity',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter the activity';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: _organizationController,
                decoration: const InputDecoration(
                  labelText: 'Organization',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter the organization';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    child: InkWell(
                      onTap: () => _selectDate(context),
                      child: InputDecorator(
                        decoration: const InputDecoration(
                          labelText: 'Date',
                          border: OutlineInputBorder(),
                        ),
                        child: Text(
                          DateFormat('MMM dd, yyyy').format(_selectedDate),
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: DropdownButtonFormField<double>(
                      value: _hours,
                      decoration: const InputDecoration(
                        labelText: 'Hours',
                        border: OutlineInputBorder(),
                      ),
                      items: List.generate(24, (index) {
                        double value = (index + 1) * 0.5;
                        return DropdownMenuItem(
                          value: value,
                          child: Text('$value hours'),
                        );
                      }),
                      onChanged: (value) {
                        setState(() {
                          _hours = value!;
                        });
                      },
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              Center(
                child: ElevatedButton(
                  onPressed: () {
                    if (_formKey.currentState!.validate()) {
                      Provider.of<VolunteerHoursProvider>(context, listen: false)
                          .addVolunteerHours(
                        VolunteerHours(
                          activity: _activityController.text,
                          organization: _organizationController.text,
                          date: _selectedDate,
                          hours: _hours,
                        ),
                      );
                      _activityController.clear();
                      _organizationController.clear();
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(
                          content: Text('Volunteer hours logged successfully!'),
                        ),
                      );
                    }
                  },
                  child: const Text('Submit'),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildVolunteerHistory() {
    return Consumer<VolunteerHoursProvider>(
      builder: (context, provider, child) {
        if (provider.volunteerHours.isEmpty) {
          return const Center(
            child: Text('No volunteer hours logged yet.'),
          );
        }

        return Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Your Volunteer History',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            ListView.builder(
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              itemCount: provider.volunteerHours.length,
              itemBuilder: (context, index) {
                final entry = provider.volunteerHours[index];
                return Card(
                  margin: const EdgeInsets.symmetric(vertical: 4),
                  child: ListTile(
                    title: Text(entry.activity),
                    subtitle: Text(
                        '${entry.organization} • ${DateFormat('MMM dd, yyyy').format(entry.date)}'),
                    trailing: Text('${entry.hours} hrs'),
                  ),
                );
              },
            ),
          ],
        );
      },
    );
  }
}

class VolunteerStatsScreen extends StatelessWidget {
  const VolunteerStatsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<VolunteerHoursProvider>(context);
    final totalHours = provider.totalHours;
    final uniqueOrganizations = provider.uniqueOrganizations;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Volunteer Statistics'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            _buildStatCard(
              'Total Hours',
              totalHours.toStringAsFixed(1),
              Icons.access_time,
            ),
            const SizedBox(height: 16),
            _buildStatCard(
              'Organizations Supported',
              uniqueOrganizations.toString(),
              Icons.people,
            ),
            const SizedBox(height: 16),
            _buildHoursChart(provider),
          ],
        ),
      ),
    );
  }

  Widget _buildStatCard(String title, String value, IconData icon) {
    return Card(
      elevation: 4,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Row(
          children: [
            Icon(icon, size: 40),
            const SizedBox(width: 16),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(fontSize: 16, color: Colors.grey),
                ),
                Text(
                  value,
                  style: const TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildHoursChart(VolunteerHoursProvider provider) {
    final monthlyHours = provider.monthlyHours;

    return Card(
      elevation: 4,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Monthly Hours',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 16),
            SizedBox(
              height: 200,
              child: ListView.builder(
                scrollDirection: Axis.horizontal,
                itemCount: monthlyHours.length,
                itemBuilder: (context, index) {
                  final entry = monthlyHours[index
