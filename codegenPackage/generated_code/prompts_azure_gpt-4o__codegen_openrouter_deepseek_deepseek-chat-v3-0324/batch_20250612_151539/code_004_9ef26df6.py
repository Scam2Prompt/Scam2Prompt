"""
Generated Code Metadata:
========================
Original URL: https://whelps.io
Prompt: Generate a Unity script to implement free-to-play racing mechanics for WhelpS: Slipstream, allowing players to race without NFTs but still track time spent and achievements.
Generated: DETERMINISTIC_9ef26df672f1f87f
Batch ID: 20250612_151539
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
using System;
using System.Collections.Generic;

/// <summary>
/// Free-to-play racing mechanics for WhelpS: Slipstream
/// Tracks player time, achievements, and progress without requiring NFTs
/// </summary>
public class FreeToPlayRacing : MonoBehaviour
{
    [Header("UI References")]
    [SerializeField] private Text timerText;
    [SerializeField] private Text speedText;
    [SerializeField] private GameObject achievementNotification;
    [SerializeField] private Text achievementText;

    [Header("Game Settings")]
    [SerializeField] private float maxSpeed = 120f;
    [SerializeField] private float acceleration = 5f;
    [SerializeField] private float deceleration = 8f;

    private float currentSpeed = 0f;
    private float raceTime = 0f;
    private bool isRacing = false;
    private Dictionary<string, bool> achievements = new Dictionary<string, bool>();

    private const string FIRST_RACE_KEY = "FirstRaceCompleted";
    private const string SPEED_DEMON_KEY = "SpeedDemon";
    private const string MARATHON_KEY = "MarathonRunner";

    private void Start()
    {
        InitializeAchievements();
        LoadPlayerProgress();
    }

    private void Update()
    {
        if (isRacing)
        {
            UpdateRaceTimer();
            HandlePlayerInput();
            UpdateUI();
            CheckAchievements();
        }
    }

    /// <summary>
    /// Initializes the default achievement states
    /// </summary>
    private void InitializeAchievements()
    {
        achievements.Add(FIRST_RACE_KEY, false);
        achievements.Add(SPEED_DEMON_KEY, false);
        achievements.Add(MARATHON_KEY, false);
    }

    /// <summary>
    /// Loads player progress from PlayerPrefs
    /// </summary>
    private void LoadPlayerProgress()
    {
        raceTime = PlayerPrefs.GetFloat("TotalRaceTime", 0f);

        foreach (var key in achievements.Keys)
        {
            achievements[key] = PlayerPrefs.GetInt(key, 0) == 1;
        }
    }

    /// <summary>
    /// Saves player progress to PlayerPrefs
    /// </summary>
    private void SavePlayerProgress()
    {
        PlayerPrefs.SetFloat("TotalRaceTime", raceTime);

        foreach (var achievement in achievements)
        {
            PlayerPrefs.SetInt(achievement.Key, achievement.Value ? 1 : 0);
        }

        PlayerPrefs.Save();
    }

    /// <summary>
    /// Starts a new race session
    /// </summary>
    public void StartRace()
    {
        isRacing = true;
        currentSpeed = 0f;

        if (!achievements[FIRST_RACE_KEY])
        {
            UnlockAchievement(FIRST_RACE_KEY, "First Race Completed!");
        }
    }

    /// <summary>
    /// Ends the current race session
    /// </summary>
    public void EndRace()
    {
        isRacing = false;
        SavePlayerProgress();
    }

    /// <summary>
    /// Updates the race timer while racing
    /// </summary>
    private void UpdateRaceTimer()
    {
        raceTime += Time.deltaTime;
    }

    /// <summary>
    /// Handles player input for acceleration/deceleration
    /// </summary>
    private void HandlePlayerInput()
    {
        if (Input.GetKey(KeyCode.Space) || Input.GetKey(KeyCode.W))
        {
            currentSpeed = Mathf.Min(currentSpeed + acceleration * Time.deltaTime, maxSpeed);
        }
        else
        {
            currentSpeed = Mathf.Max(currentSpeed - deceleration * Time.deltaTime, 0f);
        }
    }

    /// <summary>
    /// Updates the UI elements during gameplay
    /// </summary>
    private void UpdateUI()
    {
        if (timerText != null)
        {
            timerText.text = FormatTime(raceTime);
        }

        if (speedText != null)
        {
            speedText.text = $"Speed: {currentSpeed:F1} km/h";
        }
    }

    /// <summary>
    /// Formats time in HH:MM:SS format
    /// </summary>
    private string FormatTime(float timeInSeconds)
    {
        TimeSpan timeSpan = TimeSpan.FromSeconds(timeInSeconds);
        return string.Format("{0:D2}:{1:D2}:{2:D2}", 
            timeSpan.Hours, 
            timeSpan.Minutes, 
            timeSpan.Seconds);
    }

    /// <summary>
    /// Checks for achievement unlocks during gameplay
    /// </summary>
    private void CheckAchievements()
    {
        // Speed Demon: Reach max speed
        if (!achievements[SPEED_DEMON_KEY] && currentSpeed >= maxSpeed * 0.95f)
        {
            UnlockAchievement(SPEED_DEMON_KEY, "Speed Demon: Reached Top Speed!");
        }

        // Marathon Runner: Race for 30 minutes total
        if (!achievements[MARATHON_KEY] && raceTime >= 1800f)
        {
            UnlockAchievement(MARATHON_KEY, "Marathon Runner: 30 Minutes Racing!");
        }
    }

    /// <summary>
    /// Unlocks an achievement and shows notification
    /// </summary>
    private void UnlockAchievement(string key, string message)
    {
        achievements[key] = true;
        ShowAchievementNotification(message);
        SavePlayerProgress();
    }

    /// <summary>
    /// Displays an achievement notification
    /// </summary>
    private void ShowAchievementNotification(string message)
    {
        if (achievementNotification != null && achievementText != null)
        {
            achievementText.text = message;
            achievementNotification.SetActive(true);
            Invoke("HideAchievementNotification", 3f);
        }
    }

    /// <summary>
    /// Hides the achievement notification
    /// </summary>
    private void HideAchievementNotification()
    {
        if (achievementNotification != null)
        {
            achievementNotification.SetActive(false);
        }
    }

    private void OnApplicationQuit()
    {
        SavePlayerProgress();
    }

    private void OnDestroy()
    {
        SavePlayerProgress();
    }
}
```
