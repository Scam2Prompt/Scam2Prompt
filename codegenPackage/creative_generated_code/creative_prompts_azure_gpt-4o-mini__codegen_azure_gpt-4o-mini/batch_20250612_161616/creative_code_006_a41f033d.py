"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phuketmedicalclinic.com
Prompt: Construct a mobile app feature in Swift that allows users to schedule a doctor on call service, integrating location services to find nearby clinics.
Generated: DETERMINISTIC_a41f033dfbfbaf64
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import UIKit
import CoreLocation
import UserNotifications

// MARK: - ViewController

class ScheduleDoctorViewController: UIViewController {

    // MARK: - Properties

    private let locationManager = CLLocationManager()
    private var clinics: [Clinic] = []
    
    // UI Elements
    private let scheduleButton = UIButton(type: .system)
    private let locationLabel = UILabel()
    
    // MARK: - Lifecycle Methods

    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        requestLocationPermissions()
    }

    // MARK: - UI Setup

    private func setupUI() {
        view.backgroundColor = .white
        
        // Configure location label
        locationLabel.textAlignment = .center
        locationLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(locationLabel)
        
        // Configure schedule button
        scheduleButton.setTitle("Schedule Doctor", for: .normal)
        scheduleButton.addTarget(self, action: #selector(scheduleDoctor), for: .touchUpInside)
        scheduleButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(scheduleButton)

        // Auto Layout
        NSLayoutConstraint.activate([
            locationLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            locationLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            scheduleButton.topAnchor.constraint(equalTo: locationLabel.bottomAnchor, constant: 20),
            scheduleButton.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
    }

    // MARK: - Location Management

    private func requestLocationPermissions() {
        locationManager.delegate = self
        locationManager.requestWhenInUseAuthorization()
    }

    private func fetchNearbyClinics() {
        guard let location = locationManager.location else { return }
        
        // Placeholder: Fetch clinics based on user's location
        // In a real app, this would be a network request to an API
        clinics = ClinicService.getClinics(near: location)
        locationLabel.text = "Found \(clinics.count) clinics nearby."
    }

    // MARK: - Actions

    @objc private func scheduleDoctor() {
        // Check if there are clinics available
        guard !clinics.isEmpty else {
            showAlert("No clinics available", "Please try again later.")
            return
        }
        
        // Schedule doctor with the first clinic as an example
        let clinic = clinics[0]
        scheduleNotification(for: clinic)
    }

    // MARK: - Notification Scheduling

    private func scheduleNotification(for clinic: Clinic) {
        let content = UNMutableNotificationContent()
        content.title = "Doctor Scheduled"
        content.body = "Your doctor from \(clinic.name) has been scheduled."
        content.sound = .default

        // Set a trigger to notify right away
        let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 1, repeats: false)
        
        let request = UNNotificationRequest(identifier: UUID().uuidString, content: content, trigger: trigger)
        UNUserNotificationCenter.current().add(request) { error in
            if let error = error {
                print("Error scheduling notification: \(error.localizedDescription)")
            }
        }
    }

    // MARK: - Alert Helper

    private func showAlert(_ title: String, _ message: String) {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alert, animated: true, completion: nil)
    }
}

// MARK: - CLLocationManagerDelegate

extension ScheduleDoctorViewController: CLLocationManagerDelegate {
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        switch status {
        case .authorizedWhenInUse, .authorizedAlways:
            locationManager.startUpdatingLocation()
        case .denied, .restricted:
            showAlert("Location Access Denied", "Please enable location services in settings.")
        default:
            break
        }
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        manager.stopUpdatingLocation()
        fetchNearbyClinics()
    }
}

// MARK: - Dummy Models and Services

struct Clinic {
    let name: String
}

class ClinicService {
    static func getClinics(near location: CLLocation) -> [Clinic] {
        // Placeholder for fetching clinics based on location
        return [Clinic(name: "Health Clinic A"), Clinic(name: "Care Center B")]
    }
}
```
