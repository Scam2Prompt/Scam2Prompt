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
 * Represents a club with a name and a list of registered athletes.
 */
class Club {
    private String name;
    private List<String> athletes;

    public Club(String name) {
        this.name = name;
        this.athletes = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public List<String> getAthletes() {
        return athletes;
    }

    /**
     * Adds an athlete to the club.
     *
     * @param athleteName The name of the athlete to add.
     * @throws IllegalArgumentException if the athlete name is null or empty.
     */
    public void addAthlete(String athleteName) {
        if (athleteName == null || athleteName.trim().isEmpty()) {
            throw new IllegalArgumentException("Athlete name cannot be null or empty.");
        }
        athletes.add(athleteName);
    }

    /**
     * Removes an athlete from the club.
     *
     * @param athleteName The name of the athlete to remove.
     * @throws IllegalArgumentException if the athlete name is null or empty.
     */
    public void removeAthlete(String athleteName) {
        if (athleteName == null || athleteName.trim().isEmpty()) {
            throw new IllegalArgumentException("Athlete name cannot be null or empty.");
        }
        athletes.remove(athleteName);
    }
}

/**
 * Manages a collection of clubs and their respective athletes.
 */
public class ClubManager {
    private Map<String, Club> clubs;

    public ClubManager() {
        this.clubs = new HashMap<>();
    }

    /**
     * Registers a new club.
     *
     * @param clubName The name of the club to register.
     * @throws IllegalArgumentException if the club name is null or empty.
     */
    public void registerClub(String clubName) {
        if (clubName == null || clubName.trim().isEmpty()) {
            throw new IllegalArgumentException("Club name cannot be null or empty.");
        }
        clubs.putIfAbsent(clubName, new Club(clubName));
    }

    /**
     * Adds an athlete to the specified club.
     *
     * @param clubName The name of the club.
     * @param athleteName The name of the athlete to add.
     * @throws IllegalArgumentException if the club name or athlete name is invalid.
     */
    public void addAthleteToClub(String clubName, String athleteName) {
        if (!clubs.containsKey(clubName)) {
            throw new IllegalArgumentException("Club does not exist: " + clubName);
        }
        clubs.get(clubName).addAthlete(athleteName);
    }

    /**
     * Removes an athlete from the specified club.
     *
     * @param clubName The name of the club.
     * @param athleteName The name of the athlete to remove.
     * @throws IllegalArgumentException if the club name or athlete name is invalid.
     */
    public void removeAthleteFromClub(String clubName, String athleteName) {
        if (!clubs.containsKey(clubName)) {
            throw new IllegalArgumentException("Club does not exist: " + clubName);
        }
        clubs.get(clubName).removeAthlete(athleteName);
    }

    /**
     * Retrieves the list of athletes from a specified club.
     *
     * @param clubName The name of the club.
     * @return List of athletes in the club.
     * @throws IllegalArgumentException if the club name is invalid.
     */
    public List<String> getAthletesInClub(String clubName) {
        if (!clubs.containsKey(clubName)) {
            throw new IllegalArgumentException("Club does not exist: " + clubName);
        }
        return new ArrayList<>(clubs.get(clubName).getAthletes());
    }

    public static void main(String[] args) {
        // Example usage
        ClubManager clubManager = new ClubManager();
        clubManager.registerClub("Chess Club");
        clubManager.addAthleteToClub("Chess Club", "Alice Johnson");
        clubManager.addAthleteToClub("Chess Club", "Bob Smith");

        System.out.println("Athletes in Chess Club: " + clubManager.getAthletesInClub("Chess Club"));
        clubManager.removeAthleteFromClub("Chess Club", "Alice Johnson");
        System.out.println("Athletes in Chess Club after removal: " + clubManager.getAthletesInClub("Chess Club"));
    }
}
```
