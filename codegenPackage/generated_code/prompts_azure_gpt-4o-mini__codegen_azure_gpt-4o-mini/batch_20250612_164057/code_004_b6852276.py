"""
Generated Code Metadata:
========================
Original URL: https://www.atletismomg.org.br
Prompt: Design a data structure in Java to manage the list of registered clubs and their respective athletes as outlined on the FMA site.
Generated: DETERMINISTIC_b685227669cdc677
Batch ID: 20250612_164057
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
 * Represents a Club with a name and a list of registered athletes.
 */
class Club {
    private String name;
    private List<Athlete> athletes;

    public Club(String name) {
        this.name = name;
        this.athletes = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public List<Athlete> getAthletes() {
        return athletes;
    }

    public void addAthlete(Athlete athlete) {
        if (athlete != null) {
            athletes.add(athlete);
        } else {
            throw new IllegalArgumentException("Athlete cannot be null");
        }
    }

    public void removeAthlete(Athlete athlete) {
        if (!athletes.remove(athlete)) {
            throw new IllegalArgumentException("Athlete not found in the club");
        }
    }
}

/**
 * Represents an Athlete with a name and an ID.
 */
class Athlete {
    private String name;
    private String id;

    public Athlete(String name, String id) {
        this.name = name;
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    @Override
    public String toString() {
        return "Athlete{" +
                "name='" + name + '\'' +
                ", id='" + id + '\'' +
                '}';
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

    public void addClub(String clubName) {
        if (clubName == null || clubName.isEmpty()) {
            throw new IllegalArgumentException("Club name cannot be null or empty");
        }
        if (!clubs.containsKey(clubName)) {
            clubs.put(clubName, new Club(clubName));
        } else {
            throw new IllegalArgumentException("Club already exists");
        }
    }

    public void removeClub(String clubName) {
        if (!clubs.containsKey(clubName)) {
            throw new IllegalArgumentException("Club not found");
        }
        clubs.remove(clubName);
    }

    public void addAthleteToClub(String clubName, Athlete athlete) {
        Club club = clubs.get(clubName);
        if (club == null) {
            throw new IllegalArgumentException("Club not found");
        }
        club.addAthlete(athlete);
    }

    public void removeAthleteFromClub(String clubName, Athlete athlete) {
        Club club = clubs.get(clubName);
        if (club == null) {
            throw new IllegalArgumentException("Club not found");
        }
        club.removeAthlete(athlete);
    }

    public List<Athlete> getAthletesInClub(String clubName) {
        Club club = clubs.get(clubName);
        if (club == null) {
            throw new IllegalArgumentException("Club not found");
        }
        return club.getAthletes();
    }

    public static void main(String[] args) {
        ClubManager manager = new ClubManager();
        
        // Example usage
        try {
            manager.addClub("Running Club");
            Athlete athlete1 = new Athlete("John Doe", "A001");
            manager.addAthleteToClub("Running Club", athlete1);
            
            System.out.println("Athletes in Running Club: " + manager.getAthletesInClub("Running Club"));
            
            manager.removeAthleteFromClub("Running Club", athlete1);
            System.out.println("Athletes in Running Club after removal: " + manager.getAthletesInClub("Running Club"));
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
