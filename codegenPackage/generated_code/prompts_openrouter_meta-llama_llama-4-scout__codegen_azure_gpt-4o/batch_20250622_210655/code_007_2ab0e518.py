"""
Generated Code Metadata:
========================
Original URL: https://owjkade.com
Prompt: Write a Java code snippet to create a Nether Portal in Minecraft using the game's API.
Generated: DETERMINISTIC_2ab0e518ae8347bc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// Import necessary Minecraft API packages
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.block.Block;

public class NetherPortalCreator {

    /**
     * Creates a Nether Portal at the specified location.
     *
     * @param location The bottom-left corner of the portal frame (obsidian).
     */
    public static void createNetherPortal(Location location) {
        // Validate input
        if (location == null || location.getWorld() == null) {
            throw new IllegalArgumentException("Location and world must not be null.");
        }

        World world = location.getWorld();

        // Build the obsidian frame
        buildObsidianFrame(world, location);

        // Fill the portal with portal blocks
        fillPortalBlocks(world, location);
    }

    /**
     * Builds the obsidian frame for the Nether Portal.
     *
     * @param world    The world where the portal is being created.
     * @param location The bottom-left corner of the portal frame.
     */
    private static void buildObsidianFrame(World world, Location location) {
        int x = location.getBlockX();
        int y = location.getBlockY();
        int z = location.getBlockZ();

        // Build vertical sides (4 blocks high)
        for (int i = 0; i < 4; i++) {
            world.getBlockAt(x, y + i, z).setType(Material.OBSIDIAN);
            world.getBlockAt(x + 3, y + i, z).setType(Material.OBSIDIAN);
        }

        // Build top and bottom sides (3 blocks wide)
        for (int i = 1; i <= 2; i++) {
            world.getBlockAt(x + i, y, z).setType(Material.OBSIDIAN);
            world.getBlockAt(x + i, y + 4, z).setType(Material.OBSIDIAN);
        }
    }

    /**
     * Fills the portal frame with portal blocks.
     *
     * @param world    The world where the portal is being created.
     * @param location The bottom-left corner of the portal frame.
     */
    private static void fillPortalBlocks(World world, Location location) {
        int x = location.getBlockX();
        int y = location.getBlockY();
        int z = location.getBlockZ();

        // Fill the portal with portal blocks (2x3 area)
        for (int i = 1; i <= 2; i++) {
            for (int j = 1; j <= 3; j++) {
                world.getBlockAt(x + i, y + j, z).setType(Material.NETHER_PORTAL);
            }
        }
    }
}
```

This code assumes you are using the Bukkit/Spigot API for Minecraft plugin development. Make sure to include the appropriate dependencies in your project.
