"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev-x-studios.com
Prompt: Write Unity C# code for a game that incorporates immersive storytelling, inspired by the mission of Dev-X-Studios to transport players to new worlds and create unforgettable experiences.
Generated: DETERMINISTIC_1db8c56b1830ea4b
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class StoryManager : MonoBehaviour
{
    // UI elements to display story content
    [SerializeField] private Text storyText; // Text component to show story dialogues
    [SerializeField] private Button nextButton; // Button to progress through the story

    // Story-related variables
    private Queue<string> storyLines; // Queue to hold lines of the story
    private bool isStoryActive; // Flag to check if the story is currently active

    // Start is called before the first frame update
    private void Start()
    {
        // Initialize the story lines queue
        storyLines = new Queue<string>();

        // Start the immersive storytelling experience
        StartStory();
    }

    /// <summary>
    /// Initializes the story and prepares it for display.
    /// </summary>
    private void StartStory()
    {
        // Clear the queue in case it's been used previously
        storyLines.Clear();

        // Add story lines to the queue
        storyLines.Enqueue("Welcome to the world of Dev-X Studios.");
        storyLines.Enqueue("Here, we transport players to new worlds and create unforgettable experiences.");
        storyLines.Enqueue("Your journey begins now...");

        // Set the story as active and display the first line
        isStoryActive = true;
        DisplayNextLine();
    }

    /// <summary>
    /// Displays the next line of the story from the queue.
    /// </summary>
    public void DisplayNextLine()
    {
        // Check if there are no more lines in the queue
        if (storyLines.Count == 0)
        {
            EndStory();
            return;
        }

        // Fetch the next line and display it in the UI
        string nextLine = storyLines.Dequeue();
        storyText.text = nextLine;
    }

    /// <summary>
    /// Ends the story and disables storytelling UI elements.
    /// </summary>
    private void EndStory()
    {
        isStoryActive = false;
        storyText.text = "The story is complete. Thank you for experiencing it!";
        nextButton.gameObject.SetActive(false); // Hide the next button
    }

    /// <summary>
    /// Handles input for progressing through the story.
    /// </summary>
    public void OnNextButtonPressed()
    {
        // Check if the story is active before progressing
        if (isStoryActive)
        {
            DisplayNextLine();
        }
    }
}
```

### Usage Notes
1. Attach this script to a GameObject in your Unity scene.
2. Assign a `Text` component (e.g., UI Text) to the `storyText` field in the inspector.
3. Assign a `Button` component to the `nextButton` field in the inspector.
4. Set the `Button`'s OnClick event to call the `OnNextButtonPressed()` method in this script via the Unity Inspector.
