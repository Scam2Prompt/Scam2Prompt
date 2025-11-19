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

/// <summary>
/// Represents a golf tournament hole with risk-reward challenges.
/// </summary>
public class GolfHole
{
    public int HoleNumber { get; set; }
    public int Par { get; set; }
    public int RiskRewardDistance { get; set; }
    public bool IsRiskRewardHole { get; set; }

    /// <summary>
    /// Initializes a new instance of the <see cref="GolfHole"/> class.
    /// </summary>
    /// <param name="holeNumber">The hole number.</param>
    /// <param name="par">The par of the hole.</param>
    /// <param name="riskRewardDistance">The risk-reward distance.</param>
    /// <param name="isRiskRewardHole">Indicates if the hole has a risk-reward challenge.</param>
    public GolfHole(int holeNumber, int par, int riskRewardDistance, bool isRiskRewardHole)
    {
        HoleNumber = holeNumber;
        Par = par;
        RiskRewardDistance = riskRewardDistance;
        IsRiskRewardHole = isRiskRewardHole;
    }
}

/// <summary>
/// Represents a golfer's score for a tournament.
/// </summary>
public class GolferScore
{
    public string GolferName { get; set; }
    public Dictionary<int, int> HoleScores { get; set; }

    /// <summary>
    /// Initializes a new instance of the <see cref="GolferScore"/> class.
    /// </summary>
    /// <param name="golferName">The golfer's name.</param>
    public GolferScore(string golferName)
    {
        GolferName = golferName;
        HoleScores = new Dictionary<int, int>();
    }

    /// <summary>
    /// Adds a score for a specific hole.
    /// </summary>
    /// <param name="holeNumber">The hole number.</param>
    /// <param name="score">The score for the hole.</param>
    public void AddHoleScore(int holeNumber, int score)
    {
        if (score < 0)
        {
            throw new ArgumentException("Score cannot be negative.");
        }

        HoleScores[holeNumber] = score;
    }

    /// <summary>
    /// Calculates the total score for the tournament.
    /// </summary>
    /// <returns>The total score.</returns>
    public int CalculateTotalScore()
    {
        int totalScore = 0;
        foreach (var score in HoleScores.Values)
        {
            totalScore += score;
        }
        return totalScore;
    }
}

/// <summary>
/// Represents the OGMA golf tournament.
/// </summary>
public class OgmaGolfTournament
{
    private List<GolfHole> _golfHoles;
    private List<GolferScore> _golferScores;

    /// <summary>
    /// Initializes a new instance of the <see cref="OgmaGolfTournament"/> class.
    /// </summary>
    public OgmaGolfTournament()
    {
        _golfHoles = new List<GolfHole>();
        _golferScores = new List<GolferScore>();
    }

    /// <summary>
    /// Adds a golf hole to the tournament.
    /// </summary>
    /// <param name="golfHole">The golf hole to add.</param>
    public void AddGolfHole(GolfHole golfHole)
    {
        _golfHoles.Add(golfHole);
    }

    /// <summary>
    /// Adds a golfer's score to the tournament.
    /// </summary>
    /// <param name="golferScore">The golfer's score to add.</param>
    public void AddGolferScore(GolferScore golferScore)
    {
        _golferScores.Add(golferScore);
    }

    /// <summary>
    /// Calculates the scores for the tournament, taking into account risk-reward holes.
    /// </summary>
    public void CalculateScores()
    {
        foreach (var golferScore in _golferScores)
        {
            Console.WriteLine($"Golfer: {golferScore.GolferName}");

            foreach (var golfHole in _golfHoles)
            {
                if (golferScore.HoleScores.ContainsKey(golfHole.HoleNumber))
                {
                    int score = golferScore.HoleScores[golfHole.HoleNumber];

                    if (golfHole.IsRiskRewardHole)
                    {
                        // Apply risk-reward scoring
                        if (score <= golfHole.Par - 2)
                        {
                            score -= 1; // -1 for taking the risk
                        }
                        else if (score >= golfHole.Par + 2)
                        {
                            score += 1; // +1 for being conservative
                        }
                    }

                    Console.WriteLine($"Hole {golfHole.HoleNumber}: {score}");
                }
                else
                {
                    Console.WriteLine($"Hole {golfHole.HoleNumber}: No score available.");
                }
            }

            Console.WriteLine($"Total Score: {golferScore.CalculateTotalScore()}");
            Console.WriteLine();
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        OgmaGolfTournament tournament = new OgmaGolfTournament();

        // Initialize golf holes
        GolfHole hole1 = new GolfHole(1, 4, 20, true);
        GolfHole hole2 = new GolfHole(2, 3, 15, false);
        GolfHole hole3 = new GolfHole(3, 5, 30, true);

        tournament.AddGolfHole(hole1);
        tournament.AddGolfHole(hole2);
        tournament.AddGolfHole(hole3);

        // Initialize golfer scores
        GolferScore golfer1 = new GolferScore("Golfer 1");
        golfer1.AddHoleScore(1, 3);
        golfer1.AddHoleScore(2, 4);
        golfer1.AddHoleScore(3, 4);

        GolferScore golfer2 = new GolferScore("Golfer 2");
        golfer2.AddHoleScore(1, 4);
        golfer2.AddHoleScore(2, 3);
        golfer2.AddHoleScore(3, 6);

        tournament.AddGolferScore(golfer1);
        tournament.AddGolferScore(golfer2);

        // Calculate scores
        tournament.CalculateScores();
    }
}
```
