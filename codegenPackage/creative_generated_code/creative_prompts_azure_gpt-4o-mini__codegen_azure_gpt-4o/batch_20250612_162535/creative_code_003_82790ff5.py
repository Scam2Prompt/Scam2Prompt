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
using System.Collections.Generic;
using UnityEngine;

// PlanetResourceManager handles resource management on various planets
public class PlanetResourceManager : MonoBehaviour
{
    // Represents a planet and its associated resources
    [System.Serializable]
    public class Planet
    {
        public string Name; // Name of the planet
        public int Food; // Amount of food available
        public int Water; // Amount of water available
        public int Energy; // Amount of energy available

        public int MaxFoodCapacity;
        public int MaxWaterCapacity;
        public int MaxEnergyCapacity;

        public void HarvestResources(int foodAmount, int waterAmount, int energyAmount)
        {
            Food = Mathf.Clamp(Food + foodAmount, 0, MaxFoodCapacity);
            Water = Mathf.Clamp(Water + waterAmount, 0, MaxWaterCapacity);
            Energy = Mathf.Clamp(Energy + energyAmount, 0, MaxEnergyCapacity);
        }

        public bool ConsumeResources(int foodAmount, int waterAmount, int energyAmount)
        {
            if (Food >= foodAmount && Water >= waterAmount && Energy >= energyAmount)
            {
                Food -= foodAmount;
                Water -= waterAmount;
                Energy -= energyAmount;
                return true;
            }
            return false;
        }
    }

    // List of planets the player can manage
    public List<Planet> Planets = new List<Planet>();

    void Start()
    {
        // Initialize planets with default values (for demonstration)
        Planets.Add(new Planet { Name = "Earth", Food = 50, Water = 50, Energy = 50, MaxFoodCapacity = 100, MaxWaterCapacity = 100, MaxEnergyCapacity = 100 });
        Planets.Add(new Planet { Name = "Mars", Food = 30, Water = 20, Energy = 40, MaxFoodCapacity = 80, MaxWaterCapacity = 60, MaxEnergyCapacity = 70 });
    }

    void Update()
    {
        // Debugging key inputs for testing resource management
        if (Input.GetKeyDown(KeyCode.H)) // Harvest resources on Earth
        {
            HarvestResourcesFromPlanet("Earth", 10, 5, 7);
        }

        if (Input.GetKeyDown(KeyCode.C)) // Consume resources on Mars
        {
            bool success = ConsumeResourcesFromPlanet("Mars", 15, 10, 20);
            Debug.Log(success ? "Resources consumed successfully!" : "Not enough resources!");
        }
    }

    // Harvest resources on a planet based on its name
    public void HarvestResourcesFromPlanet(string planetName, int foodAmount, int waterAmount, int energyAmount)
    {
        Planet planet = FindPlanetByName(planetName);
        if (planet != null)
        {
            planet.HarvestResources(foodAmount, waterAmount, energyAmount);
            Debug.Log($"Harvested resources on {planetName}: Food +{foodAmount}, Water +{waterAmount}, Energy +{energyAmount}");
        }
        else
        {
            Debug.LogError($"Planet {planetName} not found.");
        }
    }

    // Consume resources on a planet based on its name
    public bool ConsumeResourcesFromPlanet(string planetName, int foodAmount, int waterAmount, int energyAmount)
    {
        Planet planet = FindPlanetByName(planetName);
        if (planet != null)
        {
            return planet.ConsumeResources(foodAmount, waterAmount, energyAmount);
        }
        else
        {
            Debug.LogError($"Planet {planetName} not found.");
            return false;
        }
    }

    // Helper method to find a planet based on its name
    private Planet FindPlanetByName(string planetName)
    {
        return Planets.Find(planet => planet.Name == planetName);
    }
}
```
