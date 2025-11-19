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
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Represents a football team with its statistics
 */
class Team {
    private String name;
    private int points;
    private int goalsFor;
    private int goalsAgainst;
    private int wins;
    private int draws;
    private int losses;

    public Team(String name) {
        this.name = name;
        this.points = 0;
        this.goalsFor = 0;
        this.goalsAgainst = 0;
        this.wins = 0;
        this.draws = 0;
        this.losses = 0;
    }

    public void addMatchResult(int goalsFor, int goalsAgainst) {
        this.goalsFor += goalsFor;
        this.goalsAgainst += goalsAgainst;

        if (goalsFor > goalsAgainst) {
            this.points += 3;
            this.wins++;
        } else if (goalsFor == goalsAgainst) {
            this.points += 1;
            this.draws++;
        } else {
            this.losses++;
        }
    }

    public String getName() {
        return name;
    }

    public int getPoints() {
        return points;
    }

    public int getGoalDifference() {
        return goalsFor - goalsAgainst;
    }

    public int getGoalsFor() {
        return goalsFor;
    }

    public int getGoalsAgainst() {
        return goalsAgainst;
    }

    public int getWins() {
        return wins;
    }

    public int getDraws() {
        return draws;
    }

    public int getLosses() {
        return losses;
    }
}

/**
 * Represents a football match between two teams
 */
class Match {
    private String homeTeam;
    private String awayTeam;
    private int homeScore;
    private int awayScore;

    public Match(String homeTeam, String awayTeam, int homeScore, int awayScore) {
        this.homeTeam = homeTeam;
        this.awayTeam = awayTeam;
        this.homeScore = homeScore;
        this.awayScore = awayScore;
    }

    public String getHomeTeam() {
        return homeTeam;
    }

    public String getAwayTeam() {
        return awayTeam;
    }

    public int getHomeScore() {
        return homeScore;
    }

    public int getAwayScore() {
        return awayScore;
    }
}

/**
 * Calculates and maintains football standings
 */
public class FootballStandings {
    private Map<String, Team> teams;
    private List<Match> matches;

    public FootballStandings() {
        this.teams = new HashMap<>();
        this.matches = new ArrayList<>();
    }

    /**
     * Adds a match to the standings
     */
    public void addMatch(String homeTeam, String awayTeam, int homeScore, int awayScore) {
        if (homeScore < 0 || awayScore < 0) {
            throw new IllegalArgumentException("Scores cannot be negative");
        }

        matches.add(new Match(homeTeam, awayTeam, homeScore, awayScore));

        // Get or create teams
        Team home = teams.computeIfAbsent(homeTeam, Team::new);
        Team away = teams.computeIfAbsent(awayTeam, Team::new);

        // Update team statistics
        home.addMatchResult(homeScore, awayScore);
        away.addMatchResult(awayScore, homeScore);
    }

    /**
     * Returns the current standings sorted by points, then goal difference, then goals scored
     */
    public List<Team> getStandings() {
        List<Team> standings = new ArrayList<>(teams.values());

        Collections.sort(standings, new Comparator<Team>() {
            @Override
            public int compare(Team t1, Team t2) {
                if (t1.getPoints() != t2.getPoints()) {
                    return Integer.compare(t2.getPoints(), t1.getPoints());
                }
                if (t1.getGoalDifference() != t2.getGoalDifference()) {
                    return Integer.compare(t2.getGoalDifference(), t1.getGoalDifference());
                }
                return Integer.compare(t2.getGoalsFor(), t1.getGoalsFor());
            }
        });

        return standings;
    }

    /**
     * Prints the current standings in a formatted table
     */
    public void printStandings() {
        List<Team> standings = getStandings();

        System.out.println("-------------------------------------------------------------");
        System.out.printf("%-20s %-6s %-6s %-6s %-6s %-6s %-6s %-6s%n", 
                         "Team", "Pts", "Pld", "W", "D", "L", "GF", "GA");
        System.out.println("-------------------------------------------------------------");

        for (Team team : standings) {
            System.out.printf("%-20s %-6d %-6d %-6d %-6d %-6d %-6d %-6d%n",
                            team.getName(),
                            team.getPoints(),
                            team.getWins() + team.getDraws() + team.getLosses(),
                            team.getWins(),
                            team.getDraws(),
                            team.getLosses(),
                            team.getGoalsFor(),
                            team.getGoalsAgainst());
        }
        System.out.println("-------------------------------------------------------------");
    }

    public static void main(String[] args) {
        FootballStandings standings = new FootballStandings();

        // Example matches from 2.Amatör Play-Off group
        standings.addMatch("Altayspor", "Fatihspor", 2, 1);
        standings.addMatch("Altayspor", "Bursaspor", 1, 1);
        standings.addMatch("Fatihspor", "Bursaspor", 0, 2);
        // Add more matches as needed...

        standings.printStandings();
    }
}
```
