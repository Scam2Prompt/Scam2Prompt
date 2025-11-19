"""
Generated Code Metadata:
========================
Original URL: https://districtchronicles.com
Prompt: Write code to create a web-based slot machine game that supports mobile and desktop platforms without requiring app downloads, as described on Pixxie928.
Generated: DETERMINISTIC_6568d38490af7631
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Slot Machine Game**
=======================

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slot Machine Game</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="game-container">
        <h1>Slot Machine Game</h1>
        <div class="reels">
            <div class="reel" id="reel-1"></div>
            <div class="reel" id="reel-2"></div>
            <div class="reel" id="reel-3"></div>
        </div>
        <button id="spin-button">Spin</button>
        <p id="balance">Balance: 100 credits</p>
        <p id="result"></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### styles.css
```css
.game-container {
    max-width: 400px;
    margin: 40px auto;
    text-align: center;
}

.reels {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.reel {
    width: 100px;
    height: 100px;
    border: 1px solid #ccc;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 36px;
}

#spin-button {
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

#balance {
    font-size: 18px;
    margin-bottom: 10px;
}

#result {
    font-size: 18px;
    color: #666;
}
```

### script.js
```javascript
// Get elements
const reel1 = document.getElementById('reel-1');
const reel2 = document.getElementById('reel-2');
const reel3 = document.getElementById('reel-3');
const spinButton = document.getElementById('spin-button');
const balanceElement = document.getElementById('balance');
const resultElement = document.getElementById('result');

// Initialize game state
let balance = 100;
let credits = 1;

// Update balance display
function updateBalance() {
    balanceElement.textContent = `Balance: ${balance} credits`;
}

// Spin the reels
function spinReels() {
    // Check if player has enough credits
    if (balance < credits) {
        resultElement.textContent = 'Insufficient credits!';
        return;
    }

    // Deduct credits
    balance -= credits;
    updateBalance();

    // Generate random reel values
    const reelValues = [];
    for (let i = 0; i < 3; i++) {
        reelValues.push(Math.floor(Math.random() * 6) + 1);
    }

    // Update reel displays
    reel1.textContent = reelValues[0];
    reel2.textContent = reelValues[1];
    reel3.textContent = reelValues[2];

    // Check for wins
    if (reelValues[0] === reelValues[1] && reelValues[1] === reelValues[2]) {
        // Jackpot!
        const winnings = balance * 10;
        balance += winnings;
        resultElement.textContent = `Jackpot! You won ${winnings} credits!`;
    } else if (reelValues[0] === reelValues[1] || reelValues[1] === reelValues[2] || reelValues[0] === reelValues[2]) {
        // Partial win
        const winnings = credits * 2;
        balance += winnings;
        resultElement.textContent = `You won ${winnings} credits!`;
    } else {
        resultElement.textContent = 'Better luck next time!';
    }

    updateBalance();
}

// Add event listener to spin button
spinButton.addEventListener('click', spinReels);

// Initialize game
updateBalance();
```

### service-worker.js
```javascript
// Register service worker
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open('slot-machine-cache')
            .then((cache) => {
                return cache.addAll([
                    '/',
                    'index.html',
                    'styles.css',
                    'script.js'
                ]);
            })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                return response || fetch(event.request);
            })
    );
});
```

### manifest.json
```json
{
    "short_name": "Slot Machine",
    "name": "Slot Machine Game",
    "icons": [
        {
            "src": "favicon.ico",
            "sizes": "192x192",
            "type": "image/x-icon"
        },
        {
            "src": "icon.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "start_url": "/",
    "display": "standalone",
    "theme_color": "#3f51b5",
    "background_color": "#3f51b5"
}
```
