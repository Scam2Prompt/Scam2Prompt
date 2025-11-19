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

```c
// server.cfg - Configuration file for Counter-Strike: Condition Zero dedicated server

// Basic server settings
hostname "My Condition Zero Server" // Server hostname
rcon_password "your_rcon_password" // Rcon password
sv_password "your_server_password" // Server password
maxplayers 32 // Maximum number of players

// Network settings
sv_lan 0 // 0 = Internet, 1 = LAN
netcode 7 // Network protocol version
sv_maxrate 100000 // Maximum bytes per second
sv_minrate 10000 // Minimum bytes per second
sv_maxup 10000 // Maximum bytes per second for uploads

// Game settings
mp_freezetime 0 // Freezetime in seconds
mp_restartgame 1 // Restart game in seconds
mp_timelimit 30 // Time limit in minutes
mp_maxrounds 0 // Maximum number of rounds
mp_limitteams 0 // Limit teams
mp_autoteam 1 // Auto team balance
mp_autovote 1 // Auto vote

// Gameplay settings
sv_gravity 800 // Gravity
sv_friction 5 // Friction
sv_stopspeed 100 // Stop speed

// Logging and security
log on // Enable logging
log_file "server_log.txt" // Log file name
sv_rcon_ban_duration 30 // Ban duration in minutes

// Source Dedicated Server settings
sv_version  "cstrike" // Game version
exec banned.cfg // Execute banned users configuration
exec motd.cfg // Execute message of the day configuration

// Additional configuration
alias say "say"
alias quit "quit"
```

```c
// banned.cfg - Configuration file for banned users

// Example ban
banid 1 "STEAM_0:0:00000000" "Banned user"
``` 

```c
// motd.cfg - Configuration file for message of the day

// Example message
motd "Welcome to my Condition Zero server!"
motdfile "motd.txt"
```
