"""
Generated Code Metadata:
========================
Original URL: https://rokometni.agencijau3p.si
Prompt: Develop a Java code to implement a basic membership management system for a handball club like RK Kočevje, including features for player registration, team assignment, and contact information management.
Generated: DETERMINISTIC_55d8f7e51d2b6472
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

// Represents a player in the handball club
class Player {
    private String name;
    private String email;
    private String phoneNumber;
    private Team team;

    /**
     * Constructs a new player.
     * 
     * @param name        The player's name.
     * @param email       The player's email.
     * @param phoneNumber The player's phone number.
     */
    public Player(String name, String email, String phoneNumber) {
        this.name = name;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.team = null;
    }

    // Getters and setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public Team getTeam() {
        return team;
    }

    public void setTeam(Team team) {
        this.team = team;
    }
}

// Represents a team in the handball club
class Team {
    private String name;
    private List<Player> players;

    /**
     * Constructs a new team.
     * 
     * @param name The team's name.
     */
    public Team(String name) {
        this.name = name;
        this.players = new ArrayList<>();
    }

    // Getters and setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Player> getPlayers() {
        return players;
    }

    public void addPlayer(Player player) {
        this.players.add(player);
        player.setTeam(this);
    }

    public void removePlayer(Player player) {
        this.players.remove(player);
        player.setTeam(null);
    }
}

// Represents the handball club's membership management system
public class MembershipManagementSystem {
    private Map<String, Player> players;
    private Map<String, Team> teams;

    /**
     * Constructs a new membership management system.
     */
    public MembershipManagementSystem() {
        this.players = new HashMap<>();
        this.teams = new HashMap<>();
    }

    /**
     * Registers a new player.
     * 
     * @param name        The player's name.
     * @param email       The player's email.
     * @param phoneNumber The player's phone number.
     * @return The newly created player.
     */
    public Player registerPlayer(String name, String email, String phoneNumber) {
        if (players.containsKey(email)) {
            throw new RuntimeException("Player with email already exists.");
        }
        Player player = new Player(name, email, phoneNumber);
        players.put(email, player);
        return player;
    }

    /**
     * Creates a new team.
     * 
     * @param name The team's name.
     * @return The newly created team.
     */
    public Team createTeam(String name) {
        if (teams.containsKey(name)) {
            throw new RuntimeException("Team with name already exists.");
        }
        Team team = new Team(name);
        teams.put(name, team);
        return team;
    }

    /**
     * Assigns a player to a team.
     * 
     * @param email The player's email.
     * @param teamName The team's name.
     */
    public void assignPlayerToTeam(String email, String teamName) {
        Player player = players.get(email);
        Team team = teams.get(teamName);
        if (player == null || team == null) {
            throw new RuntimeException("Player or team does not exist.");
        }
        team.addPlayer(player);
    }

    /**
     * Prints out all players and their teams.
     */
    public void printPlayers() {
        for (Player player : players.values()) {
            System.out.println("Name: " + player.getName() + ", Email: " + player.getEmail() + ", Phone Number: " + player.getPhoneNumber() + ", Team: " + (player.getTeam() != null ? player.getTeam().getName() : "None"));
        }
    }

    /**
     * Prints out all teams and their players.
     */
    public void printTeams() {
        for (Team team : teams.values()) {
            System.out.println("Team: " + team.getName());
            for (Player player : team.getPlayers()) {
                System.out.println("  - " + player.getName() + ", " + player.getEmail() + ", " + player.getPhoneNumber());
            }
        }
    }

    public static void main(String[] args) {
        MembershipManagementSystem system = new MembershipManagementSystem();

        // Register players
        Player player1 = system.registerPlayer("John Doe", "john@example.com", "1234567890");
        Player player2 = system.registerPlayer("Jane Doe", "jane@example.com", "0987654321");

        // Create teams
        Team teamA = system.createTeam("Team A");
        Team teamB = system.createTeam("Team B");

        // Assign players to teams
        system.assignPlayerToTeam("john@example.com", "Team A");
        system.assignPlayerToTeam("jane@example.com", "Team B");

        // Print out players and teams
        system.printPlayers();
        system.printTeams();
    }
}
```
