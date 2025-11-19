"""
Generated Code Metadata:
========================
Original URL: https://hamsterkombatgame.pages.dev
Prompt: Develop a C# class that represents the characters and skins in Hamster Kombat, including methods for time-limited events.
Generated: DETERMINISTIC_69144abc5a089c3a
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;

namespace HamsterKombat
{
    /// <summary>
    /// Represents a character in Hamster Kombat.
    /// </summary>
    public class Character
    {
        /// <summary>
        /// Name of the character.
        /// </summary>
        public string Name { get; private set; }

        /// <summary>
        /// List of skins available for the character.
        /// </summary>
        public List<string> Skins { get; private set; }

        /// <summary>
        /// Constructor to initialize a character with a name and skins.
        /// </summary>
        /// <param name="name">Name of the character.</param>
        /// <param name="skins">List of skins for the character.</param>
        public Character(string name, List<string> skins)
        {
            if (string.IsNullOrWhiteSpace(name))
                throw new ArgumentException("Character name cannot be null or empty.", nameof(name));

            Name = name;
            Skins = skins ?? throw new ArgumentNullException(nameof(skins), "Skins list cannot be null.");
        }

        /// <summary>
        /// Adds a new skin to the character.
        /// </summary>
        /// <param name="skin">Name of the skin to add.</param>
        public void AddSkin(string skin)
        {
            if (string.IsNullOrWhiteSpace(skin))
                throw new ArgumentException("Skin name cannot be null or empty.", nameof(skin));

            Skins.Add(skin);
        }

        /// <summary>
        /// Removes a skin from the character.
        /// </summary>
        /// <param name="skin">Name of the skin to remove.</param>
        /// <returns>True if the skin was removed, false otherwise.</returns>
        public bool RemoveSkin(string skin)
        {
            if (string.IsNullOrWhiteSpace(skin))
                throw new ArgumentException("Skin name cannot be null or empty.", nameof(skin));

            return Skins.Remove(skin);
        }

        /// <summary>
        /// Checks if the character has a specific skin.
        /// </summary>
        /// <param name="skin">Name of the skin to check.</param>
        /// <returns>True if the skin exists, false otherwise.</returns>
        public bool HasSkin(string skin)
        {
            if (string.IsNullOrWhiteSpace(skin))
                throw new ArgumentException("Skin name cannot be null or empty.", nameof(skin));

            return Skins.Contains(skin);
        }
    }

    /// <summary>
    /// Represents a time-limited event for unlocking skins.
    /// </summary>
    public class TimeLimitedEvent
    {
        /// <summary>
        /// Name of the event.
        /// </summary>
        public string EventName { get; private set; }

        /// <summary>
        /// Start time of the event.
        /// </summary>
        public DateTime StartTime { get; private set; }

        /// <summary>
        /// End time of the event.
        /// </summary>
        public DateTime EndTime { get; private set; }

        /// <summary>
        /// Skins available during the event.
        /// </summary>
        public List<string> EventSkins { get; private set; }

        /// <summary>
        /// Constructor to initialize a time-limited event.
        /// </summary>
        /// <param name="eventName">Name of the event.</param>
        /// <param name="startTime">Start time of the event.</param>
        /// <param name="endTime">End time of the event.</param>
        /// <param name="eventSkins">Skins available during the event.</param>
        public TimeLimitedEvent(string eventName, DateTime startTime, DateTime endTime, List<string> eventSkins)
        {
            if (string.IsNullOrWhiteSpace(eventName))
                throw new ArgumentException("Event name cannot be null or empty.", nameof(eventName));

            if (startTime >= endTime)
                throw new ArgumentException("Start time must be earlier than end time.", nameof(startTime));

            EventName = eventName;
            StartTime = startTime;
            EndTime = endTime;
            EventSkins = eventSkins ?? throw new ArgumentNullException(nameof(eventSkins), "Event skins list cannot be null.");
        }

        /// <summary>
        /// Checks if the event is currently active.
        /// </summary>
        /// <returns>True if the event is active, false otherwise.</returns>
        public bool IsActive()
        {
            DateTime now = DateTime.UtcNow;
            return now >= StartTime && now <= EndTime;
        }

        /// <summary>
        /// Unlocks event skins for a character if the event is active.
        /// </summary>
        /// <param name="character">Character to unlock skins for.</param>
        public void UnlockSkinsForCharacter(Character character)
        {
            if (character == null)
                throw new ArgumentNullException(nameof(character), "Character cannot be null.");

            if (!IsActive())
                throw new InvalidOperationException("Event is not active.");

            foreach (var skin in EventSkins)
            {
                if (!character.HasSkin(skin))
                {
                    character.AddSkin(skin);
                }
            }
        }
    }
}
```
