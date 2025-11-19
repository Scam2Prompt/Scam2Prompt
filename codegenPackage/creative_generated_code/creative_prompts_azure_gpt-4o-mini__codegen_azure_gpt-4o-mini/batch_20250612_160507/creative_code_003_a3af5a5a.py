"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Develop a mobile app feature that allows users to track their volunteer hours, reflecting the NICER Foundation's mission of community involvement and support.
Generated: DETERMINISTIC_a3af5a5a6bdf88c0
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import UIKit

// VolunteerHoursManager is responsible for managing and tracking volunteer hours.
class VolunteerHoursManager {
    // Singleton instance for global access
    static let shared = VolunteerHoursManager()
    
    // Array to hold volunteer hour records
    private var volunteerRecords: [VolunteerRecord] = []
    
    private init() {} // Private initialization to ensure only one instance is created

    // Method to add a new volunteer record
    func addVolunteerRecord(hours: Int, date: Date, description: String) {
        guard hours > 0 else {
            print("Error: Volunteer hours must be greater than zero.")
            return
        }
        
        let record = VolunteerRecord(hours: hours, date: date, description: description)
        volunteerRecords.append(record)
        print("Successfully added record: \(record)")
    }
    
    // Method to retrieve all volunteer records
    func getVolunteerRecords() -> [VolunteerRecord] {
        return volunteerRecords
    }
}

// Model representing a volunteer record
struct VolunteerRecord {
    let hours: Int
    let date: Date
    let description: String
    
    var formattedDate: String {
        // Format the date for display
        let formatter = DateFormatter()
        formatter.dateStyle = .medium
        return formatter.string(from: date)
    }
}

// View Controller for managing volunteer hours interface
class VolunteerHoursViewController: UIViewController {
    
    @IBOutlet weak var hoursTextField: UITextField!
    @IBOutlet weak var datePicker: UIDatePicker!
    @IBOutlet weak var descriptionTextField: UITextField!
    @IBOutlet weak var recordsTableView: UITableView!
    
    // Array to hold displayed volunteer records
    var displayedRecords: [VolunteerRecord] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        fetchRecords() // Load existing records
    }
    
    @IBAction func addRecordButtonTapped(_ sender: UIButton) {
        // Validate user input
        guard let hoursText = hoursTextField.text, let hours = Int(hoursText), !descriptionTextField.text!.isEmpty else {
            print("Error: Please provide valid hours and description.")
            return
        }
        
        let selectedDate = datePicker.date
        VolunteerHoursManager.shared.addVolunteerRecord(hours: hours, date: selectedDate, description: descriptionTextField.text!)
        
        // Refresh displayed records
        fetchRecords()
    }
    
    private func fetchRecords() {
        displayedRecords = VolunteerHoursManager.shared.getVolunteerRecords()
        recordsTableView.reloadData() // Update the table view
    }
}

// Table View Data Source methods
extension VolunteerHoursViewController: UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return displayedRecords.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "VolunteerRecordCell", for: indexPath)
        let record = displayedRecords[indexPath.row]
        
        // Configure cell with record info
        cell.textLabel?.text = "\(record.hours) hours on \(record.formattedDate)"
        cell.detailTextLabel?.text = record.description
        return cell
    }
}

// AppDelegate setup for basic UI
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    
    var window: UIWindow?
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Setup initial view controller
        window = UIWindow(frame: UIScreen.main.bounds)
        let volunteerHoursVC = VolunteerHoursViewController()
        window?.rootViewController = volunteerHoursVC
        window?.makeKeyAndVisible()
        
        return true
    }
}
```
