"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Build a mobile app using Flutter that enables users to access personalized workout plans, track their progress, and communicate with their personal trainer via WhatsApp.
Generated: DETERMINISTIC_c3deede252759e5d
Batch ID: 20250612_153225
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
import 'package:workout_tracker/screens/home_screen.dart';
import 'package:workout_tracker/screens/workout_plan_screen.dart';
import 'package:workout_tracker/screens/progress_tracking_screen.dart';
import 'package:workout_tracker/screens/trainer_chat_screen.dart';
import 'package:workout_tracker/services/auth_service.dart';
import 'package:workout_tracker/services/workout_service.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthService()),
        ChangeNotifierProvider(create: (_) => WorkoutService()),
      ],
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Workout Tracker',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const AuthWrapper(),
      routes: {
        '/home': (context) => const HomeScreen(),
        '/workout-plan': (context) => const WorkoutPlanScreen(),
        '/progress-tracking': (context) => const ProgressTrackingScreen(),
        '/trainer-chat': (context) => const TrainerChatScreen(),
      },
    );
  }
}

class AuthWrapper extends StatelessWidget {
  const AuthWrapper({super.key});

  @override
  Widget build(BuildContext context) {
    final authService = Provider.of<AuthService>(context);

    return StreamBuilder<User?>(
      stream: authService.user,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.active) {
          final user = snapshot.data;
          if (user == null) {
            return const LoginScreen();
          }
          return const HomeScreen();
        }
        return const Scaffold(
          body: Center(child: CircularProgressIndicator()),
        );
      },
    );
  }
}

// auth_service.dart
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/foundation.dart';

class AuthService with ChangeNotifier {
  final FirebaseAuth _auth = FirebaseAuth.instance;
  User? _user;

  AuthService() {
    _auth.authStateChanges().listen(_onAuthStateChanged);
  }

  User? get user => _user;

  Stream<User?> get userStream => _auth.authStateChanges();

  Future<void> _onAuthStateChanged(User? user) async {
    _user = user;
    notifyListeners();
  }

  Future<User?> signInWithEmailAndPassword(
      String email, String password) async {
    try {
      final userCredential = await _auth.signInWithEmailAndPassword(
        email: email,
        password: password,
      );
      return userCredential.user;
    } on FirebaseAuthException catch (e) {
      throw Exception(e.message);
    }
  }

  Future<void> signOut() async {
    await _auth.signOut();
  }
}

// workout_service.dart
import 'package:flutter/foundation.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class WorkoutPlan {
  final String id;
  final String name;
  final String description;
  final List<WorkoutExercise> exercises;

  WorkoutPlan({
    required this.id,
    required this.name,
    required this.description,
    required this.exercises,
  });
}

class WorkoutExercise {
  final String name;
  final String sets;
  final String reps;
  final String rest;

  WorkoutExercise({
    required this.name,
    required this.sets,
    required this.reps,
    required this.rest,
  });
}

class WorkoutService with ChangeNotifier {
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;
  List<WorkoutPlan> _workoutPlans = [];

  List<WorkoutPlan> get workoutPlans => _workoutPlans;

  Future<void> fetchWorkoutPlans(String userId) async {
    try {
      final querySnapshot = await _firestore
          .collection('users')
          .doc(userId)
          .collection('workoutPlans')
          .get();

      _workoutPlans = querySnapshot.docs.map((doc) {
        final data = doc.data();
        final exercises = (data['exercises'] as List)
            .map((e) => WorkoutExercise(
                  name: e['name'],
                  sets: e['sets'],
                  reps: e['reps'],
                  rest: e['rest'],
                ))
            .toList();

        return WorkoutPlan(
          id: doc.id,
          name: data['name'],
          description: data['description'],
          exercises: exercises,
        );
      }).toList();

      notifyListeners();
    } catch (e) {
      throw Exception('Failed to fetch workout plans: $e');
    }
  }

  Future<void> addProgressRecord(
      String userId, String workoutId, Map<String, dynamic> data) async {
    try {
      await _firestore
          .collection('users')
          .doc(userId)
          .collection('progressRecords')
          .add(data);
    } catch (e) {
      throw Exception('Failed to add progress record: $e');
    }
  }
}

// screens/login_screen.dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:workout_tracker/services/auth_service.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  bool _isLoading = false;

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  Future<void> _submit() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() => _isLoading = true);
    try {
      await Provider.of<AuthService>(context, listen: false)
          .signInWithEmailAndPassword(
        _emailController.text.trim(),
        _passwordController.text.trim(),
      );
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Login failed: $e')),
      );
    } finally {
      setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Login')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                controller: _emailController,
                decoration: const InputDecoration(labelText: 'Email'),
                keyboardType: TextInputType.emailAddress,
                validator: (value) =>
                    value!.isEmpty ? 'Please enter your email' : null,
              ),
              TextFormField(
                controller: _passwordController,
                decoration: const InputDecoration(labelText: 'Password'),
                obscureText: true,
                validator: (value) =>
                    value!.isEmpty ? 'Please enter your password' : null,
              ),
              const SizedBox(height: 20),
              _isLoading
                  ? const CircularProgressIndicator()
                  : ElevatedButton(
                      onPressed: _submit,
                      child: const Text('Login'),
                    ),
            ],
          ),
        ),
      ),
    );
  }
}

// screens/home_screen.dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:workout_tracker/services/auth_service.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Workout Tracker'),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () =>
                Provider.of<AuthService>(context, listen: false).signOut(),
          ),
        ],
      ),
      body: Column(
        children: [
          Card(
            child: ListTile(
              title: const Text('Workout Plans'),
              subtitle: const Text('View and follow your personalized plans'),
              trailing: const Icon(Icons.chevron_right),
              onTap: () =>
                  Navigator.pushNamed(context, '/workout-plan'),
            ),
          ),
          Card(
            child: ListTile(
              title: const Text('Progress Tracking'),
              subtitle: const Text('Track your workout progress'),
              trailing: const Icon(Icons.chevron_right),
              onTap: () =>
                  Navigator.pushNamed(context, '/progress-tracking'),
            ),
          ),
          Card(
            child: ListTile(
              title: const Text('Chat with Trainer'),
              subtitle: const Text('Communicate via WhatsApp'),
              trailing: const Icon(Icons.chevron_right),
              onTap: () => Navigator.pushNamed
