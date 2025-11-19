"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Create a configuration file for a Counter-Strike: Condition Zero dedicated server, following the guidelines outlined in the Source Dedicated Server Rus section of SteamCommunity.ru.
Generated: DETERMINISTIC_75acc4a8fece7516
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cfg
// Counter-Strike: Condition Zero Dedicated Server Configuration File
// Based on SteamCommunity.ru guidelines for optimal performance

hostname "Counter-Strike Condition Zero Server" // Server name displayed in server browser
rcon_password "changeme"                        // Remote console password (change this!)

// Network settings
sv_lan 0                                       // 0 = Internet, 1 = LAN
sv_region 255                                  // 255 = World, see region codes for others
sv_downloadurl ""                              // URL for fast downloads (optional)
sv_allowdownload 1                             // Allow clients to download files
sv_allowupload 1                               // Allow clients to upload spray logos

// Server performance
sv_maxupdaterate 101                           // Maximum update rate
sv_minupdaterate 30                            // Minimum update rate
sv_maxrate 25000                               // Max bandwidth rate (bytes/second)
sv_minrate 5000                                // Min bandwidth rate (bytes/second)
sv_unlag 1                                     // Enable lag compensation
sv_maxunlag 0.5                                // Max seconds of lag compensation

// Game settings
mp_timelimit 25                                // Time limit per map (minutes)
mp_roundtime 5                                 // Round time (minutes)
mp_freezetime 6                                // Freeze time at round start (seconds)
mp_buytime 1.5                                 // Time players can buy items (minutes)
mp_startmoney 800                              // Starting money
mp_c4timer 35                                  // C4 detonation time (seconds)
mp_flashlight 1                                // Allow flashlight
mp_footsteps 1                                 // Enable footsteps
mp_autoteambalance 1                           // Auto balance teams
mp_autokick 1                                  // Auto kick idle/team killers
mp_forcecamera 1                               // Force dead players to spectate
mp_limitteams 2                                // Max team difference before auto balance
mp_tkpunish 1                                  // Punish team killers
mp_friendlyfire 1                              // Enable friendly fire
mp_fadetoblack 0                               // 0 = normal death, 1 = fade to black

// Bot settings (if applicable)
bot_quota 10                                   // Number of bots to maintain
bot_difficulty 1                               // 0=easy, 1=normal, 2=hard, 3=expert
bot_join_after_player 1                        // Bots join after players connect
bot_auto_vacate 1                              // Bots leave when players join
bot_prefix "[BOT]"                             // Bot name prefix

// Logging and administration
log on                                         // Enable logging
sv_logbans 1                                   // Log banned players
sv_logecho 1                                   // Echo log info to console
sv_logfile 1                                   // Log server info to file
sv_log_onefile 0                               // 0 = new log each map, 1 = single log

// Advanced settings
sv_cheats 0                                    // Disable cheats
sv_gravity 800                                 // Default gravity
sv_airaccelerate 10                            // Air acceleration
sv_allowspectators 1                           // Allow spectators
sv_alltalk 0                                   // 0 = team chat only, 1 = all talk
sv_voiceenable 1                               // Enable voice communication
sv_voicecodec vaudio_speex                     // Voice codec
sv_voicequality 5                              // Voice quality (1-5)

// Mapcycle and game mode
mapcyclefile "mapcycle.txt"                    // File containing map rotation
exec banned.cfg                                // Load banned players list
exec listip.cfg                                // Load banned IPs

// Custom settings can be added below this line
```
