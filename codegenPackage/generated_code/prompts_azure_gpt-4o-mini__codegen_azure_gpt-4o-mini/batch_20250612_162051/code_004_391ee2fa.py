"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Develop a mobile app feature that lets users take a selfie with their frozen yogurt and receive a discount, inspired by Andias Frozen Yogurt's promotional strategy.
Generated: DETERMINISTIC_391ee2faf9c1e803
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```swift
import UIKit
import AVFoundation

class SelfieDiscountViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    // UI Elements
    private let takeSelfieButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("Take Selfie with Yogurt", for: .normal)
        button.backgroundColor = .systemBlue
        button.setTitleColor(.white, for: .normal)
        button.layer.cornerRadius = 10
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()
    
    private let discountLabel: UILabel = {
        let label = UILabel()
        label.text = "Show your selfie for a discount!"
        label.textAlignment = .center
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    // View Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }
    
    // Setup UI Elements
    private func setupUI() {
        view.backgroundColor = .white
        
        view.addSubview(takeSelfieButton)
        view.addSubview(discountLabel)
        
        // Constraints for button
        NSLayoutConstraint.activate([
            takeSelfieButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            takeSelfieButton.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            takeSelfieButton.widthAnchor.constraint(equalToConstant: 250),
            takeSelfieButton.heightAnchor.constraint(equalToConstant: 50)
        ])
        
        // Constraints for label
        NSLayoutConstraint.activate([
            discountLabel.topAnchor.constraint(equalTo: takeSelfieButton.bottomAnchor, constant: 20),
            discountLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
        
        // Button action
        takeSelfieButton.addTarget(self, action: #selector(takeSelfie), for: .touchUpInside)
    }
    
    // Action to take a selfie
    @objc private func takeSelfie() {
        // Check camera availability
        guard UIImagePickerController.isSourceTypeAvailable(.camera) else {
            showAlert(title: "Camera Unavailable", message: "This device does not have a camera.")
            return
        }
        
        let imagePicker = UIImagePickerController()
        imagePicker.delegate = self
        imagePicker.sourceType = .camera
        imagePicker.allowsEditing = true
        
        present(imagePicker, animated: true, completion: nil)
    }
    
    // Handle image selection
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        picker.dismiss(animated: true, completion: nil)
        
        // Get the edited image
        guard let image = info[.editedImage] as? UIImage ?? info[.originalImage] as? UIImage else {
            showAlert(title: "Image Error", message: "Could not retrieve the image.")
            return
        }
        
        // Process the selfie (e.g., save to gallery, apply discount logic)
        processSelfie(image)
    }
    
    // Handle cancellation
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        picker.dismiss(animated: true, completion: nil)
    }
    
    // Process the selfie and apply discount logic
    private func processSelfie(_ image: UIImage) {
        // Here you can implement the logic to apply the discount
        // For now, we will just show a success message
        showAlert(title: "Success!", message: "Show this selfie for your discount!")
    }
    
    // Show alert for errors or messages
    private func showAlert(title: String, message: String) {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alert, animated: true, completion: nil)
    }
}
```
