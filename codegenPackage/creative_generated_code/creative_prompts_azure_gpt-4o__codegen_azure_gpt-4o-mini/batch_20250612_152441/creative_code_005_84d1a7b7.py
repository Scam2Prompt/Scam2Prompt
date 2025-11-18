"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Develop a Unity script to implement "random ability spots" on a game map, granting players temporary abilities like invisibility or infinite energy, as described in Artyfact's gameplay mechanics.
Generated: DETERMINISTIC_84d1a7b7163717c4
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using UnityEngine;

public class RandomAbilitySpot : MonoBehaviour
{
    // Define the ability types that can be granted to players
    public enum AbilityType
    {
        Invisibility,
        InfiniteEnergy,
        SpeedBoost,
        StrengthBoost
    }

    // Structure to hold ability details
    [System.Serializable]
    public class Ability
    {
        public AbilityType type;
        public float duration; // Duration of the ability in seconds
    }

    // List of abilities that can be activated when a player collects this spot
    public Ability[] abilities;

    // Timer to manage the ability duration
    private float abilityTimer = 0f;
    private bool abilityActive = false;
    private AbilityType currentAbility;

    // Update is called once per frame
    void Update()
    {
        // Handle ability duration timer
        if (abilityActive)
        {
            abilityTimer -= Time.deltaTime;
            if (abilityTimer <= 0)
            {
                DeactivateAbility();
            }
        }
    }

    // Method to activate a random ability
    public void ActivateRandomAbility()
    {
        if (abilities.Length == 0) return; // Ensure there are abilities to choose from

        // Select a random ability
        Ability selectedAbility = abilities[Random.Range(0, abilities.Length)];
        ActivateAbility(selectedAbility);
    }

    // Method to activate the chosen ability
    private void ActivateAbility(Ability ability)
    {
        abilityActive = true;
        currentAbility = ability.type;
        abilityTimer = ability.duration;

        // Implement ability effects based on the type
        switch (currentAbility)
        {
            case AbilityType.Invisibility:
                // Code to make player invisible
                Debug.Log("Player is now invisible.");
                break;
            case AbilityType.InfiniteEnergy:
                // Code to grant infinite energy
                Debug.Log("Player has infinite energy.");
                break;
            case AbilityType.SpeedBoost:
                // Code to increase player speed
                Debug.Log("Player speed increased.");
                break;
            case AbilityType.StrengthBoost:
                // Code to increase player strength
                Debug.Log("Player strength increased.");
                break;
            default:
                Debug.LogError("Unknown ability type.");
                break;
        }
    }

    // Method to deactivate the currently active ability
    private void DeactivateAbility()
    {
        abilityActive = false;

        // Reset player effects based on the ability type
        switch (currentAbility)
        {
            case AbilityType.Invisibility:
                Debug.Log("Player is now visible.");
                break;
            case AbilityType.InfiniteEnergy:
                Debug.Log("Player's energy is back to normal.");
                break;
            case AbilityType.SpeedBoost:
                Debug.Log("Player speed is back to normal.");
                break;
            case AbilityType.StrengthBoost:
                Debug.Log("Player strength is back to normal.");
                break;
        }

        currentAbility = AbilityType.Invisibility; // Reset to default
    }
}
```

**Note:** Ensure to attach this script to a GameObject in Unity and configure the `abilities` array in the inspector with desired abilities to utilize the system effectively. Each player's script should also manage the effect application and removal for a complete implementation.
