"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Develop a mobile application feature in Swift that allows users to view their betting history on VZ99, including filters for date and game type.
Generated: DETERMINISTIC_b33b92fad1bd889e
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import SwiftUI
import Combine

// Model representing a single bet entry
struct BetEntry: Identifiable {
    let id: UUID
    let date: Date
    let gameType: String
    let amount: Double
    let result: String
}

// ViewModel to manage the betting history
class BettingHistoryViewModel: ObservableObject {
    @Published var betEntries: [BetEntry] = []
    @Published var filteredEntries: [BetEntry] = []
    
    // Properties for filtering
    @Published var selectedGameType: String = "All"
    @Published var selectedDateRange: ClosedRange<Date>?

    private var cancellables = Set<AnyCancellable>()

    init() {
        // Load sample data for demonstration
        loadSampleData()
        // Set up filtering
        setupFiltering()
    }
    
    // Load sample betting data (to be replaced with actual data fetching)
    private func loadSampleData() {
        let sampleData: [BetEntry] = [
            BetEntry(id: UUID(), date: Date(), gameType: "Football", amount: 100, result: "Win"),
            BetEntry(id: UUID(), date: Date().addingTimeInterval(-86400), gameType: "Basketball", amount: 50, result: "Loss"),
            BetEntry(id: UUID(), date: Date().addingTimeInterval(-172800), gameType: "Football", amount: 75, result: "Win")
        ]
        betEntries = sampleData
    }

    // Setup filtering based on selected values
    private func setupFiltering() {
        $selectedGameType
            .combineLatest($selectedDateRange)
            .map { [weak self] gameType, dateRange in
                self?.filterEntries(gameType: gameType, dateRange: dateRange) ?? []
            }
            .assign(to: &$filteredEntries)
    }

    // Filter the bet entries based on game type and date range
    private func filterEntries(gameType: String, dateRange: ClosedRange<Date>?) -> [BetEntry] {
        return betEntries.filter { entry in
            let isGameTypeMatch = gameType == "All" || entry.gameType == gameType
            let isDateInRange = dateRange?.contains(entry.date) ?? true
            return isGameTypeMatch && isDateInRange
        }
    }
}

// View to display betting history
struct BettingHistoryView: View {
    @StateObject private var viewModel = BettingHistoryViewModel()
    let gameTypes = ["All", "Football", "Basketball"]

    var body: some View {
        NavigationView {
            VStack {
                // Picker for game type selection
                Picker("Game Type", selection: $viewModel.selectedGameType) {
                    ForEach(gameTypes, id: \.self) { gameType in
                        Text(gameType)
                    }
                }
                .pickerStyle(SegmentedPickerStyle())
                .padding()

                // Date range picker
                DatePicker("Select Date Range", selection: Binding<Date?>(get: {
                    viewModel.selectedDateRange?.lowerBound
                }, set: { newValue in
                    if let newDate = newValue {
                        let newRange = newDate...Date()
                        viewModel.selectedDateRange = newRange
                    } else {
                        viewModel.selectedDateRange = nil
                    }
                }), displayedComponents: .date)
                .padding()

                // Displaying filtered betting history
                List(viewModel.filteredEntries) { entry in
                    HStack {
                        Text(entry.gameType)
                        Spacer()
                        Text("\(entry.amount, specifier: "%.2f")")
                        Spacer()
                        Text(entry.result)
                    }
                }
            }
            .navigationTitle("Betting History")
        }
        .onAppear {
            // Error handling for data loading can be added here
        }
    }
}

// Preview provider for SwiftUI previews
struct BettingHistoryView_Previews: PreviewProvider {
    static var previews: some View {
        BettingHistoryView()
    }
}

// Entry point for the app
@main
struct BettingApp: App {
    var body: some Scene {
        WindowGroup {
            BettingHistoryView()
        }
    }
}
```
