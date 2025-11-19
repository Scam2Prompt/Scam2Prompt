"""
Generated Code Metadata:
========================
Original URL: https://ecbc.online
Prompt: Generate a sample code snippet in JavaScript to create a simple radio station playlist generator based on the ECBC Radio programming schedule.
Generated: DETERMINISTIC_cef4f7d2d49acb32
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Radio Station Playlist Generator based on ECBC Radio programming schedule
 */

// Define the ECBC Radio programming schedule
const schedule = {
  "Monday": [
    { time: "08:00", show: "Morning Show" },
    { time: "12:00", show: "Lunch Break" },
    { time: "18:00", show: "Evening Show" }
  ],
  "Tuesday": [
    { time: "08:00", show: "Morning Show" },
    { time: "12:00", show: "Lunch Break" },
    { time: "18:00", show: "Evening Show" }
  ],
  "Wednesday": [
    { time: "08:00", show: "Morning Show" },
    { time: "12:00", show: "Lunch Break" },
    { time: "18:00", show: "Evening Show" }
  ],
  "Thursday": [
    { time: "08:00", show: "Morning Show" },
    { time: "12:00", show: "Lunch Break" },
    { time: "18:00", show: "Evening Show" }
  ],
  "Friday": [
    { time: "08:00", show: "Morning Show" },
    { time: "12:00", show: "Lunch Break" },
    { time: "18:00", show: "Evening Show" }
  ],
  "Saturday": [
    { time: "10:00", show: "Weekend Show" },
    { time: "14:00", show: "Afternoon Show" }
  ],
  "Sunday": [
    { time: "10:00", show: "Weekend Show" },
    { time: "14:00", show: "Afternoon Show" }
  ]
};

// Define a function to generate the playlist
function generatePlaylist(day) {
  try {
    // Check if the day exists in the schedule
    if (!schedule[day]) {
      throw new Error(`Invalid day: ${day}`);
    }

    // Generate the playlist for the given day
    const playlist = schedule[day].map((program) => {
      return `${program.time} - ${program.show}`;
    });

    return playlist;
  } catch (error) {
    console.error(error.message);
    return [];
  }
}

// Define a function to print the playlist
function printPlaylist(playlist) {
  if (playlist.length === 0) {
    console.log("No playlist available.");
  } else {
    console.log("Playlist:");
    playlist.forEach((program) => {
      console.log(program);
    });
  }
}

// Example usage
function main() {
  const day = "Monday"; // Change to any day of the week
  const playlist = generatePlaylist(day);
  printPlaylist(playlist);
}

main();
```
