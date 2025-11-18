"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Generate Java code to implement a delivery tracking system for Watpac Chemicals Pvt Ltd, considering their 24/7 delivery service and toll-free numbers.
Generated: DETERMINISTIC_652d3ea8113e2c8a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.HashMap;
import java.util.Map;

// Class representing a delivery package
class Package {
    private String trackingId;
    private String status;

    public Package(String trackingId) {
        this.trackingId = trackingId;
        this.status = "In Transit"; // Default status
    }

    public String getTrackingId() {
        return trackingId;
    }

    public String getStatus() {
        return status;
    }

    public void updateStatus(String status) {
        this.status = status;
    }
}

// Class representing the Delivery Tracking System
public class DeliveryTrackingSystem {
    // Map to store packages with their tracking IDs
    private Map<String, Package> packageMap;

    public DeliveryTrackingSystem() {
        packageMap = new HashMap<>();
    }

    // Method to add a new package to the system
    public void addPackage(String trackingId) {
        if (trackingMap.containsKey(trackingId)) {
            throw new IllegalArgumentException("Package with this tracking ID already exists.");
        }
        packageMap.put(trackingId, new Package(trackingId));
    }

    // Method to update the status of a package
    public void updatePackageStatus(String trackingId, String newStatus) {
        Package pkg = packageMap.get(trackingId);
        if (pkg == null) {
            throw new IllegalArgumentException("No package found with this tracking ID.");
        }
        pkg.updateStatus(newStatus);
    }

    // Method to get the status of a package
    public String getPackageStatus(String trackingId) {
        Package pkg = packageMap.get(trackingId);
        if (pkg == null) {
            throw new IllegalArgumentException("No package found with this tracking ID.");
        }
        return pkg.getStatus();
    }

    // Method to display all package statuses
    public void displayAllPackageStatuses() {
        if (packageMap.isEmpty()) {
            System.out.println("No packages in the system.");
            return;
        }
        System.out.println("Package Statuses:");
        for (Package pkg : packageMap.values()) {
            System.out.println("Tracking ID: " + pkg.getTrackingId() + ", Status: " + pkg.getStatus());
        }
    }

    // Main method for testing the Delivery Tracking System
    public static void main(String[] args) {
        try {
            DeliveryTrackingSystem trackingSystem = new DeliveryTrackingSystem();
            trackingSystem.addPackage("PKG001");
            trackingSystem.addPackage("PKG002");
            trackingSystem.updatePackageStatus("PKG001", "Delivered");
            
            System.out.println("Status of PKG001: " + trackingSystem.getPackageStatus("PKG001"));
            System.out.println("Status of PKG002: " + trackingSystem.getPackageStatus("PKG002"));

            trackingSystem.displayAllPackageStatuses();
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
