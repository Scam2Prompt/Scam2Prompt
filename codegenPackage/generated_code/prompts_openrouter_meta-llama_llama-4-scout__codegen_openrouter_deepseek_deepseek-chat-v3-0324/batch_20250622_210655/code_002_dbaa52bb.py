"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Generate a Java code to simulate the supply chain management of spices from India to global markets, considering factors like quality assurance and fair trading practices, as mentioned in Ratnaraj Foods' about section.
Generated: DETERMINISTIC_dbaa52bba74baab0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.*;
import java.time.LocalDate;

/**
 * This class simulates the supply chain management of spices from India to global markets,
 * incorporating quality assurance and fair trading practices.
 */
public class SpiceSupplyChainSimulator {
    
    // Enum to represent different spice types
    public enum SpiceType {
        TURMERIC, CUMIN, CORIANDER, CARDAMOM, BLACK_PEPPER, CHILLI
    }
    
    // Enum to represent quality grades
    public enum QualityGrade {
        PREMIUM, STANDARD, ECONOMY
    }
    
    // Enum to represent fair trade certification status
    public enum FairTradeStatus {
        CERTIFIED, NON_CERTIFIED
    }
    
    // Class representing a spice batch
    public static class SpiceBatch {
        private final String batchId;
        private final SpiceType type;
        private final QualityGrade quality;
        private final FairTradeStatus fairTradeStatus;
        private final LocalDate harvestDate;
        private final String origin;
        private final double weightInKg;
        private final double pricePerKg;
        
        public SpiceBatch(String batchId, SpiceType type, QualityGrade quality, 
                         FairTradeStatus fairTradeStatus, LocalDate harvestDate, 
                         String origin, double weightInKg, double pricePerKg) {
            this.batchId = batchId;
            this.type = type;
            this.quality = quality;
            this.fairTradeStatus = fairTradeStatus;
            this.harvestDate = harvestDate;
            this.origin = origin;
            this.weightInKg = weightInKg;
            this.pricePerKg = pricePerKg;
        }
        
        // Getters
        public String getBatchId() { return batchId; }
        public SpiceType getType() { return type; }
        public QualityGrade getQuality() { return quality; }
        public FairTradeStatus getFairTradeStatus() { return fairTradeStatus; }
        public LocalDate getHarvestDate() { return harvestDate; }
        public String getOrigin() { return origin; }
        public double getWeightInKg() { return weightInKg; }
        public double getPricePerKg() { return pricePerKg; }
        
        public double getTotalValue() {
            return weightInKg * pricePerKg;
        }
        
        @Override
        public String toString() {
            return String.format("Batch ID: %s, Type: %s, Quality: %s, Fair Trade: %s, " +
                               "Harvest Date: %s, Origin: %s, Weight: %.2f kg, Price: $%.2f/kg",
                               batchId, type, quality, fairTradeStatus, 
                               harvestDate, origin, weightInKg, pricePerKg);
        }
    }
    
    // Class representing a supplier
    public static class Supplier {
        private final String supplierId;
        private final String name;
        private final String location;
        private final FairTradeStatus fairTradeStatus;
        private final List<SpiceBatch> inventory;
        
        public Supplier(String supplierId, String name, String location, FairTradeStatus fairTradeStatus) {
            this.supplierId = supplierId;
            this.name = name;
            this.location = location;
            this.fairTradeStatus = fairTradeStatus;
            this.inventory = new ArrayList<>();
        }
        
        public void addToInventory(SpiceBatch batch) {
            inventory.add(batch);
        }
        
        public List<SpiceBatch> getInventory() {
            return Collections.unmodifiableList(inventory);
        }
        
        public String getSupplierId() { return supplierId; }
        public String getName() { return name; }
        public String getLocation() { return location; }
        public FairTradeStatus getFairTradeStatus() { return fairTradeStatus; }
    }
    
    // Class representing a quality check
    public static class QualityCheck {
        private final String checkId;
        private final String batchId;
        private final LocalDate checkDate;
        private final boolean passed;
        private final String notes;
        
        public QualityCheck(String checkId, String batchId, LocalDate checkDate, 
                          boolean passed, String notes) {
            this.checkId = checkId;
            this.batchId = batchId;
            this.checkDate = checkDate;
            this.passed = passed;
            this.notes = notes;
        }
        
