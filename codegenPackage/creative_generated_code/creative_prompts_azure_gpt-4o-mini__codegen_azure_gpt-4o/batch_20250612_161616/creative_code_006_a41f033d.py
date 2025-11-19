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
import MapKit

class DoctorOnCallViewController: UIViewController, CLLocationManagerDelegate {
    // UI Elements
    private let scheduleButton = UIButton(type: .system)
    private let nearestClinicLabel = UILabel()
    private let locationManager = CLLocationManager()
    private var userLocation: CLLocation?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        checkLocationServices()
    }
    
    // MARK: - UI Setup
    private func setupUI() {
        view.backgroundColor = .white
        
        // Schedule Button
        scheduleButton.setTitle("Schedule Doctor On Call", for: .normal)
        scheduleButton.addTarget(self, action: #selector(scheduleDoctorOnCall), for: .touchUpInside)
        scheduleButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(scheduleButton)
        
        // Nearest Clinic Label
        nearestClinicLabel.text = "Finding nearest clinic..."
        nearestClinicLabel.textAlignment = .center
        nearestClinicLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(nearestClinicLabel)
        
        // Add constraints
        NSLayoutConstraint.activate([
            scheduleButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            scheduleButton.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            nearestClinicLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            nearestClinicLabel.bottomAnchor.constraint(equalTo: scheduleButton.topAnchor, constant: -20)
        ])
    }
    
    // MARK: - Location Services
    private func checkLocationServices() {
        if CLLocationManager.locationServicesEnabled() {
            setupLocationManager()
            checkLocationAuthorization()
        } else {
            showLocationDisabledAlert()
        }
    }
    
    private func setupLocationManager() {
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
    }
    
    private func checkLocationAuthorization() {
        switch CLLocationManager.authorizationStatus() {
        case .authorizedWhenInUse, .authorizedAlways:
            locationManager.startUpdatingLocation()
        case .denied, .restricted:
            showPermissionDeniedAlert()
        case .notDetermined:
            locationManager.requestWhenInUseAuthorization()
        @unknown default:
            fatalError("Unhandled authorization status")
        }
    }
    
    private func showLocationDisabledAlert() {
        let alert = UIAlertController(title: "Location Disabled", message: "Please enable location services in settings to use this feature.", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alert, animated: true)
    }
    
    private func showPermissionDeniedAlert() {
        let alert = UIAlertController(title: "Permission Denied", message: "Please allow location access in settings to find nearby clinics.", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alert, animated: true)
    }
    
    // MARK: - CLLocationManagerDelegate
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let location = locations.last else { return }
        userLocation = location
        findNearestClinic()
    }
    
    func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
        print("Location update failed with error: \(error.localizedDescription)")
    }
    
    // MARK: - Nearest Clinic Finder
    private func findNearestClinic() {
        guard let userLocation = userLocation else { return }
        
        let request = MKLocalSearch.Request()
        request.naturalLanguageQuery = "Clinic"
        request.region = MKCoordinateRegion(center: userLocation.coordinate, latitudinalMeters: 5000, longitudinalMeters: 5000)
        
        let search = MKLocalSearch(request: request)
        search.start { [weak self] response, error in
            guard let self = self else { return }
            if let error = error {
                print("Search failed with error: \(error.localizedDescription)")
                self.nearestClinicLabel.text = "Error finding clinic."
                return
            }
            
            guard let clinic = response?.mapItems.first else {
                self.nearestClinicLabel.text = "No clinics found nearby."
                return
            }
            
            let clinicName = clinic.name ?? "Unknown Clinic"
            self.nearestClinicLabel.text = "Nearest Clinic: \(clinicName)"
        }
    }
    
    // MARK: - Doctor On Call Scheduling
    @objc private func scheduleDoctorOnCall() {
        let alert = UIAlertController(title: "Doctor Scheduled", message: "A doctor will contact you shortly.", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alert, animated: true)
    }
}
```
