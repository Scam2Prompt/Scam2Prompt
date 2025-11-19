"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Write a Unity (C#) script for Stellar Crop that implements a dynamic weather system affecting crop growth, including features like "güneş patlamaları" and "değişken hava olayları."
Generated: DETERMINISTIC_3c13f45276921adc
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
using System.Collections.Generic;

/// <summary>
/// Dynamic weather system for Stellar Crop that affects crop growth.
/// Includes solar flares and variable weather events.
/// </summary>
public class DynamicWeatherSystem : MonoBehaviour
{
    [System.Serializable]
    public class WeatherProfile
    {
        public string name;
        public float temperatureEffect; // Positive for heat, negative for cold
        public float moistureEffect;    // Positive for rain, negative for drought
        public float sunlightEffect;    // Positive for sunny, negative for cloudy
        public float duration;          // In seconds
        public Color skyColor;
    }

    [Header("Weather Settings")]
    public List<WeatherProfile> weatherProfiles = new List<WeatherProfile>();
    public float weatherChangeInterval = 300f; // 5 minutes
    public float weatherTransitionTime = 30f;

    [Header("Solar Flare Settings")]
    public float solarFlareProbability = 0.01f;
    public float solarFlareDuration = 60f;
    public float solarFlareIntensity = 2f;
    public GameObject solarFlareEffect;

    private WeatherProfile currentWeather;
    private WeatherProfile targetWeather;
    private float weatherTimer;
    private float transitionProgress;
    private bool isTransitioning;
    private bool isSolarFlareActive;
    private float solarFlareTimer;
    private Light sunLight;
    private Camera mainCamera;

    private void Awake()
    {
        sunLight = RenderSettings.sun;
        mainCamera = Camera.main;
        InitializeWeather();
    }

    private void InitializeWeather()
    {
        if (weatherProfiles.Count == 0)
        {
            Debug.LogError("No weather profiles defined!");
            return;
        }

        currentWeather = weatherProfiles[0];
        targetWeather = GetRandomWeatherProfile();
        weatherTimer = weatherChangeInterval;
        UpdateWeatherEffects();
    }

    private void Update()
    {
        HandleWeatherTransitions();
        HandleSolarFlares();
    }

    private void HandleWeatherTransitions()
    {
        weatherTimer -= Time.deltaTime;

        if (weatherTimer <= 0f)
        {
            if (!isTransitioning)
            {
                targetWeather = GetRandomWeatherProfile();
                isTransitioning = true;
                transitionProgress = 0f;
            }
        }

        if (isTransitioning)
        {
            transitionProgress += Time.deltaTime / weatherTransitionTime;
            LerpWeatherEffects(currentWeather, targetWeather, transitionProgress);

            if (transitionProgress >= 1f)
            {
                currentWeather = targetWeather;
                isTransitioning = false;
                weatherTimer = currentWeather.duration;
            }
        }
    }

    private void HandleSolarFlares()
    {
        if (isSolarFlareActive)
        {
            solarFlareTimer -= Time.deltaTime;
            if (solarFlareTimer <= 0f)
            {
                EndSolarFlare();
            }
        }
        else if (Random.value < solarFlareProbability * Time.deltaTime)
        {
            StartSolarFlare();
        }
    }

    private void StartSolarFlare()
    {
        isSolarFlareActive = true;
        solarFlareTimer = solarFlareDuration;
        
        if (solarFlareEffect != null)
        {
            solarFlareEffect.SetActive(true);
        }

        // Intensify sunlight
        if (sunLight != null)
        {
            sunLight.intensity *= solarFlareIntensity;
        }
    }

    private void EndSolarFlare()
    {
        isSolarFlareActive = false;
        
        if (solarFlareEffect != null)
        {
            solarFlareEffect.SetActive(false);
        }

        // Restore sunlight
        if (sunLight != null)
        {
            sunLight.intensity /= solarFlareIntensity;
        }
    }

    private WeatherProfile GetRandomWeatherProfile()
    {
        if (weatherProfiles.Count == 0) return null;
        return weatherProfiles[Random.Range(0, weatherProfiles.Count)];
    }

    private void LerpWeatherEffects(WeatherProfile from, WeatherProfile to, float progress)
    {
        RenderSettings.ambientSkyColor = Color.Lerp(from.skyColor, to.skyColor, progress);
        
        if (sunLight != null)
        {
            sunLight.color = Color.Lerp(
                Color.white * (1f - from.sunlightEffect), 
                Color.white * (1f - to.sunlightEffect), 
                progress
            );
        }
    }

    private void UpdateWeatherEffects()
    {
        RenderSettings.ambientSkyColor = currentWeather.skyColor;
        
        if (sunLight != null)
        {
            sunLight.color = Color.white * (1f - currentWeather.sunlightEffect);
        }
    }

    /// <summary>
    /// Gets the current weather effects on crop growth
    /// </summary>
    public float GetTemperatureEffect()
    {
        return currentWeather.temperatureEffect * (isSolarFlareActive ? solarFlareIntensity : 1f);
    }

    /// <summary>
    /// Gets the current moisture effect on crop growth
    /// </summary>
    public float GetMoistureEffect()
    {
        return currentWeather.moistureEffect;
    }

    /// <summary>
    /// Gets the current sunlight effect on crop growth
    /// </summary>
    public float GetSunlightEffect()
    {
        return currentWeather.sunlightEffect * (isSolarFlareActive ? solarFlareIntensity : 1f);
    }

    /// <summary>
    /// Checks if a solar flare is currently active
    /// </summary>
    public bool IsSolarFlareActive()
    {
        return isSolarFlareActive;
    }
}
```
