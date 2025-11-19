"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Develop a game mechanic in Unity (C#) for Stellar Crop that incorporates "Genetik analiz modülleri" to allow players to modify plant traits dynamically. Include a UI for selecting genetic traits.
Generated: DETERMINISTIC_06c6ab574e59d8cf
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
using UnityEngine.UI;
using System.Collections.Generic;

/// <summary>
/// Represents a genetic trait that can be modified
/// </summary>
[System.Serializable]
public class GeneticTrait
{
    public string traitName;
    public float currentValue;
    public float minValue;
    public float maxValue;
    public float defaultValue;
    public Sprite icon;
    [TextArea] public string description;
}

/// <summary>
/// Main controller for genetic analysis and modification
/// </summary>
public class GeneticAnalyzer : MonoBehaviour
{
    [Header("Genetic Traits")]
    public List<GeneticTrait> availableTraits = new List<GeneticTrait>();

    [Header("UI References")]
    public GameObject analyzerPanel;
    public GameObject traitButtonPrefab;
    public Transform traitsButtonContainer;
    public Text traitNameText;
    public Text traitValueText;
    public Text traitDescriptionText;
    public Image traitIconImage;
    public Slider traitSlider;
    public Button applyButton;
    public Button resetButton;

    private GeneticTrait currentSelectedTrait;
    private Dictionary<string, float> modifiedTraits = new Dictionary<string, float>();

    private void Start()
    {
        InitializeUI();
        analyzerPanel.SetActive(false);
    }

    /// <summary>
    /// Sets up the UI elements and event listeners
    /// </summary>
    private void InitializeUI()
    {
        // Clear existing buttons
        foreach (Transform child in traitsButtonContainer)
        {
            Destroy(child.gameObject);
        }

        // Create buttons for each trait
        foreach (GeneticTrait trait in availableTraits)
        {
            GameObject buttonObj = Instantiate(traitButtonPrefab, traitsButtonContainer);
            Button button = buttonObj.GetComponent<Button>();
            button.onClick.AddListener(() => SelectTrait(trait));

            // Set button appearance
            Image buttonIcon = buttonObj.GetComponentInChildren<Image>();
            Text buttonText = buttonObj.GetComponentInChildren<Text>();

            if (buttonIcon != null) buttonIcon.sprite = trait.icon;
            if (buttonText != null) buttonText.text = trait.traitName;
        }

        // Set up slider and buttons
        traitSlider.onValueChanged.AddListener(OnSliderValueChanged);
        applyButton.onClick.AddListener(ApplyTraitModification);
        resetButton.onClick.AddListener(ResetCurrentTrait);
    }

    /// <summary>
    /// Toggles the genetic analyzer UI panel
    /// </summary>
    public void ToggleAnalyzer()
    {
        analyzerPanel.SetActive(!analyzerPanel.activeSelf);
        
        if (analyzerPanel.activeSelf && currentSelectedTrait == null && availableTraits.Count > 0)
        {
            SelectTrait(availableTraits[0]);
        }
    }

    /// <summary>
    /// Selects a trait for modification
    /// </summary>
    private void SelectTrait(GeneticTrait trait)
    {
        currentSelectedTrait = trait;

        // Update UI with trait info
        traitNameText.text = trait.traitName;
        traitDescriptionText.text = trait.description;
        traitIconImage.sprite = trait.icon;

        // Set slider values
        traitSlider.minValue = trait.minValue;
        traitSlider.maxValue = trait.maxValue;
        
        // Check if we have a modified value for this trait
        if (modifiedTraits.ContainsKey(trait.traitName))
        {
            traitSlider.value = modifiedTraits[trait.traitName];
        }
        else
        {
            traitSlider.value = trait.currentValue;
        }

        UpdateTraitValueText();
    }

    /// <summary>
    /// Called when slider value changes
    /// </summary>
    private void OnSliderValueChanged(float value)
    {
        if (currentSelectedTrait != null)
        {
            UpdateTraitValueText();
        }
    }

    /// <summary>
    /// Updates the displayed trait value text
    /// </summary>
    private void UpdateTraitValueText()
    {
        traitValueText.text = $"{traitSlider.value:F2}";
    }

