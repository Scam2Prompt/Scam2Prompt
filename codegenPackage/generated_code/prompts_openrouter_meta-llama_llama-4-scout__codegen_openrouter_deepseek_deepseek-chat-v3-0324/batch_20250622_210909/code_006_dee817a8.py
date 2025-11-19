"""
Generated Code Metadata:
========================
Original URL: https://memeindex-ie.web.app
Prompt: Design a user interface for a Meme Index mobile app, allowing users to buy, stake, and manage their $MEMEX tokens, as well as participate in governance and submit proposals.
Generated: DETERMINISTIC_dee817a8f46fec25
Batch ID: 20250622_210909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (context) => MemexWalletProvider(),
      child: const MemexApp(),
    ),
  );
}

class MemexApp extends StatelessWidget {
  const MemexApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Meme Index',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const MainScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int _currentIndex = 0;

  final List<Widget> _screens = [
    const WalletScreen(),
    const StakeScreen(),
    const GovernanceScreen(),
    const ProfileScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Meme Index'),
        actions: [
          IconButton(
            icon: const Icon(Icons.notifications),
            onPressed: () {
              // Navigate to notifications
            },
          ),
        ],
      ),
      body: _screens[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) => setState(() => _currentIndex = index),
        type: BottomNavigationBarType.fixed,
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.account_balance_wallet),
            label: 'Wallet',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.monetization_on),
            label: 'Stake',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.gavel),
            label: 'Governance',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: 'Profile',
          ),
        ],
      ),
    );
  }
}

class MemexWalletProvider extends ChangeNotifier {
  double _balance = 0.0;
  double _staked = 0.0;
  List<Transaction> _transactions = [];
  List<Proposal> _proposals = [];

  double get balance => _balance;
  double get staked => _staked;
  List<Transaction> get transactions => _transactions;
  List<Proposal> get proposals => _proposals;

  Future<void> buyTokens(double amount) async {
    try {
      // Simulate API call
      await Future.delayed(const Duration(seconds: 1));
      _balance += amount;
      _transactions.add(Transaction(
        amount: amount,
        type: TransactionType.buy,
        timestamp: DateTime.now(),
      ));
      notifyListeners();
    } catch (e) {
      throw Exception('Failed to buy tokens: $e');
    }
  }

  Future<void> stakeTokens(double amount) async {
    try {
      if (amount > _balance) {
        throw Exception('Insufficient balance');
      }
      // Simulate API call
      await Future.delayed(const Duration(seconds: 1));
      _balance -= amount;
      _staked += amount;
      _transactions.add(Transaction(
        amount: amount,
        type: TransactionType.stake,
        timestamp: DateTime.now(),
      ));
      notifyListeners();
    } catch (e) {
      throw Exception('Failed to stake tokens: $e');
    }
  }

  Future<void> unstakeTokens(double amount) async {
    try {
      if (amount > _staked) {
        throw Exception('Insufficient staked amount');
      }
      // Simulate API call
      await Future.delayed(const Duration(seconds: 1));
      _staked -= amount;
      _balance += amount;
      _transactions.add(Transaction(
        amount: amount,
        type: TransactionType.unstake,
        timestamp: DateTime.now(),
      ));
      notifyListeners();
    } catch (e) {
      throw Exception('Failed to unstake tokens: $e');
    }
  }

  Future<void> submitProposal(Proposal proposal) async {
    try {
      // Simulate API call
      await Future.delayed(const Duration(seconds: 1));
      _proposals.add(proposal);
      notifyListeners();
    } catch (e) {
      throw Exception('Failed to submit proposal: $e');
    }
  }

  Future<void> voteOnProposal(String proposalId, bool vote) async {
    try {
      // Simulate API call
      await Future.delayed(const Duration(seconds: 1));
      final proposal = _proposals.firstWhere((p) => p.id == proposalId);
      proposal.votes += vote ? 1 : -1;
      notifyListeners();
    } catch (e) {
      throw Exception('Failed to vote: $e');
    }
  }
}

enum TransactionType { buy, stake, unstake }

class Transaction {
  final double amount;
  final TransactionType type;
  final DateTime timestamp;

  Transaction({
    required this.amount,
    required this.type,
    required this.timestamp,
  });
}

class Proposal {
  final String id;
  final String title;
  final String description;
  final DateTime createdAt;
  int votes;

  Proposal({
    required this.id,
    required this.title,
    required this.description,
    required this.createdAt,
    this.votes = 0,
  });
}

class WalletScreen extends StatelessWidget {
  const WalletScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final wallet = Provider.of<MemexWalletProvider>(context);
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                children: [
                  const Text(
                    'Total Balance',
                    style: TextStyle(fontSize: 16, color: Colors.grey),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '${wallet.balance.toStringAsFixed(2)} MEMEX',
                    style: const TextStyle(
                      fontSize: 32,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 16),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ElevatedButton(
                        onPressed: () => _showBuyDialog(context),
                        child: const Text('Buy'),
                      ),
                      ElevatedButton(
                        onPressed: () => _showStakeDialog(context),
                        child: const Text('Stake'),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),
          const Text(
            'Recent Transactions',
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          Expanded(
            child: ListView.builder(
              itemCount: wallet.transactions.length,
              itemBuilder: (context, index) {
                final tx = wallet.transactions[index];
                return ListTile(
                  leading: Icon(
                    _getTransactionIcon(tx.type),
                    color: _getTransactionColor(tx.type),
                  ),
                  title: Text(
                    '${tx.type.toString().split('.').last}: ${tx.amount} MEMEX',
                  ),
                  subtitle: Text(
                    '${tx.timestamp.day}/${tx.timestamp.month}/${tx.timestamp.year}',
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }

  IconData _getTransactionIcon(TransactionType type) {
    switch (type) {
      case TransactionType.buy:
        return Icons.shopping_cart;
      case TransactionType.stake:
        return Icons.lock;
      case TransactionType.unstake:
        return Icons.lock_open;
    }
  }

  Color _getTransactionColor(TransactionType type) {
    switch (type) {
      case TransactionType.buy:
        return Colors.green;
      case TransactionType.stake:
        return Colors.blue;
      case TransactionType.unstake:
        return Colors.orange;
    }
  }

  void _showBuyDialog(BuildContext context) {
    final amountController = TextEditingController();
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text('Buy MEMEX Tokens'),
          content: TextField(
            controller: amountController,
            keyboardType: TextInputType.number,
            inputFormatters: [FilteringTextInputFormatter.allow(RegExp(r'^\d+\.?\d{0,2}'))],
            decoration: const InputDecoration(
              labelText: 'Amount',
              hintText: 'Enter amount to buy',
            ),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: const Text('Cancel'),
            ),
            ElevatedButton(
              onPressed: () async {
                try {
