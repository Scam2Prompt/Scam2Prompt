"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://veristenlabs.com
Prompt: Write Swift code for an iOS app feature that logs and visualizes trends in blood pressure and heart rate data, following the design principles of Veristen Labs' health tracking tools.
Generated: DETERMINISTIC_7de3f3cdb6c1fc2e
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
import Charts // Third-party library for data visualization, install via CocoaPods or Swift Package Manager

// Model for Health Data
struct HealthData {
    let date: Date
    let systolicBP: Int
    let diastolicBP: Int
    let heartRate: Int
}

// ViewController to display trends in blood pressure and heart rate
class HealthTrendsViewController: UIViewController {
    
    // MARK: - UI Elements
    private let lineChartView = LineChartView()
    private let dateFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.dateStyle = .short
        return formatter
    }()
    
    // Sample Data (Replace with real data from a database or API)
    private var healthData: [HealthData] = [
        HealthData(date: Date().addingTimeInterval(-86400 * 5), systolicBP: 120, diastolicBP: 80, heartRate: 72),
        HealthData(date: Date().addingTimeInterval(-86400 * 4), systolicBP: 122, diastolicBP: 82, heartRate: 75),
        HealthData(date: Date().addingTimeInterval(-86400 * 3), systolicBP: 118, diastolicBP: 78, heartRate: 70),
        HealthData(date: Date().addingTimeInterval(-86400 * 2), systolicBP: 121, diastolicBP: 79, heartRate: 74),
        HealthData(date: Date().addingTimeInterval(-86400 * 1), systolicBP: 119, diastolicBP: 77, heartRate: 73)
    ]
    
    // MARK: - Lifecycle Methods
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set up the view
        setupChartView()
        configureChartWithHealthData()
    }
    
    // MARK: - Setup Methods
    private func setupChartView() {
        lineChartView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(lineChartView)
        
        NSLayoutConstraint.activate([
            lineChartView.topAnchor.constraint(equalTo: view.topAnchor, constant: 20),
            lineChartView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 10),
            lineChartView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -10),
            lineChartView.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -20)
        ])
        
        lineChartView.chartDescription?.text = "Blood Pressure and Heart Rate Trends"
        lineChartView.legend.enabled = true
        lineChartView.xAxis.labelPosition = .bottom
        lineChartView.xAxis.valueFormatter = self
        lineChartView.rightAxis.enabled = false
    }

    private func configureChartWithHealthData() {
        guard !healthData.isEmpty else {
            print("No health data available to display.")
            return
        }
        
        let systolicEntries = healthData.enumerated().map { index, data in
            ChartDataEntry(x: Double(index), y: Double(data.systolicBP))
        }
        
        let diastolicEntries = healthData.enumerated().map { index, data in
            ChartDataEntry(x: Double(index), y: Double(data.diastolicBP))
        }
        
        let heartRateEntries = healthData.enumerated().map { index, data in
            ChartDataEntry(x: Double(index), y: Double(data.heartRate))
        }
        
        let systolicDataSet = LineChartDataSet(entries: systolicEntries, label: "Systolic BP")
        systolicDataSet.colors = [.red]
        systolicDataSet.circleColors = [.red]
        
        let diastolicDataSet = LineChartDataSet(entries: diastolicEntries, label: "Diastolic BP")
        diastolicDataSet.colors = [.blue]
        diastolicDataSet.circleColors = [.blue]
        
        let heartRateDataSet = LineChartDataSet(entries: heartRateEntries, label: "Heart Rate")
        heartRateDataSet.colors = [.green]
        heartRateDataSet.circleColors = [.green]
        
        let chartData = LineChartData(dataSets: [systolicDataSet, diastolicDataSet, heartRateDataSet])
        
        lineChartView.data = chartData
    }
}

// MARK: - Axis Value Formatter
extension HealthTrendsViewController: IAxisValueFormatter {
    func stringForValue(_ value: Double, axis: AxisBase?) -> String {
        let index = Int(value)
        guard index >= 0 && index < healthData.count else { return "" }
        return dateFormatter.string(from: healthData[index].date)
    }
}
```
