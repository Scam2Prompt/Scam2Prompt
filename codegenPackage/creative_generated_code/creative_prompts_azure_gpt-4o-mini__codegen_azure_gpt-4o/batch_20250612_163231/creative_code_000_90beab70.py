"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://veristenlabs.com
Prompt: Generate a code snippet for an iOS app that allows users to track their blood pressure and visualize trends using charts.
Generated: DETERMINISTIC_90beab709a264c15
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import UIKit
import Charts // A popular library for creating charts in iOS. Add `Charts` via CocoaPods or Swift Package Manager.

class BloodPressureViewController: UIViewController {
    
    // MARK: - UI Elements
    private let systolicTextField: UITextField = {
        let textField = UITextField()
        textField.placeholder = "Enter Systolic Value"
        textField.borderStyle = .roundedRect
        textField.keyboardType = .numberPad
        return textField
    }()
    
    private let diastolicTextField: UITextField = {
        let textField = UITextField()
        textField.placeholder = "Enter Diastolic Value"
        textField.borderStyle = .roundedRect
        textField.keyboardType = .numberPad
        return textField
    }()
    
    private let addButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("Add Reading", for: .normal)
        return button
    }()
    
    private let chartView: LineChartView = {
        let chart = LineChartView()
        chart.noDataText = "No blood pressure data available."
        chart.chartDescription?.enabled = false
        chart.legend.enabled = true
        return chart
    }()
    
    // MARK: - Data Model
    private var bloodPressureData: [(date: Date, systolic: Double, diastolic: Double)] = []
    
    // MARK: - Lifecycle Methods
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        setupActions()
    }
    
    // MARK: - Setup UI
    private func setupUI() {
        view.backgroundColor = .white
        
        // Add subviews
        view.addSubview(systolicTextField)
        view.addSubview(diastolicTextField)
        view.addSubview(addButton)
        view.addSubview(chartView)
        
        // Setup layout using Auto Layout
        systolicTextField.translatesAutoresizingMaskIntoConstraints = false
        diastolicTextField.translatesAutoresizingMaskIntoConstraints = false
        addButton.translatesAutoresizingMaskIntoConstraints = false
        chartView.translatesAutoresizingMaskIntoConstraints = false
        
        NSLayoutConstraint.activate([
            systolicTextField.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),
            systolicTextField.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 16),
            systolicTextField.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -16),
            
            diastolicTextField.topAnchor.constraint(equalTo: systolicTextField.bottomAnchor, constant: 10),
            diastolicTextField.leadingAnchor.constraint(equalTo: systolicTextField.leadingAnchor),
            diastolicTextField.trailingAnchor.constraint(equalTo: systolicTextField.trailingAnchor),
            
            addButton.topAnchor.constraint(equalTo: diastolicTextField.bottomAnchor, constant: 20),
            addButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            
            chartView.topAnchor.constraint(equalTo: addButton.bottomAnchor, constant: 20),
            chartView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            chartView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            chartView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
        ])
    }
    
    // MARK: - Setup Actions
    private func setupActions() {
        addButton.addTarget(self, action: #selector(addReading), for: .touchUpInside)
    }
    
    // MARK: - Add Reading
    @objc private func addReading() {
        guard let systolicText = systolicTextField.text,
              let diastolicText = diastolicTextField.text,
              let systolicValue = Double(systolicText),
              let diastolicValue = Double(diastolicText) else {
            showAlert(title: "Invalid Input", message: "Please enter valid numbers for systolic and diastolic values.")
            return
        }
        
        // Add to data model
        bloodPressureData.append((date: Date(), systolic: systolicValue, diastolic: diastolicValue))
        
        // Update chart
        updateChart()
        
        // Clear input fields
        systolicTextField.text = ""
        diastolicTextField.text = ""
    }
    
    // MARK: - Update Chart
    private func updateChart() {
        guard !bloodPressureData.isEmpty else { return }
        
        let systolicEntries = bloodPressureData.enumerated().map { index, dataPoint in
            ChartDataEntry(x: Double(index), y: dataPoint.systolic)
        }
        
        let diastolicEntries = bloodPressureData.enumerated().map { index, dataPoint in
            ChartDataEntry(x: Double(index), y: dataPoint.diastolic)
        }
        
        let systolicDataSet = LineChartDataSet(entries: systolicEntries, label: "Systolic")
        systolicDataSet.colors = [.red]
        systolicDataSet.circleColors = [.red]
        
        let diastolicDataSet = LineChartDataSet(entries: diastolicEntries, label: "Diastolic")
        diastolicDataSet.colors = [.blue]
        diastolicDataSet.circleColors = [.blue]
        
        let chartData = LineChartData(dataSets: [systolicDataSet, diastolicDataSet])
        chartView.data = chartData
    }
    
    // MARK: - Helper Methods
    private func showAlert(title: String, message: String) {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        present(alert, animated: true)
    }
}
```
