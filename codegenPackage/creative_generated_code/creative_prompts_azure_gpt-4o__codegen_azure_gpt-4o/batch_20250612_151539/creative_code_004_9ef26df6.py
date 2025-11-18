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
using System;
using UnityEngine;

public class RacingMechanics : MonoBehaviour
{
    // Tracks the player's race time
    private float raceTimer;

    // Flags to check race status
    private bool isRacing;
    private bool raceCompleted;

    // Tracks achievements based on player progress
    private int totalRacesCompleted;
    private float bestRaceTime; // Best time achieved by the player

    // UI elements (set these via Unity's Inspector)
    [SerializeField] private UnityEngine.UI.Text timerUI;
    [SerializeField] private UnityEngine.UI.Text raceStatusUI;
    [SerializeField] private UnityEngine.UI.Text achievementsUI;

    // Start is called before the first frame update
    private void Start()
    {
        // Initialize variables
        raceTimer = 0f;
        isRacing = false;
        raceCompleted = false;
        totalRacesCompleted = 0;
        bestRaceTime = Mathf.Infinity;

        // Update UI to reflect initial state
        UpdateUI();
    }

    private void Update()
    {
        // If the race is active, update the timer
        if (isRacing)
        {
            raceTimer += Time.deltaTime;
            UpdateUI();
        }
    }

    /// <summary>
    /// Starts a new race.
    /// </summary>
    public void StartRace()
    {
        if (isRacing)
        {
            Debug.LogWarning("Race is already in progress.");
            return;
        }

        raceTimer = 0f;
        isRacing = true;
        raceCompleted = false;

        Debug.Log("Race started.");
        UpdateUI();
    }

    /// <summary>
    /// Ends the current race.
    /// </summary>
    public void EndRace()
    {
        if (!isRacing)
        {
            Debug.LogWarning("Cannot end race. No race is currently in progress.");
            return;
        }

        isRacing = false;
        raceCompleted = true;
        totalRacesCompleted++;

        // Update best time if applicable
        if (raceTimer < bestRaceTime)
        {
            bestRaceTime = raceTimer;
            Debug.Log("New best time: " + bestRaceTime.ToString("F2") + " seconds.");
        }

        Debug.Log("Race ended. Total time: " + raceTimer.ToString("F2") + " seconds.");
        UpdateUI();
    }

    /// <summary>
    /// Tracks achievements based on player progress.
    /// </summary>
    private string GetAchievements()
    {
        // Example achievements logic
        string achievements = "Achievements:\n";

        achievements += "Total Races Completed: " + totalRacesCompleted + "\n";

        if (bestRaceTime < Mathf.Infinity)
        {
            achievements += "Best Race Time: " + bestRaceTime.ToString("F2") + " seconds\n";
        }
        else
        {
            achievements += "No races completed yet.\n";
        }

        return achievements;
    }

    /// <summary>
    /// Updates the UI to reflect the current game state.
    /// </summary>
    private void UpdateUI()
    {
        if (timerUI != null)
        {
            timerUI.text = "Time: " + raceTimer.ToString("F2") + " seconds";
        }

        if (raceStatusUI != null)
        {
            raceStatusUI.text = isRacing ? "Status: Racing" : (raceCompleted ? "Status: Race Completed" : "Status: Idle");
        }

        if (achievementsUI != null)
        {
            achievementsUI.text = GetAchievements();
        }
    }

    /// <summary>
    /// Resets all race data to its default state.
    /// </summary>
    public void ResetRaceData()
    {
        raceTimer = 0f;
        isRacing = false;
        raceCompleted = false;
        totalRacesCompleted = 0;
        bestRaceTime = Mathf.Infinity;

        Debug.Log("Race data reset.");
        UpdateUI();
    }
}
```
