"""
Generated Code Metadata:
========================
Original URL: https://appadvice.com
Prompt: "Write code for a simple iOS app that provides local multiplayer game features similar to those reviewed on AppAdvice."
Generated: DETERMINISTIC_9c4a11ef98a5eb9a
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```swift
import UIKit
import GameKit

class ViewController: UIViewController, GKLocalPlayerListener {
    
    // MARK: - Properties
    private let game = Game()
    private var localPlayer: GKLocalPlayer = GKLocalPlayer.local
    
    // UI Elements
    private let statusLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.font = UIFont.systemFont(ofSize: 18, weight: .semibold)
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    private let startButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("Start Game", for: .normal)
        button.titleLabel?.font = UIFont.systemFont(ofSize: 20, weight: .bold)
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()
    
    private let inviteButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("Invite Friends", for: .normal)
        button.titleLabel?.font = UIFont.systemFont(ofSize: 20, weight: .bold)
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()
    
    // MARK: - Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        authenticateLocalPlayer()
    }
    
    // MARK: - UI Setup
    private func setupUI() {
        view.backgroundColor = .white
        
        let stackView = UIStackView(arrangedSubviews: [statusLabel, startButton, inviteButton])
        stackView.axis = .vertical
        stackView.spacing = 20
        stackView.translatesAutoresizingMaskIntoConstraints = false
        
        view.addSubview(stackView)
        
        NSLayoutConstraint.activate([
            stackView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            stackView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            stackView.widthAnchor.constraint(equalToConstant: 200)
        ])
        
        startButton.addTarget(self, action: #selector(startGame), for: .touchUpInside)
        inviteButton.addTarget(self, action: #selector(showInviteUI), for: .touchUpInside)
    }
    
    // MARK: - GameKit Authentication
    private func authenticateLocalPlayer() {
        localPlayer.authenticateHandler = { [weak self] viewController, error in
            guard let self = self else { return }
            
            if let viewController = viewController {
                self.present(viewController, animated: true)
                return
            }
            
            if let error = error {
                self.statusLabel.text = "Authentication failed: \(error.localizedDescription)"
                return
            }
            
            self.statusLabel.text = "Welcome, \(self.localPlayer.displayName)"
            self.localPlayer.register(self)
        }
    }
    
    // MARK: - Game Actions
    @objc private func startGame() {
        game.start()
        statusLabel.text = "Game started!"
    }
    
    @objc private func showInviteUI() {
        let request = GKMatchRequest()
        request.minPlayers = 2
        request.maxPlayers = 4
        
        let vc = GKMatchmakerViewController(matchRequest: request)
        vc?.matchmakerDelegate = self
        present(vc!, animated: true)
    }
}

// MARK: - GameKit Delegate Extensions
extension ViewController: GKMatchmakerViewControllerDelegate {
    func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFind match: GKMatch) {
        viewController.dismiss(animated: true)
        statusLabel.text = "Match found! Starting game..."
        game.startMultiplayer(match: match)
    }
    
    func matchmakerViewControllerWasCancelled(_ viewController: GKMatchmakerViewController) {
        viewController.dismiss(animated: true)
        statusLabel.text = "Matchmaking cancelled"
    }
    
    func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFailWithError error: Error) {
        viewController.dismiss(animated: true)
        statusLabel.text = "Matchmaking failed: \(error.localizedDescription)"
    }
}

// MARK: - Game Model
class Game {
    private var match: GKMatch?
    
    func start() {
        // Single player game logic
    }
    
    func startMultiplayer(match: GKMatch) {
        self.match = match
        // Multiplayer game logic
    }
    
    func sendDataToPlayers(_ data: Data) {
        do {
            try match?.sendData(toAllPlayers: data, with: .reliable)
        } catch {
            print("Failed to send data: \(error.localizedDescription)")
        }
    }
}
```
