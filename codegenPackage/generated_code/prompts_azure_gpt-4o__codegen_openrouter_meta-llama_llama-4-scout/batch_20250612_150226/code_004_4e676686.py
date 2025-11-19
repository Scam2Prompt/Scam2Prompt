"""
Generated Code Metadata:
========================
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a code snippet in Unity/C# to implement the "Adventure Instances" feature of "Big Time," including boss challenges and reward collection mechanics.
Generated: DETERMINISTIC_4e67668660e09470
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Enum for instance difficulty levels
public enum InstanceDifficulty { Easy, Medium, Hard }

// Class representing an Adventure Instance
public class AdventureInstance : MonoBehaviour
{
    // Instance properties
    public string instanceName;
    public InstanceDifficulty difficulty;
    public GameObject bossPrefab;
    public List<Reward> rewards;

    // Instance state
    private bool isInstanceActive = false;
    private GameObject bossInstance;

    // Initialize the instance
    public void InitializeInstance()
    {
        // Check if instance is already active
        if (isInstanceActive)
        {
            Debug.LogError("Instance is already active.");
            return;
        }

        // Spawn the boss
        bossInstance = Instantiate(bossPrefab, transform.position, Quaternion.identity);

        // Set instance state
        isInstanceActive = true;
    }

    // Update is called once per frame
    void Update()
    {
        // Check if the boss is defeated
        if (isInstanceActive && bossInstance.GetComponent<BossHealth>().IsDefeated())
        {
            // Reward the player
            RewardPlayer();

            // Deactivate the instance
            DeactivateInstance();
        }
    }

    // Reward the player for completing the instance
    private void RewardPlayer()
    {
        // Loop through each reward
        foreach (Reward reward in rewards)
        {
            // Apply the reward to the player
            reward.ApplyReward();
        }
    }

    // Deactivate the instance
    private void DeactivateInstance()
    {
        // Destroy the boss instance
        Destroy(bossInstance);

        // Set instance state
        isInstanceActive = false;
    }
}

// Class representing a reward
[System.Serializable]
public class Reward
{
    public string rewardName;
    public int rewardAmount;

    // Apply the reward to the player
    public void ApplyReward()
    {
        // Assuming a PlayerInventory script
        PlayerInventory.instance.AddItem(rewardName, rewardAmount);
    }
}

// Class representing a boss's health
public class BossHealth : MonoBehaviour
{
    public int maxHealth;
    private int currentHealth;

    // Initialize the boss's health
    void Start()
    {
        currentHealth = maxHealth;
    }

    // Check if the boss is defeated
    public bool IsDefeated()
    {
        return currentHealth <= 0;
    }

    // Take damage from the player
    public void TakeDamage(int damage)
    {
        currentHealth -= damage;

        // Check if the boss is defeated
        if (IsDefeated())
        {
            // Handle boss defeat logic
        }
    }
}

// Example usage:
public class PlayerAttack : MonoBehaviour
{
    public int attackDamage = 10;

    // Attack the boss
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            // Assuming a reference to the boss instance
            GameObject bossInstance = GameObject.FindGameObjectWithTag("Boss");

            // Get the boss's health script
            BossHealth bossHealth = bossInstance.GetComponent<BossHealth>();

            // Deal damage to the boss
            bossHealth.TakeDamage(attackDamage);
        }
    }
}

// Player inventory script for demonstration purposes
public class PlayerInventory : MonoBehaviour
{
    public static PlayerInventory instance;

    private Dictionary<string, int> items = new Dictionary<string, int>();

    void Awake()
    {
        if (instance == null)
        {
            instance = this;
        }
        else if (instance != this)
        {
            Destroy(gameObject);
        }
    }

    // Add an item to the player's inventory
    public void AddItem(string itemName, int itemAmount)
    {
        // Check if the item already exists in the inventory
        if (items.ContainsKey(itemName))
        {
            items[itemName] += itemAmount;
        }
        else
        {
            items.Add(itemName, itemAmount);
        }

        Debug.Log("Added " + itemAmount + " " + itemName + "(s) to the player's inventory.");
    }
}
```
