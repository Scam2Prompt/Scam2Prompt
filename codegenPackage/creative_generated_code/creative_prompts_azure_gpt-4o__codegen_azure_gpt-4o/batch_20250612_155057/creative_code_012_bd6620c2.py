"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Develop a Unity (C#) script for Stellar Crop that allows players to interact with "Otonom hasat robotları," including pathfinding and task assignment mechanics.
Generated: DETERMINISTIC_bd6620c2d6182531
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

// Class defining the autonomous harvest robot's behaviors and interactions
public class HarvestRobotController : MonoBehaviour
{
    // Pathfinding Component
    private NavMeshAgent agent;

    // Robot Task States
    private enum RobotState { Idle, MovingToTarget, Harvesting }
    private RobotState currentState = RobotState.Idle;

    // Target Position for Harvesting
    private Transform target;

    // Robot Speed Configuration
    [Header("Robot Settings")]
    [SerializeField] private float movementSpeed = 3.5f;

    // Interaction Range
    [Header("Interaction Settings")]
    [SerializeField] private float interactionRange = 2.0f;

    // Harvest Task Duration
    [SerializeField] private float harvestDuration = 5.0f;

    // Debugging Purpose
    private bool debugMode = true;

    private void Start()
    {
        // Initialize the NavMeshAgent for pathfinding
        agent = GetComponent<NavMeshAgent>();
        if (agent == null)
        {
            Debug.LogError("NavMeshAgent component missing on Harvest Robot!");
        }

        // Set the movement speed for the robot
        if (agent != null)
        {
            agent.speed = movementSpeed;
        }
    }

    private void Update()
    {
        // State management logic
        switch (currentState)
        {
            case RobotState.Idle:
                // Awaiting new task assignment
                if (debugMode) Debug.Log("Harvest Robot is idle.");
                break;

            case RobotState.MovingToTarget:
                // Pathfinding routine
                HandleMovement();
                break;

            case RobotState.Harvesting:
                // Handle harvesting logic (harvest simulation)
                break;
        }
    }

    /// <summary>
    /// Assigns a harvesting task to the robot.
    /// </summary>
    /// <param name="targetTransform">The target position of the harvest location.</param>
    public void AssignHarvestTask(Transform targetTransform)
    {
        // Validate target
        if (targetTransform == null)
        {
            Debug.LogError("Invalid target assigned to Harvest Robot!");
            return;
        }

        // Update the target and switch to moving state
        target = targetTransform;
        currentState = RobotState.MovingToTarget;

        // Set the NavMeshAgent destination
        if (agent != null)
        {
            agent.SetDestination(target.position);
        }

        if (debugMode) Debug.Log("Assigned harvest task to robot.");
    }

    /// <summary>
    /// Handles the robot's movement towards the target.
    /// </summary>
    private void HandleMovement()
    {
        if (target == null || agent == null) return;

        // Check if the robot has reached the target
        float distanceToTarget = Vector3.Distance(transform.position, target.position);

        if (distanceToTarget <= interactionRange)
        {
            // Switch to harvesting state
            currentState = RobotState.Harvesting;
            StartCoroutine(HarvestRoutine());
        }
    }

    /// <summary>
    /// Coroutine simulating the harvesting process.
    /// </summary>
    private IEnumerator HarvestRoutine()
    {
        if (debugMode) Debug.Log("Harvesting in progress...");

        // Simulate harvesting for the duration
        yield return new WaitForSeconds(harvestDuration);

        // Reset state to idle after harvesting
        currentState = RobotState.Idle;
        target = null;

        if (debugMode) Debug.Log("Harvesting complete.");
    }

    /// <summary>
    /// Debugging utility to draw interaction range in scene view.
    /// </summary>
    private void OnDrawGizmosSelected()
    {
        // Draw the interaction range around the robot
        Gizmos.color = Color.green;
        Gizmos.DrawWireSphere(transform.position, interactionRange);
    }
}
```
