"""
Generated Code Metadata:
========================
Original URL: https://hypersteakin.site
Prompt: Develop a Unity-based indie game prototype inspired by Berlin's indie gaming scene, as highlighted in the HyperSteakin Indie Showcase.
Generated: DETERMINISTIC_1528c8c0cf0dc45b
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Berlin Indie Game Prototype**
================================

### Game Description

A Unity-based indie game prototype inspired by Berlin's indie gaming scene.

### Code

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Game Manager class
public class GameManager : MonoBehaviour
{
    // Singleton instance
    public static GameManager instance;

    // Game state
    public enum GameState { Menu, Playing, Paused, GameOver }
    public GameState currentState;

    // Player object
    public GameObject player;

    // Score and lives
    public int score = 0;
    public int lives = 3;

    private void Awake()
    {
        // Initialize singleton instance
        if (instance == null)
        {
            instance = this;
        }
        else if (instance != this)
        {
            Destroy(gameObject);
        }
    }

    private void Start()
    {
        // Initialize game state
        currentState = GameState.Menu;
    }

    // Update game state
    public void UpdateGameState(GameState newState)
    {
        currentState = newState;

        // Handle game state changes
        switch (newState)
        {
            case GameState.Menu:
                // Show menu
                break;
            case GameState.Playing:
                // Start game
                break;
            case GameState.Paused:
                // Pause game
                break;
            case GameState.GameOver:
                // Game over logic
                break;
        }
    }

    // Update score
    public void UpdateScore(int points)
    {
        score += points;
    }

    // Update lives
    public void UpdateLives(int livesLost)
    {
        lives -= livesLost;

        // Check for game over
        if (lives <= 0)
        {
            UpdateGameState(GameState.GameOver);
        }
    }
}

// Player class
public class Player : MonoBehaviour
{
    // Player movement speed
    public float speed = 5.0f;

    // Player rigidbody
    private Rigidbody rb;

    private void Start()
    {
        // Initialize rigidbody
        rb = GetComponent<Rigidbody>();
    }

    private void Update()
    {
        // Get input
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        // Move player
        Vector3 movement = new Vector3(horizontalInput, 0, verticalInput);
        rb.velocity = movement * speed;
    }

    // Collision detection
    private void OnCollisionEnter(Collision collision)
    {
        // Check for collision with enemy
        if (collision.gameObject.CompareTag("Enemy"))
        {
            // Update lives
            GameManager.instance.UpdateLives(1);
        }
    }
}

// Enemy class
public class Enemy : MonoBehaviour
{
    // Enemy movement speed
    public float speed = 2.0f;

    // Enemy rigidbody
    private Rigidbody rb;

    private void Start()
    {
        // Initialize rigidbody
        rb = GetComponent<Rigidbody>();
    }

    private void Update()
    {
        // Move enemy
        rb.velocity = transform.forward * speed;
    }

    // Collision detection
    private void OnCollisionEnter(Collision collision)
    {
        // Check for collision with player
        if (collision.gameObject.CompareTag("Player"))
        {
            // Update score
            GameManager.instance.UpdateScore(10);
        }
    }
}

// Score UI class
public class ScoreUI : MonoBehaviour
{
    // Score text
    public UnityEngine.UI.Text scoreText;

    private void Update()
    {
        // Update score text
        scoreText.text = "Score: " + GameManager.instance.score;
    }
}

// Lives UI class
public class LivesUI : MonoBehaviour
{
    // Lives text
    public UnityEngine.UI.Text livesText;

    private void Update()
    {
        // Update lives text
        livesText.text = "Lives: " + GameManager.instance.lives;
    }
}
```

### Example Usage

1. Create a new Unity project.
2. Create a new scene and add a `GameManager` game object.
3. Create a new player game object and add a `Player` script.
4. Create new enemy game objects and add an `Enemy` script.
5. Create new UI text objects for score and lives, and add `ScoreUI` and `LivesUI` scripts.
6. Run the game.

### Notes

* This code uses Unity's built-in physics engine and UI system.
* The game manager class uses a singleton pattern to manage game state and player data.
* The player, enemy, and UI classes use Unity's built-in components and scripts.
* The game uses a simple scoring system and lives mechanic.
* The game can be extended and modified to add more features and gameplay mechanics.
