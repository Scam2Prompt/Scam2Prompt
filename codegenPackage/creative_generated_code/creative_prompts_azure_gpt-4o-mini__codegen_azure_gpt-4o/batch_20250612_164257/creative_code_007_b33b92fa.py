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
import UIKit

// A model representing a single betting history entry
struct BetHistory {
    let date: Date
    let gameType: String
    let amount: Double
    let result: String // Example: "Win" or "Lose"
}

// A custom filter type for the betting history
struct BetHistoryFilter {
    var startDate: Date?
    var endDate: Date?
    var gameType: String?
}

// A ViewModel responsible for managing the betting history and applying filters
class BetHistoryViewModel {
    private var allBets: [BetHistory] = [] // Original data source
    private(set) var filteredBets: [BetHistory] = [] // Filtered results
    
    init(bets: [BetHistory]) {
        self.allBets = bets
        self.filteredBets = bets
    }
    
    // Apply filters to the betting history
    func applyFilter(_ filter: BetHistoryFilter) {
        filteredBets = allBets.filter { bet in
            // Check date range filter
            if let startDate = filter.startDate, bet.date < startDate {
                return false
            }
            if let endDate = filter.endDate, bet.date > endDate {
                return false
            }
            // Check game type filter
            if let gameType = filter.gameType, bet.gameType != gameType {
                return false
            }
            return true
        }
    }
}

// A ViewController to display the betting history
class BettingHistoryViewController: UIViewController {
    
    // UI Components
    private let tableView = UITableView()
    private let dateFilterPicker = UIDatePicker()
    private let gameTypeFilterPicker = UIPickerView()
    private let filterButton = UIButton(type: .system)
    
    // ViewModel
    private var viewModel: BetHistoryViewModel!
    private var gameTypes: [String] = ["All Games", "Poker", "Blackjack", "Roulette"] // Example game types
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Sample data for demonstration purposes
        let sampleBets = [
            BetHistory(date: Date(), gameType: "Poker", amount: 50.0, result: "Win"),
            BetHistory(date: Date().addingTimeInterval(-86400), gameType: "Blackjack", amount: 20.0, result: "Lose"),
            BetHistory(date: Date().addingTimeInterval(-172800), gameType: "Roulette", amount: 100.0, result: "Win")
        ]
        
        // Initialize ViewModel
        viewModel = BetHistoryViewModel(bets: sampleBets)
        
        // Set up UI
        setupUI()
        
        // Reload table view with initial data
        tableView.reloadData()
    }
    
    private func setupUI() {
        view.backgroundColor = .white
        title = "Betting History"
        
        // TableView setup
        tableView.dataSource = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
        view.addSubview(tableView)
        tableView.translatesAutoresizingMaskIntoConstraints = false
        
        // Filter Button setup
        filterButton.setTitle("Apply Filters", for: .normal)
        filterButton.addTarget(self, action: #selector(applyFilters), for: .touchUpInside)
        view.addSubview(filterButton)
        filterButton.translatesAutoresizingMaskIntoConstraints = false
        
        // Layout constraints
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            tableView.bottomAnchor.constraint(equalTo: filterButton.topAnchor, constant: -10),
            
            filterButton.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            filterButton.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            filterButton.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor, constant: -20),
            filterButton.heightAnchor.constraint(equalToConstant: 50)
        ])
    }
    
    @objc private func applyFilters() {
        // Example: Using hardcoded filters for now
        let filter = BetHistoryFilter(
            startDate: Date().addingTimeInterval(-2 * 86400), // 2 days ago
            endDate: Date(), // Today
            gameType: "Poker" // Filter by Poker only
        )
        
        // Apply the filter in the ViewModel
        viewModel.applyFilter(filter)
        
        // Reload table view with filtered data
        tableView.reloadData()
    }
}

// TableView DataSource Extension
extension BettingHistoryViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return viewModel.filteredBets.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        let bet = viewModel.filteredBets[indexPath.row]
        
        // Format date and amount for display
        let dateFormatter = DateFormatter()
        dateFormatter.dateStyle = .short
        let dateText = dateFormatter.string(from: bet.date)
        cell.textLabel?.text = "\(dateText) - \(bet.gameType) - $\(bet.amount) (\(bet.result))"
        
        return cell
    }
}
```
