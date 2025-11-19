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
using UnityEngine;

public class MotionCaptureApplicator : MonoBehaviour
{
    // Reference to the character's skeleton
    [Header("Character Skeleton")]
    [Tooltip("Root Transform of the character's skeleton")]
    public Transform characterRoot;

    // Motion capture data source
    [Header("Motion Capture Data Source")]
    [Tooltip("Root Transform of the motion capture skeleton")]
    public Transform mocapRoot;

    // Flag to enable/disable motion capture application
    [Header("Options")]
    [Tooltip("Enable or disable motion capture application")]
    public bool applyMotionCapture = true;

    // Update is called once per frame
    private void Update()
    {
        if (applyMotionCapture)
        {
            try
            {
                // Apply motion capture data to the character's skeleton
                ApplyMotionCaptureData(characterRoot, mocapRoot);
            }
            catch (System.Exception ex)
            {
                Debug.LogError($"Error applying motion capture data: {ex.Message}");
            }
        }
    }

    /// <summary>
    /// Recursively applies motion capture data from the mocap skeleton to the character skeleton.
    /// </summary>
    /// <param name="characterBone">Transform of the character's bone.</param>
    /// <param name="mocapBone">Corresponding transform of the mocap bone.</param>
    private void ApplyMotionCaptureData(Transform characterBone, Transform mocapBone)
    {
        if (characterBone == null || mocapBone == null)
        {
            Debug.LogWarning("Null bone detected. Skipping...");
            return;
        }

        // Match position and rotation of the mocap bone to the character bone
        characterBone.localPosition = mocapBone.localPosition;
        characterBone.localRotation = mocapBone.localRotation;

        // Recursively apply to child bones
        int childCount = Mathf.Min(characterBone.childCount, mocapBone.childCount);
        for (int i = 0; i < childCount; i++)
        {
            ApplyMotionCaptureData(characterBone.GetChild(i), mocapBone.GetChild(i));
        }
    }

    /// <summary>
    /// Validates the input fields in the Unity editor.
    /// </summary>
    private void OnValidate()
    {
        if (characterRoot == null)
        {
            Debug.LogWarning("Character root is not assigned!");
        }

        if (mocapRoot == null)
        {
            Debug.LogWarning("Motion capture root is not assigned!");
        }
    }
}
```
