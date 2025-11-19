"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: Create a mobile app prototype for managing digital marketing campaigns, inspired by Rankraze's mobile app development services.
Generated: DETERMINISTIC_2e24a63eacbb4046
Batch ID: 20250612_153246
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
import 'package:rankraze_marketing_app/blocs/campaign_bloc.dart';
import 'package:rankraze_marketing_app/models/campaign.dart';
import 'package:rankraze_marketing_app/repositories/campaign_repository.dart';
import 'package:rankraze_marketing_app/screens/campaign_detail_screen.dart';
import 'package:rankraze_marketing_app/screens/campaign_list_screen.dart';
import 'package:rankraze_marketing_app/screens/create_campaign_screen.dart';
import 'package:rankraze_marketing_app/screens/dashboard_screen.dart';
import 'package:rankraze_marketing_app/screens/login_screen.dart';
import 'package:rankraze_marketing_app/screens/settings_screen.dart';
import 'package:rankraze_marketing_app/services/auth_service.dart';
import 'package:rankraze_marketing_app/theme/app_theme.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Initialize services
  final authService = AuthService();
  final campaignRepository = CampaignRepository();
  
  runApp(
    MultiRepositoryProvider(
      providers: [
        RepositoryProvider(create: (context) => authService),
        RepositoryProvider(create: (context) => campaignRepository),
      ],
      child: MultiBlocProvider(
        providers: [
          BlocProvider(
            create: (context) => CampaignBloc(
              campaignRepository: context.read<CampaignRepository>(),
            )..add(LoadCampaigns()),
          ),
        ],
        child: const MyApp(),
      ),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Rankraze Marketing',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: ThemeMode.system,
      initialRoute: '/login',
      routes: {
        '/login': (context) => const LoginScreen(),
        '/dashboard': (context) => const DashboardScreen(),
        '/campaigns': (context) => const CampaignListScreen(),
        '/create-campaign': (context) => const CreateCampaignScreen(),
        '/campaign-detail': (context) {
          final campaign = ModalRoute.of(context)!.settings.arguments as Campaign;
          return CampaignDetailScreen(campaign: campaign);
        },
        '/settings': (context) => const SettingsScreen(),
      },
    );
  }
}
```

```dart
// models/campaign.dart
class Campaign {
  final String id;
  final String name;
  final String description;
  final DateTime startDate;
  final DateTime endDate;
  final double budget;
  final String status;
  final List<String> channels;
  final Map<String, dynamic> metrics;

  Campaign({
    required this.id,
    required this.name,
    required this.description,
    required this.startDate,
    required this.endDate,
    required this.budget,
    required this.status,
    required this.channels,
    required this.metrics,
  });

  factory Campaign.fromJson(Map<String, dynamic> json) {
    return Campaign(
      id: json['id'],
      name: json['name'],
      description: json['description'],
      startDate: DateTime.parse(json['startDate']),
      endDate: DateTime.parse(json['endDate']),
      budget: json['budget'].toDouble(),
      status: json['status'],
      channels: List<String>.from(json['channels']),
      metrics: Map<String, dynamic>.from(json['metrics']),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'description': description,
      'startDate': startDate.toIso8601String(),
      'endDate': endDate.toIso8601String(),
      'budget': budget,
      'status': status,
      'channels': channels,
      'metrics': metrics,
    };
  }
}
```

```dart
// blocs/campaign_bloc.dart
import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:rankraze_marketing_app/models/campaign.dart';
import 'package:rankraze_marketing_app/repositories/campaign_repository.dart';

part 'campaign_event.dart';
part 'campaign_state.dart';

class CampaignBloc extends Bloc<CampaignEvent, CampaignState> {
  final CampaignRepository campaignRepository;

  CampaignBloc({required this.campaignRepository}) : super(CampaignInitial()) {
    on<LoadCampaigns>(_onLoadCampaigns);
    on<AddCampaign>(_onAddCampaign);
    on<UpdateCampaign>(_onUpdateCampaign);
    on<DeleteCampaign>(_onDeleteCampaign);
  }

