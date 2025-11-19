"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftbuy.site
Prompt: Explain how to integrate a scoring system into a puzzle game like "Bubble Ocean" using Unity or another game development framework.
Generated: DETERMINISTIC_a2719cf41454fc1b
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

/// <summary>
/// Manages the scoring system for the Bubble Ocean puzzle game.
/// This class handles score updates, displaying the score, and resetting the score.
/// </summary>
public class ScoreManager : MonoBehaviour
{
    // Variable to hold the player's score
    private int score;

    // UI Text element to display the score
    [SerializeField]
    private Text scoreText;

    /// <summary>
    /// Initializes the score to zero and updates the UI display.
    /// </summary>
    void Start()
    {
        ResetScore();
    }

    /// <summary>
    /// Resets the score to zero and updates the UI.
    /// </summary>
    public void ResetScore()
    {
        score = 0;
        UpdateScoreDisplay();
    }

    /// <summary>
    /// Increases the score by the specified amount.
    /// </summary>
    /// <param name="points">The number of points to add to the score.</param>
    public void AddScore(int points)
    {
        // Validate the points to ensure it's a positive integer
        if (points < 0)
        {
            Debug.LogError("Points to add must be non-negative.");
            return;
        }
        
        score += points;
        UpdateScoreDisplay();
    }

    /// <summary>
    /// Updates the score display on the UI.
    /// </summary>
    private void UpdateScoreDisplay()
    {
        // Ensure the UI Text element is assigned
        if (scoreText == null)
        {
            Debug.LogError("ScoreText is not assigned in the Inspector.");
            return;
        }
        
        scoreText.text = "Score: " + score.ToString();
    }

    /// <summary>
    /// Retrieves the current score.
    /// </summary>
    /// <returns>The current score as an integer.</returns>
    public int GetScore()
    {
        return score;
    }
}
```

### Integration Instructions:
1. Attach the `ScoreManager` script to a GameObject in your Unity scene.
2. Assign a UI Text element to the `scoreText` field in the Inspector.
3. Call the `AddScore(int points)` method whenever a player achieves a scoring action in the game (e.g., clearing bubbles).
4. Call `ResetScore()` at the start of a new game or level to reset the score.
