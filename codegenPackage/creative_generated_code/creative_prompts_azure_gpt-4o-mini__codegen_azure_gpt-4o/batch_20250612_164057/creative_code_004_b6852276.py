"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.atletismomg.org.br
Prompt: Design a data structure in Java to manage the list of registered clubs and their respective athletes as outlined on the FMA site.
Generated: DETERMINISTIC_b685227669cdc677
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Represents a system to manage clubs and their athletes.
 */
public class ClubManager {

    // Data structure for managing clubs and their athletes
    private final Map<String, List<String>> clubAthletesMap;

    /**
     * Constructor to initialize the club manager.
     */
    public ClubManager() {
        clubAthletesMap = new HashMap<>();
    }

    /**
     * Registers a new club in the system.
     *
     * @param clubName The name of the club to register.
     * @throws IllegalArgumentException if the club already exists or name is invalid.
     */
    public void registerClub(String clubName) {
        if (clubName == null || clubName.isEmpty()) {
            throw new IllegalArgumentException("Club name cannot be null or empty.");
        }
        if (clubAthletesMap.containsKey(clubName)) {
            throw new IllegalArgumentException("Club already exists: " + clubName);
        }
        clubAthletesMap.put(clubName, new ArrayList<>());
    }

    /**
     * Adds a new athlete to a registered club.
     *
     * @param clubName   The name of the club where the athlete should be added.
     * @param athleteName The name of the athlete to add.
     * @throws IllegalArgumentException if the club does not exist or athlete name is invalid.
     */
    public void addAthlete(String clubName, String athleteName) {
        if (clubName == null || clubName.isEmpty() || athleteName == null || athleteName.isEmpty()) {
            throw new IllegalArgumentException("Club name and athlete name cannot be null or empty.");
        }
        if (!clubAthletesMap.containsKey(clubName)) {
            throw new IllegalArgumentException("Club does not exist: " + clubName);
        }
        clubAthletesMap.get(clubName).add(athleteName);
    }

    /**
     * Returns a list of athletes registered in a specific club.
     *
     * @param clubName The name of the club to fetch athletes for.
     * @return List of athletes in the club.
     * @throws IllegalArgumentException if the club does not exist.
     */
    public List<String> getAthletes(String clubName) {
        if (clubName == null || clubName.isEmpty()) {
            throw new IllegalArgumentException("Club name cannot be null or empty.");
        }
        if (!clubAthletesMap.containsKey(clubName)) {
            throw new IllegalArgumentException("Club does not exist: " + clubName);
        }
        return new ArrayList<>(clubAthletesMap.get(clubName)); // Return a copy to prevent external modification
    }

    /**
     * Returns a list of all registered clubs.
     *
     * @return List of club names.
     */
    public List<String> getRegisteredClubs() {
        return new ArrayList<>(clubAthletesMap.keySet()); // Return a copy to prevent external modification
    }

    /**
     * Removes an athlete from a specific club.
     *
     * @param clubName    The name of the club.
     * @param athleteName The name of the athlete to remove.
     * @throws IllegalArgumentException if the club does not exist or athlete is not found.
     */
    public void removeAthlete(String clubName, String athleteName) {
        if (clubName == null || clubName.isEmpty() || athleteName == null || athleteName.isEmpty()) {
            throw new IllegalArgumentException("Club name and athlete name cannot be null or empty.");
        }
        if (!clubAthletesMap.containsKey(clubName)) {
            throw new IllegalArgumentException("Club does not exist: " + clubName);
        }
        List<String> athletes = clubAthletesMap.get(clubName);
        if (!athletes.remove(athleteName)) {
            throw new IllegalArgumentException("Athlete not found in club: " + athleteName);
        }
    }

    /**
     * Removes a club and all its athletes from the system.
     *
     * @param clubName The name of the club to remove.
     * @throws IllegalArgumentException if the club does not exist.
     */
    public void removeClub(String clubName) {
        if (clubName == null || clubName.isEmpty()) {
            throw new IllegalArgumentException("Club name cannot be null or empty.");
        }
        if (!clubAthletesMap.containsKey(clubName)) {
            throw new IllegalArgumentException("Club does not exist: " + clubName);
        }
        clubAthletesMap.remove(clubName);
    }

    /**
     * Main method for demonstration purposes.
     */
    public static void main(String[] args) {
        try {
            ClubManager clubManager = new ClubManager();

            // Register clubs
            clubManager.registerClub("ClubA");
            clubManager.registerClub("ClubB");

            // Add athletes
            clubManager.addAthlete("ClubA", "John Doe");
            clubManager.addAthlete("ClubA", "Jane Smith");
            clubManager.addAthlete("ClubB", "Alice Brown");

            // Get and print athletes
            System.out.println("Athletes in ClubA: " + clubManager.getAthletes("ClubA"));
            System.out.println("Athletes in ClubB: " + clubManager.getAthletes("ClubB"));

            // Remove athlete
            clubManager.removeAthlete("ClubA", "John Doe");
            System.out.println("Athletes in ClubA after removal: " + clubManager.getAthletes("ClubA"));

            // Remove club
            clubManager.removeClub("ClubB");
            System.out.println("Registered clubs after removal: " + clubManager.getRegisteredClubs());

        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
