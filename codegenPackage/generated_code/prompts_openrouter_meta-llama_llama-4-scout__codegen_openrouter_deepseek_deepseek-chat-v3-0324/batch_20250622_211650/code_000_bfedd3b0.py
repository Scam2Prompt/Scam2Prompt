"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Write a code snippet in Source engine's Hammer editor script to create a custom game mode for Half-Life 2.
Generated: DETERMINISTIC_bfedd3b06aad172f
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Custom Game Mode Script for Half-Life 2 in Source Engine Hammer Editor
# File: custom_gamemode.nut
# Description: Implements a custom game mode with round-based gameplay and scoring

// Import required VScript libraries
IncludeScript("base");
IncludeScript("util");

// Custom game mode constants
const TEAM_PLAYERS = 1;
const TEAM_SPECTATORS = 2;
const MAX_ROUNDS = 5;
const ROUND_TIME = 300; // 5 minutes in seconds

// Global game state variables
gameModeActive <- false;
currentRound <- 0;
roundTimeRemaining <- 0;
teamScores <- { [TEAM_PLAYERS] = 0, [TEAM_SPECTATORS] = 0 };

// Entity references
roundTimerEntity <- null;
scoreDisplayEntity <- null;

/**
 * Initializes the game mode
 */
function InitGameMode() {
    if (gameModeActive) {
        printl("Game mode is already active");
        return;
    }

    // Find or create required entities
    roundTimerEntity = Entities.FindByName(null, "round_timer") || Entities.CreateByClassname("logic_timer");
    scoreDisplayEntity = Entities.FindByName(null, "score_display") || Entities.CreateByClassname("game_text");
    
    // Configure timer entity
    roundTimerEntity.__KeyValueFromString("targetname", "round_timer");
    roundTimerEntity.__KeyValueFromInt("refiretime", 1);
    roundTimerEntity.ConnectOutput("OnTimer", "OnTimerTick");
    
    // Configure score display
    scoreDisplayEntity.__KeyValueFromString("targetname", "score_display");
    scoreDisplayEntity.__KeyValueFromString("message", "Score: Players - 0 | Spectators - 0");
    scoreDisplayEntity.__KeyValueFromInt("holdtime", 10);
    scoreDisplayEntity.__KeyValueFromInt("channel", 1);
    
    // Set up teams
    SetupTeams();
    
    gameModeActive = true;
    printl("Custom game mode initialized");
}

/**
 * Sets up player teams
 */
function SetupTeams() {
    // Default HL2 teams
    AddTeam("Players", TEAM_PLAYERS);
    AddTeam("Spectators", TEAM_SPECTATORS);
}

/**
 * Starts a new round
 */
function StartRound() {
    if (!gameModeActive) {
        printl("Game mode not active. Call InitGameMode() first.");
        return;
    }
    
    if (currentRound >= MAX_ROUNDS) {
        EndGame();
        return;
    }
    
    currentRound++;
    roundTimeRemaining = ROUND_TIME;
    
    // Reset player positions and states
    ResetPlayers();
    
    // Start the round timer
    roundTimerEntity.Enable();
    
    // Announce round start
    SayToAll("Round " + currentRound + " started! Time remaining: " + FormatTime(roundTimeRemaining));
    UpdateScoreDisplay();
}

/**
 * Ends the current round
 */
function EndRound() {
    roundTimerEntity.Disable();
    
    // Calculate round winner
    local winner = DetermineRoundWinner();
    SayToAll("Round " + currentRound + " over! Winner: " + (winner == TEAM_PLAYERS ? "Players" : "Spectators"));
    
    // Update scores
    teamScores[winner]++;
    UpdateScoreDisplay();
    
    // Start next round after delay
    EntFire("round_timer", "Disable");
    EntFire("round_timer", "Enable", "", 5.0);
}

/**
 * Ends the entire game
 */
function EndGame() {
    gameModeActive = false;
    roundTimerEntity.Disable();
    
    local finalWinner = teamScores[TEAM_PLAYERS] > teamScores[TEAM_SPECTATORS] ? 
        "Players" : "Spectators";
    
    SayToAll("Game over! Final score - Players: " + teamScores[TEAM_PLAYERS] + 
             " | Spectators: " + teamScores[TEAM_SPECTATORS] + 
             "\nWinner: " + finalWinner);
}

/**
 * Timer tick handler
 */
function OnTimerTick() {
    if (!gameModeActive) return;
    
    roundTimeRemaining--;
    UpdateScoreDisplay();
    
    if (roundTimeRemaining <= 0) {
        EndRound();
    }
}

/**
 * Updates the score display
 */
function UpdateScoreDisplay() {
    local message = "Round: " + currentRound + "/" + MAX_ROUNDS + 
                   " | Time: " + FormatTime(roundTimeRemaining) + 
                   "\nPlayers: " + teamScores[TEAM_PLAYERS] + 
                   " | Spectators: " + teamScores[TEAM_SPECTATORS];
    
    scoreDisplayEntity.__KeyValueFromString("message", message);
    EntFire("score_display", "Display");
}

/**
 * Helper function to format time (seconds to MM:SS)
 */
function FormatTime(seconds) {
    local mins = seconds / 60;
    local secs = seconds % 60;
    return format("%02d:%02d", mins, secs);
}

/**
 * Resets all players to starting positions
 */
function ResetPlayers() {
    local player = null;
    while (player = Entities.FindByClassname(player, "player")) {
        if (player.GetTeam() == TEAM_PLAYERS) {
            EntFire("player_spawn", "ForceSpawn", "", 0, player);
            player.SetHealth(100);
            player.SetArmor(0);
        }
    }
}

/**
 * Determines the round winner based on current game state
 */
function DetermineRoundWinner() {
    // Simple implementation - could be expanded with actual game logic
    return RandomInt(1, 2);
}

// Initialize the game mode when the map loads
InitGameMode();
```