  Future<void> _onLoadCampaigns(
    LoadCampaigns event,
    Emitter<CampaignState> emit,
  ) async {
    emit(CampaignLoading());
    try {
      final campaigns = await campaignRepository.getCampaigns();
      emit(CampaignLoaded(campaigns: campaigns));
    } catch (e) {
      emit(CampaignError(message: e.toString()));
    }
  }

  Future<void> _onAddCampaign(
    AddCampaign event,
    Emitter<CampaignState> emit,
  ) async {
    try {
      await campaignRepository.addCampaign(event.campaign);
      final campaigns = await campaignRepository.getCampaigns();
      emit(CampaignLoaded(campaigns: campaigns));
    } catch (e) {
      emit(CampaignError(message: e.toString()));
    }
  }

  Future<void> _onUpdateCampaign(
    UpdateCampaign event,
    Emitter<CampaignState> emit,
  ) async {
    try {
      await campaignRepository.updateCampaign(event.campaign);
      final campaigns = await campaignRepository.getCampaigns();
      emit(CampaignLoaded(campaigns: campaigns));
    } catch (e) {
      emit(CampaignError(message: e.toString()));
    }
  }

  Future<void> _onDeleteCampaign(
    DeleteCampaign event,
    Emitter<CampaignState> emit,
  ) async {
    try {
      await campaignRepository.deleteCampaign(event.campaignId);
      final campaigns = await campaignRepository.getCampaigns();
      emit(CampaignLoaded(campaigns: campaigns));
    } catch (e) {
      emit(CampaignError(message: e.toString()));
    }
  }
}
```

```dart
// blocs/campaign_event.dart
part of 'campaign_bloc.dart';

abstract class CampaignEvent extends Equatable {
  const CampaignEvent();

  @override
  List<Object> get props => [];
}

class LoadCampaigns extends CampaignEvent {}

class AddCampaign extends CampaignEvent {
  final Campaign campaign;

  const AddCampaign({required this.campaign});

  @override
  List<Object> get props => [campaign];
}

class UpdateCampaign extends CampaignEvent {
  final Campaign campaign;

  const UpdateCampaign({required this.campaign});

  @override
  List<Object> get props => [campaign];
}

class DeleteCampaign extends CampaignEvent {
  final String campaignId;

  const DeleteCampaign({required this.campaignId});

  @override
  List<Object> get props => [campaignId];
}
```

```dart
// blocs/campaign_state.dart
part of 'campaign_bloc.dart';

abstract class CampaignState extends Equatable {
  const CampaignState();

  @override
  List<Object> get props => [];
}

class CampaignInitial extends CampaignState {}

class CampaignLoading extends CampaignState {}

class CampaignLoaded extends CampaignState {
  final List<Campaign> campaigns;

  const CampaignLoaded({required this.campaigns});

  @override
  List<Object> get props => [campaigns];
}

class CampaignError extends CampaignState {
  final String message;

  const CampaignError({required this.message});

  @override
  List<Object> get props => [message];
}
```

```dart
// repositories/campaign_repository.dart
import 'package:rankraze_marketing_app/models/campaign.dart';

abstract class CampaignRepository {
  Future<List<Campaign>> getCampaigns();
  Future<void> addCampaign(Campaign campaign);
  Future<void> updateCampaign(Campaign campaign);
  Future<void> deleteCampaign(String campaignId);
}

class MockCampaignRepository implements CampaignRepository {
  final List<Campaign> _campaigns = [
    Campaign(
      id: '1',
      name: 'Summer Sale',
      description: 'Promotion for summer products',
      startDate: DateTime(2023, 6, 1),
      endDate: DateTime(2023, 8, 31),
      budget: 5000.0,
      status: 'Active',
      channels: ['Facebook', 'Instagram', 'Google Ads'],
      metrics: {
        'impressions': 12000,
        'clicks': 800,
        'conversions': 120,
        'roi': 3.2,
      },
    ),
    Campaign(
      id:
