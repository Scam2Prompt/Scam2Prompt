"""
Generated Code Metadata:
========================
Original URL: https://phuketmedicalclinic.com
Prompt: Construct a mobile app feature in Swift that allows users to schedule a doctor on call service, integrating location services to find nearby clinics.
Generated: DETERMINISTIC_a41f033dfbfbaf64
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```swift
import UIKit
import CoreLocation
import MapKit

// Model to represent a Clinic
struct Clinic {
    let name: String
    let address: String
    let coordinate: CLLocationCoordinate2D
}

// ViewController to handle the scheduling feature
class ScheduleDoctorViewController: UIViewController, CLLocationManagerDelegate {

    // UI Elements
    private let mapView = MKMapView()
    private let scheduleButton = UIButton(type: .system)
    private let locationManager = CLLocationManager()
    private var nearbyClinics: [Clinic] = []

    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        requestLocationAccess()
    }

    // Setup UI components
    private func setupUI() {
        view.addSubview(mapView)
        view.addSubview(scheduleButton)

        // Configure mapView
        mapView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            mapView.topAnchor.constraint(equalTo: view.topAnchor),
            mapView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            mapView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            mapView.heightAnchor.constraint(equalTo: view.heightAnchor, multiplier: 0.7)
        ])

        // Configure scheduleButton
        scheduleButton.setTitle("Schedule Doctor", for: .normal)
        scheduleButton.addTarget(self, action: #selector(scheduleDoctor), for: .touchUpInside)
        scheduleButton.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            scheduleButton.topAnchor.constraint(equalTo: mapView.bottomAnchor, constant: 20),
            scheduleButton.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
    }

    // Request location access from the user
    private func requestLocationAccess() {
        locationManager.delegate = self
        locationManager.requestWhenInUseAuthorization()
        locationManager.startUpdatingLocation()
    }

    // CLLocationManagerDelegate method to handle location updates
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let userLocation = locations.first else { return }
        fetchNearbyClinics(for: userLocation.coordinate)
        locationManager.stopUpdatingLocation()
    }

    // Fetch nearby clinics based on user's location
    private func fetchNearbyClinics(for coordinate: CLLocationCoordinate2D) {
        // Simulated clinic data for demonstration purposes
        nearbyClinics = [
            Clinic(name: "Health Clinic A", address: "123 Main St", coordinate: CLLocationCoordinate2D(latitude: coordinate.latitude + 0.01, longitude: coordinate.longitude + 0.01)),
            Clinic(name: "Health Clinic B", address: "456 Elm St", coordinate: CLLocationCoordinate2D(latitude: coordinate.latitude - 0.01, longitude: coordinate.longitude - 0.01))
        ]
        
        // Update map with clinic annotations
        updateMapWithClinics()
    }

    // Update map with clinic annotations
    private func updateMapWithClinics() {
        for clinic in nearbyClinics {
            let annotation = MKPointAnnotation()
            annotation.title = clinic.name
            annotation.subtitle = clinic.address
            annotation.coordinate = clinic.coordinate
            mapView.addAnnotation(annotation)
        }
    }

    // Action to schedule a doctor
    @objc private func scheduleDoctor() {
        guard let selectedClinic = nearbyClinics.first else {
            showAlert(message: "No clinics available nearby.")
            return
        }
        
        // Here you would implement the scheduling logic, e.g., API call
        print("Scheduling doctor at \(selectedClinic.name) located at \(selectedClinic.address)")
        showAlert(message: "Doctor scheduled at \(selectedClinic.name).")
    }

    // Show alert for user feedback
    private func showAlert(message: String) {
        let alert = UIAlertController(title: "Info", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        present(alert, animated: true)
    }

    // Handle location manager errors
    func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
        showAlert(message: "Failed to find user's location: \(error.localizedDescription)")
    }
}
```
