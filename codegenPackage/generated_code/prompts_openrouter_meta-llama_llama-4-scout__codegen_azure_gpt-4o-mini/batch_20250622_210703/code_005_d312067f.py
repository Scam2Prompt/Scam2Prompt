"""
Generated Code Metadata:
========================
Original URL: https://rjbmudanzas.es
Prompt: Write a code snippet in Java to simulate the allocation of moving trucks and personnel for a set of moves, ensuring efficient use of resources as described in RJB Moving's services.
Generated: DETERMINISTIC_d312067fff618065
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

// Class representing a moving truck
class MovingTruck {
    private String truckId;
    private int capacity; // Capacity in cubic feet
    private boolean isAvailable;

    public MovingTruck(String truckId, int capacity) {
        this.truckId = truckId;
        this.capacity = capacity;
        this.isAvailable = true;
    }

    public String getTruckId() {
        return truckId;
    }

    public int getCapacity() {
        return capacity;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void allocate() {
        if (!isAvailable) {
            throw new IllegalStateException("Truck is already allocated.");
        }
        isAvailable = false;
    }

    public void release() {
        isAvailable = true;
    }
}

// Class representing a moving personnel
class Personnel {
    private String personnelId;
    private boolean isAvailable;

    public Personnel(String personnelId) {
        this.personnelId = personnelId;
        this.isAvailable = true;
    }

    public String getPersonnelId() {
        return personnelId;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void allocate() {
        if (!isAvailable) {
            throw new IllegalStateException("Personnel is already allocated.");
        }
        isAvailable = false;
    }

    public void release() {
        isAvailable = true;
    }
}

// Class to manage the allocation of trucks and personnel
class MoveManager {
    private List<MovingTruck> trucks;
    private List<Personnel> personnel;

    public MoveManager(List<MovingTruck> trucks, List<Personnel> personnel) {
        this.trucks = trucks;
        this.personnel = personnel;
    }

    // Method to allocate resources for a move
    public void allocateResources(int requiredCapacity, int requiredPersonnel) {
        MovingTruck allocatedTruck = null;
        List<Personnel> allocatedPersonnel = new ArrayList<>();

        // Find an available truck
        for (MovingTruck truck : trucks) {
            if (truck.isAvailable() && truck.getCapacity() >= requiredCapacity) {
                allocatedTruck = truck;
                break;
            }
        }

        // Find available personnel
        for (Personnel p : personnel) {
            if (p.isAvailable()) {
                allocatedPersonnel.add(p);
                if (allocatedPersonnel.size() == requiredPersonnel) {
                    break;
                }
            }
        }

        // Check if resources are available
        if (allocatedTruck == null || allocatedPersonnel.size() < requiredPersonnel) {
            throw new IllegalStateException("Insufficient resources available for the move.");
        }

        // Allocate the truck and personnel
        allocatedTruck.allocate();
        for (Personnel p : allocatedPersonnel) {
            p.allocate();
        }

        System.out.println("Allocated Truck: " + allocatedTruck.getTruckId());
        System.out.println("Allocated Personnel: " + allocatedPersonnel.size());
    }

    // Method to release resources after a move
    public void releaseResources(MovingTruck truck, List<Personnel> personnel) {
        truck.release();
        for (Personnel p : personnel) {
            p.release();
        }
        System.out.println("Released Truck: " + truck.getTruckId());
        System.out.println("Released Personnel: " + personnel.size());
    }
}

// Main class to simulate the moving service
public class RJBMovingService {
    public static void main(String[] args) {
        // Create sample trucks and personnel
        List<MovingTruck> trucks = new ArrayList<>();
        trucks.add(new MovingTruck("Truck1", 1000));
        trucks.add(new MovingTruck("Truck2", 1500));
        trucks.add(new MovingTruck("Truck3", 2000));

        List<Personnel> personnel = new ArrayList<>();
        personnel.add(new Personnel("Person1"));
        personnel.add(new Personnel("Person2"));
        personnel.add(new Personnel("Person3"));

        // Create MoveManager instance
        MoveManager moveManager = new MoveManager(trucks, personnel);

        // Simulate resource allocation
        try {
            moveManager.allocateResources(1200, 2);
            // Simulate move operation...
            // After the move, release resources
            // For demonstration, we release the first truck and personnel
            moveManager.releaseResources(trucks.get(0), personnel.subList(0, 2));
        } catch (IllegalStateException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
