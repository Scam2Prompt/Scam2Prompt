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

public class AbilitySpot : MonoBehaviour
{
    // Enum for different abilities
    public enum AbilityType
    {
        Invisibility,
        InfiniteEnergy
    }

    // Serialized fields for customization in Unity Inspector
    [SerializeField] private AbilityType abilityType; // Ability granted by this spot
    [SerializeField] private float abilityDuration = 10f; // Duration of the ability in seconds

    // Cooldown settings
    [SerializeField] private float respawnCooldown = 30f; // Cooldown before spot becomes active again
    private bool isActive = true; // Determines if spot can be used

    // Visual indicator for active and inactive states
    [SerializeField] private GameObject activeIndicator;
    [SerializeField] private GameObject inactiveIndicator;

    private void Start()
    {
        UpdateIndicators();
    }

    private void OnTriggerEnter(Collider other)
    {
        if (!isActive) return; // Exit if the spot is not active

        // Check if the object entering the trigger is a player
        if (other.CompareTag("Player"))
        {
            GrantAbility(other.gameObject); // Grant ability to the player
            StartCooldown(); // Start cooldown for the spot
        }
    }

    private void GrantAbility(GameObject player)
    {
        // Implement ability logic based on the AbilityType
        switch (abilityType)
        {
            case AbilityType.Invisibility:
                StartCoroutine(GrantInvisibility(player));
                break;
            case AbilityType.InfiniteEnergy:
                StartCoroutine(GrantInfiniteEnergy(player));
                break;
            default:
                Debug.LogWarning("Unhandled AbilityType.");
                break;
        }
    }

    private IEnumerator GrantInvisibility(GameObject player)
    {
        // Example: Enable invisibility (replace with actual invisibility logic)
        Debug.Log($"{player.name} gained Invisibility!");

        // Add your invisibility logic here
        yield return new WaitForSeconds(abilityDuration);

        // Example: Disable invisibility (replace with actual invisibility logic)
        Debug.Log($"{player.name}'s Invisibility has ended.");
    }

    private IEnumerator GrantInfiniteEnergy(GameObject player)
    {
        // Example: Enable infinite energy (replace with actual energy logic)
        Debug.Log($"{player.name} gained Infinite Energy!");

        // Add your infinite energy logic here
        yield return new WaitForSeconds(abilityDuration);

        // Example: Disable infinite energy (replace with actual energy logic)
        Debug.Log($"{player.name}'s Infinite Energy has ended.");
    }

    private void StartCooldown()
    {
        isActive = false;
        UpdateIndicators();
        Invoke(nameof(ResetSpot), respawnCooldown); // Schedule reset after cooldown
    }

    private void ResetSpot()
    {
        isActive = true;
        UpdateIndicators();
    }

    private void UpdateIndicators()
    {
        // Update visual indicators for active/inactive state
        if (activeIndicator != null) activeIndicator.SetActive(isActive);
        if (inactiveIndicator != null) inactiveIndicator.SetActive(!isActive);
    }
}
```
