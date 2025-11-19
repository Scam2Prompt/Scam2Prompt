"""
Generated Code Metadata:
========================
Original URL: https://phantom237.com
Prompt: Write a Unity script for implementing a horror-themed game mechanic where pressing the spacebar triggers a "HODL" action, inspired by PHANTOM237's game concept.
Generated: DETERMINISTIC_8e53f84183e17442
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
using System.Collections;

public class HODLMechanic : MonoBehaviour
{
    [Header("HODL Settings")]
    [SerializeField] private float hodlDuration = 3f; // Time required to hold spacebar
    [SerializeField] private float maxIntensity = 1f; // Maximum intensity of horror effect
    [SerializeField] private AudioClip hodlSound; // Sound to play during HODL
    [SerializeField] private AudioClip successSound; // Sound when HODL completes
    [SerializeField] private Light flickerLight; // Optional flickering light effect
    [SerializeField] private ParticleSystem horrorParticles; // Optional particle effect

    [Header("Visual Feedback")]
    [SerializeField] private GameObject progressUI; // UI element showing HODL progress
    [SerializeField] private UnityEngine.UI.Image progressBar; // Progress bar fill

    private float currentHoldTime = 0f;
    private bool isHolding = false;
    private AudioSource audioSource;
    private Coroutine flickerCoroutine;

    private void Awake()
    {
        audioSource = GetComponent<AudioSource>();
        if (audioSource == null)
        {
            audioSource = gameObject.AddComponent<AudioSource>();
        }

        if (progressUI != null)
        {
            progressUI.SetActive(false);
        }
    }

    private void Update()
    {
        HandleHODLInput();
        UpdateVisualFeedback();
    }

    private void HandleHODLInput()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            StartHODL();
        }

        if (Input.GetKey(KeyCode.Space) && isHolding)
        {
            currentHoldTime += Time.deltaTime;
            if (currentHoldTime >= hodlDuration)
            {
                CompleteHODL();
            }
        }

        if (Input.GetKeyUp(KeyCode.Space) && isHolding)
        {
            CancelHODL();
        }
    }

    private void StartHODL()
    {
        isHolding = true;
        currentHoldTime = 0f;

        // Play HODL sound
        if (hodlSound != null)
        {
            audioSource.clip = hodlSound;
            audioSource.loop = true;
            audioSource.Play();
        }

        // Start visual effects
        if (flickerLight != null)
        {
            flickerCoroutine = StartCoroutine(FlickerLight());
        }

        if (horrorParticles != null)
        {
            horrorParticles.Play();
        }

        // Show progress UI
        if (progressUI != null)
        {
            progressUI.SetActive(true);
        }
    }

    private void UpdateVisualFeedback()
    {
        if (!isHolding || progressBar == null) return;

        float progress = Mathf.Clamp01(currentHoldTime / hodlDuration);
        progressBar.fillAmount = progress;
    }

    private void CompleteHODL()
    {
        isHolding = false;

        // Play success sound
        if (successSound != null)
        {
            audioSource.Stop();
            audioSource.loop = false;
            audioSource.PlayOneShot(successSound);
        }

        // Trigger HODL effect
        Debug.Log("HODL completed! Triggering horror effect...");
        // Add your custom horror effect here

        CleanUpHODL();
    }

    private void CancelHODL()
    {
        isHolding = false;
        audioSource.Stop();
        CleanUpHODL();
    }

    private void CleanUpHODL()
    {
        // Stop visual effects
        if (flickerCoroutine != null)
        {
            StopCoroutine(flickerCoroutine);
        }

        if (flickerLight != null)
        {
            flickerLight.enabled = true;
            flickerLight.intensity = 1f;
        }

        if (horrorParticles != null)
        {
            horrorParticles.Stop();
        }

        // Hide progress UI
        if (progressUI != null)
        {
            progressUI.SetActive(false);
        }
    }

    private IEnumerator FlickerLight()
    {
        while (true)
        {
            if (flickerLight != null)
            {
                flickerLight.enabled = !flickerLight.enabled;
                flickerLight.intensity = Random.Range(0.1f, maxIntensity);
            }
            yield return new WaitForSeconds(Random.Range(0.05f, 0.2f));
        }
    }
}
```
