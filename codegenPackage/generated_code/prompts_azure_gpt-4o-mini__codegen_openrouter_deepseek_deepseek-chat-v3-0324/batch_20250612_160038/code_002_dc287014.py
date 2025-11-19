"""
Generated Code Metadata:
========================
Original URL: https://simons-17h.pages.dev
Prompt: Create a mobile app prototype that includes a feature for users to take the "Which Simon’s Cat character are you?" quiz, based on the design elements highlighted on the Simon's Cat page.
Generated: DETERMINISTIC_dc287014bc5b228a
Batch ID: 20250612_160038
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
import 'quiz_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Simon\'s Cat Quiz',
      theme: ThemeData(
        primarySwatch: Colors.orange,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const HomeScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Simon\'s Cat Quiz'),
        centerTitle: true,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(
              'assets/simons_cat_logo.png',
              height: 150,
            ),
            const SizedBox(height: 30),
            const Text(
              'Which Simon\'s Cat character are you?',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 30),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => const QuizScreen(),
                  ),
                );
              },
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15),
              ),
              child: const Text(
                'Start Quiz',
                style: TextStyle(fontSize: 18),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

```dart
// quiz_screen.dart
import 'package:flutter/material.dart';

class QuizScreen extends StatefulWidget {
  const QuizScreen({super.key});

  @override
  _QuizScreenState createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  int _currentQuestionIndex = 0;
  int _simonsCatScore = 0;
  int _jazzScore = 0;
  int _mumScore = 0;
  int _chloeScore = 0;

  final List<Map<String, dynamic>> _questions = [
    {
      'question': 'What\'s your favorite activity?',
      'answers': [
        {'text': 'Sleeping', 'character': 'Simon\'s Cat'},
        {'text': 'Playing with toys', 'character': 'Jazz'},
        {'text': 'Eating', 'character': 'Mum'},
        {'text': 'Exploring outdoors', 'character': 'Chloe'},
      ],
    },
    {
      'question': 'How do you react to new people?',
      'answers': [
        {'text': 'Curious but cautious', 'character': 'Simon\'s Cat'},
        {'text': 'Excited and playful', 'character': 'Jazz'},
        {'text': 'Hungry for attention', 'character': 'Mum'},
        {'text': 'Shy at first', 'character': 'Chloe'},
      ],
    },
    {
      'question': 'What\'s your typical mood?',
      'answers': [
        {'text': 'Mischievous', 'character': 'Simon\'s Cat'},
        {'text': 'Energetic', 'character': 'Jazz'},
        {'text': 'Relaxed', 'character': 'Mum'},
        {'text': 'Independent', 'character': 'Chloe'},
      ],
    },
  ];

  void _answerQuestion(String character) {
    setState(() {
      switch (character) {
        case 'Simon\'s Cat':
          _simonsCatScore++;
          break;
        case 'Jazz':
          _jazzScore++;
          break;
        case 'Mum':
          _mumScore++;
          break;
        case 'Chloe':
          _chloeScore++;
          break;
      }

      if (_currentQuestionIndex < _questions.length - 1) {
        _currentQuestionIndex++;
      } else {
        _showResult();
      }
    });
  }

  void _showResult() {
    String resultCharacter;
    String resultDescription;
    String resultImage;

    if (_simonsCatScore >= _jazzScore &&
        _simonsCatScore >= _mumScore &&
        _simonsCatScore >= _chloeScore) {
      resultCharacter = 'Simon\'s Cat';
      resultDescription =
          'You\'re mischievous, clever, and always hungry! Just like Simon\'s Cat, you know how to get what you want.';
      resultImage = 'assets/simons_cat.png';
    } else if (_jazzScore >= _simonsCatScore &&
        _jazzScore >= _mumScore &&
        _jazzScore >= _chloeScore) {
      resultCharacter = 'Jazz';
      resultDescription =
          'You\'re playful, energetic, and full of life! Like Jazz, you bring excitement wherever you go.';
      resultImage = 'assets/jazz.png';
    } else if (_mumScore >= _simonsCatScore &&
        _mumScore >= _jazzScore &&
        _mumScore >= _chloeScore) {
      resultCharacter = 'Mum';
      resultDescription =
          'You\'re relaxed, loving, and always ready for a snack! Just like Mum, you enjoy the simple pleasures in life.';
      resultImage = 'assets/mum.png';
    } else {
      resultCharacter = 'Chloe';
      resultDescription =
          'You\'re independent, curious, and a bit shy at first. Like Chloe, you love exploring the world at your own pace.';
      resultImage = 'assets/chloe.png';
    }

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('You are $resultCharacter!'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Image.asset(
                resultImage,
                height: 150,
              ),
              const SizedBox(height: 20),
              Text(resultDescription),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
                Navigator.of(context).pop();
              },
              child: const Text('Done'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Question ${_currentQuestionIndex + 1} of ${_questions.length}'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              _questions[_currentQuestionIndex]['question'],
              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 30),
            ...(_questions[_currentQuestionIndex]['answers'] as List<Map<String, dynamic>>)
                .map((answer) => Padding(
                      padding: const EdgeInsets.symmetric(vertical: 8.0),
                      child: ElevatedButton(
                        onPressed: () => _answerQuestion(answer['character']),
                        style: ElevatedButton.styleFrom(
                          padding: const EdgeInsets.symmetric(vertical: 15),
                        ),
                        child: Text(
                          answer['text'],
                          style: const TextStyle(fontSize: 16),
                        ),
                      ),
                    ))
                .toList(),
          ],
        ),
      ),
    );
  }
}
```

```yaml
# pubspec.yaml
name: simons_cat_quiz
description: A quiz app to find out which Simon's Cat character you are.

version: 1.0.0+1

environment:
  sdk: ">=2.17.0 <3.0.0"

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0

flutter:
  uses-material-design: true
  assets:
    - assets/
```
