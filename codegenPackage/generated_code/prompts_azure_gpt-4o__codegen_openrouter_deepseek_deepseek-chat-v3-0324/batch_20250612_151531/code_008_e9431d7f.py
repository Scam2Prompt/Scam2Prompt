"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Develop a mobile application in Flutter that integrates with Ziber's blockchain system to enable users to make VOIP calls and earn money by acting as proxy servers.
Generated: DETERMINISTIC_e9431d7fa87055e0
Batch ID: 20250612_151531
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
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:ziber_voip/bloc/auth_bloc.dart';
import 'package:ziber_voip/bloc/call_bloc.dart';
import 'package:ziber_voip/bloc/proxy_bloc.dart';
import 'package:ziber_voip/repositories/auth_repository.dart';
import 'package:ziber_voip/repositories/blockchain_repository.dart';
import 'package:ziber_voip/repositories/call_repository.dart';
import 'package:ziber_voip/screens/auth_screen.dart';
import 'package:ziber_voip/screens/call_screen.dart';
import 'package:ziber_voip/screens/home_screen.dart';
import 'package:ziber_voip/screens/proxy_setup_screen.dart';
import 'package:ziber_voip/utils/app_router.dart';
import 'package:ziber_voip/utils/constants.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  final AppRouter _appRouter = AppRouter();

  @override
  Widget build(BuildContext context) {
    return MultiRepositoryProvider(
      providers: [
        RepositoryProvider(create: (context) => AuthRepository()),
        RepositoryProvider(create: (context) => BlockchainRepository()),
        RepositoryProvider(create: (context) => CallRepository()),
      ],
      child: MultiBlocProvider(
        providers: [
          BlocProvider(
            create: (context) => AuthBloc(
              authRepository: context.read<AuthRepository>(),
              blockchainRepository: context.read<BlockchainRepository>(),
            ),
          ),
          BlocProvider(
            create: (context) => CallBloc(
              callRepository: context.read<CallRepository>(),
              blockchainRepository: context.read<BlockchainRepository>(),
            ),
          ),
          BlocProvider(
            create: (context) => ProxyBloc(
              blockchainRepository: context.read<BlockchainRepository>(),
            ),
          ),
        ],
        child: MaterialApp(
          title: 'Ziber VOIP',
          theme: ThemeData(
            primarySwatch: Colors.blue,
            visualDensity: VisualDensity.adaptivePlatformDensity,
          ),
          onGenerateRoute: _appRouter.onGenerateRoute,
          initialRoute: AuthScreen.routeName,
          debugShowCheckedModeBanner: false,
        ),
      ),
    );
  }
}
```

```dart
// app_router.dart
import 'package:flutter/material.dart';
import 'package:ziber_voip/screens/auth_screen.dart';
import 'package:ziber_voip/screens/call_screen.dart';
import 'package:ziber_voip/screens/home_screen.dart';
import 'package:ziber_voip/screens/proxy_setup_screen.dart';

class AppRouter {
  Route onGenerateRoute(RouteSettings settings) {
    switch (settings.name) {
      case AuthScreen.routeName:
        return MaterialPageRoute(builder: (_) => AuthScreen());
      case HomeScreen.routeName:
        return MaterialPageRoute(builder: (_) => HomeScreen());
      case CallScreen.routeName:
        final args = settings.arguments as CallScreenArguments;
        return MaterialPageRoute(
          builder: (_) => CallScreen(
            callId: args.callId,
            isInitiator: args.isInitiator,
          ),
        );
      case ProxySetupScreen.routeName:
        return MaterialPageRoute(builder: (_) => ProxySetupScreen());
      default:
        return MaterialPageRoute(
          builder: (_) => Scaffold(
            body: Center(
              child: Text('No route defined for ${settings.name}'),
            ),
          ),
        );
    }
  }
}
```

```dart
// screens/auth_screen.dart
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:ziber_voip/bloc/auth_bloc.dart';
import 'package:ziber_voip/utils/constants.dart';

class AuthScreen extends StatelessWidget {
  static const routeName = '/auth';

  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Ziber VOIP - Login')),
      body: BlocConsumer<AuthBloc, AuthState>(
        listener: (context, state) {
          if (state is AuthError) {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text(state.message)),
            );
          }
        },
        builder: (context, state) {
          if (state is AuthLoading) {
            return Center(child: CircularProgressIndicator());
          }
          return Padding(
            padding: const EdgeInsets.all(16.0),
            child: Form(
              key: _formKey,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  TextFormField(
                    controller: _emailController,
                    decoration: InputDecoration(labelText: 'Email'),
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter your email';
                      }
                      return null;
                    },
                  ),
                  SizedBox(height: 16),
                  TextFormField(
                    controller: _passwordController,
                    decoration: InputDecoration(labelText: 'Password'),
                    obscureText: true,
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter your password';
                      }
                      return null;
                    },
                  ),
                  SizedBox(height: 32),
                  ElevatedButton(
                    onPressed: () {
                      if (_formKey.currentState!.validate()) {
                        context.read<AuthBloc>().add(
                              LoginWithEmailAndPassword(
                                email: _emailController.text,
                                password: _passwordController.text,
                              ),
                            );
                      }
                    },
                    child: Text('Login'),
                  ),
                  SizedBox(height: 16),
                  TextButton(
                    onPressed: () {
                      context.read<AuthBloc>().add(RegisterWithBlockchain());
                    },
                    child: Text('Register with Blockchain'),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }
}
```

```dart
// screens/home_screen.dart
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:ziber_voip/bloc/auth_bloc.dart';
import 'package:ziber_voip/bloc/call_bloc.dart';
import 'package:ziber_voip/bloc/proxy_bloc.dart';
import 'package:ziber_voip/screens/call_screen.dart';
import 'package:ziber_voip/screens/proxy_setup_screen.dart';
import 'package:ziber_voip/utils/constants.dart';

class HomeScreen extends StatelessWidget {
  static const routeName = '/home';

  final _recipientController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Ziber VOIP'),
        actions: [
          IconButton(
            icon: Icon(Icons.logout),
            onPressed: () {
              context.read<AuthBloc>().add(Logout());
            },
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _recipientController,
              decoration: InputDecoration(
                labelText: 'Recipient Address',
                hintText: 'Enter blockchain address',
              ),
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                final recipient = _recipientController.text;
                if (recipient.isNotEmpty) {
                  context.read<CallBloc>().add(InitiateCall(recipient));
                }
              },
              child: Text('Start Call'),
            ),
            SizedBox(height: 32),
            BlocBuilder<ProxyBloc, ProxyState>(
              builder: (context, state) {
                return Column(
                  children: [
                    Text(
                      'Proxy Server Status: ${state is ProxyActive ? 'Active' : 'Inactive'}',
                      style: TextStyle(fontSize: 18),
                    ),
                    SizedBox(height: 16),
                    ElevatedButton(
                      onPressed: () {
                        Navigator.pushNamed(
                          context,
                          ProxySetupScreen.routeName,
                        );
                      },
                      child: Text('Configure Proxy'),
                    ),
                  ],
                );
              },
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _recipientController.dispose();
    super.dispose();
  }
}
```

```dart
// screens/call_screen.dart
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:ziber_voip/bloc/call_bloc.dart';

class CallScreenArguments {
  final String callId;
  final bool isInitiator;

  CallScreenArguments({
    required this.call
