"""
Generated Code Metadata:
========================
Original URL: https://selinaphantom.github.io
Prompt: Develop a Unity script to apply motion capture data to a 3D character, based on the animation project featured on 蘇李冠穎's portfolio.
Generated: DETERMINISTIC_a3a814e772088b0d
Batch ID: 20250612_163224
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
using System.IO;

/// <summary>
/// Applies motion capture data to a 3D character in Unity.
/// </summary>
public class MotionCapturePlayer : MonoBehaviour
{
    [Header("Motion Capture Settings")]
    [Tooltip("The target character to apply motion capture data to.")]
    public GameObject targetCharacter;

    [Tooltip("The file containing motion capture data (CSV format).")]
    public TextAsset motionCaptureDataFile;

    [Tooltip("Frame rate for playback (frames per second).")]
    public float playbackFrameRate = 30f;

    [Tooltip("Whether to loop the animation.")]
    public bool loopAnimation = true;

    [Tooltip("List of bones to apply motion data to.")]
    public List<string> boneNames = new List<string>();

    // Private variables
    private List<Dictionary<string, Quaternion>> frameData;
    private int currentFrame = 0;
    private float frameTimer = 0f;
    private bool isPlaying = false;

    /// <summary>
    /// Initializes the motion capture player and loads data.
    /// </summary>
    void Start()
    {
        if (targetCharacter == null)
        {
            Debug.LogError("Target character is not assigned!");
            return;
        }

        if (motionCaptureDataFile == null)
        {
            Debug.LogError("Motion capture data file is not assigned!");
            return;
        }

        LoadMotionCaptureData();
        isPlaying = true;
    }

    /// <summary>
    /// Loads motion capture data from the CSV file.
    /// </summary>
    private void LoadMotionCaptureData()
    {
        frameData = new List<Dictionary<string, Quaternion>>();

        try
        {
            string[] lines = motionCaptureDataFile.text.Split('\n');

            for (int i = 1; i < lines.Length; i++) // Skip header row
            {
                if (string.IsNullOrEmpty(lines[i].Trim())) continue;

                string[] values = lines[i].Split(',');
                Dictionary<string, Quaternion> frame = new Dictionary<string, Quaternion>();

                for (int j = 0; j < boneNames.Count; j++)
                {
                    if (j * 4 + 3 >= values.Length) continue;

                    float x = float.Parse(values[j * 4]);
                    float y = float.Parse(values[j * 4 + 1]);
                    float z = float.Parse(values[j * 4 + 2]);
                    float w = float.Parse(values[j * 4 + 3]);

                    frame[boneNames[j]] = new Quaternion(x, y, z, w);
                }

                frameData.Add(frame);
            }

            Debug.Log($"Successfully loaded {frameData.Count} frames of motion capture data.");
        }
        catch (System.Exception e)
        {
            Debug.LogError($"Error loading motion capture data: {e.Message}");
        }
    }

    /// <summary>
    /// Updates the character's pose based on current frame data.
    /// </summary>
    private void UpdateCharacterPose()
    {
        if (currentFrame >= frameData.Count) return;

        Dictionary<string, Quaternion> currentFrameData = frameData[currentFrame];

        foreach (var bone in boneNames)
        {
            Transform boneTransform = FindDeepChild(targetCharacter.transform, bone);
            if (boneTransform != null && currentFrameData.ContainsKey(bone))
            {
                boneTransform.localRotation = currentFrameData[bone];
            }
        }
    }

    /// <summary>
    /// Recursively searches for a child transform by name.
    /// </summary>
    private Transform FindDeepChild(Transform parent, string name)
    {
        foreach (Transform child in parent)
        {
            if (child.name == name)
                return child;

            Transform result = FindDeepChild(child, name);
            if (result != null)
                return result;
        }
        return null;
    }

    /// <summary>
    /// Handles frame advancement and animation playback.
    /// </summary>
    void Update()
    {
        if (!isPlaying || frameData == null || frameData.Count == 0) return;

        frameTimer += Time.deltaTime;
        float frameDuration = 1f / playbackFrameRate;

        if (frameTimer >= frameDuration)
        {
            frameTimer = 0f;
            currentFrame++;

            if (currentFrame >= frameData.Count)
            {
                if (loopAnimation)
                {
                    currentFrame = 0;
                }
                else
                {
                    isPlaying = false;
                    return;
                }
            }

            UpdateCharacterPose();
        }
    }

    /// <summary>
    /// Starts or resumes animation playback.
    /// </summary>
    public void Play()
    {
        isPlaying = true;
    }

    /// <summary>
    /// Pauses animation playback.
    /// </summary>
    public void Pause()
    {
        isPlaying = false;
    }

    /// <summary>
    /// Stops animation playback and resets to first frame.
    /// </summary>
    public void Stop()
    {
        isPlaying = false;
        currentFrame = 0;
        frameTimer = 0f;
        if (frameData != null && frameData.Count > 0)
        {
            UpdateCharacterPose();
        }
    }

    /// <summary>
    /// Jumps to a specific frame in the animation.
    /// </summary>
    public void GoToFrame(int frameNumber)
    {
        if (frameData == null) return;

        currentFrame = Mathf.Clamp(frameNumber, 0, frameData.Count - 1);
        frameTimer = 0f;
        UpdateCharacterPose();
    }
}
```
