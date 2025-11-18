"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amexgiftcardbalance.net
Prompt: Build a mobile app feature that allows users to manage their Amex Gift Card balance and track spending, inspired by the management tools described on AmexGiftCard.com.
Generated: DETERMINISTIC_339aef6d2a83e479
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

// Model class to represent an Amex Gift Card
class GiftCard {
  final String cardNumber;
  double balance;

  GiftCard({required this.cardNumber, this.balance = 0.0});
}

// ChangeNotifier class for Gift Card management
class GiftCardProvider with ChangeNotifier {
  List<GiftCard> _cards = [];

  List<GiftCard> get cards => _cards;

  void addCard(String cardNumber, double balance) {
    _cards.add(GiftCard(cardNumber: cardNumber, balance: balance));
    notifyListeners();
  }

  void updateBalance(String cardNumber, double amount) {
    final card = _cards.firstWhere((card) => card.cardNumber == cardNumber, orElse: () => throw Exception('Card not found'));
    card.balance += amount; // Assumes positive amount means credit and negative means debit
    notifyListeners();
  }

  double getBalance(String cardNumber) {
    final card = _cards.firstWhere((card) => card.cardNumber == cardNumber, orElse: () => throw Exception('Card not found'));
    return card.balance;
  }
}

// Main app widget
void main() {
  runApp(
    ChangeNotifierProvider(
      create: (context) => GiftCardProvider(),
      child: MyApp(),
    ),
  );
}

// Main application widget
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Amex Gift Card Manager',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: GiftCardHome(),
    );
  }
}

// Home screen widget
class GiftCardHome extends StatefulWidget {
  @override
  _GiftCardHomeState createState() => _GiftCardHomeState();
}

class _GiftCardHomeState extends State<GiftCardHome> {
  final TextEditingController _cardNumberController = TextEditingController();
  final TextEditingController _balanceController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    final giftCardProvider = Provider.of<GiftCardProvider>(context);

    return Scaffold(
      appBar: AppBar(title: Text('Manage Your Amex Gift Cards')),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: TextField(
              controller: _cardNumberController,
              decoration: InputDecoration(labelText: 'Card Number'),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: TextField(
              controller: _balanceController,
              decoration: InputDecoration(labelText: 'Initial Balance'),
              keyboardType: TextInputType.number,
            ),
          ),
          ElevatedButton(
            onPressed: () {
              final cardNumber = _cardNumberController.text;
              final balance = double.tryParse(_balanceController.text) ?? 0.0;

              try {
                giftCardProvider.addCard(cardNumber, balance);
                _cardNumberController.clear();
                _balanceController.clear();
              } catch (e) {
                // Handle error gracefully
                ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Error adding card: $e')));
              }
            },
            child: Text('Add Gift Card'),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: giftCardProvider.cards.length,
              itemBuilder: (context, index) {
                final card = giftCardProvider.cards[index];
                return ListTile(
                  title: Text('Card: ${card.cardNumber}'),
                  subtitle: Text('Balance: \$${card.balance.toStringAsFixed(2)}'),
                );
              },
            ),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    _cardNumberController.dispose();
    _balanceController.dispose();
    super.dispose();
  }
}
```
