"""
Generated Code Metadata:
========================
Original URL: https://districtchronicles.com
Prompt: Design a simple slot game with a free trial mode using JavaScript and HTML5, incorporating features like bonus rounds and free spins.
Generated: DETERMINISTIC_6d8f620c4b93b94c
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Simple Slot Game with Free Trial Mode

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lucky Spin Slot Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1a1a2e;
            color: white;
            text-align: center;
            margin: 0;
            padding: 20px;
        }
        
        .game-container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #16213e;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }
        
        .slot-machine {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
        
        .reel {
            width: 100px;
            height: 100px;
            background-color: #0f3460;
            margin: 0 10px;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 40px;
            overflow: hidden;
            position: relative;
        }
        
        .reel-content {
            position: absolute;
            transition: top 0.5s ease-out;
        }
        
        .controls {
            margin: 20px 0;
        }
        
        button {
            background-color: #e94560;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 0 10px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        
        button:hover {
            background-color: #ff6b81;
        }
        
        button:disabled {
            background-color: #555;
            cursor: not-allowed;
        }
        
        .balance {
            font-size: 18px;
            margin: 10px 0;
        }
        
        .message {
            min-height: 30px;
            margin: 10px 0;
            font-weight: bold;
            color: #f9c74f;
        }
        
        .free-spins {
            color: #4cc9f0;
            font-weight: bold;
        }
        
        .bonus-round {
            animation: pulse 1s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>Lucky Spin Slot Game</h1>
        
        <div class="balance">
            Balance: $<span id="balance">100</span>
        </div>
        
        <div class="message" id="message"></div>
        
        <div class="free-spins" id="free-spins"></div>
        
        <div class="slot-machine">
            <div class="reel" id="reel1">
                <div class="reel-content" id="reel1-content"></div>
            </div>
            <div class="reel" id="reel2">
                <div class="reel-content" id="reel2-content"></div>
            </div>
            <div class="reel" id="reel3">
                <div class="reel-content" id="reel3-content"></div>
            </div>
        </div>
        
        <div class="controls">
            <button id="spin-btn">Spin ($10)</button>
            <button id="free-spin-btn" disabled>Free Spin</button>
            <button id="reset-btn">Reset Game</button>
        </div>
        
        <div class="trial-mode">
            <input type="checkbox" id="trial-mode" checked>
            <label for="trial-mode">Free Trial Mode (Unlimited Credits)</label>
        </div>
    </div>

    <script>
        // Game configuration
        const config = {
            symbols: ['🍒', '🍋', '🍊', '🍇', '🍉', '7', '💰', '🎁'],
            spinCost: 10,
            winMultipliers: {
                '7': 10,
                '💰': 5,
                '🎁': 3,
                'default': 2
            },
            freeSpinThreshold: 3, // Number of bonus symbols to trigger free spins
            freeSpinsAwarded: 5,
            initialBalance: 100
        };

        // Game state
        let state = {
            balance: config.initialBalance,
            isSpinning: false,
            freeSpins: 0,
            trialMode: true
        };

        // DOM elements
        const elements = {
            balance: document.getElementById('balance'),
            message: document.getElementById('message'),
            freeSpins: document.getElementById('free-spins'),
            reel1: document.getElementById('reel1-content'),
            reel2: document.getElementById('reel2-content'),
            reel3: document.getElementById('reel3-content'),
            spinBtn: document.getElementById('spin-btn'),
            freeSpinBtn: document.getElementById('free-spin-btn'),
            resetBtn: document.getElementById('reset-btn'),
            trialMode: document.getElementById('trial-mode')
        };

        // Initialize the game
        function initGame() {
            updateUI();
            elements.spinBtn.addEventListener('click', spin);
            elements.freeSpinBtn.addEventListener('click', freeSpin);
            elements.resetBtn.addEventListener('click', resetGame);
            elements.trialMode.addEventListener('change', toggleTrialMode);
            
            // Set initial reel positions
            const symbols = getRandomSymbols();
            elements.reel1.textContent = symbols[0];
            elements.reel2.textContent = symbols[1];
            elements.reel3.textContent = symbols[2];
        }

        // Get random symbols for the reels
        function getRandomSymbols() {
            return [
                config.symbols[Math.floor(Math.random() * config.symbols.length)],
                config.symbols[Math.floor(Math.random() * config.symbols.length)],
                config.symbols[Math.floor(Math.random() * config.symbols.length)]
            ];
        }

        // Spin the reels
        function spin() {
            if (state.isSpinning) return;
            
            // Check if player has enough balance
            if (!state.trialMode && state.balance < config.spinCost) {
                showMessage("Not enough balance to spin!");
                return;
            }
            
            // Deduct spin cost
            if (!state.trialMode) {
                state.balance -= config.spinCost;
            }
            
            state.isSpinning = true;
            updateUI();
            showMessage("Spinning...");
            
            // Animate the reels
            animateReels().then(handleSpinResult);
        }

        // Free spin
        function freeSpin() {
            if (state.isSpinning || state.freeSpins <= 0) return;
            
            state.freeSpins--;
            state.isSpinning = true;
            updateUI();
            showMessage("Free Spin!");
            
            // Animate the reels
            animateReels().then(handleSpinResult);
        }

        // Animate the reels with spinning effect
        function animateReels() {
            return new Promise((resolve) => {
                const reels = [elements.reel1, elements.reel2, elements.reel3];
                const durations = [1000, 1200, 1400]; // Different durations for each reel
                let completed = 0;
                
                reels.forEach((reel, index) => {
                    const duration = durations[index];
                    const startTime = Date.now();
                    
                    // Create spinning effect
                    const spinInterval = setInterval(() => {
                        reel.textContent = config.symbols[Math.floor(Math.random() * config.symbols.length)];
                    }, 50);
                    
                    // Stop spinning after duration
                    setTimeout(() => {
                        clearInterval(spinInterval);
                        completed++;
                        
                        if (completed === reels.length) {
                            resolve();
                        }
                    }, duration);
                });
            });
        }

        // Handle spin result
        function handleSpinResult() {
            const symbols = getRandomSymbols();
            elements.reel1.textContent = symbols[0];
            elements.reel2.textContent = symbols[1];
            elements.reel3.textContent = symbols[2];
            
            // Check for wins
            const winAmount = calculateWin(symbols);
            
            // Check for bonus (free spins)
            const bonusSymbols = symbols.filter(s => s === '🎁').length;
            if (bonusSymbols >= config.freeSpinThreshold) {
                state.freeSpins += config.freeSpinsAwarded;
                showMessage(`Bonus! ${config.freeSpinsAwarded} free spins awarded!`);
            } else if (
