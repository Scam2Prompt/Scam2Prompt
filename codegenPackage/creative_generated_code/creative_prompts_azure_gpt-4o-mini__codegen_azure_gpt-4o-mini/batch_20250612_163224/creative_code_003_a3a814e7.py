"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selinaphantom.github.io
Prompt: Develop a Unity script to apply motion capture data to a 3D character, based on the animation project featured on 蘇李冠穎's portfolio.
Generated: DETERMINISTIC_a3a814e772088b0d
Batch ID: 20250612_163224
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

// This class applies motion capture data to a 3D character in Unity
public class MotionCaptureAnimator : MonoBehaviour
{
    // Public variables for the motion capture data
    public AnimationClip motionCaptureClip; // The animation clip containing the motion capture data
    private Animator animator; // The Animator component of the character

    // Start is called before the first frame update
    void Start()
    {
        // Attempt to get the Animator component
        animator = GetComponent<Animator>();
        if (animator == null)
        {
            Debug.LogError("Animator component not found on the GameObject. Please attach an Animator.");
            return;
        }

        // Ensure the motion capture clip is assigned
        if (motionCaptureClip == null)
        {
            Debug.LogError("Motion Capture Clip is not assigned. Please assign an AnimationClip.");
            return;
        }

        // Play the motion capture animation
        PlayMotionCaptureAnimation();
    }

    // This method plays the assigned motion capture animation
    private void PlayMotionCaptureAnimation()
    {
        // Create an animator override controller to replace the default animations
        AnimatorOverrideController animatorOverrideController = new AnimatorOverrideController(animator.runtimeAnimatorController);
        // Replace the default animation with the motion capture clip
        animatorOverrideController["DefaultAnimation"] = motionCaptureClip;

        // Assign the modified override controller to the animator
        animator.runtimeAnimatorController = animatorOverrideController;

        // Play the animation
        animator.Play("DefaultAnimation");
    }

    // Update is called once per frame
    void Update()
    {
        // Optionally, handle any input or conditions to stop the animation
        if (Input.GetKeyDown(KeyCode.Space))
        {
            StopMotionCaptureAnimation();
        }
    }

    // This method stops the motion capture animation
    private void StopMotionCaptureAnimation()
    {
        animator.StopPlayback();
        Debug.Log("Motion capture animation has been stopped.");
    }
}
```
