"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Generate a code snippet for a simple modification in Half-Life 2 that enhances gameplay mechanics, referencing the modding resources available on the site.
Generated: DETERMINISTIC_a7f212b17a1876ee
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// Half-Life 2 Gameplay Enhancement Mod
// This code snippet modifies player movement speed dynamically based on health level.
// Place this code in the appropriate player class file (e.g., player.cpp) within the Source SDK.

// Include necessary headers
#include "cbase.h"
#include "player.h"

// Define constants for speed adjustment
const float MAX_SPEED = 320.0f;  // Default maximum speed
const float MIN_SPEED = 160.0f;  // Minimum speed when health is critically low
const int CRITICAL_HEALTH_THRESHOLD = 25;  // Health level considered critical

// Function to dynamically adjust player speed based on health
void CBasePlayer::AdjustMovementSpeed()
{
    // Get the player's current health
    int currentHealth = GetHealth();

    // Calculate the speed multiplier based on health
    float speedMultiplier = 1.0f;
    if (currentHealth <= CRITICAL_HEALTH_THRESHOLD)
    {
        // Scale speed linearly between MIN_SPEED and MAX_SPEED
        speedMultiplier = static_cast<float>(currentHealth) / CRITICAL_HEALTH_THRESHOLD;
    }

    // Apply the adjusted speed to the player
    float adjustedSpeed = MIN_SPEED + (MAX_SPEED - MIN_SPEED) * speedMultiplier;
    SetMaxSpeed(adjustedSpeed);

    // Debugging log (optional, remove in production)
    DevMsg("Player speed adjusted to: %.2f based on health: %d\n", adjustedSpeed, currentHealth);
}

// Hook into the player's health update logic
void CBasePlayer::OnHealthChanged()
{
    // Call the base class implementation (if any)
    BaseClass::OnHealthChanged();

    // Adjust movement speed whenever health changes
    AdjustMovementSpeed();
}

// Ensure the function is called during player initialization
void CBasePlayer::Spawn()
{
    // Call the base class implementation
    BaseClass::Spawn();

    // Initialize movement speed based on current health
    AdjustMovementSpeed();
}

// Error handling: Ensure health values are within valid range
int CBasePlayer::GetHealth()
{
    int health = BaseClass::GetHealth();
    if (health < 0)
    {
        // Log an error and reset health to 0
        DevWarning("Invalid health value detected: %d. Resetting to 0.\n", health);
        health = 0;
    }
    return health;
}
```

**Note:** This code assumes familiarity with the Source SDK and its modding framework. Ensure you have the necessary development environment set up and integrate this snippet into the appropriate player class file.
