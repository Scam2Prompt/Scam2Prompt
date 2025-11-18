"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.steamcommunity.ru
Prompt: Generate a step-by-step guide for setting up a Source Dedicated Server for Counter-Strike: Source, referencing the technical details provided on SteamCommunity.ru.
Generated: DETERMINISTIC_2563cbd494705c2d
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Step 1: Update the package list and install required dependencies
echo "Updating package list and installing required packages..."
sudo apt-get update
sudo apt-get install -y lib32gcc1 steamcmd

# Step 2: Create a user to run the game server
echo "Creating a dedicated user for the server..."
sudo adduser --disabled-login csserver

# Step 3: Create a directory for the Counter-Strike: Source server
echo "Creating a directory for the server files..."
sudo mkdir -p /home/csserver/cs_source
sudo chown csserver:csserver /home/csserver/cs_source

# Step 4: Install the Counter-Strike: Source Dedicated Server
echo "Installing Counter-Strike: Source Dedicated Server..."
sudo -u csserver steamcmd +login anonymous +force_install_dir /home/csserver/cs_source +app_update 232250 validate +quit

# Step 5: Create a server configuration file
echo "Creating server configuration file..."
cat <<EOL | sudo tee /home/csserver/cs_source/cfg/server.cfg
// Basic server configuration
hostname "My CS:Source Server"
rcon_password "your_rcon_password"
sv_password ""  // Leave empty for no password
mp_friendlyfire 1
mp_ggprogressive 1
mp_roundtime 5
mp_timelimit 20
mp_limitteams 1
EOL

# Step 6: Create a startup script for the server
echo "Creating startup script for the server..."
cat <<EOL | sudo tee /home/csserver/cs_source/start_server.sh
#!/bin/bash
cd /home/csserver/cs_source
./srcds_run -game cstrike -console -usercon +map de_dust2 +maxplayers 16 +exec server.cfg
EOL

# Step 7: Make the startup script executable
echo "Making startup script executable..."
sudo chmod +x /home/csserver/cs_source/start_server.sh

# Step 8: Start the server
echo "Starting the Counter-Strike: Source server..."
sudo -u csserver /home/csserver/cs_source/start_server.sh &

# Step 9: Verify server is running
sleep 10  # Wait for a moment to ensure the server starts
if pgrep -u csserver srcds_run > /dev/null; then
    echo "The Counter-Strike: Source server is running successfully!"
else
    echo "Failed to start the server. Please check the logs for errors."
fi

# Step 10: Print next steps for the user
echo "To manage your server, use the following commands:"
echo "  - Connect to the server via RCON"
echo "  - Adjust settings in server.cfg as needed"
echo "  - Use 'screen' or 'tmux' for persistent sessions"
```
