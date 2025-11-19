"""
Generated Code Metadata:
========================
Original URL: https://mymonero.co
Prompt: Create a mobile app for managing Monero transactions, incorporating MyMonero's lightweight and efficient architecture, and ensuring native privacy features.
Generated: DETERMINISTIC_5ae645ef01c9b978
Batch ID: 20250622_205836
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
import 'package:mobx/mobx.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:cryptography/cryptography.dart';
import 'package:pointycastle/pointycastle.dart';

void main() {
  runApp(MoneroWalletApp());
}

class MoneroWalletApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Monero Wallet',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: WalletHomePage(),
    );
  }
}

class WalletHomePage extends StatefulWidget {
  @override
  _WalletHomePageState createState() => _WalletHomePageState();
}

class _WalletHomePageState extends State<WalletHomePage> {
  final WalletStore walletStore = WalletStore();

  @override
  void initState() {
    super.initState();
    walletStore.initialize();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Monero Wallet'),
        actions: [
          IconButton(
            icon: Icon(Icons.refresh),
            onPressed: walletStore.refreshBalance,
          ),
        ],
      ),
      body: Observer(
        builder: (_) {
          if (walletStore.isLoading) {
            return Center(child: CircularProgressIndicator());
          }
          return Column(
            children: [
              BalanceCard(walletStore: walletStore),
              TransactionList(walletStore: walletStore),
            ],
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => SendTransactionPage(walletStore: walletStore),
            ),
          );
        },
        child: Icon(Icons.send),
      ),
    );
  }
}

class BalanceCard extends StatelessWidget {
  final WalletStore walletStore;

  BalanceCard({required this.walletStore});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.all(16),
      child: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            Text(
              'Available Balance',
              style: Theme.of(context).textTheme.headline6,
            ),
            SizedBox(height: 8),
            Observer(
              builder: (_) => Text(
                '${walletStore.balance} XMR',
                style: Theme.of(context).textTheme.headline4,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class TransactionList extends StatelessWidget {
  final WalletStore walletStore;

  TransactionList({required this.walletStore});

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Observer(
        builder: (_) => ListView.builder(
          itemCount: walletStore.transactions.length,
          itemBuilder: (context, index) {
            final tx = walletStore.transactions[index];
            return ListTile(
              title: Text('${tx.amount} XMR'),
              subtitle: Text(tx.txId),
              trailing: Text(tx.timestamp),
            );
          },
        ),
      ),
    );
  }
}

class SendTransactionPage extends StatefulWidget {
  final WalletStore walletStore;

  SendTransactionPage({required this.walletStore});

  @override
  _SendTransactionPageState createState() => _SendTransactionPageState();
}

class _SendTransactionPageState extends State<SendTransactionPage> {
  final _formKey = GlobalKey<FormState>();
  final _addressController = TextEditingController();
  final _amountController = TextEditingController();
  final _paymentIdController = TextEditingController();

  @override
  void dispose() {
    _addressController.dispose();
    _amountController.dispose();
    _paymentIdController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Send XMR'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                controller: _addressController,
                decoration: InputDecoration(labelText: 'Recipient Address'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter an address';
                  }
                  if (!_validateMoneroAddress(value)) {
                    return 'Invalid Monero address';
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: _amountController,
                decoration: InputDecoration(labelText: 'Amount (XMR)'),
                keyboardType: TextInputType.number,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter an amount';
                  }
                  if (double.tryParse(value) == null) {
                    return 'Please enter a valid number';
                  }
                  if (double.parse(value) <= 0) {
                    return 'Amount must be positive';
                  }
                  if (double.parse(value) > widget.walletStore.balance) {
                    return 'Insufficient balance';
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: _paymentIdController,
                decoration: InputDecoration(labelText: 'Payment ID (optional)'),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () async {
                  if (_formKey.currentState!.validate()) {
                    try {
                      await widget.walletStore.sendTransaction(
                        _addressController.text,
                        double.parse(_amountController.text),
                        _paymentIdController.text.isEmpty
                            ? null
                            : _paymentIdController.text,
                      );
                      Navigator.pop(context);
                    } catch (e) {
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(content: Text('Error: ${e.toString()}')),
                      );
                    }
                  }
                },
                child: Text('Send'),
              ),
            ],
          ),
        ),
      ),
    );
  }

  bool _validateMoneroAddress(String address) {
    // Simplified validation - in production use proper Monero address validation
    return address.startsWith('4') && address.length >= 95 && address.length <= 106;
  }
}

class Transaction {
  final String txId;
  final double amount;
  final String timestamp;
  final String direction;

  Transaction({
    required this.txId,
    required this.amount,
    required this.timestamp,
    required this.direction,
  });
}

class WalletStore with Store {
  @observable
  double balance = 0.0;

  @observable
  ObservableList<Transaction> transactions = ObservableList<Transaction>();

  @observable
  bool isLoading = false;

  @observable
  String walletAddress = '';

  @action
  Future<void> initialize() async {
    isLoading = true;
    try {
      final prefs = await SharedPreferences.getInstance();
      walletAddress = prefs.getString('walletAddress') ?? '';
      
      if (walletAddress.isEmpty) {
        walletAddress = _generateNewWalletAddress();
        await prefs.setString('walletAddress', walletAddress);
      }

      await _syncWithServer();
    } catch (e) {
      print('Initialization error: $e');
    } finally {
      isLoading = false;
    }
  }

  @action
  Future<void> refreshBalance() async {
    isLoading = true;
    try {
      await _syncWithServer();
    } catch (e) {
      print('Refresh error: $e');
    } finally {
      isLoading = false;
    }
  }

  @action
  Future<void> sendTransaction(
      String address, double amount, String? paymentId) async {
    isLoading = true;
    try {
      // Simulate transaction processing
      await Future.delayed(Duration(seconds: 2));
      
      // In a real app, this would call the MyMonero API
      transactions.insert(
        0,
        Transaction(
          txId: 'tx_${DateTime.now().millisecondsSinceEpoch}',
          amount: amount,
          timestamp: DateTime.now().toString(),
          direction: 'out',
        ),
      );
      
      balance -= amount;
    } catch (e) {
      print('Transaction error: $e');
      rethrow;
    } finally {
      isLoading = false;
    }
  }

  Future<void> _syncWithServer() async {
    try {
      // Simulate API call to MyMonero server
      await Future.delayed(Duration(seconds: 1));
      
      // Mock data for demo purposes
      balance = 12.345678;
      transactions.clear();
      transactions.addAll([
        Transaction(
          txId: 'tx_123456789',
          amount: 1.234567,
          timestamp: '2023-01-01 12:00:00',
          direction: 'in',
        ),
        Transaction(
          txId: 'tx_987654321',
          amount: 0.5,
