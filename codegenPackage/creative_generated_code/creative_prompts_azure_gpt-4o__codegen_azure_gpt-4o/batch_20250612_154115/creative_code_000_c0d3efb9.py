"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://veristenlabs.com
Prompt: Write Swift code for an iOS app feature that scans food items and provides detailed nutritional information, including sugar load, nutrients, and risky ingredients, as described on Veristen Labs' website.
Generated: DETERMINISTIC_c0d3efb976d6abaa
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import UIKit
import Vision
import CoreML

/// FoodScannerViewController is responsible for scanning food items and providing detailed nutritional information.
class FoodScannerViewController: UIViewController {
    
    // MARK: - UI Components
    private let scanButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("Scan Food Item", for: .normal)
        button.titleLabel?.font = UIFont.boldSystemFont(ofSize: 18)
        button.backgroundColor = UIColor.systemBlue
        button.setTitleColor(.white, for: .normal)
        button.layer.cornerRadius = 8
        button.addTarget(self, action: #selector(scanButtonTapped), for: .touchUpInside)
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()
    
    private let resultTextView: UITextView = {
        let textView = UITextView()
        textView.isEditable = false
        textView.font = UIFont.systemFont(ofSize: 16)
        textView.textColor = .black
        textView.layer.borderWidth = 1
        textView.layer.borderColor = UIColor.lightGray.cgColor
        textView.layer.cornerRadius = 8
        textView.translatesAutoresizingMaskIntoConstraints = false
        return textView
    }()
    
    // MARK: - Properties
    private let nutritionalModel: VNCoreMLModel = {
        // Load CoreML model for food recognition and nutritional analysis
        guard let model = try? VNCoreMLModel(for: NutritionalAnalysis().model) else {
            fatalError("Failed to load the CoreML model.")
        }
        return model
    }()
    
    private let imagePicker = UIImagePickerController()
    
    // MARK: - Lifecycle Methods
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        imagePicker.delegate = self
        imagePicker.sourceType = .camera // Configure image picker to use the camera
    }
    
    // MARK: - UI Setup
    private func setupUI() {
        view.backgroundColor = .white
        view.addSubview(scanButton)
        view.addSubview(resultTextView)
        
        NSLayoutConstraint.activate([
            scanButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            scanButton.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            scanButton.widthAnchor.constraint(equalToConstant: 200),
            scanButton.heightAnchor.constraint(equalToConstant: 50),
            
            resultTextView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 16),
            resultTextView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -16),
            resultTextView.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -32),
            resultTextView.heightAnchor.constraint(equalToConstant: 200)
        ])
    }
    
    // MARK: - Actions
    @objc private func scanButtonTapped() {
        present(imagePicker, animated: true, completion: nil)
    }
    
    // MARK: - Handle Image Analysis
    private func analyzeImage(_ image: UIImage) {
        guard let cgImage = image.cgImage else {
            resultTextView.text = "Invalid image format. Unable to scan."
            return
        }
        
        let request = VNCoreMLRequest(model: nutritionalModel) { [weak self] request, error in
            if let error = error {
                self?.resultTextView.text = "Error analyzing the image: \(error.localizedDescription)"
                return
            }
            
            guard let results = request.results as? [VNClassificationObservation],
                  let topResult = results.first else {
                self?.resultTextView.text = "No nutritional information found."
                return
            }
            
            DispatchQueue.main.async {
                self?.displayNutritionalInformation(for: topResult.identifier)
            }
        }
        
        let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
        
        DispatchQueue.global(qos: .userInitiated).async {
            do {
                try handler.perform([request])
            } catch {
                DispatchQueue.main.async {
                    self.resultTextView.text = "Error performing image analysis: \(error.localizedDescription)"
                }
            }
        }
    }
    
    private func displayNutritionalInformation(for foodItem: String) {
        // Mocking a detailed nutritional info retrieval based on food item
        let mockedData: [String: String] = [
            "Apple": "Sugar Load: 19g, Nutrients: Vitamin C, Fiber, Risky Ingredients: None",
            "Pizza": "Sugar Load: 4g, Nutrients: Protein, Carbs, Risky Ingredients: Saturated Fats",
            "Chocolate": "Sugar Load: 24g, Nutrients: Magnesium, Risky Ingredients: High Sugar Content"
        ]
        
        let nutritionalInfo = mockedData[foodItem] ?? "No data available for \(foodItem)."
        resultTextView.text = "Food Item: \(foodItem)\n\n\(nutritionalInfo)"
    }
}

// MARK: - UIImagePickerControllerDelegate & UINavigationControllerDelegate
extension FoodScannerViewController: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        picker.dismiss(animated: true, completion: nil)
        
        guard let selectedImage = info[.originalImage] as? UIImage else {
            resultTextView.text = "Failed to capture the image. Please try again."
            return
        }
        
        analyzeImage(selectedImage)
    }
    
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        picker.dismiss(animated: true, completion: nil)
    }
}
```
