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
 * Simple Radio Station Playlist Generator for ECBC Radio
 * This script generates a playlist based on the ECBC Radio programming schedule.
 */

// Sample ECBC Radio programming schedule data
const ecbcSchedule = {
    morning: {
        startTime: '06:00',
        endTime: '10:00',
        programs: [
            { title: 'Morning Show', duration: 120, genre: 'Talk' },
            { title: 'News Update', duration: 15, genre: 'News' },
            { title: 'Pop Hits', duration: 45, genre: 'Pop' }
        ]
    },
    afternoon: {
        startTime: '12:00',
        endTime: '16:00',
        programs: [
            { title: 'Afternoon Lounge', duration: 180, genre: 'Jazz' },
            { title: 'News Update', duration: 15, genre: 'News' },
            { title: 'Classic Rock', duration: 45, genre: 'Rock' }
        ]
    },
    evening: {
        startTime: '18:00',
        endTime: '22:00',
        programs: [
            { title: 'Evening Drive', duration: 120, genre: 'Pop' },
            { title: 'News Update', duration: 15, genre: 'News' },
            { title: 'Electronic Vibes', duration: 45, genre: 'Electronic' }
        ]
    }
};

/**
 * Generates a playlist for a given time slot
 * @param {string} timeSlot - The time slot (morning, afternoon, evening)
 * @returns {Array} Array of program objects for the playlist
 * @throws {Error} If timeSlot is invalid
 */
function generatePlaylist(timeSlot) {
    if (!ecbcSchedule[timeSlot]) {
        throw new Error(`Invalid time slot: ${timeSlot}. Valid slots are morning, afternoon, evening.`);
    }

    const slot = ecbcSchedule[timeSlot];
    const playlist = [];

    // Add each program to the playlist
    slot.programs.forEach(program => {
        playlist.push({
            title: program.title,
            duration: program.duration,
            genre: program.genre,
            startTime: slot.startTime,
            endTime: slot.endTime
        });
    });

    return playlist;
}

/**
 * Formats the playlist for display
 * @param {Array} playlist - The playlist to format
 * @returns {string} Formatted playlist string
 */
function formatPlaylist(playlist) {
    if (!Array.isArray(playlist) || playlist.length === 0) {
        return 'No programs in the playlist.';
    }

    let output = `Playlist (${playlist[0].startTime} - ${playlist[0].endTime}):\n`;
    playlist.forEach((program, index) => {
        output += `${index + 1}. ${program.title} (${program.duration} mins) - ${program.genre}\n`;
    });

    return output;
}

// Example usage with error handling
try {
    const timeSlot = 'afternoon'; // Can be morning, afternoon, or evening
    const playlist = generatePlaylist(timeSlot);
    console.log(formatPlaylist(playlist));
} catch (error) {
    console.error('Error generating playlist:', error.message);
}
```