    /// <summary>
    /// Applies the current trait modification
    /// </summary>
    private void ApplyTraitModification()
    {
        if (currentSelectedTrait == null) return;

        float newValue = traitSlider.value;
        string traitName = currentSelectedTrait.traitName;

        if (modifiedTraits.ContainsKey(traitName))
        {
            modifiedTraits[traitName] = newValue;
        }
        else
        {
            modifiedTraits.Add(traitName, newValue);
        }

        // Apply the change to the actual trait
        currentSelectedTrait.currentValue = newValue;

        // Notify other systems about the change
        EventManager.Instance?.InvokeEvent(new GeneticTraitModifiedEvent(traitName, newValue));
    }

    /// <summary>
    /// Resets the current trait to its default value
    /// </summary>
    private void ResetCurrentTrait()
    {
        if (currentSelectedTrait == null) return;

        traitSlider.value = currentSelectedTrait.defaultValue;
        UpdateTraitValueText();

        // Remove from modified traits if it exists
        if (modifiedTraits.ContainsKey(currentSelectedTrait.traitName))
        {
            modifiedTraits.Remove(currentSelectedTrait.traitName);
        }

        // Reset the actual trait
        currentSelectedTrait.currentValue = currentSelectedTrait.defaultValue;

        // Notify other systems about the change
        EventManager.Instance?.InvokeEvent(new GeneticTraitModifiedEvent(
            currentSelectedTrait.traitName, 
            currentSelectedTrait.defaultValue
        ));
    }

    /// <summary>
    /// Gets the current value of a trait (modified or original)
    /// </summary>
    public float GetTraitValue(string traitName)
    {
        if (modifiedTraits.TryGetValue(traitName, out float value))
        {
            return value;
        }

        GeneticTrait trait = availableTraits.Find(t => t.traitName == traitName);
        return trait?.currentValue ?? 0f;
    }
}

/// <summary>
/// Event for when a genetic trait is modified
/// </summary>
public class GeneticTraitModifiedEvent
{
    public string traitName;
    public float newValue;

    public GeneticTraitModifiedEvent(string traitName, float newValue)
    {
        this.traitName = traitName;
        this.newValue = newValue;
    }
}

/// <summary>
/// Simple event manager for handling genetic trait modifications
/// </summary>
public class EventManager : MonoBehaviour
{
    public static EventManager Instance { get; private set; }

    public delegate void EventDelegate<T>(T e) where T : GeneticTraitModifiedEvent;
    private delegate void EventDelegate(GeneticTraitModifiedEvent e);

    private Dictionary<System.Type, EventDelegate> delegates = new Dictionary<System.Type, EventDelegate>();
    private Dictionary<System.Delegate, EventDelegate> delegateLookup = new Dictionary<System.Delegate, EventDelegate>();

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    public void InvokeEvent(GeneticTraitModifiedEvent e)
    {
        if (e == null)
        {
            Debug.LogWarning("Attempted to invoke null event");
            return;
        }

        if (delegates.TryGetValue(e.GetType(), out EventDelegate del))
        {
            del.Invoke(e);
        }
    }

    public void AddListener<T>(EventDelegate<T> del) where T : GeneticTraitModifiedEvent
    {
        if (delegateLookup.ContainsKey(del))
        {
            return;
        }

        EventDelegate internalDelegate = (e) => del((T)e);
        delegateLookup[del] = internalDelegate;

        if (delegates.TryGetValue(typeof(T), out EventDelegate tempDel))
        {
            delegates[typeof(T)] = tempDel += internalDelegate;
        }
        else
        {
            delegates[typeof(T)] = internalDelegate;
        }
    }

    public void RemoveListener<T>(EventDelegate<T> del) where T : GeneticTraitModifiedEvent
    {
        if (delegateLookup.TryGetValue(del, out EventDelegate internalDelegate))
        {
            if (delegates.TryGetValue(typeof(T), out EventDelegate tempDel))
            {
                tempDel -= internalDelegate;
                if (tempDel == null)
                {
                    delegates.Remove(typeof(T));
                }
                else
                {
                    delegates[typeof(T)] = tempDel;
                }
            }

            delegateLookup.Remove(del);
        }
    }
}
```
