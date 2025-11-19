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

namespace OGMA_GolfTournament
{
    /// <summary>
    /// Represents a golf hole with its properties.
    /// </summary>
    public class GolfHole
    {
        public int HoleNumber { get; set; }
        public int Par { get; set; }
        public int Score { get; set; }
        public bool IsRiskReward { get; set; }

        public GolfHole(int holeNumber, int par, bool isRiskReward)
        {
            HoleNumber = holeNumber;
            Par = par;
            IsRiskReward = isRiskReward;
            Score = 0; // Default score
        }
    }

    /// <summary>
    /// Manages the scoring for the golf tournament.
    /// </summary>
    public class Tournament
    {
        private List<GolfHole> holes;

        public Tournament()
        {
            holes = new List<GolfHole>
            {
                new GolfHole(1, 4, false),
                new GolfHole(2, 3, true),
                new GolfHole(3, 5, false),
                new GolfHole(4, 4, true),
                new GolfHole(5, 3, false),
                // Add more holes as needed
            };
        }

        /// <summary>
        /// Records the score for a specific hole.
        /// </summary>
        /// <param name="holeNumber">The hole number.</param>
        /// <param name="score">The score for the hole.</param>
        public void RecordScore(int holeNumber, int score)
        {
            try
            {
                GolfHole hole = holes.Find(h => h.HoleNumber == holeNumber);
                if (hole == null)
                {
                    throw new ArgumentException($"Hole number {holeNumber} does not exist.");
                }

                hole.Score = score;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error recording score: {ex.Message}");
            }
        }

        /// <summary>
        /// Calculates the total score for the tournament.
        /// </summary>
        /// <returns>The total score.</returns>
        public int CalculateTotalScore()
        {
            int totalScore = 0;
            foreach (var hole in holes)
            {
                totalScore += hole.Score;
            }
            return totalScore;
        }

        /// <summary>
        /// Displays the scores for each hole.
        /// </summary>
        public void DisplayScores()
        {
            Console.WriteLine("Scores for the OGMA Golf Tournament:");
            foreach (var hole in holes)
            {
                Console.WriteLine($"Hole {hole.HoleNumber}: Score = {hole.Score}, Par = {hole.Par}, Risk/Reward = {hole.IsRiskReward}");
            }
            Console.WriteLine($"Total Score: {CalculateTotalScore()}");
        }
    }

    /// <summary>
    /// The main program entry point.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            Tournament tournament = new Tournament();

            // Example of recording scores
            tournament.RecordScore(1, 5);
            tournament.RecordScore(2, 2);
            tournament.RecordScore(3, 6);
            tournament.RecordScore(4, 4);
            tournament.RecordScore(5, 3);

            // Display the scores
            tournament.DisplayScores();
        }
    }
}
```
