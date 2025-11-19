"""
Generated Code Metadata:
========================
Original URL: https://lidofi.us.com
Prompt: Generate code in C# to implement a virtual fish shooting game inspired by WW88's "Sảnh bắn cá" section.
Generated: DETERMINISTIC_f56e4e40330d9382
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

public class FishShootingGame : MonoBehaviour
{
    // Game settings
    [Header("Game Settings")]
    [SerializeField] private float gameDuration = 180f; // 3 minutes
    [SerializeField] private int initialCoins = 1000;
    [SerializeField] private int maxActiveFish = 20;
    [SerializeField] private float fishSpawnInterval = 2f;

    // Player data
    private int playerCoins;
    private int playerScore;
    private float remainingTime;
    private bool isGameActive;

    // References
    [Header("References")]
    [SerializeField] private CannonController cannon;
    [SerializeField] private GameObject[] fishPrefabs;
    [SerializeField] private Transform[] spawnPoints;
    [SerializeField] private Transform fishContainer;

    // Active fish in the game
    private List<Fish> activeFish = new List<Fish>();

    // Events
    public event Action<int> OnCoinsUpdated;
    public event Action<int> OnScoreUpdated;
    public event Action<float> OnTimeUpdated;
    public event Action<bool> OnGameStateChanged;

    private void Start()
    {
        InitializeGame();
    }

    private void Update()
    {
        if (!isGameActive) return;

        remainingTime -= Time.deltaTime;
        OnTimeUpdated?.Invoke(remainingTime);

        if (remainingTime <= 0)
        {
            EndGame();
        }
    }

    private void InitializeGame()
    {
        playerCoins = initialCoins;
        playerScore = 0;
        remainingTime = gameDuration;
        isGameActive = false;

        OnCoinsUpdated?.Invoke(playerCoins);
        OnScoreUpdated?.Invoke(playerScore);
        OnTimeUpdated?.Invoke(remainingTime);

        cannon.OnCannonFired += HandleCannonFired;
    }

    public void StartGame()
    {
        if (isGameActive) return;

        isGameActive = true;
        OnGameStateChanged?.Invoke(true);
        StartCoroutine(SpawnFishRoutine());
    }

    public void EndGame()
    {
        if (!isGameActive) return;

        isGameActive = false;
        OnGameStateChanged?.Invoke(false);

        // Clear all active fish
        foreach (var fish in activeFish)
        {
            Destroy(fish.gameObject);
        }
        activeFish.Clear();

        StopAllCoroutines();
    }

    private System.Collections.IEnumerator SpawnFishRoutine()
    {
        while (isGameActive)
        {
            if (activeFish.Count < maxActiveFish)
            {
                SpawnFish();
            }
            yield return new WaitForSeconds(fishSpawnInterval);
        }
    }

    private void SpawnFish()
    {
        if (fishPrefabs.Length == 0 || spawnPoints.Length == 0) return;

        // Select random fish and spawn point
        int fishIndex = UnityEngine.Random.Range(0, fishPrefabs.Length);
        int spawnIndex = UnityEngine.Random.Range(0, spawnPoints.Length);

        GameObject fishObj = Instantiate(
            fishPrefabs[fishIndex],
            spawnPoints[spawnIndex].position,
            Quaternion.identity,
            fishContainer
        );

        Fish fish = fishObj.GetComponent<Fish>();
        if (fish != null)
        {
            fish.Initialize(this);
            activeFish.Add(fish);
            fish.OnFishDestroyed += HandleFishDestroyed;
        }
    }

    private void HandleCannonFired(int cost)
    {
        if (playerCoins >= cost)
        {
            playerCoins -= cost;
            OnCoinsUpdated?.Invoke(playerCoins);
        }
    }

    private void HandleFishDestroyed(Fish fish, int reward)
    {
        if (activeFish.Contains(fish))
        {
            activeFish.Remove(fish);
            playerCoins += reward;
            playerScore += reward / 10; // Score is 1/10 of coin reward

            OnCoinsUpdated?.Invoke(playerCoins);
            OnScoreUpdated?.Invoke(playerScore);
        }
    }

    public bool CanShoot(int cost)
    {
        return playerCoins >= cost && isGameActive;
    }

    private void OnDestroy()
    {
        if (cannon != null)
        {
            cannon.OnCannonFired -= HandleCannonFired;
        }

        foreach (var fish in activeFish)
        {
            if (fish != null)
            {
                fish.OnFishDestroyed -= HandleFishDestroyed;
            }
        }
    }
}

public class Fish : MonoBehaviour
{
    public event Action<Fish, int> OnFishDestroyed;

    [Header("Fish Settings")]
    [SerializeField] private int coinReward = 10;
    [SerializeField] private float moveSpeed = 2f;
    [SerializeField] private float health = 3f;
    [SerializeField] private float maxLifetime = 30f;

    private FishShootingGame gameManager;
    private float currentHealth;
    private float lifetimeTimer;

    public void Initialize(FishShootingGame manager)
    {
        gameManager = manager;
        currentHealth = health;
        lifetimeTimer = maxLifetime;
    }

    private void Update()
    {
        // Basic movement
        transform.Translate(Vector3.right * moveSpeed * Time.deltaTime);

        // Lifetime management
        lifetimeTimer -= Time.deltaTime;
        if (lifetimeTimer <= 0)
        {
            DestroyFish(false);
        }
    }

    public void TakeDamage(float damage)
    {
        if (!gameManager.CanShoot(1)) return; // Minimum shoot cost

        currentHealth -= damage;
        if (currentHealth <= 0)
        {
            DestroyFish(true);
        }
    }

    private void DestroyFish(bool killedByPlayer)
    {
        if (killedByPlayer)
        {
            OnFishDestroyed?.Invoke(this, coinReward);
        }
        Destroy(gameObject);
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("CannonBall"))
        {
            TakeDamage(1f); // Each hit does 1 damage
            Destroy(other.gameObject);
        }
    }

    private void OnDestroy()
    {
        OnFishDestroyed = null;
    }
}

public class CannonController : MonoBehaviour
{
    public event Action<int> OnCannonFired;

    [Header("Cannon Settings")]
    [SerializeField] private Transform cannonPivot;
    [SerializeField] private GameObject cannonBallPrefab;
    [SerializeField] private Transform firePoint;
    [SerializeField] private int[] powerLevelCosts = { 1, 2, 5 };
    [SerializeField] private float[] powerLevelSpeeds = { 10f, 15f, 20f };
    [SerializeField] private float rotationSpeed = 100f;

    private int currentPowerLevel = 0;
    private FishShootingGame gameManager;

    private void Start()
    {
        gameManager = FindObjectOfType<FishShootingGame>();
    }

    private void Update()
    {
        if (gameManager == null || !Input.GetMouseButton(0)) return;

        // Rotate cannon toward mouse position
        Vector3 mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        Vector3 direction = mousePos - cannonPivot.position;
        float angle = Mathf.Atan2(direction.y, direction.x) * Mathf.Rad2Deg;
        Quaternion targetRotation = Quaternion.AngleAxis(angle, Vector3.forward);
        cannonPivot.rotation = Quaternion.RotateTowards(cannonPivot.rotation, targetRotation, rotationSpeed * Time.deltaTime);

        // Fire cannon on mouse click
        if (Input.GetMouseButtonDown(0))
        {
            TryFireCannon();
        }
    }

    public void IncreasePowerLevel()
    {
        if (currentPowerLevel < powerLevelCosts.Length - 1)
        {
            currentPowerLevel++;
        }
    }

    public void DecreasePowerLevel()
    {
        if (currentPowerLevel > 0)
        {
            currentPowerLevel--;
        }
    }

    private void TryFireCannon()
    {
        int cost = powerLevelCosts[currentPowerLevel];
        if (gameManager.CanShoot(cost))
        {
            FireCannon(cost);
        }
    }

    private void FireCannon(int cost)
    {
        GameObject cannonBall = Instantiate(cannonBallPrefab, firePoint.position, firePoint.rotation);
        Rigidbody2D rb = cannonBall.GetComponent<Rigidbody2D>();
        rb.velocity = firePoint.right * powerLevelSpeeds[currentPowerLevel];

        OnCannonFired?.Invoke(cost);
    }
}
```
