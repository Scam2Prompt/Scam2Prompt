"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: How can I use Unity to develop a Build Mode feature for a game like Moon Tropica, enabling players to create and share their worlds?
Generated: DETERMINISTIC_d1ee359265ed24e6
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

// BuildModeManager.cs
public class BuildModeManager : MonoBehaviour
{
    // Singleton instance
    public static BuildModeManager Instance { get; private set; }

    // Current build mode state
    public bool IsBuildModeEnabled { get; private set; }

    // Available build mode tools
    public enum ToolType { Terrain, Object, Light }
    public ToolType CurrentTool { get; private set; }

    // Initialize the build mode manager
    private void Awake()
    {
        // Ensure only one instance exists
        if (Instance == null)
        {
            Instance = this;
        }
        else if (Instance != this)
        {
            Destroy(gameObject);
        }

        // Initialize build mode state
        IsBuildModeEnabled = false;
        CurrentTool = ToolType.Terrain;
    }

    // Toggle build mode
    public void ToggleBuildMode()
    {
        IsBuildModeEnabled = !IsBuildModeEnabled;
        // Update UI and cursor accordingly
    }

    // Switch to a different tool
    public void SwitchTool(ToolType tool)
    {
        CurrentTool = tool;
        // Update UI and cursor accordingly
    }

    // Save the current world
    public void SaveWorld(string filename)
    {
        // Create a new scene for the world
        Scene worldScene = SceneManager.GetActiveScene();

        // Serialize the scene data
        WorldData worldData = new WorldData(worldScene);

        // Save the world data to a file
        BinaryFormatter formatter = new BinaryFormatter();
        FileStream file = File.Create(filename);
        formatter.Serialize(file, worldData);
        file.Close();
    }

    // Load a saved world
    public void LoadWorld(string filename)
    {
        // Check if the file exists
        if (File.Exists(filename))
        {
            // Deserialize the world data from the file
            BinaryFormatter formatter = new BinaryFormatter();
            FileStream file = File.Open(filename, FileMode.Open);
            WorldData worldData = (WorldData)formatter.Deserialize(file);
            file.Close();

            // Load the world data into the scene
            worldData.ApplyToScene();
        }
        else
        {
            Debug.LogError("World file not found: " + filename);
        }
    }
}

// WorldData.cs
[System.Serializable]
public class WorldData
{
    // Scene data
    public string sceneName;
    public List<GameObject> gameObjects;
    public List<TerrainData> terrainData;

    // Constructor
    public WorldData(Scene scene)
    {
        sceneName = scene.name;
        gameObjects = new List<GameObject>();
        terrainData = new List<TerrainData>();

        // Serialize all game objects in the scene
        foreach (GameObject obj in scene.GetRootGameObjects())
        {
            gameObjects.Add(obj);
        }

        // Serialize all terrain data in the scene
        Terrain[] terrains = scene.GetComponentsInChildren<Terrain>();
        foreach (Terrain terrain in terrains)
        {
            terrainData.Add(new TerrainData(terrain));
        }
    }

    // Apply the world data to the scene
    public void ApplyToScene()
    {
        // Load game objects
        foreach (GameObject obj in gameObjects)
        {
            GameObject.Instantiate(obj);
        }

        // Load terrain data
        foreach (TerrainData data in terrainData)
        {
            data.ApplyToTerrain();
        }
    }
}

// TerrainData.cs
[System.Serializable]
public class TerrainData
{
    // Terrain properties
    public Vector3 terrainPosition;
    public float terrainWidth;
    public float terrainHeight;
    public float[,] terrainHeights;

    // Constructor
    public TerrainData(Terrain terrain)
    {
        terrainPosition = terrain.transform.position;
        terrainWidth = terrain.terrainData.size.x;
        terrainHeight = terrain.terrainData.size.y;
        terrainHeights = terrain.terrainData.GetHeights(0, 0, terrain.terrainData.heightmapWidth, terrain.terrainData.heightmapHeight);
    }

    // Apply the terrain data to a terrain
    public void ApplyToTerrain()
    {
        // Create a new terrain
        GameObject terrainObject = new GameObject();
        Terrain terrain = terrainObject.AddComponent<Terrain>();

        // Set terrain properties
        terrain.transform.position = terrainPosition;
        terrain.terrainData.size = new Vector3(terrainWidth, terrainHeight, terrainWidth);
        terrain.terrainData.SetHeights(0, 0, terrainHeights);
    }
}

// BuildModeUI.cs
public class BuildModeUI : MonoBehaviour
{
    // UI elements
    public UIButton buildModeButton;
    public UIButton saveWorldButton;
    public UIButton loadWorldButton;
    public UIDropdown toolDropdown;

    // Reference to the build mode manager
    public BuildModeManager buildModeManager;

    // Initialize the UI
    private void Start()
    {
        // Initialize UI elements
        buildModeButton.onClick.AddListener(ToggleBuildMode);
        saveWorldButton.onClick.AddListener(SaveWorld);
        loadWorldButton.onClick.AddListener(LoadWorld);
        toolDropdown.onValueChanged.AddListener(SwitchTool);

        // Initialize tool dropdown options
        List<Dropdown.OptionData> options = new List<Dropdown.OptionData>();
        options.Add(new Dropdown.OptionData("Terrain"));
        options.Add(new Dropdown.OptionData("Object"));
        options.Add(new Dropdown.OptionData("Light"));
        toolDropdown.AddOptions(options);
    }

    // Toggle build mode
    private void ToggleBuildMode()
    {
        buildModeManager.ToggleBuildMode();
    }

    // Save the current world
    private void SaveWorld()
    {
        buildModeManager.SaveWorld("saved_world.dat");
    }

    // Load a saved world
    private void LoadWorld()
    {
        buildModeManager.LoadWorld("saved_world.dat");
    }

    // Switch to a different tool
    private void SwitchTool(int index)
    {
        switch (index)
        {
            case 0:
                buildModeManager.SwitchTool(BuildModeManager.ToolType.Terrain);
                break;
            case 1:
                buildModeManager.SwitchTool(BuildModeManager.ToolType.Object);
                break;
            case 2:
                buildModeManager.SwitchTool(BuildModeManager.ToolType.Light);
                break;
        }
    }
}
```
