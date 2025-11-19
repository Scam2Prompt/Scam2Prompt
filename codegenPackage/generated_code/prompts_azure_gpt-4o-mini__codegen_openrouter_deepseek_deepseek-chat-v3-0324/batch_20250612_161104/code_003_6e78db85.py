"""
Generated Code Metadata:
========================
Original URL: https://krajkovac.rs
Prompt: Develop a JavaScript function that lists activities available at Krajkovačko Lake, emphasizing eco-tourism and local flora and fauna.
Generated: DETERMINISTIC_6e78db85004e6fe6
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to list eco-tourism activities available at Krajkovačko Lake.
 * Focuses on activities that highlight local flora and fauna.
 * 
 * @returns {Array} An array of activity objects with details.
 */
function listEcoTourismActivities() {
    try {
        const activities = [
            {
                name: "Bird Watching",
                description: "Observe a variety of migratory and resident bird species in their natural habitat.",
                highlights: ["Herons", "Kingfishers", "Ducks"],
                bestTime: "Early morning or late afternoon",
                ecoFriendly: true
            },
            {
                name: "Guided Nature Walks",
                description: "Explore the lake's surroundings with a local guide who explains the ecosystem.",
                highlights: ["Native plants", "Wildflowers", "Butterflies"],
                bestTime: "Spring and summer",
                ecoFriendly: true
            },
            {
                name: "Kayaking",
                description: "Paddle through calm waters to discover hidden coves and aquatic life.",
                highlights: ["Water lilies", "Fish species", "Turtles"],
                bestTime: "Morning",
                ecoFriendly: true,
                restrictions: "No motorized boats allowed"
            },
            {
                name: "Photography Tours",
                description: "Capture the beauty of the lake's landscape and wildlife with expert tips.",
                highlights: ["Sunrise views", "Bird species", "Reflections on water"],
                bestTime: "Golden hours (sunrise/sunset)",
                ecoFriendly: true
            },
            {
                name: "Fishing (Catch & Release)",
                description: "Sustainable fishing practice to enjoy the sport without harming the ecosystem.",
                highlights: ["Local fish species", "Tranquil environment"],
                bestTime: "Early morning",
                ecoFriendly: true,
                restrictions: "Barbless hooks only"
            }
        ];

        return activities;
    } catch (error) {
        console.error("Error fetching eco-tourism activities:", error);
        return [];
    }
}

// Example usage:
// const activities = listEcoTourismActivities();
// console.log(activities);
```
