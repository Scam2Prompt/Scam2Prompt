"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whelps.io
Prompt: Generate a Unity script to implement free-to-play racing mechanics for WhelpS: Slipstream, allowing players to race without NFTs but still track time spent and achievements.
Generated: DETERMINISTIC_9ef26df672f1f87f
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class RacingManager : MonoBehaviour
{
    // UI Elements
    public Text timerText; // Text element to display the timer
    public Text achievementsText; // Text element to display achievements
    public Button startButton; // Button to start the race

    // Race state
    private bool isRaceActive = false;
    private float raceTime = 0f; // Time tracker for the race
    private int achievementsCount = 0; // Counter for achievements

    void Start()
    {
        // Attach the StartRace method to the button's onClick event
        startButton.onClick.AddListener(StartRace);
        UpdateUI();
    }

    void Update()
    {
        // Update the timer if the race is active
        if (isRaceActive)
        {
            raceTime += Time.deltaTime;
            UpdateUI();
        }
    }

    /// <summary>
    /// Starts the race and resets the timer and achievements.
    /// </summary>
    private void StartRace()
    {
        // Reset race parameters
        raceTime = 0f;
        achievementsCount = 0;
        isRaceActive = true;

        // Start the race
        StartCoroutine(RaceCoroutine());
    }

    /// <summary>
    /// Coroutine to simulate race duration and completion.
    /// </summary>
    private IEnumerator RaceCoroutine()
    {
        // Simulate a race duration of 60 seconds
        yield return new WaitForSeconds(60f);

        // End the race
        EndRace();
    }

    /// <summary>
    /// Ends the race, stops the timer, and updates achievements.
    /// </summary>
    private void EndRace()
    {
        isRaceActive = false;

        // Check for achievements (for example, if the time is less than a threshold)
        if (raceTime < 30f) // Example condition for an achievement
        {
            achievementsCount++;
        }

        // Update UI with final results
        UpdateUI();
    }

    /// <summary>
    /// Updates the UI elements with the current race time and achievements.
    /// </summary>
    private void UpdateUI()
    {
        timerText.text = $"Time: {raceTime:F2} seconds";
        achievementsText.text = $"Achievements: {achievementsCount}";
    }

    /// <summary>
    /// Resets the race data. Can be called externally for a new race session.
    /// </summary>
    public void ResetRaceData()
    {
        raceTime = 0f;
        achievementsCount = 0;
        isRaceActive = false;
        UpdateUI();
    }
}
```
