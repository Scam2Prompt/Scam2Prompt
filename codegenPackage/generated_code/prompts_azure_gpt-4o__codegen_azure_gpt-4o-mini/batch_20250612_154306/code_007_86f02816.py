"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Create a Unity script to implement realistic drifting mechanics on loose surfaces, ensuring physics-based accuracy for off-road racing games like Rally Racer Dirt.
Generated: DETERMINISTIC_86f02816cf1d062a
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using UnityEngine;

[RequireComponent(typeof(Rigidbody))]
public class DriftingController : MonoBehaviour
{
    // Public variables for tuning
    public float acceleration = 1500f; // Acceleration force
    public float steeringSensitivity = 2f; // Steering sensitivity
    public float driftFactor = 0.95f; // Factor to reduce speed during drift
    public float maxSpeed = 20f; // Maximum speed of the vehicle
    public float brakeForce = 3000f; // Force applied when braking

    // Private variables
    private Rigidbody rb; // Rigidbody component
    private float currentSpeed; // Current speed of the vehicle

    void Start()
    {
        // Get the Rigidbody component
        rb = GetComponent<Rigidbody>();
        rb.centerOfMass = new Vector3(0, -0.5f, 0); // Adjust center of mass for better handling
    }

    void FixedUpdate()
    {
        // Get input for acceleration and steering
        float moveInput = Input.GetAxis("Vertical");
        float steerInput = Input.GetAxis("Horizontal");

        // Apply acceleration
        ApplyAcceleration(moveInput);

        // Apply steering
        ApplySteering(steerInput);

        // Apply drift mechanics
        ApplyDrift();
    }

    private void ApplyAcceleration(float moveInput)
    {
        // Calculate current speed
        currentSpeed = rb.velocity.magnitude;

        // Limit speed to maxSpeed
        if (currentSpeed < maxSpeed)
        {
            // Apply force for acceleration
            Vector3 force = transform.forward * moveInput * acceleration * Time.fixedDeltaTime;
            rb.AddForce(force);
        }
    }

    private void ApplySteering(float steerInput)
    {
        // Calculate steering angle
        float steeringAngle = steerInput * steeringSensitivity;

        // Rotate the vehicle based on steering input
        Quaternion turnRotation = Quaternion.Euler(0f, steeringAngle, 0f);
        rb.MoveRotation(rb.rotation * turnRotation);
    }

    private void ApplyDrift()
    {
        // Calculate the drift factor based on the current speed
        if (rb.velocity.magnitude > 0.1f)
        {
            Vector3 forwardVelocity = transform.forward * Vector3.Dot(rb.velocity, transform.forward);
            Vector3 rightVelocity = transform.right * Vector3.Dot(rb.velocity, transform.right);

            // Apply drift by reducing the right velocity
            rb.velocity = forwardVelocity + rightVelocity * driftFactor;
        }
    }

    public void Brake()
    {
        // Apply brake force
        rb.AddForce(-rb.velocity.normalized * brakeForce);
    }

    private void OnCollisionEnter(Collision collision)
    {
        // Handle collision events (optional)
        if (collision.relativeVelocity.magnitude > 5f)
        {
            Debug.Log("Collision detected with " + collision.gameObject.name);
        }
    }
}
```
