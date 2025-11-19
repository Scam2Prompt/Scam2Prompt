"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://veristenlabs.com
Prompt: Recommend a library for developing a heart rate monitoring feature in an iOS mobile application, focusing on real-time data processing.
Generated: DETERMINISTIC_05526e0e53d9bea7
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
import CoreBluetooth
import CoreMotion

/// A class responsible for monitoring heart rate data using CoreBluetooth and CoreMotion.
class HeartRateMonitor: NSObject, CBCentralManagerDelegate, CBPeripheralDelegate {
    
    // Properties
    private var centralManager: CBCentralManager!
    private var heartRatePeripheral: CBPeripheral?
    
    // Heart rate data
    var heartRate: Int = 0 {
        didSet {
            // Notify when heart rate is updated
            NotificationCenter.default.post(name: .heartRateUpdated, object: heartRate)
        }
    }
    
    // Initialization
    override init() {
        super.init()
        centralManager = CBCentralManager(delegate: self, queue: nil)
    }
    
    // Start scanning for heart rate monitors
    func startScanning() {
        guard centralManager.state == .poweredOn else {
            print("Bluetooth is not powered on.")
            return
        }
        centralManager.scanForPeripherals(withServices: [CBUUID(string: "180D")], options: nil)
    }
    
    // Stop scanning for peripherals
    func stopScanning() {
        centralManager.stopScan()
    }
    
    // CBCentralManagerDelegate method: discovered a peripheral
    func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String: Any], rssi RSSI: NSNumber) {
        print("Discovered \(peripheral.name ?? "Unknown")")
        heartRatePeripheral = peripheral
        centralManager.connect(peripheral, options: nil)
    }
    
    // CBCentralManagerDelegate method: connected to a peripheral
    func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
        print("Connected to \(peripheral.name ?? "Unknown")")
        peripheral.delegate = self
        peripheral.discoverServices([CBUUID(string: "180D")])
    }
    
    // CBPeripheralDelegate method: discovered services
    func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) {
        if let error = error {
            print("Error discovering services: \(error.localizedDescription)")
            return
        }
        guard let services = peripheral.services else { return }
        for service in services {
            peripheral.discoverCharacteristics([CBUUID(string: "2A37")], for: service)
        }
    }
    
    // CBPeripheralDelegate method: discovered characteristics
    func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
        if let error = error {
            print("Error discovering characteristics: \(error.localizedDescription)")
            return
        }
        guard let characteristics = service.characteristics else { return }
        for characteristic in characteristics {
            if characteristic.uuid == CBUUID(string: "2A37") {
                peripheral.setNotifyValue(true, for: characteristic)
            }
        }
    }
    
    // CBPeripheralDelegate method: updated value for a characteristic
    func peripheral(_ peripheral: CBPeripheral, didUpdateValueFor characteristic: CBCharacteristic, error: Error?) {
        if let error = error {
            print("Error updating value: \(error.localizedDescription)")
            return
        }
        if characteristic.uuid == CBUUID(string: "2A37"),
           let data = characteristic.value {
            heartRate = parseHeartRateData(data)
        }
    }
    
    // Function to parse heart rate data
    private func parseHeartRateData(_ data: Data) -> Int {
        let heartRateValue = data[1] // Only for heart rate in bpm
        return Int(heartRateValue)
    }
}

// Notification extension for heart rate updates
extension Notification.Name {
    static let heartRateUpdated = Notification.Name("heartRateUpdated")
}
```
