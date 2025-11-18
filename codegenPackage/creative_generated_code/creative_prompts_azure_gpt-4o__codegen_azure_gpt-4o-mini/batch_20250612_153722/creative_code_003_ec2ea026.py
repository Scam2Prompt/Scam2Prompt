"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paymentsbot.site
Prompt: Provide code examples for enabling JavaScript functionality in an admin panel designed for payment bots, similar to the implementation on paymentsbot.site.
Generated: DETERMINISTIC_ec2ea026bf96e49a
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel - Payment Bots</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Load JavaScript file -->
</head>
<body>
    <header>
        <h1>Admin Panel</h1>
    </header>
    <main>
        <section id="payment-bots">
            <h2>Payment Bots</h2>
            <button id="fetch-bots">Fetch Payment Bots</button>
            <ul id="bots-list"></ul>
        </section>
        <section id="bot-action">
            <h2>Actions</h2>
            <input type="text" id="bot-id" placeholder="Enter Bot ID" required>
            <button id="activate-bot">Activate Bot</button>
            <button id="deactivate-bot">Deactivate Bot</button>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Payment Bots Admin Panel</p>
    </footer>
</body>
</html>
```

```javascript
// script.js

// Handle DOMContentLoaded event to ensure DOM is fully loaded before executing scripts
document.addEventListener("DOMContentLoaded", () => {
    const fetchBotsButton = document.getElementById("fetch-bots");
    const botsList = document.getElementById("bots-list");
    const activateBotButton = document.getElementById("activate-bot");
    const deactivateBotButton = document.getElementById("deactivate-bot");
    const botIdInput = document.getElementById("bot-id");

    // Fetch and display payment bots from the server
    fetchBotsButton.addEventListener("click", async () => {
        try {
            const response = await fetch("/api/payment-bots"); // API endpoint to fetch bots
            if (!response.ok) {
                throw new Error(`Error fetching bots: ${response.statusText}`);
            }
            const bots = await response.json();
            displayBots(bots);
        } catch (error) {
            console.error("Failed to fetch payment bots:", error);
            alert("There was an error fetching payment bots. Please try again later.");
        }
    });

    // Activate a payment bot
    activateBotButton.addEventListener("click", async () => {
        handleBotAction("activate");
    });

    // Deactivate a payment bot
    deactivateBotButton.addEventListener("click", async () => {
        handleBotAction("deactivate");
    });

    // Helper function to handle bot activation and deactivation actions
    async function handleBotAction(action) {
        const botId = botIdInput.value.trim();
        if (!botId) {
            alert("Please enter a valid Bot ID.");
            return;
        }

        try {
            const response = await fetch(`/api/payment-bots/${botId}/${action}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
            });
            if (!response.ok) {
                throw new Error(`Error ${action} bot: ${response.statusText}`);
            }
            alert(`Bot ${action}d successfully.`);
        } catch (error) {
            console.error(`Failed to ${action} bot:`, error);
            alert(`There was an error trying to ${action} the bot. Please try again later.`);
        }
    }

    // Function to display the list of payment bots
    function displayBots(bots) {
        botsList.innerHTML = ""; // Clear previous entries
        bots.forEach(bot => {
            const listItem = document.createElement("li");
            listItem.textContent = `Bot ID: ${bot.id}, Status: ${bot.status}`;
            botsList.appendChild(listItem);
        });
    }
});
```

```css
/* styles.css */

/* Basic styling for the admin panel */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #333;
    color: #fff;
    padding: 10px 15px;
    text-align: center;
}

main {
    padding: 20px;
}

h2 {
    color: #333;
}

button {
    margin-top: 10px;
    padding: 10px 15px;
    border: none;
    background-color: #007BFF;
    color: white;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

footer {
    text-align: center;
    padding: 10px;
    background: #333;
    color: #fff;
    position: absolute;
    width: 100%;
    bottom: 0;
}
```

This code provides a basic structure for an admin panel that includes functionality to fetch, activate, and deactivate payment bots. Error handling is implemented to ensure graceful degradation in the case of network issues or invalid input. The CSS styles ensure a simple and clean layout.
