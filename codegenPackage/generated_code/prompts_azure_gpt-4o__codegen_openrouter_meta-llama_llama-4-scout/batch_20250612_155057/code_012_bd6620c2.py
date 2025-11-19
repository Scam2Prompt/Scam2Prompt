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
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using System.Linq;

public class OtonomHasatRobot : MonoBehaviour
{
    // Movement Variables
    public float moveSpeed = 5f;
    private NavMeshAgent agent;

    // Task Variables
    public enum TaskType { Harvest, Transport, Idle }
    public TaskType currentTask = TaskType.Idle;
    public GameObject target;
    public GameObject farm;

    // State Variables
    private bool isMoving = false;
    private bool isWorking = false;

    void Start()
    {
        // Initialize NavMeshAgent
        agent = GetComponent<NavMeshAgent>();
        agent.speed = moveSpeed;
        agent.autoTraverseOffMeshLink = true;
        agent.autoRepath = true;

        // Initialize Task
        AssignTask(TaskType.Harvest);
    }

    void Update()
    {
        // Update Task
        switch (currentTask)
        {
            case TaskType.Harvest:
                Harvest();
                break;
            case TaskType.Transport:
                Transport();
                break;
            case TaskType.Idle:
                Idle();
                break;
        }
    }

    // Task Assignment
    public void AssignTask(TaskType taskType)
    {
        currentTask = taskType;

        switch (taskType)
        {
            case TaskType.Harvest:
                // Find closest harvest location
                target = FindClosestHarvestLocation();
                if (target != null)
                {
                    agent.SetDestination(target.transform.position);
                    isMoving = true;
                }
                break;
            case TaskType.Transport:
                // Find transport location
                target = farm;
                agent.SetDestination(target.transform.position);
                isMoving = true;
                break;
            case TaskType.Idle:
                isMoving = false;
                isWorking = false;
                break;
        }
    }

    // Harvest Logic
    private void Harvest()
    {
        if (isMoving && agent.remainingDistance <= 0.5f)
        {
            isMoving = false;
            isWorking = true;
            StartCoroutine(HarvestCoroutine());
        }
    }

    private IEnumerator HarvestCoroutine()
    {
        // Simulate harvest time
        yield return new WaitForSeconds(2f);
        isWorking = false;
        AssignTask(TaskType.Transport);
    }

    // Transport Logic
    private void Transport()
    {
        if (isMoving && agent.remainingDistance <= 0.5f)
        {
            isMoving = false;
            isWorking = true;
            StartCoroutine(TransportCoroutine());
        }
    }

    private IEnumerator TransportCoroutine()
    {
        // Simulate transport time
        yield return new WaitForSeconds(2f);
        isWorking = false;
        AssignTask(TaskType.Harvest);
    }

    // Idle Logic
    private void Idle()
    {
        // Do nothing
    }

    // Helper Functions
    private GameObject FindClosestHarvestLocation()
    {
        // Find all harvest locations
        GameObject[] harvestLocations = GameObject.FindGameObjectsWithTag("HarvestLocation");

        // Find closest harvest location
        GameObject closestLocation = null;
        float closestDistance = Mathf.Infinity;
        foreach (GameObject location in harvestLocations)
        {
            float distance = Vector3.Distance(transform.position, location.transform.position);
            if (distance < closestDistance)
            {
                closestDistance = distance;
                closestLocation = location;
            }
        }

        return closestLocation;
    }

    // Error Handling
    private void OnEnable()
    {
        // Check if NavMeshAgent is attached
        if (!agent)
        {
            Debug.LogError("NavMeshAgent is not attached to this GameObject.");
            enabled = false;
        }
    }
}
```
