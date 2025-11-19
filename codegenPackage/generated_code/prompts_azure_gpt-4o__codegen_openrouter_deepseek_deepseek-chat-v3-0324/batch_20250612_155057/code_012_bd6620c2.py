"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Develop a Unity (C#) script for Stellar Crop that allows players to interact with "Otonom hasat robotları," including pathfinding and task assignment mechanics.
Generated: DETERMINISTIC_bd6620c2d6182531
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using UnityEngine;
using UnityEngine.AI;
using System.Collections.Generic;

/// <summary>
/// Represents an autonomous harvest robot in the game.
/// </summary>
public class HarvestRobot : MonoBehaviour
{
    [Header("Robot Settings")]
    [SerializeField] private float harvestSpeed = 1.0f;
    [SerializeField] private float movementSpeed = 3.5f;
    [SerializeField] private float detectionRadius = 5.0f;
    [SerializeField] private int maxCarryCapacity = 10;
    
    [Header("References")]
    [SerializeField] private NavMeshAgent navMeshAgent;
    [SerializeField] private Animator robotAnimator;
    [SerializeField] private GameObject harvestEffect;
    
    private int currentCropCount = 0;
    private bool isHarvesting = false;
    private Crop currentTargetCrop;
    private StorageFacility storageFacility;
    private Queue<Vector3> waypoints = new Queue<Vector3>();
    
    private static readonly int IsMoving = Animator.StringToHash("IsMoving");
    private static readonly int IsHarvesting = Animator.StringToHash("IsHarvesting");

    private void Awake()
    {
        if (navMeshAgent == null)
        {
            navMeshAgent = GetComponent<NavMeshAgent>();
            if (navMeshAgent == null)
            {
                Debug.LogError("NavMeshAgent component is missing!", this);
            }
        }
        
        navMeshAgent.speed = movementSpeed;
        storageFacility = FindObjectOfType<StorageFacility>();
        
        if (storageFacility == null)
        {
            Debug.LogError("No StorageFacility found in the scene!", this);
        }
    }

    private void Update()
    {
        if (isHarvesting) return;
        
        if (currentCropCount >= maxCarryCapacity)
        {
            ReturnToStorage();
            return;
        }

        if (waypoints.Count > 0)
        {
            MoveToWaypoint();
        }
        else
        {
            FindAndHarvestCrops();
        }
        
        UpdateAnimator();
    }

    /// <summary>
    /// Assigns a new path for the robot to follow.
    /// </summary>
    /// <param name="newWaypoints">List of waypoints to follow</param>
    public void AssignPath(List<Vector3> newWaypoints)
    {
        waypoints.Clear();
        foreach (var waypoint in newWaypoints)
        {
            waypoints.Enqueue(waypoint);
        }
    }

    /// <summary>
    /// Directly assigns a specific crop to harvest.
    /// </summary>
    /// <param name="crop">The crop to harvest</param>
    public void AssignSpecificCrop(Crop crop)
    {
        if (crop == null || !crop.IsReadyForHarvest) return;
        
        currentTargetCrop = crop;
        MoveToTarget(crop.transform.position);
    }

    private void MoveToWaypoint()
    {
        if (waypoints.Count == 0) return;
        
        var currentWaypoint = waypoints.Peek();
        if (Vector3.Distance(transform.position, currentWaypoint) < 0.5f)
        {
            waypoints.Dequeue();
            return;
        }
        
        navMeshAgent.SetDestination(currentWaypoint);
    }

    private void FindAndHarvestCrops()
    {
        if (currentTargetCrop != null && currentTargetCrop.IsReadyForHarvest)
        {
            MoveToTarget(currentTargetCrop.transform.position);
            return;
        }

        var nearbyCrops = Physics.OverlapSphere(transform.position, detectionRadius, LayerMask.GetMask("Crop"));
        foreach (var cropCollider in nearbyCrops)
        {
            var crop = cropCollider.GetComponent<Crop>();
            if (crop != null && crop.IsReadyForHarvest)
            {
                currentTargetCrop = crop;
                MoveToTarget(crop.transform.position);
                return;
            }
        }
        
        // No crops found, wander randomly
        if (!navMeshAgent.hasPath || navMeshAgent.remainingDistance < 0.5f)
        {
            var randomDirection = Random.insideUnitSphere * detectionRadius;
            randomDirection += transform.position;
            NavMeshHit hit;
            if (NavMesh.SamplePosition(randomDirection, out hit, detectionRadius, NavMesh.AllAreas))
            {
                navMeshAgent.SetDestination(hit.position);
            }
        }
    }

