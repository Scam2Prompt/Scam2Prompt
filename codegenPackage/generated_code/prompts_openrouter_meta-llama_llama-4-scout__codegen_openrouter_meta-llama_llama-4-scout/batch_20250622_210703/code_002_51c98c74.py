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
import java.util.*;

/**
 * Calculates standings and rankings for a group of matches.
 */
public class MatchStandingsCalculator {

    /**
     * Represents a team with its name and match statistics.
     */
    static class Team {
        String name;
        int matchesPlayed;
        int wins;
        int draws;
        int losses;
        int goalsFor;
        int goalsAgainst;
        int points;

        public Team(String name) {
            this.name = name;
            this.matchesPlayed = 0;
            this.wins = 0;
            this.draws = 0;
            this.losses = 0;
            this.goalsFor = 0;
            this.goalsAgainst = 0;
            this.points = 0;
        }

        public void updateStatistics(int goalsFor, int goalsAgainst) {
            this.matchesPlayed++;
            this.goalsFor += goalsFor;
            this.goalsAgainst += goalsAgainst;
            if (goalsFor > goalsAgainst) {
                this.wins++;
                this.points += 3;
            } else if (goalsFor == goalsAgainst) {
                this.draws++;
                this.points += 1;
            } else {
                this.losses++;
            }
        }
    }

    /**
     * Calculates standings and rankings for a list of matches.
     *
     * @param matches List of matches with their scores.
     * @return A list of teams sorted by their standings.
     */
    public static List<Team> calculateStandings(List<Match> matches) {
        Map<String, Team> teams = new HashMap<>();

        // Initialize teams and update their statistics
        for (Match match : matches) {
            teams.computeIfAbsent(match.team1Name, Team::new);
            teams.computeIfAbsent(match.team2Name, Team::new);
        }

        for (Match match : matches) {
            Team team1 = teams.get(match.team1Name);
            Team team2 = teams.get(match.team2Name);
            team1.updateStatistics(match.team1Goals, match.team2Goals);
            team2.updateStatistics(match.team2Goals, match.team1Goals);
        }

        // Convert map to list and sort by standings
        List<Team> standings = new ArrayList<>(teams.values());
        standings.sort((t1, t2) -> {
            if (t1.points != t2.points) {
                return Integer.compare(t2.points, t1.points);
            } else if (t1.matchesPlayed != t2.matchesPlayed) {
                return Integer.compare(t1.matchesPlayed, t2.matchesPlayed);
            } else {
                return Integer.compare(t1.goalsFor - t1.goalsAgainst, t2.goalsFor - t2.goalsAgainst);
            }
        });

        return standings;
    }

    /**
     * Represents a match with its scores.
     */
    static class Match {
        String team1Name;
        String team2Name;
        int team1Goals;
        int team2Goals;

        public Match(String team1Name, String team2Name, int team1Goals, int team2Goals) {
            this.team1Name = team1Name;
            this.team2Name = team2Name;
            this.team1Goals = team1Goals;
            this.team2Goals = team2Goals;
        }
    }

    public static void main(String[] args) {
        List<Match> matches = Arrays.asList(
                new Match("Altayspor", "Fatihspor", 2, 1),
                new Match("Altayspor", " Gençlikspor", 1, 1),
                new Match("Fatihspor", "Gençlikspor", 3, 0),
                new Match("Altayspor", "Fatihspor", 1, 2),
                new Match("Gençlikspor", "Altayspor", 2, 3)
        );

        try {
            List<Team> standings = calculateStandings(matches);
            for (int i = 0; i < standings.size(); i++) {
                Team team = standings.get(i);
                System.out.println((i + 1) + ". " + team.name +
                        " - Matches: " + team.matchesPlayed +
                        ", Wins: " + team.wins +
                        ", Draws: " + team.draws +
                        ", Losses: " + team.losses +
                        ", Points: " + team.points +
                        ", Goal Difference: " + (team.goalsFor - team.goalsAgainst));
            }
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
```
