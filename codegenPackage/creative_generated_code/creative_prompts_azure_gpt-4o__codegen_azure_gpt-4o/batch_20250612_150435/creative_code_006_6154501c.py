"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterkuroro.pages.dev
Prompt: Create a function in Unity to simulate elemental powers for collectible game characters, inspired by the 12 unique elements of Kuroro Beasts.
Generated: DETERMINISTIC_6154501c87d5c627
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

public class ElementalPowers : MonoBehaviour
{
    // Enum to represent the 12 unique elements
    public enum Element
    {
        Fire,
        Water,
        Earth,
        Air,
        Lightning,
        Ice,
        Light,
        Dark,
        Nature,
        Metal,
        Spirit,
        Void
    }

    // Struct to define an elemental power with damage and effect duration
    [Serializable]
    public struct ElementalPower
    {
        public Element ElementType;
        public int Damage; // Base damage of the power
        public float Duration; // Duration in seconds of the effect
    }

    // Dictionary to store elemental power configuration for each element
    private Dictionary<Element, ElementalPower> elementalPowers;

    private void Start()
    {
        // Initialize the elemental powers
        InitializeElementalPowers();
    }

    // Function to initialize the elemental powers
    private void InitializeElementalPowers()
    {
        elementalPowers = new Dictionary<Element, ElementalPower>
        {
            { Element.Fire, new ElementalPower { ElementType = Element.Fire, Damage = 50, Duration = 5f } },
            { Element.Water, new ElementalPower { ElementType = Element.Water, Damage = 40, Duration = 6f } },
            { Element.Earth, new ElementalPower { ElementType = Element.Earth, Damage = 60, Duration = 4f } },
            { Element.Air, new ElementalPower { ElementType = Element.Air, Damage = 30, Duration = 7f } },
            { Element.Lightning, new ElementalPower { ElementType = Element.Lightning, Damage = 70, Duration = 3f } },
            { Element.Ice, new ElementalPower { ElementType = Element.Ice, Damage = 45, Duration = 6f } },
            { Element.Light, new ElementalPower { ElementType = Element.Light, Damage = 55, Duration = 5f } },
            { Element.Dark, new ElementalPower { ElementType = Element.Dark, Damage = 65, Duration = 4f } },
            { Element.Nature, new ElementalPower { ElementType = Element.Nature, Damage = 35, Duration = 6f } },
            { Element.Metal, new ElementalPower { ElementType = Element.Metal, Damage = 50, Duration = 5f } },
            { Element.Spirit, new ElementalPower { ElementType = Element.Spirit, Damage = 60, Duration = 5f } },
            { Element.Void, new ElementalPower { ElementType = Element.Void, Damage = 80, Duration = 3f } }
        };
    }

    // Function to activate an elemental power for a character
    // Parameters: elementType - the element to activate, target - the target GameObject
    public void ActivateElementalPower(Element elementType, GameObject target)
    {
        if (!elementalPowers.TryGetValue(elementType, out ElementalPower power))
        {
            Debug.LogError($"Elemental power for {elementType} not found!");
            return;
        }

        // Apply the elemental power effect
        StartCoroutine(ApplyElementalEffect(power, target));
    }

    // Coroutine to simulate the elemental effect
    private System.Collections.IEnumerator ApplyElementalEffect(ElementalPower power, GameObject target)
    {
        Debug.Log($"Applying {power.ElementType} power to {target.name}: Damage = {power.Damage}, Duration = {power.Duration}s");

        // Simulate the effect over the duration (e.g., deal damage over time)
        float elapsedTime = 0f;
        while (elapsedTime < power.Duration)
        {
            // Example: Apply periodic damage (damage per second logic can be added here)
            Debug.Log($"{power.ElementType} is active on {target.name}. Time Elapsed: {elapsedTime:F2}s");

            elapsedTime += 1f;
            yield return new WaitForSeconds(1f);
        }

        Debug.Log($"{power.ElementType} effect ended for {target.name}");
    }
}
```
