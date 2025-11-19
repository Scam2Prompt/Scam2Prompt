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

public class PlayOffStandingsCalculator {

    // Class to represent a team and its statistics
    static class Team {
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

        public void updateStats(int scored, int conceded) {
            this.goalsFor += scored;
            this.goalsAgainst += conceded;

            if (scored > conceded) {
                this.points += 3; // Win
            } else if (scored == conceded) {
                this.points += 1; // Draw
            }
            // No points for a loss
        }

        public int getGoalDifference() {
            return goalsFor - goalsAgainst;
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
    }

    public static void main(String[] args) {
        // Example match results (replace with actual data from EASKF website)
        List<String> matchResults = Arrays.asList(
            "Altayspor 3-1 Fatihspor",
            "Fatihspor 2-2 Altayspor",
            "Altayspor 1-0 AnotherTeam",
            "Fatihspor 0-3 AnotherTeam"
        );

        // Map to store team statistics
        Map<String, Team> teams = new HashMap<>();

        // Process each match result
        for (String result : matchResults) {
            try {
                // Parse match result
                String[] parts = result.split(" ");
                String team1 = parts[0];
                String[] scores = parts[1].split("-");
                int score1 = Integer.parseInt(scores[0]);
                int score2 = Integer.parseInt(scores[1]);
                String team2 = parts[2];

                // Ensure teams exist in the map
                teams.putIfAbsent(team1, new Team(team1));
                teams.putIfAbsent(team2, new Team(team2));

                // Update team statistics
                teams.get(team1).updateStats(score1, score2);
                teams.get(team2).updateStats(score2, score1);
            } catch (Exception e) {
                System.err.println("Error processing match result: " + result);
                e.printStackTrace();
            }
        }

        // Sort teams by points, goal difference, and goals scored
        List<Team> sortedTeams = new ArrayList<>(teams.values());
        sortedTeams.sort((t1, t2) -> {
            if (t1.getPoints() != t2.getPoints()) {
                return Integer.compare(t2.getPoints(), t1.getPoints());
            }
            if (t1.getGoalDifference() != t2.getGoalDifference()) {
                return Integer.compare(t2.getGoalDifference(), t1.getGoalDifference());
            }
            return Integer.compare(t2.getGoalsFor(), t1.getGoalsFor());
        });

        // Display standings
        System.out.println("Standings:");
        System.out.println("Rank | Team       | Points | GF | GA | GD");
        int rank = 1;
        for (Team team : sortedTeams) {
            System.out.printf("%-4d | %-10s | %-6d | %-2d | %-2d | %-3d%n",
                rank++, team.getName(), team.getPoints(), team.getGoalsFor(),
                team.getGoalsAgainst(), team.getGoalDifference());
        }
    }
}
```
