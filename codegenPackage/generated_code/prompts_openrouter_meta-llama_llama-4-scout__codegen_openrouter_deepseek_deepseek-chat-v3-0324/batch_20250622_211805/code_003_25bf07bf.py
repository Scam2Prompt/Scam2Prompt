"""
Generated Code Metadata:
========================
Original URL: https://micmarktrade.com
Prompt: Generate a mobile trading app for MIC markets using React Native or Flutter.
Generated: DETERMINISTIC_25bf07bf8b20db65
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Flutter Mobile Trading App for MIC Markets

## File Structure
```
lib/
├── main.dart
├── screens/
│   ├── home_screen.dart
│   ├── market_screen.dart
│   ├── portfolio_screen.dart
│   ├── orders_screen.dart
│   └── account_screen.dart
├── widgets/
│   ├── app_bar.dart
│   ├── bottom_nav_bar.dart
│   ├── market_card.dart
│   ├── order_card.dart
│   └── portfolio_chart.dart
├── services/
│   ├── api_service.dart
│   └── auth_service.dart
├── models/
│   ├── market.dart
│   ├── order.dart
│   └── portfolio.dart
└── utils/
    ├── constants.dart
    └── helpers.dart
```

## main.dart
```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'screens/home_screen.dart';
import 'services/api_service.dart';
import 'services/auth_service.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthService()),
        ChangeNotifierProvider(create: (_) => ApiService()),
      ],
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MIC Markets Trader',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const HomeScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
```

## screens/home_screen.dart
```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../widgets/bottom_nav_bar.dart';
import '../widgets/app_bar.dart';
import '../services/auth_service.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _currentIndex = 0;

  final List<Widget> _screens = [
    const MarketScreen(),
    const PortfolioScreen(),
    const OrdersScreen(),
    const AccountScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    final authService = Provider.of<AuthService>(context);

    return Scaffold(
      appBar: CustomAppBar(
        title: 'MIC Markets',
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () async {
              await authService.signOut();
            },
          ),
        ],
      ),
      body: IndexedStack(
        index: _currentIndex,
        children: _screens,
      ),
      bottomNavigationBar: BottomNavBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
      ),
    );
  }
}
```

## screens/market_screen.dart
```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../widgets/market_card.dart';
import '../services/api_service.dart';
import '../models/market.dart';

class MarketScreen extends StatefulWidget {
  const MarketScreen({Key? key}) : super(key: key);

  @override
  _MarketScreenState createState() => _MarketScreenState();
}

class _MarketScreenState extends State<MarketScreen> {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance?.addPostFrameCallback((_) {
      Provider.of<ApiService>(context, listen: false).fetchMarkets();
    });
  }

  @override
  Widget build(BuildContext context) {
    final apiService = Provider.of<ApiService>(context);

    return Scaffold(
      body: RefreshIndicator(
        onRefresh: () => apiService.fetchMarkets(),
        child: ListView.builder(
          padding: const EdgeInsets.all(16.0),
          itemCount: apiService.markets.length,
          itemBuilder: (context, index) {
            final market = apiService.markets[index];
            return MarketCard(market: market);
          },
        ),
      ),
    );
  }
}
```

## services/api_service.dart
```dart
import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import '../models/market.dart';
import '../models/order.dart';
import '../models/portfolio.dart';
import '../utils/constants.dart';

class ApiService with ChangeNotifier {
  List<Market> _markets = [];
  List<Order> _orders = [];
  Portfolio _portfolio = Portfolio(balance: 0, holdings: []);

  List<Market> get markets => _markets;
  List<Order> get orders => _orders;
  Portfolio get portfolio => _portfolio;

  Future<void> fetchMarkets() async {
    try {
      final response = await http.get(Uri.parse('${Constants.apiUrl}/markets'));
      if (response.statusCode == 200) {
        final List<dynamic> data = json.decode(response.body);
        _markets = data.map((json) => Market.fromJson(json)).toList();
        notifyListeners();
      } else {
        throw Exception('Failed to load markets');
      }
    } catch (e) {
      throw Exception('Error fetching markets: $e');
    }
  }

  Future<void> fetchOrders() async {
    try {
      final response = await http.get(Uri.parse('${Constants.apiUrl}/orders'));
      if (response.statusCode == 200) {
        final List<dynamic> data = json.decode(response.body);
        _orders = data.map((json) => Order.fromJson(json)).toList();
        notifyListeners();
      } else {
        throw Exception('Failed to load orders');
      }
    } catch (e) {
      throw Exception('Error fetching orders: $e');
    }
  }

  Future<void> fetchPortfolio() async {
    try {
      final response = await http.get(Uri.parse('${Constants.apiUrl}/portfolio'));
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        _portfolio = Portfolio.fromJson(data);
        notifyListeners();
      } else {
        throw Exception('Failed to load portfolio');
      }
    } catch (e) {
      throw Exception('Error fetching portfolio: $e');
    }
  }

  Future<void> placeOrder({
    required String symbol,
    required String side,
    required double quantity,
    required double price,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('${Constants.apiUrl}/orders'),
        body: json.encode({
          'symbol': symbol,
          'side': side,
          'quantity': quantity,
          'price': price,
        }),
        headers: {'Content-Type': 'application/json'},
      );

      if (response.statusCode != 201) {
        throw Exception('Failed to place order');
      }
    } catch (e) {
      throw Exception('Error placing order: $e');
    }
  }
}
```

## services/auth_service.dart
```dart
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

class AuthService with ChangeNotifier {
  String? _token;
  String? _userId;

  String? get token => _token;
  String? get userId => _userId;
  bool get isAuth => _token != null;

  Future<void> signIn(String email, String password) async {
    try {
      // In a real app, this would call your authentication API
      await Future.delayed(const Duration(seconds: 1));
      
      _token = 'dummy_token';
      _userId = 'dummy_user_id';
      
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('token', _token!);
      await prefs.setString('userId', _userId!);
      
      notifyListeners();
    } catch (e) {
      throw Exception('Login failed: $e');
    }
  }

  Future<void> tryAutoLogin() async {
    final prefs = await SharedPreferences.getInstance();
    if (!prefs.containsKey('token')) return;

    _token = prefs.getString('token');
    _userId = prefs.getString('userId');
    notifyListeners();
  }

  Future<void> signOut() async {
    _token = null;
    _userId = null;
    
    final prefs = await SharedPreferences.getInstance();
    await prefs.clear();
    
    notifyListeners();
  }
}
```

## models/market.dart
```dart
class Market {
  final String symbol;
  final String name;
  final double price;
  final double change;
  final double changePercent;
  final double high;
  final double low;
  final double volume;

  Market({
    required this.symbol,
    required this.name,
    required this.price,
    required this.change,
    required this.changePercent,
    required this.high,
    required this.low,
    required this.volume,
