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
using UnityEngine;
using UnityEngine.AI;

// Class responsible for player interaction with Otonom hasat robotları
public class RobotInteraction : MonoBehaviour
{
    // Reference to the NavMeshAgent for pathfinding
    private NavMeshAgent agent;

    // Reference to the assigned target for the robot
    private Transform target;

    // Enum to define the states of the robot
    public enum RobotState
    {
        Idle,
        Moving,
        Harvesting
    }

    // Current state of the robot
    private RobotState currentState;

    private void Start()
    {
        // Initialize the NavMeshAgent component
        agent = GetComponent<NavMeshAgent>();
        currentState = RobotState.Idle;
    }

    private void Update()
    {
        // Handle state-specific behavior
        switch (currentState)
        {
            case RobotState.Moving:
                HandleMovement();
                break;
            case RobotState.Harvesting:
                HandleHarvesting();
                break;
        }
    }

    // Method to assign a target for the robot to move towards
    public void AssignTarget(Transform newTarget)
    {
        if (newTarget == null)
        {
            Debug.LogError("Target cannot be null.");
            return;
        }

        target = newTarget;
        currentState = RobotState.Moving;
        agent.SetDestination(target.position);
    }

    // Handle movement logic for the robot
    private void HandleMovement()
    {
        // Check if the robot has reached the target
        if (agent.reachedDestination)
        {
            Debug.Log("Reached Destination: " + target.name);
            currentState = RobotState.Harvesting;
        }
    }

    // Handle harvesting logic for the robot
    private void HandleHarvesting()
    {
        // Simulate harvesting process
        Debug.Log("Harvesting from: " + target.name);
        // Here you can add logic to actually harvest resources

        // After harvesting, return to idle state
        currentState = RobotState.Idle;
        target = null; // Clear target after harvesting
    }

    // Method to cancel current task
    public void CancelTask()
    {
        if (currentState == RobotState.Moving || currentState == RobotState.Harvesting)
        {
            Debug.Log("Task canceled.");
            agent.ResetPath(); // Stop the robot's current pathfinding
            currentState = RobotState.Idle; // Reset to idle
            target = null; // Clear target
        }
    }
}
```
