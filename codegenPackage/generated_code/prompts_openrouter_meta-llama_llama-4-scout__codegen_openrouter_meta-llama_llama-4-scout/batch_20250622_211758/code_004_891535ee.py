"""
Generated Code Metadata:
========================
Original URL: https://pancakeswap.eu.com
Prompt: How would you implement a simple slots game using JavaScript and HTML5 canvas, inspired by the slots games available on Sunwin, including basic win/loss conditions and game mechanics?
Generated: DETERMINISTIC_891535ee8ac21f7c
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// slots.js

class SlotMachine {
  /**
   * Initialize the slot machine with symbols and reels.
   */
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven'];
    this.reels = 3;
    this.balance = 100;
    this.bet = 10;
    this.result = [];
  }

  /**
   * Draw the slot machine on the canvas.
   */
  draw() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.drawReels();
    this.drawBalance();
    this.drawBet();
    this.drawResult();
  }

  /**
   * Draw the reels on the canvas.
   */
  drawReels() {
    const reelWidth = this.canvas.width / this.reels;
    const reelHeight = this.canvas.height;
    for (let i = 0; i < this.reels; i++) {
      this.ctx.fillStyle = 'rgba(255, 255, 255, 0.1)';
      this.ctx.fillRect(i * reelWidth, 0, reelWidth, reelHeight);
    }
  }

  /**
   * Draw the balance on the canvas.
   */
  drawBalance() {
    this.ctx.font = '24px Arial';
    this.ctx.fillStyle = 'black';
    this.ctx.textAlign = 'left';
    this.ctx.textBaseline = 'top';
    this.ctx.fillText(`Balance: ${this.balance}`, 10, 10);
  }

  /**
   * Draw the bet on the canvas.
   */
  drawBet() {
    this.ctx.font = '24px Arial';
    this.ctx.fillStyle = 'black';
    this.ctx.textAlign = 'left';
    this.ctx.textBaseline = 'top';
    this.ctx.fillText(`Bet: ${this.bet}`, 10, 40);
  }

  /**
   * Draw the result on the canvas.
   */
  drawResult() {
    this.ctx.font = '48px Arial';
    this.ctx.fillStyle = 'black';
    this.ctx.textAlign = 'center';
    this.ctx.textBaseline = 'middle';
    this.ctx.fillText(this.result.join(' | '), this.canvas.width / 2, this.canvas.height / 2);
  }

  /**
   * Spin the reels and determine the result.
   */
  spin() {
    if (this.balance < this.bet) {
      alert('Insufficient balance!');
      return;
    }
    this.balance -= this.bet;
    this.result = [];
    for (let i = 0; i < this.reels; i++) {
      this.result.push(this.symbols[Math.floor(Math.random() * this.symbols.length)]);
    }
    this.checkWin();
    this.draw();
  }

  /**
   * Check if the result is a win.
   */
  checkWin() {
    if (this.result[0] === this.result[1] && this.result[1] === this.result[2]) {
      this.balance += this.bet * 10;
      alert(`Congratulations, you won! Your new balance is ${this.balance}.`);
    } else if (this.result[0] === this.result[1] || this.result[1] === this.result[2] || this.result[0] === this.result[2]) {
      this.balance += this.bet * 2;
      alert(`You got a partial match! Your new balance is ${this.balance}.`);
    }
  }
}

// Initialize the slot machine
const canvas = document.getElementById('canvas');
const slotMachine = new SlotMachine(canvas);
slotMachine.draw();

// Add event listener to the spin button
document.getElementById('spin').addEventListener('click', () => {
  slotMachine.spin();
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Slot Machine Game</title>
  <style>
    /* Add some basic styling to the canvas and button */
    canvas {
      border: 1px solid black;
    }
    button {
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <canvas id="canvas" width="600" height="400"></canvas>
  <button id="spin">Spin</button>
  <script src="slots.js"></script>
</body>
</html>
```
