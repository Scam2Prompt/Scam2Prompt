"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.net
Prompt: Recommend a library or API for integrating Steam achievements into a Unity game, and provide example code for implementation.
Generated: DETERMINISTIC_804cbf88067b9098
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using UnityEngine;
using System;
using System.Runtime.InteropServices;

public class SteamAchievementsManager : MonoBehaviour
{
    // PInvoke for the Steam API
    [DllImport("steam_api64", CallingConvention = CallingConvention.Cdecl)]
    private static extern bool SteamAPI_Init();

    [DllImport("steam_api64", CallingConvention = CallingConvention.Cdecl)]
    private static extern void SteamAPI_RunCallbacks();

    [DllImport("steam_api64", CallingConvention = CallingConvention.Cdecl)]
    private static extern void SteamAPI_Shutdown();

    // Achievements
    private const string ACHIEVEMENT_NAME = "ACHIEVEMENT_NAME_HERE"; // Replace with your achievement name

    void Start()
    {
        // Initialize Steam API
        if (!SteamAPI_Init())
        {
            Debug.LogError("Steam API Initialization failed.");
            return;
        }

        // Example: Unlock an achievement
        UnlockAchievement(ACHIEVEMENT_NAME);
    }

    void Update()
    {
        // Run callbacks for the Steam API
        SteamAPI_RunCallbacks();
    }

    private void UnlockAchievement(string achievementName)
    {
        // Check if the achievement name is valid
        if (string.IsNullOrEmpty(achievementName))
        {
            Debug.LogError("Achievement name is invalid.");
            return;
        }

        // Here we simulate unlocking an achievement
        // You should replace this with actual Steam achievement unlocking logic
        bool success = UnlockSteamAchievement(achievementName);

        if (success)
        {
            Debug.Log($"Achievement '{achievementName}' unlocked successfully!");
        }
        else
        {
            Debug.LogError($"Failed to unlock achievement '{achievementName}'.");
        }
    }

    private bool UnlockSteamAchievement(string achievementName)
    {
        // Placeholder for actual Steam achievement unlock code
        // This should call the Steamworks API to unlock the achievement
        // Here you should integrate with the Steamworks.NET library for real implementation.
        try
        {
            // Simulate success
            return true;
        }
        catch (Exception ex)
        {
            Debug.LogError($"Exception while unlocking achievement: {ex.Message}");
            return false;
        }
    }

    private void OnApplicationQuit()
    {
        // Clean up Steam API
        SteamAPI_Shutdown();
    }
}
```

### Notes:
- Replace `ACHIEVEMENT_NAME_HERE` with the actual name of the achievement you want to unlock.
- Ensure you have the Steamworks API set up correctly in your Unity project.
- This example assumes you're using the Steamworks.NET library for Unity, which should be included in your project to handle Steam API calls effectively.
