"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Develop a game mechanic in Unity (C#) for Stellar Crop that incorporates "Genetik analiz modülleri" to allow players to modify plant traits dynamically. Include a UI for selecting genetic traits.
Generated: DETERMINISTIC_06c6ab574e59d8cf
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
using UnityEngine.UI;

public class GeneticTrait
{
    public string Name { get; private set; }
    public float Value { get; private set; }

    public GeneticTrait(string name, float value)
    {
        Name = name;
        Value = value;
    }
}

public class Plant
{
    public string PlantName { get; private set; }
    public GeneticTrait[] Traits { get; private set; }

    public Plant(string plantName, GeneticTrait[] traits)
    {
        PlantName = plantName;
        Traits = traits;
    }

    public void ModifyTrait(string traitName, float newValue)
    {
        foreach (var trait in Traits)
        {
            if (trait.Name == traitName)
            {
                trait.Value = newValue;
                return;
            }
        }
        Debug.LogError($"Trait {traitName} not found on plant {PlantName}");
    }
}

public class TraitSelector : MonoBehaviour
{
    public Plant CurrentPlant; // The plant being modified
    public Dropdown TraitDropdown; // Dropdown to select traits
    public InputField TraitValueInput; // Input field for new trait value
    public Button ApplyButton; // Button to apply changes

    private void Start()
    {
        // Set up the UI elements
        SetupDropdown();
        ApplyButton.onClick.AddListener(OnApplyButtonClicked);
    }

    private void SetupDropdown()
    {
        // Populate the dropdown with trait names
        TraitDropdown.ClearOptions();
        foreach (var trait in CurrentPlant.Traits)
        {
            TraitDropdown.options.Add(new Dropdown.OptionData(trait.Name));
        }
        TraitDropdown.RefreshShownValue();
    }

    private void OnApplyButtonClicked()
    {
        try
        {
            // Get the selected trait and new value from UI
            string selectedTrait = TraitDropdown.options[TraitDropdown.value].text;
            float newValue = float.Parse(TraitValueInput.text);

            // Modify the plant trait
            CurrentPlant.ModifyTrait(selectedTrait, newValue);
            Debug.Log($"Modified {selectedTrait} to {newValue} for plant {CurrentPlant.PlantName}");
        }
        catch (System.FormatException)
        {
            Debug.LogError("Please enter a valid number for the trait value.");
        }
        catch (System.Exception ex)
        {
            Debug.LogError($"An error occurred: {ex.Message}");
        }
    }
}
```

```csharp
// Additional example script to initialize game objects
public class GameInitializer : MonoBehaviour
{
    public TraitSelector traitSelectorPrefab; // Prefab for the TraitSelector
    private Plant samplePlant;

    private void Start()
    {
        // Create a sample plant with some genetic traits
        var traits = new GeneticTrait[]
        {
            new GeneticTrait("Growth Rate", 1.0f),
            new GeneticTrait("Resistance", 0.8f),
            new GeneticTrait("Color Intensity", 0.5f)
        };
        
        samplePlant = new Plant("Sample Plant", traits);

        // Instantiate the TraitSelector and set the current plant
        TraitSelector traitSelector = Instantiate(traitSelectorPrefab);
        traitSelector.CurrentPlant = samplePlant;
    }
}
```
