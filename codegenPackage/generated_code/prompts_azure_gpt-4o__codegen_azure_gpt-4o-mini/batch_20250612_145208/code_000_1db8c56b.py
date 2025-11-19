"""
Generated Code Metadata:
========================
Original URL: https://dev-x-studios.com
Prompt: Write Unity C# code for a game that incorporates immersive storytelling, inspired by the mission of Dev-X-Studios to transport players to new worlds and create unforgettable experiences.
Generated: DETERMINISTIC_1db8c56b1830ea4b
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class StoryManager : MonoBehaviour
{
    // UI elements for displaying story text and options
    public Text storyText;
    public Button[] optionButtons;

    // Story data structure
    [System.Serializable]
    public class StoryNode
    {
        public string text; // The text to display
        public StoryNode[] options; // Possible next nodes
    }

    // The starting point of the story
    public StoryNode startNode;

    // Current node in the story
    private StoryNode currentNode;

    void Start()
    {
        // Initialize the story with the starting node
        if (startNode != null)
        {
            currentNode = startNode;
            DisplayStoryNode(currentNode);
        }
        else
        {
            Debug.LogError("Start node is not assigned in the StoryManager.");
        }
    }

    // Display the current story node
    void DisplayStoryNode(StoryNode node)
    {
        // Set the story text
        storyText.text = node.text;

        // Clear previous options
        foreach (Button button in optionButtons)
        {
            button.gameObject.SetActive(false);
        }

        // Display options if available
        if (node.options != null && node.options.Length > 0)
        {
            for (int i = 0; i < node.options.Length; i++)
            {
                if (i < optionButtons.Length)
                {
                    optionButtons[i].gameObject.SetActive(true);
                    optionButtons[i].GetComponentInChildren<Text>().text = node.options[i].text;
                    int index = i; // Capture the index for the button listener
                    optionButtons[i].onClick.RemoveAllListeners(); // Clear previous listeners
                    optionButtons[i].onClick.AddListener(() => OnOptionSelected(node.options[index]));
                }
            }
        }
    }

    // Handle option selection
    void OnOptionSelected(StoryNode selectedNode)
    {
        currentNode = selectedNode; // Update the current node
        DisplayStoryNode(currentNode); // Display the new node
    }

    // Load a new scene (if needed)
    public void LoadScene(string sceneName)
    {
        try
        {
            SceneManager.LoadScene(sceneName);
        }
        catch (System.Exception ex)
        {
            Debug.LogError($"Failed to load scene '{sceneName}': {ex.Message}");
        }
    }
}
```

```csharp
using UnityEngine;

public class GameManager : MonoBehaviour
{
    // Singleton instance
    public static GameManager Instance { get; private set; }

    // Player's current state
    public int playerHealth = 100;

    void Awake()
    {
        // Ensure only one instance of GameManager exists
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject); // Persist across scenes
        }
        else
        {
            Destroy(gameObject); // Destroy duplicate
        }
    }

    // Method to handle player damage
    public void TakeDamage(int damage)
    {
        playerHealth -= damage;
        if (playerHealth <= 0)
        {
            GameOver();
        }
    }

    // Handle game over logic
    void GameOver()
    {
        Debug.Log("Game Over! Restarting...");
        // Restart the game or load a game over scene
        LoadScene("MainMenu");
    }

    // Load a new scene
    public void LoadScene(string sceneName)
    {
        try
        {
            SceneManager.LoadScene(sceneName);
        }
        catch (System.Exception ex)
        {
            Debug.LogError($"Failed to load scene '{sceneName}': {ex.Message}");
        }
    }
}
```

```csharp
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float moveSpeed = 5f; // Speed of the player movement

    void Update()
    {
        // Handle player movement
        MovePlayer();
    }

    // Move the player based on input
    void MovePlayer()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");

        Vector3 movement = new Vector3(horizontal, 0, vertical) * moveSpeed * Time.deltaTime;
        transform.Translate(movement, Space.World);
    }
}
```

```csharp
using UnityEngine;

public class AudioManager : MonoBehaviour
{
    public AudioSource backgroundMusic; // Background music source

    void Start()
    {
        PlayBackgroundMusic();
    }

    // Play background music
    void PlayBackgroundMusic()
    {
        if (backgroundMusic != null)
        {
            backgroundMusic.Play();
        }
        else
        {
            Debug.LogError("Background music source is not assigned.");
        }
    }
}
```

```csharp
using UnityEngine;

public class SceneLoader : MonoBehaviour
{
    // Load a scene by name
    public void LoadScene(string sceneName)
    {
        try
        {
            UnityEngine.SceneManagement.SceneManager.LoadScene(sceneName);
        }
        catch (System.Exception ex)
        {
            Debug.LogError($"Failed to load scene '{sceneName}': {ex.Message}");
        }
    }
}
```

```csharp
using UnityEngine;

public class GameInitializer : MonoBehaviour
{
    void Start()
    {
        // Initialize game settings or load initial scene
        LoadInitialScene();
    }

    // Load the initial scene
    void LoadInitialScene()
    {
        SceneLoader sceneLoader = FindObjectOfType<SceneLoader>();
        if (sceneLoader != null)
        {
            sceneLoader.LoadScene("MainMenu");
        }
        else
        {
            Debug.LogError("SceneLoader not found in the scene.");
        }
    }
}
```

This code provides a basic structure for a Unity game that incorporates immersive storytelling, player control, audio management, and scene loading, following best practices and including error handling.
