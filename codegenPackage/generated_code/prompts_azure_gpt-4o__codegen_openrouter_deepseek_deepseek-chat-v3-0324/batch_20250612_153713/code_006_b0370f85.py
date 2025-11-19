"""
Generated Code Metadata:
========================
Original URL: https://stethevent.org
Prompt: Create a Unity script to design a robot laser battle scene, referencing the "Instructables Robot Laser Battle Scene in Unity" project on Instructables.
Generated: DETERMINISTIC_b0370f8594db1c1b
Batch ID: 20250612_153713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using UnityEngine;

public class RobotLaserBattle : MonoBehaviour
{
    [Header("Robot Settings")]
    public GameObject robotPrefab;
    public int numberOfRobots = 2;
    public float spawnRadius = 5f;
    public float robotSpeed = 3f;
    public float rotationSpeed = 5f;

    [Header("Laser Settings")]
    public GameObject laserPrefab;
    public float laserSpeed = 20f;
    public float fireRate = 0.5f;
    public float laserLifetime = 2f;

    [Header("Battlefield Settings")]
    public float battlefieldRadius = 10f;
    public Material battlefieldMaterial;

    private GameObject[] robots;
    private float[] nextFireTimes;

    void Start()
    {
        InitializeBattlefield();
        SpawnRobots();
        InitializeFireTimes();
    }

    void Update()
    {
        HandleRobotMovement();
        HandleLaserFiring();
    }

    private void InitializeBattlefield()
    {
        GameObject battlefield = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
        battlefield.transform.position = Vector3.zero;
        battlefield.transform.localScale = new Vector3(battlefieldRadius * 2, 0.1f, battlefieldRadius * 2);
        battlefield.GetComponent<Renderer>().material = battlefieldMaterial;
        Destroy(battlefield.GetComponent<Collider>());
    }

    private void SpawnRobots()
    {
        robots = new GameObject[numberOfRobots];
        for (int i = 0; i < numberOfRobots; i++)
        {
            Vector3 spawnPosition = Random.insideUnitCircle * spawnRadius;
            spawnPosition.z = spawnPosition.y;
            spawnPosition.y = 0;

            robots[i] = Instantiate(robotPrefab, spawnPosition, Quaternion.identity);
            robots[i].name = "Robot_" + i;
        }
    }

    private void InitializeFireTimes()
    {
        nextFireTimes = new float[numberOfRobots];
        for (int i = 0; i < numberOfRobots; i++)
        {
            nextFireTimes[i] = Time.time + Random.Range(0f, fireRate);
        }
    }

    private void HandleRobotMovement()
    {
        for (int i = 0; i < robots.Length; i++)
        {
            // Random movement within battlefield
            Vector3 randomDirection = new Vector3(
                Random.Range(-1f, 1f),
                0,
                Random.Range(-1f, 1f)
            ).normalized;

            // Move robot
            robots[i].transform.position += randomDirection * robotSpeed * Time.deltaTime;

            // Keep robots within battlefield
            if (robots[i].transform.position.magnitude > battlefieldRadius)
            {
                robots[i].transform.position = robots[i].transform.position.normalized * battlefieldRadius * 0.9f;
            }

            // Rotate robot to face movement direction
            if (randomDirection != Vector3.zero)
            {
                Quaternion targetRotation = Quaternion.LookRotation(randomDirection);
                robots[i].transform.rotation = Quaternion.Slerp(
                    robots[i].transform.rotation,
                    targetRotation,
                    rotationSpeed * Time.deltaTime
                );
            }
        }
    }

    private void HandleLaserFiring()
    {
        for (int i = 0; i < robots.Length; i++)
        {
            if (Time.time >= nextFireTimes[i])
            {
                FireLaser(robots[i]);
                nextFireTimes[i] = Time.time + fireRate + Random.Range(-0.1f, 0.1f);
            }
        }
    }

    private void FireLaser(GameObject robot)
    {
        // Create laser at robot's position and rotation
        GameObject laser = Instantiate(
            laserPrefab,
            robot.transform.position + robot.transform.forward,
            robot.transform.rotation
        );

        // Set laser velocity
        Rigidbody laserRb = laser.GetComponent<Rigidbody>();
        if (laserRb != null)
        {
            laserRb.velocity = robot.transform.forward * laserSpeed;
        }

        // Destroy laser after lifetime
        Destroy(laser, laserLifetime);
    }

    private void OnDrawGizmos()
    {
        // Draw battlefield boundary
        Gizmos.color = Color.cyan;
        Gizmos.DrawWireSphere(Vector3.zero, battlefieldRadius);
    }
}
```
