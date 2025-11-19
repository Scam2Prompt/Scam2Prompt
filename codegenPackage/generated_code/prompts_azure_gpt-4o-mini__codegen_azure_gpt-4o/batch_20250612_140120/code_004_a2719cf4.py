"""
Generated Code Metadata:
========================
Original URL: https://nftbuy.site
Prompt: Explain how to integrate a scoring system into a puzzle game like "Bubble Ocean" using Unity or another game development framework.
Generated: DETERMINISTIC_a2719cf41454fc1b
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using UnityEngine;
using UnityEngine.UI;

public class ScoreManager : MonoBehaviour
{
    // Public variable to display the score in the UI
    public Text scoreText;

    // Private variable to keep track of the score
    private int currentScore;

    // Singleton instance for global access (optional, if needed elsewhere)
    public static ScoreManager Instance { get; private set; }

    private void Awake()
    {
        // Ensure only one instance of ScoreManager exists
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject); // Optional: Persist across scenes
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void Start()
    {
        // Initialize the score to zero
        currentScore = 0;
        UpdateScoreUI();
    }

    /// <summary>
    /// Adds points to the current score.
    /// </summary>
    /// <param name="points">The number of points to add.</param>
    public void AddScore(int points)
    {
        if (points < 0)
        {
            Debug.LogWarning("Points cannot be negative.");
            return;
        }

        currentScore += points;
        UpdateScoreUI();
    }

    /// <summary>
    /// Resets the score to zero.
    /// </summary>
    public void ResetScore()
    {
        currentScore = 0;
        UpdateScoreUI();
    }

    /// <summary>
    /// Updates the score display in the UI.
    /// </summary>
    private void UpdateScoreUI()
    {
        if (scoreText != null)
        {
            scoreText.text = "Score: " + currentScore;
        }
        else
        {
            Debug.LogError("Score Text UI element is not assigned.");
        }
    }

    /// <summary>
    /// Retrieves the current score.
    /// </summary>
    /// <returns>The current score as an integer.</returns>
    public int GetCurrentScore()
    {
        return currentScore;
    }
}
```

### Usage Instructions:
1. Attach this script to a GameObject in your Unity scene (e.g., an empty GameObject named "ScoreManager").
2. Assign a `Text` UI element to the `scoreText` field in the Unity Inspector.
3. Call `AddScore(int points)` whenever the player earns points (e.g., when bubbles are popped).
4. Call `ResetScore()` to reset the score (e.g., when starting a new game).
5. Optionally, use `GetCurrentScore()` to retrieve the score for other purposes (e.g., saving progress).
