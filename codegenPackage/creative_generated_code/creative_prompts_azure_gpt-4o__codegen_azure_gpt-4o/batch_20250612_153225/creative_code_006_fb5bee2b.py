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
import AVFoundation

// MARK: - Model for Exercise
struct Exercise {
    let title: String
    let description: String
    let audioFileName: String
}

// MARK: - ViewController for Exercises List
class ExercisesViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    private let exercises: [Exercise] = [
        Exercise(title: "Eye Massage Tutorial", description: "Learn techniques to gently massage your eyes.", audioFileName: "eyeMassage.mp3"),
        Exercise(title: "Guided Relaxation", description: "Follow this guided relaxation to reduce eye strain.", audioFileName: "guidedRelaxation.mp3")
    ]
    
    private let tableView = UITableView()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }
    
    private func setupUI() {
        // Configure ViewController
        title = "Holistic Eye Therapy"
        view.backgroundColor = .systemBackground
        
        // Configure TableView
        tableView.frame = view.bounds
        tableView.delegate = self
        tableView.dataSource = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "ExerciseCell")
        view.addSubview(tableView)
    }
    
    // MARK: - TableView DataSource Methods
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return exercises.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "ExerciseCell", for: indexPath)
        let exercise = exercises[indexPath.row]
        cell.textLabel?.text = exercise.title
        cell.textLabel?.font = UIFont.systemFont(ofSize: 16, weight: .medium)
        cell.textLabel?.numberOfLines = 0
        cell.accessoryType = .disclosureIndicator
        return cell
    }
    
    // MARK: - TableView Delegate Method
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        let selectedExercise = exercises[indexPath.row]
        let detailVC = ExerciseDetailViewController(exercise: selectedExercise)
        navigationController?.pushViewController(detailVC, animated: true)
    }
}

// MARK: - ViewController for Exercise Details
class ExerciseDetailViewController: UIViewController {
    
    private let exercise: Exercise
    private var audioPlayer: AVAudioPlayer?
    
    init(exercise: Exercise) {
        self.exercise = exercise
        super.init(nibName: nil, bundle: nil)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }
    
    private func setupUI() {
        title = exercise.title
        view.backgroundColor = .systemBackground
        
        // Description Label
        let descriptionLabel = UILabel()
        descriptionLabel.text = exercise.description
        descriptionLabel.font = UIFont.systemFont(ofSize: 16)
        descriptionLabel.numberOfLines = 0
        descriptionLabel.textAlignment = .center
        descriptionLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(descriptionLabel)
        
        // Play Button
        let playButton = UIButton(type: .system)
        playButton.setTitle("Play Audio", for: .normal)
        playButton.titleLabel?.font = UIFont.systemFont(ofSize: 18, weight: .bold)
        playButton.addTarget(self, action: #selector(playAudio), for: .touchUpInside)
        playButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(playButton)
        
        // Layout constraints
        NSLayoutConstraint.activate([
            descriptionLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            descriptionLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: -30),
            descriptionLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            descriptionLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            
            playButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            playButton.topAnchor.constraint(equalTo: descriptionLabel.bottomAnchor, constant: 20)
        ])
    }
    
    @objc private func playAudio() {
        guard let path = Bundle.main.path(forResource: exercise.audioFileName, ofType: nil) else {
            showError(message: "Audio file not found.")
            return
        }
        
        do {
            let url = URL(fileURLWithPath: path)
            audioPlayer = try AVAudioPlayer(contentsOf: url)
            audioPlayer?.play()
        } catch {
            showError(message: "Unable to play audio.")
        }
    }
    
    private func showError(message: String) {
        let alert = UIAlertController(title: "Error", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        present(alert, animated: true)
    }
}

// MARK: - App Delegate
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    
    var window: UIWindow?
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        let window = UIWindow(frame: UIScreen.main.bounds)
        let navigationController = UINavigationController(rootViewController: ExercisesViewController())
        window.rootViewController = navigationController
        window.makeKeyAndVisible()
        self.window = window
        return true
    }
}
```
