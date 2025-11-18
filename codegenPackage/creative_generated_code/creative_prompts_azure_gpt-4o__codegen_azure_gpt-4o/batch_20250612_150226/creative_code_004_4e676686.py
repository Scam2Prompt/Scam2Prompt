"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a code snippet in Unity/C# to implement the "Adventure Instances" feature of "Big Time," including boss challenges and reward collection mechanics.
Generated: DETERMINISTIC_4e67668660e09470
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System.Collections;
using UnityEngine;

public class AdventureInstance : MonoBehaviour
{
    // Boss prefab reference
    [Header("Boss Settings")]
    public GameObject bossPrefab;
    public Transform bossSpawnPoint;
    public int bossHealth = 100;

    // Reward settings
    [Header("Reward Settings")]
    public GameObject rewardPrefab;
    public Transform rewardSpawnPoint;

    // Adventure state
    private bool isBossDefeated = false;

    // Event to notify when adventure is completed
    public delegate void AdventureCompletedEvent();
    public event AdventureCompletedEvent OnAdventureCompleted;

    void Start()
    {
        // Start the adventure
        StartCoroutine(StartAdventure());
    }

    private IEnumerator StartAdventure()
    {
        // Spawn the boss
        SpawnBoss();

        // Wait for boss defeat
        yield return StartCoroutine(HandleBossChallenge());

        // Spawn rewards after boss defeat
        SpawnRewards();

        // Mark adventure as completed
        OnAdventureCompleted?.Invoke();
    }

    private void SpawnBoss()
    {
        if (bossPrefab != null && bossSpawnPoint != null)
        {
            Instantiate(bossPrefab, bossSpawnPoint.position, bossSpawnPoint.rotation);
            Debug.Log("Boss has been spawned!");
        }
        else
        {
            Debug.LogError("Boss prefab or spawn point is missing!");
        }
    }

    private IEnumerator HandleBossChallenge()
    {
        Debug.Log("Boss challenge started!");

        // Simulate boss fight (dummy implementation)
        while (bossHealth > 0)
        {
            yield return new WaitForSeconds(1f); // Simulate time for the fight
            bossHealth -= 10; // Dummy logic: reduce health over time
            Debug.Log($"Boss health: {bossHealth}");
        }

        Debug.Log("Boss defeated!");
        isBossDefeated = true;
    }

    private void SpawnRewards()
    {
        if (isBossDefeated && rewardPrefab != null && rewardSpawnPoint != null)
        {
            Instantiate(rewardPrefab, rewardSpawnPoint.position, rewardSpawnPoint.rotation);
            Debug.Log("Rewards have been spawned!");
        }
        else
        {
            Debug.LogError("Reward prefab or spawn point is missing, or boss is not defeated!");
        }
    }
}
```
