"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Develop a simple game mechanic in Unity that allows players to manage resources on various planets, utilizing the advanced farming systems outlined in Stellar Crop.
Generated: DETERMINISTIC_82790ff5a307aa8a
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// ResourceManager is responsible for managing resources on various planets.
/// It includes functionality to manage crop growth and resource collection.
/// </summary>
public class ResourceManager : MonoBehaviour
{
    // Define a list to hold available crops
    private List<Crop> availableCrops;

    // Define a dictionary to hold resources for each planet
    private Dictionary<string, PlanetResources> planetResources;

    private void Start()
    {
        // Initialize the available crops and planet resources
        InitializeCrops();
        InitializePlanetResources();
    }

    /// <summary>
    /// Initializes available crops.
    /// </summary>
    private void InitializeCrops()
    {
        availableCrops = new List<Crop>
        {
            new Crop("Wheat", 5, 10), // Crop name, growth time, yield
            new Crop("Corn", 7, 15),
            new Crop("Rice", 6, 12)
        };
    }

    /// <summary>
    /// Initializes resources for each planet.
    /// </summary>
    private void InitializePlanetResources()
    {
        planetResources = new Dictionary<string, PlanetResources>
        {
            { "Earth", new PlanetResources(100, 50) },
            { "Mars", new PlanetResources(80, 40) }
        };
    }

    /// <summary>
    /// Start the growth of a crop on a specified planet.
    /// </summary>
    /// <param name="planetName">The name of the planet.</param>
    /// <param name="cropName">The name of the crop to grow.</param>
    public void StartCropGrowth(string planetName, string cropName)
    {
        if (planetResources.ContainsKey(planetName))
        {
            Crop cropToGrow = availableCrops.Find(c => c.Name == cropName);
            if (cropToGrow != null)
            {
                StartCoroutine(GrowCrop(planetName, cropToGrow));
            }
            else
            {
                Debug.LogError($"Crop '{cropName}' not found.");
            }
        }
        else
        {
            Debug.LogError($"Planet '{planetName}' not found.");
        }
    }

    /// <summary>
    /// Coroutine to grow a crop over time.
    /// </summary>
    /// <param name="planetName">The name of the planet.</param>
    /// <param name="crop">The crop to grow.</param>
    private IEnumerator GrowCrop(string planetName, Crop crop)
    {
        yield return new WaitForSeconds(crop.GrowthTime);

        // Once the crop has grown, add the yield to the planet's resources
        planetResources[planetName].Food += crop.Yield;
        Debug.Log($"Crop '{crop.Name}' has been harvested on planet '{planetName}'.");
    }

    /// <summary>
    /// Collect resources from a specified planet.
    /// </summary>
    /// <param name="planetName">The name of the planet.</param>
    public void CollectResources(string planetName)
    {
        if (planetResources.ContainsKey(planetName))
        {
            PlanetResources resources = planetResources[planetName];
            Debug.Log($"Collected {resources.Food} food and {resources.Water} water from planet '{planetName}'.");

            // Reset resources after collection
            resources.Food = 0;
            resources.Water = 0;
        }
        else
        {
            Debug.LogError($"Planet '{planetName}' not found.");
        }
    }
}

/// <summary>
/// Represents a crop with a name, growth time, and yield.
/// </summary>
[System.Serializable]
public class Crop
{
    public string Name { get; private set; }
    public float GrowthTime { get; private set; } // in seconds
    public int Yield { get; private set; } // amount of resources yielded

    public Crop(string name, float growthTime, int yield)
    {
        Name = name;
        GrowthTime = growthTime;
        Yield = yield;
    }
}

/// <summary>
/// Represents the resources available on a planet.
/// </summary>
[System.Serializable]
public class PlanetResources
{
    public int Food { get; set; }
    public int Water { get; set; }

    public PlanetResources(int food, int water)
    {
        Food = food;
        Water = water;
    }
}
```
