"""
Generated Code Metadata:
========================
Original URL: https://easkf.org
Prompt: Generate a code snippet in Java to calculate the standings and rankings for the 2.Amatör Play-Off group matches, such as the Altayspor vs. Fatihspor match, based on the scores provided on the EASKF website.
Generated: DETERMINISTIC_51c98c7480ff7ecd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;
import java.util.Comparator;

// Class to represent a team and its statistics
class Team {
    private String name;
    private int points;
    private int goalsFor;
    private int goalsAgainst;

    public Team(String name) {
        this.name = name;
        this.points = 0;
        this.goalsFor = 0;
        this.goalsAgainst = 0;
    }

    public String getName() {
        return name;
    }

    public int getPoints() {
        return points;
    }

    public int getGoalsFor() {
        return goalsFor;
    }

    public int getGoalsAgainst() {
        return goalsAgainst;
    }

    public void addMatchResult(int goalsScored, int goalsConceded) {
        this.goalsFor += goalsScored;
        this.goalsAgainst += goalsConceded;
        if (goalsScored > goalsConceded) {
            this.points += 3; // Win
        } else if (goalsScored == goalsConceded) {
            this.points += 1; // Draw
        }
        // No points for loss
    }
}

// Class to manage the league standings
public class LeagueStandings {
    private Map<String, Team> teams;

    public LeagueStandings() {
        teams = new HashMap<>();
    }

    // Method to add a match result
    public void addMatch(String team1Name, int team1Score, String team2Name, int team2Score) {
        teams.putIfAbsent(team1Name, new Team(team1Name));
        teams.putIfAbsent(team2Name, new Team(team2Name));

        Team team1 = teams.get(team1Name);
        Team team2 = teams.get(team2Name);

        team1.addMatchResult(team1Score, team2Score);
        team2.addMatchResult(team2Score, team1Score);
    }

    // Method to get the standings sorted by points and goal difference
    public List<Team> getStandings() {
        List<Team> standings = new ArrayList<>(teams.values());
        standings.sort(Comparator.comparingInt(Team::getPoints)
                .reversed()
                .thenComparingInt(t -> t.getGoalsFor() - t.getGoalsAgainst())
                .reversed());
        return standings;
    }

    // Main method for testing
    public static void main(String[] args) {
        LeagueStandings league = new LeagueStandings();

        // Example match results
        league.addMatch("Altayspor", 2, "Fatihspor", 1);
        league.addMatch("Altayspor", 3, "Fatihspor", 3);
        league.addMatch("Fatihspor", 0, "Altayspor", 1);

        // Display standings
        List<Team> standings = league.getStandings();
        System.out.println("Standings:");
        for (Team team : standings) {
            System.out.printf("%s - Points: %d, Goals For: %d, Goals Against: %d%n",
                    team.getName(), team.getPoints(), team.getGoalsFor(), team.getGoalsAgainst());
        }
    }
}
```
