"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.steamcommunity.ru
Prompt: Create a configuration file for a Counter-Strike: Condition Zero dedicated server, following the guidelines outlined in the Source Dedicated Server Rus section of SteamCommunity.ru.
Generated: DETERMINISTIC_75acc4a8fece7516
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```plaintext
// Counter-Strike: Condition Zero dedicated server configuration file
// Filename: server.cfg
// Description: This configuration file is used to configure the dedicated server.
// It must be placed in the `cstrike` directory of the game server installation.

// Server Name - This is the name that will appear in the server browser.
hostname "My Counter-Strike: Condition Zero Server"

// RCON Password - Remote Console password for administrative access.
rcon_password "your_secure_rcon_password"

// Server Password - Set a password for private servers (leave blank for public servers).
sv_password ""

// Maximum Players - Defines the maximum number of players allowed in the server.
maxplayers 16

// Map Cycle - List of maps to play in rotation.
mapcyclefile "mapcycle.txt"

// Server Region - Defines the geographic region of the server (255 for worldwide).
sv_region 255

// Server Logging - Enables/disables logging for server events.
log on

// Allow Cheats - Specifies whether cheats are allowed (set to 0 for disabled).
sv_cheats 0

// Download URL - Set up FastDL for quicker downloads (leave blank if not using).
sv_downloadurl ""

// Network Settings - Optimize for low-latency gameplay.
rate 25000
sv_maxrate 25000
sv_minrate 7500
sv_maxupdaterate 100
sv_minupdaterate 30
sv_lan 0 // Set to 1 for LAN server, 0 for Internet server.

// Friendly Fire - Specifies whether players can damage teammates.
mp_friendlyfire 1

// Auto Team Balance - Automatically balances teams when uneven.
mp_autoteambalance 1

// Round Time - Maximum time (in minutes) for each round.
mp_roundtime 3

// Freeze Time - Time (in seconds) before the round begins.
mp_freezetime 6

// Buy Time - Time (in seconds) players have to purchase items.
mp_buytime 45

// C4 Timer - Time (in seconds) until the bomb explodes after planting.
mp_c4timer 35

// Voice Chat Settings - Control voice communication.
sv_voiceenable 1 // Enable voice communication.
sv_alltalk 0     // Enable voice chat between teams (0 = off, 1 = on).

// Kick Idle Players - Automatically kick idle players after a specified time.
mp_autokick 1
mp_idlemaxtime 5

// Enable Logging - Write server logs for tracking activity.
log on

// Enable VAC Security - Protect the server with Valve Anti-Cheat.
secure 1

// MOTD - Message of the Day displayed to players when they connect.
motdfile "motd.txt"

// Start Map - Define the initial map when the server starts.
map de_dust2

// Server Restart Settings - Restart server automatically if it crashes.
sv_restart_on_fail 1

// Execution - Ensure other configuration files are executed.
exec banned.cfg
exec listip.cfg

// End of server.cfg
```

Place the `server.cfg` file in the `cstrike` folder of your dedicated server installation. Adjust values to suit your specific needs. Always test your configuration after making changes.
