"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://klar-sehen.ch
Prompt: Write code in Swift for an iOS app that includes features like eye massage tutorials and guided relaxation exercises, based on the holistic eye therapy methods from Klar Sehen.
Generated: DETERMINISTIC_fb5bee2b0cb6034b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import UIKit

// MARK: - Constants
struct Constants {
    static let appTitle = "Klar Sehen Eye Therapy"
    static let tutorialVideos = [
        "Eye Massage Tutorial 1",
        "Guided Relaxation Exercise 1",
        "Eye Massage Tutorial 2",
        "Guided Relaxation Exercise 2"
    ]
}

// MARK: - Main View Controller
class MainViewController: UIViewController {

    // UI Elements
    private let tableView = UITableView()

    // MARK: - Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }

    // MARK: - UI Setup
    private func setupUI() {
        title = Constants.appTitle
        view.backgroundColor = .white
        
        // Set up table view
        tableView.delegate = self
        tableView.dataSource = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
        
        // Add table view to the main view
        view.addSubview(tableView)
        tableView.translatesAutoresizingMaskIntoConstraints = false
        
        // Layout constraints
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor)
        ])
    }
}

// MARK: - UITableViewDataSource
extension MainViewController: UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return Constants.tutorialVideos.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        cell.textLabel?.text = Constants.tutorialVideos[indexPath.row]
        return cell
    }
}

// MARK: - UITableViewDelegate
extension MainViewController: UITableViewDelegate {
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        // Handle tutorial selection
        let selectedTutorial = Constants.tutorialVideos[indexPath.row]
        showTutorialDetail(tutorialName: selectedTutorial)
        tableView.deselectRow(at: indexPath, animated: true)
    }
    
    private func showTutorialDetail(tutorialName: String) {
        // Present tutorial detail view controller
        let detailVC = TutorialDetailViewController(tutorialName: tutorialName)
        navigationController?.pushViewController(detailVC, animated: true)
    }
}

// MARK: - Tutorial Detail View Controller
class TutorialDetailViewController: UIViewController {
    
    var tutorialName: String
    
    // MARK: - Initializer
    init(tutorialName: String) {
        self.tutorialName = tutorialName
        super.init(nibName: nil, bundle: nil)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    // UI Elements
    private let titleLabel = UILabel()
    
    // MARK: - Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }

    // MARK: - UI Setup
    private func setupUI() {
        view.backgroundColor = .white
        
        titleLabel.text = tutorialName
        titleLabel.font = UIFont.systemFont(ofSize: 24, weight: .bold)
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        
        view.addSubview(titleLabel)
        
        // Layout constraints
        NSLayoutConstraint.activate([
            titleLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    }
}

// MARK: - AppDelegate
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    
    var window: UIWindow?

    // MARK: - Application Entry Point
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        window = UIWindow(frame: UIScreen.main.bounds)
        let mainVC = MainViewController()
        let navigationController = UINavigationController(rootViewController: mainVC)
        window?.rootViewController = navigationController
        window?.makeKeyAndVisible()
        return true
    }
}
```