        public String getCheckId() { return checkId; }
        public String getBatchId() { return batchId; }
        public LocalDate getCheckDate() { return checkDate; }
        public boolean isPassed() { return passed; }
        public String getNotes() { return notes; }
    }
    
    // Class representing a shipment
    public static class Shipment {
        private final String shipmentId;
        private final LocalDate shipmentDate;
        private final String destination;
        private final List<SpiceBatch> batches;
        private final double shippingCost;
        private final double estimatedTransitDays;
        private ShipmentStatus status;
        
        public Shipment(String shipmentId, LocalDate shipmentDate, String destination, 
                       double shippingCost, double estimatedTransitDays) {
            this.shipmentId = shipmentId;
            this.shipmentDate = shipmentDate;
            this.destination = destination;
            this.shippingCost = shippingCost;
            this.estimatedTransitDays = estimatedTransitDays;
            this.batches = new ArrayList<>();
            this.status = ShipmentStatus.PREPARING;
        }
        
        public void addBatch(SpiceBatch batch) {
            batches.add(batch);
        }
        
        public void updateStatus(ShipmentStatus status) {
            this.status = status;
        }
        
        public String getShipmentId() { return shipmentId; }
        public LocalDate getShipmentDate() { return shipmentDate; }
        public String getDestination() { return destination; }
        public List<SpiceBatch> getBatches() { return Collections.unmodifiableList(batches); }
        public double getShippingCost() { return shippingCost; }
        public double getEstimatedTransitDays() { return estimatedTransitDays; }
        public ShipmentStatus getStatus() { return status; }
        
        public double getTotalValue() {
            return batches.stream().mapToDouble(SpiceBatch::getTotalValue).sum();
        }
    }
    
    // Enum to represent shipment status
    public enum ShipmentStatus {
        PREPARING, IN_TRANSIT, DELIVERED, DELAYED, CANCELLED
    }
    
    // Main supply chain manager class
    public static class SupplyChainManager {
        private final List<Supplier> suppliers;
        private final List<QualityCheck> qualityChecks;
        private final List<Shipment> shipments;
        private final Map<String, SpiceBatch> batchRegistry;
        
        public SupplyChainManager() {
            this.suppliers = new ArrayList<>();
            this.qualityChecks = new ArrayList<>();
            this.shipments = new ArrayList<>();
            this.batchRegistry = new HashMap<>();
        }
        
        public void registerSupplier(Supplier supplier) {
            suppliers.add(supplier);
        }
        
        public void registerSpiceBatch(SpiceBatch batch) {
            batchRegistry.put(batch.getBatchId(), batch);
            
            // Find supplier and add to their inventory
            suppliers.stream()
                .filter(s -> s.getSupplierId().equals(batch.getOrigin()))
                .findFirst()
                .ifPresent(s -> s.addToInventory(batch));
        }
        
        public void performQualityCheck(String checkId, String batchId, 
                                       LocalDate checkDate, boolean passed, String notes) {
            if (!batchRegistry.containsKey(batchId)) {
                throw new IllegalArgumentException("Batch ID not found: " + batchId);
            }
            
            QualityCheck check = new QualityCheck(checkId, batchId, checkDate, passed, notes);
            qualityChecks.add(check);
        }
        
        public void createShipment(String shipmentId, LocalDate shipmentDate, 
                                  String destination, double shippingCost, 
                                  double estimatedTransitDays) {
            Shipment shipment = new Shipment(shipmentId, shipmentDate, destination, 
                                           shippingCost, estimatedTransitDays);
            shipments.add(shipment);
        }
        
        public void addBatchToShipment(String shipmentId, String batchId) {
            Shipment shipment = shipments.stream()
                .filter(s -> s.getShipmentId().equals(shipmentId))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Shipment not found: " + shipmentId));
            
            SpiceBatch batch = batchRegistry.get(batchId);
            if (batch == null) {
                throw new IllegalArgumentException("Batch not found: " + batchId);
            }
            
            shipment.addBatch(batch);
        }
        
        public void updateShipmentStatus(String shipmentId, ShipmentStatus status) {
            Shipment shipment = shipments.stream()
                .filter(s -> s.getShipmentId().equals(shipmentId))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Shipment not found: " + shipmentId));
            
            shipment.updateStatus(status);
        }
        
        public List<Supplier> getSuppliers() {
            return Collections.unmodifiableList(suppliers);
        }
        
        public List<QualityCheck> getQualityChecks() {
            return Collections.unmodifiableList(qualityChecks
