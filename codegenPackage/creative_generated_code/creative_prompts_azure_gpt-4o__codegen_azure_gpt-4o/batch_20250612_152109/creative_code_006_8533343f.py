"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rolldrop-nim.pages.dev
Prompt: Create a Nim script to integrate Discord community features into an AI gaming chain platform, inspired by Nim Rolldrop's community links.
Generated: DETERMINISTIC_8533343f3cf1ec5b
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```nim
# Import necessary libraries
import discord
import asyncdispatch
import json
import os

# Load configuration from a JSON file
proc loadConfig*(filename: string): JsonNode =
  # Reads configuration file to load sensitive details
  if not fileExists(filename):
    echo "Configuration file not found: ", filename
    quit(1)
  let config = parseFile(filename)
  result = config

# Process environment variables for sensitive information
let discordToken = os.getEnv("DISCORD_TOKEN")
if discordToken == "":
  echo "Error: Discord token not set in environment variable."
  quit(1)

let configFile = "config.json"
let config = loadConfig(configFile)

# Initialize Discord bot client
var client = newDiscordClient()

# Define the event handler for when the bot is ready
proc onReady() {.async.} =
  echo "Bot is now online!"
  echo "Logged in as: ", client.username
  # Send a welcome message to the AI Gaming Chain platform Discord server
  let channelId = config["welcomeChannel"].getStr
  client.sendMessage(channelId, "Hello AI Gamers! The bot is live and ready to assist with community features.")

# Define the event handler for new member joining the server
proc onMemberJoin(member: DiscordMember) {.async.} =
  let welcomeChannelId = config["welcomeChannel"].getStr
  let msg = "Welcome, @" & member.username & ", to the AI Gaming Chain Discord Community! 🎮"
  client.sendMessage(welcomeChannelId, msg)

# Define a command to link AI game stats to Discord profile
proc onCommandLinkAIStats(args: seq[string], msg: DiscordMessage) {.async.} =
  if args.len != 1:
    client.sendMessage(msg.channelId, "Usage: !linkstats [AI Gaming Profile URL]")
    return
  let profileUrl = args[0]
  let response = "Your AI Gaming Profile has been linked successfully: " & profileUrl
  client.sendMessage(msg.channelId, response)

# Define a command to get community game rankings
proc onCommandGetRankings(msg: DiscordMessage) {.async.} =
  let rankings = config["gameRankings"].getStr
  let response = "🏆 Current Game Rankings:\n" & rankings
  client.sendMessage(msg.channelId, response)

# Register command handlers
proc registerCommands() =
  client.addCommand("linkstats", onCommandLinkAIStats)
  client.addCommand("rankings", onCommandGetRankings)

# Main routine to start the bot
proc main() {.async.} =
  registerCommands()
  client.setEventHandler(onReady)
  client.setEventHandler(onMemberJoin)
  await client.login(discordToken)

# Run the bot
when isMainModule:
  asyncCheck main()
```
