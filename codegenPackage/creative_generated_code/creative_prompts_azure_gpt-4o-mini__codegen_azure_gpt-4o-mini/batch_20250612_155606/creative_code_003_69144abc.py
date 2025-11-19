"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkombatgame.pages.dev
Prompt: Develop a C# class that represents the characters and skins in Hamster Kombat, including methods for time-limited events.
Generated: DETERMINISTIC_69144abc5a089c3a
Batch ID: 20250612_155606
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

/// <summary>
/// Represents a character in Hamster Kombat with associated skins.
/// </summary>
public class HamsterCharacter
{
    // Properties to store character details
    public string Name { get; private set; }
    public List<HamsterSkin> Skins { get; private set; }
    
    // Constructor to initialize a character with a name and skins
    public HamsterCharacter(string name)
    {
        if (string.IsNullOrWhiteSpace(name))
        {
            throw new ArgumentException("Character name cannot be null or empty.", nameof(name));
        }

        Name = name;
        Skins = new List<HamsterSkin>();
    }

    /// <summary>
    /// Adds a skin to the character.
    /// </summary>
    /// <param name="skin">The skin to add.</param>
    public void AddSkin(HamsterSkin skin)
    {
        if (skin == null)
        {
            throw new ArgumentNullException(nameof(skin), "Skin cannot be null.");
        }

        Skins.Add(skin);
    }
    
    /// <summary>
    /// Selects a skin for the character.
    /// </summary>
    /// <param name="skinName">The name of the skin to select.</param>
    /// <returns>Selected skin.</returns>
    public HamsterSkin SelectSkin(string skinName)
    {
        var skin = Skins.Find(s => s.Name.Equals(skinName, StringComparison.OrdinalIgnoreCase));
        if (skin == null)
        {
            throw new InvalidOperationException($"Skin '{skinName}' not found for character '{Name}'.");
        }

        return skin;
    }
}

/// <summary>
/// Represents a skin that a character can use.
/// </summary>
public class HamsterSkin
{
    // Properties to store skin details
    public string Name { get; private set; }
    public string Description { get; private set; }
    public DateTime AvailableUntil { get; private set; }

    // Constructor to initialize a skin with details
    public HamsterSkin(string name, string description, DateTime availableUntil)
    {
        if (string.IsNullOrWhiteSpace(name))
        {
            throw new ArgumentException("Skin name cannot be null or empty.", nameof(name));
        }

        if (availableUntil <= DateTime.Now)
        {
            throw new ArgumentException("Skin must be available in the future.", nameof(availableUntil));
        }

        Name = name;
        Description = description;
        AvailableUntil = availableUntil;
    }

    /// <summary>
    /// Checks if the skin is currently available.
    /// </summary>
    /// <returns>True if available; otherwise, false.</returns>
    public bool IsAvailable()
    {
        return DateTime.Now < AvailableUntil;
    }
}
```
