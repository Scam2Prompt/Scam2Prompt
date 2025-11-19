"""
Generated Code Metadata:
========================
Original URL: https://jito.pro
Prompt: Generate code for a farming simulation game inspired by "Tiled Farm - Swipe and Solve" on jito.pro, using Unity and C# to implement tile-based gameplay.
Generated: DETERMINISTIC_006e714bc7585d51
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Represents the type of tile in the farming grid.
/// </summary>
public enum TileType
{
    Empty,
    Soil,
    Planted,
    Watered,
    Harvestable
}

/// <summary>
/// Represents a single tile in the farming grid.
/// </summary>
[System.Serializable]
public class FarmTile
{
    public TileType type = TileType.Empty;
    public int growthStage = 0;
    public int maxGrowthStages = 3;
    public Crop crop;
    public GameObject tileObject;

    /// <summary>
    /// Advances the growth stage if conditions are met.
    /// </summary>
    /// <returns>True if growth stage changed</returns>
    public bool Grow()
    {
        if (type == TileType.Planted || type == TileType.Watered)
        {
            growthStage++;
            if (growthStage >= maxGrowthStages)
            {
                type = TileType.Harvestable;
                return true;
            }
            return true;
        }
        return false;
    }

    /// <summary>
    /// Waters the tile if it's plantable.
    /// </summary>
    public void Water()
    {
        if (type == TileType.Planted || type == TileType.Soil)
        {
            type = TileType.Watered;
        }
    }

    /// <summary>
    /// Harvests the crop if ready.
    /// </summary>
    /// <returns>The harvested crop or null if not harvestable</returns>
    public Crop Harvest()
    {
        if (type == TileType.Harvestable)
        {
            type = TileType.Soil;
            growthStage = 0;
            return crop;
        }
        return null;
    }
}

/// <summary>
/// Represents a crop that can be planted.
/// </summary>
[System.Serializable]
public class Crop
{
    public string name;
    public int value;
    public Sprite[] growthSprites;
    public float growthTime = 1f;
}

/// <summary>
/// Main controller for the farming game.
/// </summary>
public class FarmGameController : MonoBehaviour
{
    [Header("Game Settings")]
    public int gridWidth = 5;
    public int gridHeight = 5;
    public float tileSize = 1f;
    public float growthCheckInterval = 5f;

    [Header("Prefabs")]
    public GameObject tilePrefab;
    public List<Crop> availableCrops = new List<Crop>();

    private FarmTile[,] grid;
    private float growthTimer = 0f;

    private void Start()
    {
        InitializeGrid();
    }

    private void Update()
    {
        HandleGrowthCycle();
    }

    /// <summary>
    /// Initializes the farming grid with empty tiles.
    /// </summary>
    private void InitializeGrid()
    {
        grid = new FarmTile[gridWidth, gridHeight];
        
        for (int x = 0; x < gridWidth; x++)
        {
            for (int y = 0; y < gridHeight; y++)
            {
                Vector3 position = new Vector3(x * tileSize, y * tileSize, 0);
                GameObject tileObj = Instantiate(tilePrefab, position, Quaternion.identity, transform);
                tileObj.name = $"Tile_{x}_{y}";
                
                grid[x, y] = new FarmTile
                {
                    type = TileType.Empty,
                    tileObject = tileObj
                };
            }
        }
    }

    /// <summary>
    /// Handles the periodic growth cycle check.
    /// </summary>
    private void HandleGrowthCycle()
    {
        growthTimer += Time.deltaTime;
        if (growthTimer >= growthCheckInterval)
        {
            growthTimer = 0f;
            ProcessGrowth();
        }
    }

    /// <summary>
    /// Processes growth for all tiles in the grid.
    /// </summary>
    private void ProcessGrowth()
    {
        for (int x = 0; x < gridWidth; x++)
        {
            for (int y = 0; y < gridHeight; y++)
            {
                if (grid[x, y].Grow())
                {
                    UpdateTileVisual(x, y);
                }
            }
        }
    }

    /// <summary>
    /// Updates the visual representation of a tile.
    /// </summary>
    private void UpdateTileVisual(int x, int y)
    {
        FarmTile tile = grid[x, y];
        SpriteRenderer renderer = tile.tileObject.GetComponent<SpriteRenderer>();

        switch (tile.type)
        {
            case TileType.Empty:
                renderer.sprite = null;
                break;
            case TileType.Soil:
                renderer.color = new Color(0.5f, 0.3f, 0.1f);
                break;
            case TileType.Planted:
            case TileType.Watered:
                if (tile.crop != null && tile.growthStage < tile.crop.growthSprites.Length)
                {
                    renderer.sprite = tile.crop.growthSprites[tile.growthStage];
                }
                break;
            case TileType.Harvestable:
                if (tile.crop != null && tile.crop.growthSprites.Length > 0)
                {
                    renderer.sprite = tile.crop.growthSprites[tile.crop.growthSprites.Length - 1];
                }
                break;
        }
    }

    /// <summary>
    /// Handles player interaction with a tile.
    /// </summary>
    public void InteractWithTile(int x, int y, ToolType tool)
    {
        if (x < 0 || x >= gridWidth || y < 0 || y >= gridHeight) return;

        FarmTile tile = grid[x, y];

        switch (tool)
        {
            case ToolType.Hoe:
                if (tile.type == TileType.Empty)
                {
                    tile.type = TileType.Soil;
                }
                break;
            case ToolType.WateringCan:
                tile.Water();
                break;
            case ToolType.Seed:
                if (tile.type == TileType.Soil && availableCrops.Count > 0)
                {
                    tile.type = TileType.Planted;
                    tile.crop = availableCrops[0]; // Default to first crop
                    tile.maxGrowthStages = tile.crop.growthSprites.Length;
                }
                break;
            case ToolType.Harvest:
                Crop harvested = tile.Harvest();
                if (harvested != null)
                {
                    // Add to player inventory or score
                }
                break;
        }

        UpdateTileVisual(x, y);
    }

    /// <summary>
    /// Clears all tiles in the grid.
    /// </summary>
    public void ClearAllTiles()
    {
        for (int x = 0; x < gridWidth; x++)
        {
            for (int y = 0; y < gridHeight; y++)
            {
                grid[x, y].type = TileType.Empty;
                grid[x, y].growthStage = 0;
                grid[x, y].crop = null;
                UpdateTileVisual(x, y);
            }
        }
    }
}

/// <summary>
/// Represents the type of tool being used.
/// </summary>
public enum ToolType
{
    Hoe,
    WateringCan,
    Seed,
    Harvest
}

/// <summary>
/// Handles player input for tile interaction.
/// </summary>
public class PlayerInputHandler : MonoBehaviour
{
    public FarmGameController farmController;
    public ToolType currentTool = ToolType.Hoe;
    private Camera mainCamera;

    private void Start()
    {
        mainCamera = Camera.main;
    }

    private void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            HandleTileClick();
        }
    }

    /// <summary>
    /// Handles mouse click on tiles.
    /// </summary>
    private void HandleTileClick()
    {
        Ray ray = mainCamera.ScreenPointToRay(Input.mousePosition);
        if (Physics.Raycast(ray, out RaycastHit hit))
        {
            Vector3 hitPosition = hit.transform.position;
            int x = Mathf.RoundToInt(hitPosition.x / farmController.tileSize);
            int y = Mathf.RoundToInt(hitPosition.y / farmController.tileSize);
            
            farmController.InteractWithTile(x, y, currentTool);
        }
    }

    /// <summary>
    /// Changes the currently selected tool.
    /// </summary>
    public void SetTool(ToolType newTool)
    {
        currentTool = newTool;
    }
}

/// <summary>
/// Simple UI controller for tool selection.
/// </summary>
public class ToolSelectionUI : MonoBehaviour
{
    public PlayerInputHandler playerInput;

    public void SelectHoe() => playerInput.SetTool(ToolType.Hoe);
    public void SelectWateringCan() => playerInput.SetTool(ToolType.WateringCan);
    public void SelectSeed() => playerInput.SetTool(ToolType.Seed);
    public void SelectHarvest() => playerInput.SetTool(ToolType.Harvest);
}
```
