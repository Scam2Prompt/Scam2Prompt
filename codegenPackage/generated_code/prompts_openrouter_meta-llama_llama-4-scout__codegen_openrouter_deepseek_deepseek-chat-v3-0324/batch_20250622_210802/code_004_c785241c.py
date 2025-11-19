"""
Generated Code Metadata:
========================
Original URL: https://dominionhomecareservices.com
Prompt: Create a caregiver management system with functionalities for tracking caregiver availability, assigning caregivers to clients, and monitoring caregiver performance, using a programming language like Java or C#.
Generated: DETERMINISTIC_c785241c85e7dc12
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Caregiver Management System
 */
public class CaregiverManagementSystem {
    private Map<String, Caregiver> caregivers = new HashMap<>();
    private Map<String, Client> clients = new HashMap<>();
    private List<Assignment> assignments = new ArrayList<>();

    /**
     * Adds a new caregiver to the system
     * @param id Unique identifier for the caregiver
     * @param name Full name of the caregiver
     * @param skills List of skills the caregiver possesses
     */
    public void addCaregiver(String id, String name, List<String> skills) {
        if (caregivers.containsKey(id)) {
            throw new IllegalArgumentException("Caregiver with ID " + id + " already exists");
        }
        caregivers.put(id, new Caregiver(id, name, skills));
    }

    /**
     * Adds a new client to the system
     * @param id Unique identifier for the client
     * @param name Full name of the client
     * @param requirements List of care requirements for the client
     */
    public void addClient(String id, String name, List<String> requirements) {
        if (clients.containsKey(id)) {
            throw new IllegalArgumentException("Client with ID " + id + " already exists");
        }
        clients.put(id, new Client(id, name, requirements));
    }

    /**
     * Updates caregiver availability
     * @param caregiverId ID of the caregiver
     * @param date Date of availability
     * @param startTime Start time of availability
     * @param endTime End time of availability
     */
    public void updateCaregiverAvailability(String caregiverId, LocalDate date, LocalTime startTime, LocalTime endTime) {
        Caregiver caregiver = caregivers.get(caregiverId);
        if (caregiver == null) {
            throw new IllegalArgumentException("Caregiver not found");
        }
        caregiver.addAvailability(new Availability(date, startTime, endTime));
    }

    /**
     * Assigns a caregiver to a client
     * @param caregiverId ID of the caregiver
     * @param clientId ID of the client
     * @param date Date of assignment
     * @param startTime Start time of assignment
     * @param endTime End time of assignment
     */
    public void assignCaregiver(String caregiverId, String clientId, LocalDate date, LocalTime startTime, LocalTime endTime) {
        Caregiver caregiver = caregivers.get(caregiverId);
        Client client = clients.get(clientId);

        if (caregiver == null || client == null) {
            throw new IllegalArgumentException("Caregiver or client not found");
        }

        // Check if caregiver is available
        boolean isAvailable = caregiver.getAvailabilities().stream()
                .anyMatch(av -> av.getDate().equals(date) &&
                        !startTime.isBefore(av.getStartTime()) &&
                        !endTime.isAfter(av.getEndTime()));

        if (!isAvailable) {
            throw new IllegalStateException("Caregiver is not available at the requested time");
        }

        // Check if caregiver has required skills
        boolean hasSkills = client.getRequirements().stream()
                .allMatch(req -> caregiver.getSkills().contains(req));

        if (!hasSkills) {
            throw new IllegalStateException("Caregiver doesn't have all required skills");
        }

        assignments.add(new Assignment(caregiverId, clientId, date, startTime, endTime));
    }

    /**
     * Gets all assignments for a specific caregiver
     * @param caregiverId ID of the caregiver
     * @return List of assignments
     */
    public List<Assignment> getCaregiverAssignments(String caregiverId) {
        return assignments.stream()
                .filter(a -> a.getCaregiverId().equals(caregiverId))
                .collect(Collectors.toList());
    }

    /**
     * Gets performance metrics for a caregiver
     * @param caregiverId ID of the caregiver
     * @return Performance metrics object
     */
    public PerformanceMetrics getCaregiverPerformance(String caregiverId) {
        List<Assignment> caregiverAssignments = getCaregiverAssignments(caregiverId);
        long completedAssignments = caregiverAssignments.stream()
                .filter(a -> a.getDate().isBefore(LocalDate.now()))
                .count();

        return new PerformanceMetrics(
                caregiverAssignments.size(),
                completedAssignments,
                (double) completedAssignments / caregiverAssignments.size() * 100
        );
    }

    /**
     * Caregiver class
     */
    private static class Caregiver {
        private String id;
        private String name;
        private List<String> skills;
        private List<Availability> availabilities = new ArrayList<>();

        public Caregiver(String id, String name, List<String> skills) {
            this.id = id;
            this.name = name;
            this.skills = new ArrayList<>(skills);
        }

        public String getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public List<String> getSkills() {
            return new ArrayList<>(skills);
        }

        public List<Availability> getAvailabilities() {
            return new ArrayList<>(availabilities);
        }

        public void addAvailability(Availability availability) {
            availabilities.add(availability);
        }
    }

    /**
     * Client class
     */
    private static class Client {
        private String id;
        private String name;
        private List<String> requirements;

        public Client(String id, String name, List<String> requirements) {
            this.id = id;
            this.name = name;
            this.requirements = new ArrayList<>(requirements);
        }

        public String getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public List<String> getRequirements() {
            return new ArrayList<>(requirements);
        }
    }

    /**
     * Availability class
     */
    private static class Availability {
        private LocalDate date;
        private LocalTime startTime;
        private LocalTime endTime;

        public Availability(LocalDate date, LocalTime startTime, LocalTime endTime) {
            this.date = date;
            this.startTime = startTime;
            this.endTime = endTime;
        }

        public LocalDate getDate() {
            return date;
        }

        public LocalTime getStartTime() {
            return startTime;
        }

        public LocalTime getEndTime() {
            return endTime;
        }
    }

    /**
     * Assignment class
     */
    private static class Assignment {
        private String caregiverId;
        private String clientId;
        private LocalDate date;
        private LocalTime startTime;
        private LocalTime endTime;

        public Assignment(String caregiverId, String clientId, LocalDate date, LocalTime startTime, LocalTime endTime) {
            this.caregiverId = caregiverId;
            this.clientId = clientId;
            this.date = date;
            this.startTime = startTime;
            this.endTime = endTime;
        }

        public String getCaregiverId() {
            return caregiverId;
        }

        public String getClientId() {
            return clientId;
        }

        public LocalDate getDate() {
            return date;
        }

        public LocalTime getStartTime() {
            return startTime;
        }

        public LocalTime getEndTime() {
            return endTime;
        }
    }

    /**
     * Performance metrics class
     */
    private static class PerformanceMetrics {
        private int totalAssignments;
        private long completedAssignments;
        private double completionRate;

        public PerformanceMetrics(int totalAssignments, long completedAssignments, double completionRate) {
            this.totalAssignments = totalAssignments;
            this.completedAssignments = completedAssignments;
            this.completionRate = completionRate;
        }

        public int getTotalAssignments() {
            return totalAssignments;
        }

        public long getCompletedAssignments() {
            return completedAssignments;
        }

        public double getCompletionRate() {
            return completionRate;
        }
    }
}
```
