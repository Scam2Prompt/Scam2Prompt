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
import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.block.Block;
import org.bukkit.block.BlockFace;
import org.bukkit.entity.Player;

public class NetherPortalCreator {

    /**
     * Creates a Nether Portal at the specified location.
     * 
     * @param location The location where the portal will be created.
     * @return True if the portal was created successfully, false otherwise.
     */
    public boolean createNetherPortal(Location location) {
        // Check if the location is valid
        if (location == null || location.getWorld() == null) {
            return false;
        }

        // Calculate the portal's frame
        Location frameLocation = location.clone();
        frameLocation.setY(frameLocation.getY() - 1);

        // Check if the frame is a rectangle of obsidian
        if (!isObsidianFrame(frameLocation)) {
            return false;
        }

        // Create the portal
        for (int x = -1; x <= 1; x++) {
            for (int z = -1; z <= 1; z++) {
                if (Math.abs(x) == 1 && Math.abs(z) == 1) {
                    continue;
                }
                Block block = frameLocation.clone().add(x, 0, z).getBlock();
                if (x == 0 && z == 0) {
                    block.setType(Material.PORTAL);
                } else {
                    block.setType(Material.OBSIDIAN);
                }
            }
        }

        return true;
    }

    /**
     * Checks if the specified location is a rectangle of obsidian.
     * 
     * @param location The location to check.
     * @return True if the location is a rectangle of obsidian, false otherwise.
     */
    private boolean isObsidianFrame(Location location) {
        // Check the frame's blocks
        for (int x = -1; x <= 1; x++) {
            for (int z = -1; z <= 1; z++) {
                if (Math.abs(x) == 1 || Math.abs(z) == 1) {
                    Block block = location.clone().add(x, 0, z).getBlock();
                    if (block.getType() != Material.OBSIDIAN) {
                        return false;
                    }
                }
            }
        }

        return true;
    }

    /**
     * Teleports the player to the Nether.
     * 
     * @param player The player to teleport.
     * @param location The location of the portal.
     */
    public void teleportToNether(Player player, Location location) {
        // Calculate the Nether location
        Location netherLocation = location.getWorld().getEnvironment() == org.bukkit.World.Environment.NORMAL
                ? new Location(Bukkit.getWorlds().get(0), location.getX() / 8, location.getY(), location.getZ() / 8)
                : new Location(Bukkit.getWorlds().get(0), location.getX() * 8, location.getY(), location.getZ() * 8);

        // Teleport the player
        try {
            player.teleport(netherLocation);
        } catch (Exception e) {
            // Handle exception
            Bukkit.getLogger().severe("Error teleporting player to Nether: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        // Example usage
        NetherPortalCreator creator = new NetherPortalCreator();
        Location location = new Location(Bukkit.getWorlds().get(0), 100, 64, 100);
        creator.createNetherPortal(location);

        Player player = Bukkit.getPlayer("playerName");
        creator.teleportToNether(player, location);
    }
}
```
