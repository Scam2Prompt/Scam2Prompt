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
import java.util.*;

/**
 * Simulates the allocation of moving trucks and personnel for a set of moves.
 */
public class MovingResourceAllocator {

    // Define a class to represent a move
    static class Move {
        private String id;
        private int requiredTrucks;
        private int requiredPersonnel;

        public Move(String id, int requiredTrucks, int requiredPersonnel) {
            this.id = id;
            this.requiredTrucks = requiredTrucks;
            this.requiredPersonnel = requiredPersonnel;
        }

        public String getId() {
            return id;
        }

        public int getRequiredTrucks() {
            return requiredTrucks;
        }

        public int getRequiredPersonnel() {
            return requiredPersonnel;
        }
    }

    // Define a class to represent a moving truck
    static class Truck {
        private String id;
        private boolean isAllocated;

        public Truck(String id) {
            this.id = id;
            this.isAllocated = false;
        }

        public String getId() {
            return id;
        }

        public boolean isAllocated() {
            return isAllocated;
        }

        public void setAllocated(boolean allocated) {
            isAllocated = allocated;
        }
    }

    // Define a class to represent personnel
    static class Personnel {
        private String id;
        private boolean isAllocated;

        public Personnel(String id) {
            this.id = id;
            this.isAllocated = false;
        }

        public String getId() {
            return id;
        }

        public boolean isAllocated() {
            return isAllocated;
        }

        public void setAllocated(boolean allocated) {
            isAllocated = allocated;
        }
    }

    /**
     * Allocates moving trucks and personnel for a set of moves.
     *
     * @param moves     List of moves to be allocated
     * @param trucks    List of available trucks
     * @param personnel List of available personnel
     * @return A map of move IDs to their allocated resources
     */
    public static Map<String, Map<String, Object>> allocateResources(List<Move> moves, List<Truck> trucks, List<Personnel> personnel) {
        // Sort moves by required trucks and personnel in descending order
        moves.sort((m1, m2) -> {
            if (m1.getRequiredTrucks() == m2.getRequiredTrucks()) {
                return Integer.compare(m2.getRequiredPersonnel(), m1.getRequiredPersonnel());
            }
            return Integer.compare(m2.getRequiredTrucks(), m1.getRequiredTrucks());
        });

        // Sort trucks and personnel by ID
        trucks.sort(Comparator.comparing(Truck::getId));
        personnel.sort(Comparator.comparing(Personnel::getId));

        Map<String, Map<String, Object>> allocations = new HashMap<>();

        for (Move move : moves) {
            int allocatedTrucks = 0;
            int allocatedPersonnel = 0;

            // Allocate trucks
            for (Truck truck : trucks) {
                if (!truck.isAllocated() && allocatedTrucks < move.getRequiredTrucks()) {
                    truck.setAllocated(true);
                    allocatedTrucks++;
                }
            }

            // Allocate personnel
            for (Personnel person : personnel) {
                if (!person.isAllocated() && allocatedPersonnel < move.getRequiredPersonnel()) {
                    person.setAllocated(true);
                    allocatedPersonnel++;
                }
            }

            // Check if all required resources are allocated
            if (allocatedTrucks < move.getRequiredTrucks() || allocatedPersonnel < move.getRequiredPersonnel()) {
                throw new RuntimeException("Insufficient resources for move " + move.getId());
            }

            // Store allocation
            Map<String, Object> resources = new HashMap<>();
            resources.put("trucks", allocatedTrucks);
            resources.put("personnel", allocatedPersonnel);
            allocations.put(move.getId(), resources);
        }

        return allocations;
    }

    public static void main(String[] args) {
        // Create moves
        List<Move> moves = Arrays.asList(
                new Move("move1", 2, 4),
                new Move("move2", 1, 2),
                new Move("move3", 3, 6)
        );

        // Create trucks
        List<Truck> trucks = Arrays.asList(
                new Truck("truck1"),
                new Truck("truck2"),
                new Truck("truck3"),
                new Truck("truck4"),
                new Truck("truck5")
        );

        // Create personnel
        List<Personnel> personnel = Arrays.asList(
                new Personnel("person1"),
                new Personnel("person2"),
                new Personnel("person3"),
                new Personnel("person4"),
                new Personnel("person5"),
                new Personnel("person6"),
                new Personnel("person7"),
                new Personnel("person8")
        );

        try {
            Map<String, Map<String, Object>> allocations = allocateResources(moves, trucks, personnel);
            System.out.println("Allocations:");
            for (Map.Entry<String, Map<String, Object>> entry : allocations.entrySet()) {
                System.out.println(entry.getKey() + ": trucks=" + entry.getValue().get("trucks") + ", personnel=" + entry.getValue().get("personnel"));
            }
        } catch (RuntimeException e) {
            System.err.println(e.getMessage());
        }
    }
}
```