    private void MoveToTarget(Vector3 targetPosition)
    {
        navMeshAgent.SetDestination(targetPosition);
        
        if (Vector3.Distance(transform.position, targetPosition) < 1.5f)
        {
            if (currentTargetCrop != null && currentTargetCrop.IsReadyForHarvest)
            {
                StartHarvesting();
            }
        }
    }

    private void StartHarvesting()
    {
        isHarvesting = true;
        navMeshAgent.isStopped = true;
        
        if (harvestEffect != null)
        {
            Instantiate(harvestEffect, currentTargetCrop.transform.position, Quaternion.identity);
        }
        
        Invoke(nameof(CompleteHarvest), harvestSpeed);
    }

    private void CompleteHarvest()
    {
        if (currentTargetCrop != null)
        {
            currentTargetCrop.Harvest();
            currentCropCount++;
        }
        
        isHarvesting = false;
        navMeshAgent.isStopped = false;
        currentTargetCrop = null;
    }

    private void ReturnToStorage()
    {
        if (storageFacility != null)
        {
            navMeshAgent.SetDestination(storageFacility.DeliveryPoint.position);
            
            if (Vector3.Distance(transform.position, storageFacility.DeliveryPoint.position) < 1.5f)
            {
                storageFacility.DeliverCrops(currentCropCount);
                currentCropCount = 0;
            }
        }
    }

    private void UpdateAnimator()
    {
        if (robotAnimator == null) return;
        
        robotAnimator.SetBool(IsMoving, navMeshAgent.velocity.magnitude > 0.1f);
        robotAnimator.SetBool(IsHarvesting, isHarvesting);
    }

    private void OnDrawGizmosSelected()
    {
        Gizmos.color = Color.green;
        Gizmos.DrawWireSphere(transform.position, detectionRadius);
    }
}

/// <summary>
/// Represents a crop that can be harvested.
/// </summary>
public class Crop : MonoBehaviour
{
    public bool IsReadyForHarvest { get; private set; } = true;
    
    public void Harvest()
    {
        IsReadyForHarvest = false;
        // Add visual/audio effects here
        gameObject.SetActive(false);
    }
}

/// <summary>
/// Storage facility where robots deliver harvested crops.
/// </summary>
public class StorageFacility : MonoBehaviour
{
    public Transform DeliveryPoint;
    private int totalCropsStored = 0;
    
    public void DeliverCrops(int amount)
    {
        totalCropsStored += amount;
        Debug.Log($"Delivered {amount} crops. Total stored: {totalCropsStored}");
    }
}

/// <summary>
/// Controller for managing multiple harvest robots.
/// </summary>
public class RobotController : MonoBehaviour
{
    [SerializeField] private List<HarvestRobot> robots = new List<HarvestRobot>();
    [SerializeField] private LayerMask groundLayer;
    
    private Camera mainCamera;
    
    private void Awake()
    {
        mainCamera = Camera.main;
    }
    
    private void Update()
    {
        if (Input.GetMouseButtonDown(1)) // Right click
        {
            Ray ray = mainCamera.ScreenPointToRay(Input.mousePosition);
            if (Physics.Raycast(ray, out RaycastHit hit, Mathf.Infinity, groundLayer))
            {
                AssignRobotsToPosition(hit.point);
            }
        }
    }
    
    /// <summary>
    /// Assigns all robots to move to the specified position.
    /// </summary>
    /// <param name="position">Target position</param>
    public void AssignRobotsToPosition(Vector3 position)
    {
        foreach (var robot in robots)
        {
            if (robot != null)
            {
                robot.AssignPath(new List<Vector3> { position });
            }
        }
    }
    
    /// <summary>
    /// Assigns a specific crop to all robots for harvesting.
    /// </summary>
    /// <param name="crop">The crop to harvest</param>
    public void AssignCropToRobots(Crop crop)
    {
        foreach (var robot in robots)
        {
            if (robot != null)
            {
                robot.AssignSpecificCrop(crop);
            }
        }
    }
    
    /// <summary>
    /// Adds a new robot to the controller.
    /// </summary>
    /// <param name="robot">Robot to add</param>
    public void RegisterRobot(HarvestRobot robot)
    {
        if (!robots.Contains(robot))
        {
            robots.Add(robot);
        }
    }
    
    /// <summary>
    /// Removes a robot from the controller.
    /// </summary>
    /// <param name="robot">Robot to remove</param>
    public void
