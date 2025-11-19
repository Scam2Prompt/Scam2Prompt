"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Develop a Unity script to implement "armored vehicles" with unique weapons, allowing players to drive mechs, drones, and cars in a battle royale setting, as described in Artyfact.
Generated: DETERMINISTIC_13c1667e313fd22f
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using UnityEngine;
using System.Collections.Generic;

[System.Serializable]
public class ArmoredVehicleStats
{
    public float maxHealth = 100f;
    public float currentHealth;
    public float speed = 10f;
    public float acceleration = 5f;
    public float rotationSpeed = 100f;
    public float weaponCooldown = 1f;
}

[System.Serializable]
public class WeaponSystem
{
    public string weaponName;
    public float damage = 10f;
    public float range = 50f;
    public float fireRate = 1f;
    public GameObject projectilePrefab;
    public Transform firePoint;
    public ParticleSystem muzzleFlash;
    
    private float lastFireTime;
    
    public bool CanFire()
    {
        return Time.time > lastFireTime + 1f / fireRate;
    }
    
    public void Fire()
    {
        if (!CanFire() || projectilePrefab == null || firePoint == null) return;
        
        lastFireTime = Time.time;
        
        if (muzzleFlash != null)
        {
            muzzleFlash.Play();
        }
        
        GameObject projectile = Object.Instantiate(projectilePrefab, firePoint.position, firePoint.rotation);
        Projectile projScript = projectile.GetComponent<Projectile>();
        if (projScript != null)
        {
            projScript.Initialize(damage, range);
        }
    }
}

public class ArmoredVehicleController : MonoBehaviour
{
    public ArmoredVehicleStats vehicleStats;
    public List<WeaponSystem> weapons;
    public int currentWeaponIndex = 0;
    
    private Rigidbody rb;
    private bool isDestroyed = false;
    
    private void Awake()
    {
        rb = GetComponent<Rigidbody>();
        vehicleStats.currentHealth = vehicleStats.maxHealth;
        
        if (weapons.Count > 0)
        {
            foreach (var weapon in weapons)
            {
                if (weapon.firePoint == null)
                {
                    Debug.LogWarning($"Weapon {weapon.weaponName} has no fire point assigned!");
                }
            }
        }
    }
    
    private void Update()
    {
        if (isDestroyed) return;
        
        HandleWeaponInput();
    }
    
    private void FixedUpdate()
    {
        if (isDestroyed) return;
        
        HandleMovement();
    }
    
    private void HandleMovement()
    {
        float moveInput = Input.GetAxis("Vertical");
        float turnInput = Input.GetAxis("Horizontal");
        
        Vector3 movement = transform.forward * moveInput * vehicleStats.speed * Time.fixedDeltaTime;
        rb.MovePosition(rb.position + movement);
        
        float turn = turnInput * vehicleStats.rotationSpeed * Time.fixedDeltaTime;
        Quaternion turnRotation = Quaternion.Euler(0f, turn, 0f);
        rb.MoveRotation(rb.rotation * turnRotation);
    }
    
    private void HandleWeaponInput()
    {
        if (weapons.Count == 0) return;
        
        // Switch weapons
        if (Input.GetKeyDown(KeyCode.Q))
        {
            currentWeaponIndex = (currentWeaponIndex - 1 + weapons.Count) % weapons.Count;
        }
        else if (Input.GetKeyDown(KeyCode.E))
        {
            currentWeaponIndex = (currentWeaponIndex + 1) % weapons.Count;
        }
        
        // Fire current weapon
        if (Input.GetButton("Fire1"))
        {
            weapons[currentWeaponIndex].Fire();
        }
    }
    
    public void TakeDamage(float damage)
    {
        if (isDestroyed) return;
        
        vehicleStats.currentHealth -= damage;
        
        if (vehicleStats.currentHealth <= 0)
        {
            DestroyVehicle();
        }
    }
    
    private void DestroyVehicle()
    {
        isDestroyed = true;
        
        // Disable controls and physics
        rb.isKinematic = true;
        GetComponent<Collider>().enabled = false;
        
        // Play destruction effects
        // TODO: Add explosion effects, sound, etc.
        
        // Notify game manager
        GameManager.Instance?.VehicleDestroyed(this);
        
        // Destroy after delay
        Destroy(gameObject, 3f);
    }
    
    private void OnCollisionEnter(Collision collision)
    {
        if (isDestroyed) return;
        
        // Take damage from collisions
        float impactForce = collision.relativeVelocity.magnitude;
        if (impactForce > 5f)
        {
            TakeDamage(impactForce * 0.5f);
        }
    }
}

public class Projectile : MonoBehaviour
{
    private float damage;
    private float range;
    private Vector3 startPosition;
    
    public void Initialize(float damage, float range)
    {
        this.damage = damage;
        this.range = range;
        startPosition = transform.position;
    }
    
    private void Update()
    {
        // Destroy if beyond range
        if (Vector3.Distance(startPosition, transform.position) > range)
        {
            Destroy(gameObject);
        }
    }
    
    private void OnTriggerEnter(Collider other)
    {
        ArmoredVehicleController vehicle = other.GetComponent<ArmoredVehicleController>();
        if (vehicle != null)
        {
            vehicle.TakeDamage(damage);
        }
        
        // TODO: Add impact effects
        
        Destroy(gameObject);
    }
}

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }
    
    public List<ArmoredVehicleController> activeVehicles = new List<ArmoredVehicleController>();
    
    private void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(this);
            return;
        }
        
        Instance = this;
    }
    
    public void VehicleDestroyed(ArmoredVehicleController vehicle)
    {
        if (activeVehicles.Contains(vehicle))
        {
            activeVehicles.Remove(vehicle);
        }
        
        CheckBattleRoyaleEnd();
    }
    
    private void CheckBattleRoyaleEnd()
    {
        if (activeVehicles.Count <= 1)
        {
            // Game over, last vehicle standing wins
            Debug.Log("Battle Royale ended!");
        }
    }
}

public class VehicleSpawner : MonoBehaviour
{
    public GameObject[] vehiclePrefabs;
    public Transform[] spawnPoints;
    
    private void Start()
    {
        if (vehiclePrefabs.Length == 0 || spawnPoints.Length == 0)
        {
            Debug.LogError("VehicleSpawner not properly configured!");
            return;
        }
        
        SpawnVehicles();
    }
    
    private void SpawnVehicles()
    {
        for (int i = 0; i < spawnPoints.Length; i++)
        {
            if (i >= vehiclePrefabs.Length) break;
            
            GameObject vehicle = Instantiate(
                vehiclePrefabs[i % vehiclePrefabs.Length],
                spawnPoints[i].position,
                spawnPoints[i].rotation
            );
            
            ArmoredVehicleController controller = vehicle.GetComponent<ArmoredVehicleController>();
            if (controller != null)
            {
                GameManager.Instance.activeVehicles.Add(controller);
            }
        }
    }
}
```
