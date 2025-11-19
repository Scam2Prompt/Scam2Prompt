"""
Generated Code Metadata:
========================
Original URL: https://diskonin.id
Prompt: Design a user interface for a mobile application, similar to the Pulsa app, that allows users to easily deposit funds into their MAXSLOT88 account.
Generated: DETERMINISTIC_263184668495e444
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is the code for a simple mobile application user interface using Flutter (Dart). This code provides a clean and functional UI for depositing funds into a MAXSLOT88 account.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MaxSlot88App());
}

class MaxSlot88App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MAXSLOT88 Deposit',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: DepositScreen(),
    );
  }
}

class DepositScreen extends StatefulWidget {
  @override
  _DepositScreenState createState() => _DepositScreenState();
}

class _DepositScreenState extends State<DepositScreen> {
  final _formKey = GlobalKey<FormState>();
  final _accountController = TextEditingController();
  final _amountController = TextEditingController();

  @override
  void dispose() {
    _accountController.dispose();
    _amountController.dispose();
    super.dispose();
  }

  void _handleDeposit() {
    if (_formKey.currentState!.validate()) {
      // Simulate deposit process
      final account = _accountController.text;
      final amount = double.tryParse(_amountController.text);

      if (amount != null && amount > 0) {
        // Show success message
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Deposit of \$${amount.toStringAsFixed(2)} to account $account successful!')),
        );
      } else {
        // Show error message
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Invalid deposit amount.')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Deposit Funds'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Account ID input field
              TextFormField(
                controller: _accountController,
                decoration: InputDecoration(
                  labelText: 'Account ID',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your account ID';
                  }
                  return null;
                },
              ),
              SizedBox(height: 16.0),
              // Deposit amount input field
              TextFormField(
                controller: _amountController,
                decoration: InputDecoration(
                  labelText: 'Deposit Amount',
                  border: OutlineInputBorder(),
                ),
                keyboardType: TextInputType.number,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter a deposit amount';
                  }
                  final amount = double.tryParse(value);
                  if (amount == null || amount <= 0) {
                    return 'Please enter a valid deposit amount';
                  }
                  return null;
                },
              ),
              SizedBox(height: 16.0),
              // Deposit button
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: _handleDeposit,
                  child: Text('Deposit'),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

### Key Features:
1. **Account ID Input**: Allows users to enter their MAXSLOT88 account ID.
2. **Deposit Amount Input**: Validates the deposit amount to ensure it's a positive number.
3. **Error Handling**: Provides feedback for invalid inputs.
4. **Responsive UI**: Adjusts to different screen sizes.

To run this code:
1. Install Flutter SDK.
2. Create a new Flutter project.
3. Replace the `main.dart` file content with the code above.
4. Run the app using `flutter run`.
