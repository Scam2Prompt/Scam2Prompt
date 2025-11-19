"""
Generated Code Metadata:
========================
Original URL: https://ogma.ca
Prompt: Create a C# program to calculate the scores for the OGMA golf tournament, taking into account the risk-reward holes and challenges of the Hoot course.
Generated: DETERMINISTIC_9c3d535ecf021adc
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;

namespace OGMA_Golf_Tournament
{
    /// <summary>
    /// Represents a golf player with their scores and statistics
    /// </summary>
    public class Player
    {
        public string Name { get; set; }
        public int[] HoleScores { get; set; }
        public int TotalScore { get; set; }
        public int RiskRewardBonus { get; set; }
        public int ChallengesCompleted { get; set; }

        public Player(string name, int holeCount)
        {
            Name = name;
            HoleScores = new int[holeCount];
            TotalScore = 0;
            RiskRewardBonus = 0;
            ChallengesCompleted = 0;
        }

        /// <summary>
        /// Calculates the player's total score including bonuses
        /// </summary>
        public void CalculateTotalScore()
        {
            TotalScore = 0;
            foreach (int score in HoleScores)
            {
                TotalScore += score;
            }
            TotalScore -= RiskRewardBonus;
        }
    }

    /// <summary>
    /// Represents the Hoot golf course with its special features
    /// </summary>
    public class HootCourse
    {
        public int HoleCount { get; }
        public List<int> RiskRewardHoles { get; } // Holes that offer bonus points
        public int MaxChallenges { get; } // Maximum number of challenges available

        public HootCourse(int holeCount, List<int> riskRewardHoles, int maxChallenges)
        {
            if (holeCount <= 0)
                throw new ArgumentException("Hole count must be positive", nameof(holeCount));

            HoleCount = holeCount;
            RiskRewardHoles = riskRewardHoles ?? throw new ArgumentNullException(nameof(riskRewardHoles));
            MaxChallenges = maxChallenges;
        }

        /// <summary>
        /// Checks if a hole is a risk-reward hole
        /// </summary>
        public bool IsRiskRewardHole(int holeNumber)
        {
            if (holeNumber < 1 || holeNumber > HoleCount)
                throw new ArgumentOutOfRangeException(nameof(holeNumber), "Invalid hole number");

            return RiskRewardHoles.Contains(holeNumber);
        }
    }

    /// <summary>
    /// Manages the OGMA golf tournament scoring
    /// </summary>
    public class TournamentManager
    {
        private readonly HootCourse _course;
        private readonly List<Player> _players;

        public TournamentManager(HootCourse course)
        {
            _course = course ?? throw new ArgumentNullException(nameof(course));
            _players = new List<Player>();
        }

        /// <summary>
        /// Adds a player to the tournament
        /// </summary>
        public void AddPlayer(Player player)
        {
            if (player == null)
                throw new ArgumentNullException(nameof(player));

            if (player.HoleScores.Length != _course.HoleCount)
                throw new ArgumentException("Player's hole count doesn't match course", nameof(player));

            _players.Add(player);
        }

        /// <summary>
        /// Records a player's score for a specific hole
        /// </summary>
        public void RecordHoleScore(Player player, int holeNumber, int score)
        {
            if (player == null)
                throw new ArgumentNullException(nameof(player));

            if (holeNumber < 1 || holeNumber > _course.HoleCount)
                throw new ArgumentOutOfRangeException(nameof(holeNumber), "Invalid hole number");

            if (score < 1)
                throw new ArgumentException("Score must be positive", nameof(score));

            player.HoleScores[holeNumber - 1] = score;

            // Apply risk-reward bonus if applicable
            if (_course.IsRiskRewardHole(holeNumber) && score <= 3)
            {
                player.RiskRewardBonus += (4 - score); // 3 points for eagle, 2 for birdie, 1 for par
            }
        }

        /// <summary>
        /// Records a challenge completion for a player
        /// </summary>
        public void RecordChallengeCompletion(Player player)
        {
            if (player == null)
                throw new ArgumentNullException(nameof(player));

            if (player.ChallengesCompleted >= _course.MaxChallenges)
                throw new InvalidOperationException("Player has already completed all challenges");

            player.ChallengesCompleted++;
            player.RiskRewardBonus += 2; // 2 bonus points per challenge
        }

        /// <summary>
        /// Calculates and returns the tournament standings
        /// </summary>
        public List<Player> GetStandings()
        {
            foreach (var player in _players)
            {
                player.CalculateTotalScore();
            }

            // Sort players by total score (ascending - lower is better in golf)
            var standings = new List<Player>(_players);
            standings.Sort((p1, p2) => p1.TotalScore.CompareTo(p2.TotalScore));

            return standings;
        }
    }

    /// <summary>
    /// Main program to run the OGMA golf tournament scoring system
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Set up the Hoot course with 18 holes, risk-reward holes, and max challenges
                var riskRewardHoles = new List<int> { 4, 8, 12, 16 }; // Example risk-reward holes
                var course = new HootCourse(18, riskRewardHoles, 3); // 3 challenges available

                var tournament = new TournamentManager(course);

                // Example: Add players and record their scores
                var player1 = new Player("John Doe", course.HoleCount);
                tournament.AddPlayer(player1);

                // Record scores for player1 (example)
                tournament.RecordHoleScore(player1, 1, 4); // Regular hole
                tournament.RecordHoleScore(player1, 4, 2); // Risk-reward hole (birdie)
                tournament.RecordChallengeCompletion(player1); // Completed a challenge

                var player2 = new Player("Jane Smith", course.HoleCount);
                tournament.AddPlayer(player2);

                // Record scores for player2 (example)
                tournament.RecordHoleScore(player2, 1, 5); // Regular hole
                tournament.RecordHoleScore(player2, 4, 3); // Risk-reward hole (par)
                tournament.RecordChallengeCompletion(player2); // Completed a challenge
                tournament.RecordChallengeCompletion(player2); // Completed another challenge

                // Get and display standings
                var standings = tournament.GetStandings();
                Console.WriteLine("OGMA Golf Tournament Standings:");
                Console.WriteLine("--------------------------------");
                Console.WriteLine("Pos\tPlayer\t\tScore\tBonuses\tChallenges");

                for (int i = 0; i < standings.Count; i++)
                {
                    var player = standings[i];
                    Console.WriteLine($"{i + 1}\t{player.Name}\t{player.TotalScore}\t{player.RiskRewardBonus}\t{player.ChallengesCompleted}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
