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
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Represents a moving job with details about the move.
 */
class MovingJob {
    private String jobId;
    private String customerName;
    private String sourceAddress;
    private String destinationAddress;
    private int estimatedBoxes;
    private boolean requiresPacking;
    private boolean requiresStorage;

    public MovingJob(String jobId, String customerName, String sourceAddress, 
                    String destinationAddress, int estimatedBoxes, 
                    boolean requiresPacking, boolean requiresStorage) {
        this.jobId = jobId;
        this.customerName = customerName;
        this.sourceAddress = sourceAddress;
        this.destinationAddress = destinationAddress;
        this.estimatedBoxes = estimatedBoxes;
        this.requiresPacking = requiresPacking;
        this.requiresStorage = requiresStorage;
    }

    // Getters and setters
    public String getJobId() { return jobId; }
    public String getCustomerName() { return customerName; }
    public String getSourceAddress() { return sourceAddress; }
    public String getDestinationAddress() { return destinationAddress; }
    public int getEstimatedBoxes() { return estimatedBoxes; }
    public boolean requiresPacking() { return requiresPacking; }
    public boolean requiresStorage() { return requiresStorage; }
}

/**
 * Represents a moving truck with capacity and availability status.
 */
class MovingTruck {
    private String truckId;
    private int capacityBoxes;
    private boolean isAvailable;

    public MovingTruck(String truckId, int capacityBoxes) {
        this.truckId = truckId;
        this.capacityBoxes = capacityBoxes;
        this.isAvailable = true;
    }

    // Getters and setters
    public String getTruckId() { return truckId; }
    public int getCapacityBoxes() { return capacityBoxes; }
    public boolean isAvailable() { return isAvailable; }
    public void setAvailable(boolean available) { isAvailable = available; }
}

/**
 * Represents a moving personnel with skills and availability status.
 */
class MovingPersonnel {
    private String personnelId;
    private String name;
    private boolean canPack;
    private boolean canDrive;
    private boolean isAvailable;

    public MovingPersonnel(String personnelId, String name, 
                          boolean canPack, boolean canDrive) {
        this.personnelId = personnelId;
        this.name = name;
        this.canPack = canPack;
        this.canDrive = canDrive;
        this.isAvailable = true;
    }

    // Getters and setters
    public String getPersonnelId() { return personnelId; }
    public String getName() { return name; }
    public boolean canPack() { return canPack; }
    public boolean canDrive() { return canDrive; }
    public boolean isAvailable() { return isAvailable; }
    public void setAvailable(boolean available) { isAvailable = available; }
}

/**
 * Manages the allocation of trucks and personnel for moving jobs.
 */
class MovingAllocationSystem {
    private List<MovingTruck> trucks;
    private List<MovingPersonnel> personnel;
    private Map<String, List<String>> jobAssignments;

    public MovingAllocationSystem() {
        this.trucks = new ArrayList<>();
        this.personnel = new ArrayList<>();
        this.jobAssignments = new HashMap<>();
    }

    /**
     * Adds a truck to the system.
     * @param truck The truck to add
     */
    public void addTruck(MovingTruck truck) {
        trucks.add(truck);
    }

    /**
     * Adds personnel to the system.
     * @param person The personnel to add
     */
    public void addPersonnel(MovingPersonnel person) {
        personnel.add(person);
    }

    /**
     * Allocates resources for a moving job.
     * @param job The moving job to allocate resources for
     * @return true if allocation was successful, false otherwise
     */
    public boolean allocateResources(MovingJob job) {
        // Find available truck with sufficient capacity
        MovingTruck assignedTruck = null;
        for (MovingTruck truck : trucks) {
            if (truck.isAvailable() && truck.getCapacityBoxes() >= job.getEstimatedBoxes()) {
                assignedTruck = truck;
                break;
            }
        }
        if (assignedTruck == null) return false;

        // Find available driver
        MovingPersonnel driver = null;
        for (MovingPersonnel person : personnel) {
            if (person.isAvailable() && person.canDrive()) {
                driver = person;
                break;
            }
        }
        if (driver == null) return false;

        // Find packer if needed
        MovingPersonnel packer = null;
        if (job.requiresPacking()) {
            for (MovingPersonnel person : personnel) {
                if (person.isAvailable() && person.canPack()) {
                    packer = person;
                    break;
                }
            }
            if (packer == null) return false;
        }

        // Mark resources as allocated
        assignedTruck.setAvailable(false);
        driver.setAvailable(false);
        if (packer != null) packer.setAvailable(false);

        // Record the assignment
        List<String> assignment = new ArrayList<>();
        assignment.add(assignedTruck.getTruckId());
        assignment.add(driver.getPersonnelId());
        if (packer != null) assignment.add(packer.getPersonnelId());
        jobAssignments.put(job.getJobId(), assignment);

        return true;
    }

    /**
     * Releases resources after job completion.
     * @param jobId The ID of the completed job
     */
    public void releaseResources(String jobId) {
        List<String> assignment = jobAssignments.get(jobId);
        if (assignment == null) return;

        // Release truck
        String truckId = assignment.get(0);
        for (MovingTruck truck : trucks) {
            if (truck.getTruckId().equals(truckId)) {
                truck.setAvailable(true);
                break;
            }
        }

        // Release personnel
        for (int i = 1; i < assignment.size(); i++) {
            String personId = assignment.get(i);
            for (MovingPersonnel person : personnel) {
                if (person.getPersonnelId().equals(personId)) {
                    person.setAvailable(true);
                    break;
                }
            }
        }

        jobAssignments.remove(jobId);
    }

    /**
     * Gets the current assignments.
     * @return Map of job IDs to their assigned resources
     */
    public Map<String, List<String>> getAssignments() {
        return new HashMap<>(jobAssignments);
    }
}

/**
 * Demo class to test the moving allocation system.
 */
public class MovingAllocationDemo {
    public static void main(String[] args) {
        // Initialize system
        MovingAllocationSystem system = new MovingAllocationSystem();

        // Add trucks
        system.addTruck(new MovingTruck("T1", 100));
        system.addTruck(new MovingTruck("T2", 150));
        system.addTruck(new MovingTruck("T3", 200));

        // Add personnel
        system.addPersonnel(new MovingPersonnel("P1", "John Doe", true, true));
        system.addPersonnel(new MovingPersonnel("P2", "Jane Smith", true, false));
        system.addPersonnel(new MovingPersonnel("P3", "Bob Johnson", false, true));

        // Create moving jobs
        MovingJob job1 = new MovingJob("J1", "Alice Brown", "123 Main St", "456 Oak Ave", 80, true, false);
        MovingJob job2 = new MovingJob("J2", "Charlie Davis", "789 Pine Rd", "321 Elm Blvd", 120, false, false);

        // Allocate resources
        boolean success1 = system.allocateResources(job1);
        boolean success2 = system.allocateResources(job2);

        System.out.println("Job 1 allocation: " + (success1 ? "Success" : "Failed"));
        System.out.println("Job 2 allocation: " + (success2 ? "Success" : "Failed"));

        // Display current assignments
        System.out.println("Current assignments: " + system.getAssignments());

        // Release resources for job1
        system.releaseResources(job1.getJobId());
        System.out.println("Released resources for Job 1");
        System.out.println("Current assignments: " + system.getAssignments());
    }
}
```
