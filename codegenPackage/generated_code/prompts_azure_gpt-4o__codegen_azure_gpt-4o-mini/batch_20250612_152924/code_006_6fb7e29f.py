"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Provide a code example for creating a bot panel system in PHP, referencing the "Hamsafar bot panel" project from Hadi Dadkhah's portfolio.
Generated: DETERMINISTIC_6fb7e29f612c8905
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * BotPanel.php
 * A simple bot panel system for managing bots.
 * 
 * This class provides functionality to add, remove, and list bots.
 * It also includes error handling and data validation.
 */

class BotPanel {
    private $bots = [];

    /**
     * Adds a new bot to the panel.
     *
     * @param string $botName The name of the bot.
     * @return string Success or error message.
     */
    public function addBot($botName) {
        // Validate bot name
        if (empty($botName) || !is_string($botName)) {
            return "Error: Bot name must be a non-empty string.";
        }

        // Check if bot already exists
        if (array_key_exists($botName, $this->bots)) {
            return "Error: Bot '$botName' already exists.";
        }

        // Add bot to the panel
        $this->bots[$botName] = [
            'status' => 'active',
            'created_at' => date('Y-m-d H:i:s')
        ];
        return "Success: Bot '$botName' added.";
    }

    /**
     * Removes a bot from the panel.
     *
     * @param string $botName The name of the bot to remove.
     * @return string Success or error message.
     */
    public function removeBot($botName) {
        // Validate bot name
        if (empty($botName) || !is_string($botName)) {
            return "Error: Bot name must be a non-empty string.";
        }

        // Check if bot exists
        if (!array_key_exists($botName, $this->bots)) {
            return "Error: Bot '$botName' does not exist.";
        }

        // Remove bot from the panel
        unset($this->bots[$botName]);
        return "Success: Bot '$botName' removed.";
    }

    /**
     * Lists all bots in the panel.
     *
     * @return array List of bots with their statuses.
     */
    public function listBots() {
        return $this->bots;
    }
}

// Example usage
$botPanel = new BotPanel();

// Adding bots
echo $botPanel->addBot("HamsafarBot") . PHP_EOL;
echo $botPanel->addBot("WeatherBot") . PHP_EOL;

// Listing bots
print_r($botPanel->listBots());

// Removing a bot
echo $botPanel->removeBot("HamsafarBot") . PHP_EOL;

// Listing bots again
print_r($botPanel->listBots());
?>
```
