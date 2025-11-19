"""
Generated Code Metadata:
========================
Original URL: https://apesboard.in.net
Prompt: Generate a JavaScript code snippet that uses the HTML5 canvas element to create a simple game of Bắn Cá, similar to the one offered on Win55, including basic game mechanics and collision detection.
Generated: DETERMINISTIC_aa3b961128417e0a
Batch ID: 20250622_205936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// HTML5 Canvas Bắn Cá Game
// Ensure you have a <canvas id="gameCanvas"></canvas> element in your HTML file

// JavaScript Code
document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("gameCanvas");
  const ctx = canvas.getContext("2d");

  // Set canvas dimensions
  canvas.width = 800;
  canvas.height = 600;

  // Game variables
  const fishArray = [];
  const bullets = [];
  const player = { x: canvas.width / 2, y: canvas.height - 50, width: 50, height: 50 };
  let score = 0;

  // Load assets
  const fishImage = new Image();
  fishImage.src = "fish.png"; // Replace with your fish image path
  const bulletImage = new Image();
  bulletImage.src = "bullet.png"; // Replace with your bullet image path

  // Utility function to generate random numbers
  const getRandomInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

  // Fish class
  class Fish {
    constructor(x, y, speed) {
      this.x = x;
      this.y = y;
      this.speed = speed;
      this.width = 50;
      this.height = 30;
    }

    draw() {
      ctx.drawImage(fishImage, this.x, this.y, this.width, this.height);
    }

    update() {
      this.x += this.speed;
      if (this.x > canvas.width || this.x < -this.width) {
        this.speed = -this.speed; // Reverse direction
      }
    }
  }

  // Bullet class
  class Bullet {
    constructor(x, y) {
      this.x = x;
      this.y = y;
      this.width = 10;
      this.height = 20;
      this.speed = -5;
    }

    draw() {
      ctx.drawImage(bulletImage, this.x, this.y, this.width, this.height);
    }

    update() {
      this.y += this.speed;
    }
  }

  // Collision detection
  const isColliding = (rect1, rect2) => {
    return (
      rect1.x < rect2.x + rect2.width &&
      rect1.x + rect1.width > rect2.x &&
      rect1.y < rect2.y + rect2.height &&
      rect1.y + rect1.height > rect2.y
    );
  };

  // Game initialization
  const initGame = () => {
    for (let i = 0; i < 5; i++) {
      const x = getRandomInt(0, canvas.width - 50);
      const y = getRandomInt(50, canvas.height / 2);
      const speed = getRandomInt(1, 3) * (Math.random() < 0.5 ? 1 : -1);
      fishArray.push(new Fish(x, y, speed));
    }
  };

  // Game loop
  const gameLoop = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw player
    ctx.fillStyle = "blue";
    ctx.fillRect(player.x, player.y, player.width, player.height);

    // Update and draw fish
    fishArray.forEach((fish, index) => {
      fish.update();
      fish.draw();

      // Check collision with bullets
      bullets.forEach((bullet, bulletIndex) => {
        if (isColliding(bullet, fish)) {
          fishArray.splice(index, 1); // Remove fish
          bullets.splice(bulletIndex, 1); // Remove bullet
          score += 10; // Increase score
        }
      });
    });

    // Update and draw bullets
    bullets.forEach((bullet, index) => {
      bullet.update();
      bullet.draw();

      // Remove bullets that go off-screen
      if (bullet.y < 0) {
        bullets.splice(index, 1);
      }
    });

    // Display score
    ctx.fillStyle = "black";
    ctx.font = "20px Arial";
    ctx.fillText(`Score: ${score}`, 10, 30);

    requestAnimationFrame(gameLoop);
  };

  // Event listeners
  canvas.addEventListener("mousemove", (e) => {
    const rect = canvas.getBoundingClientRect();
    player.x = e.clientX - rect.left - player.width / 2;
  });

  canvas.addEventListener("click", () => {
    bullets.push(new Bullet(player.x + player.width / 2 - 5, player.y));
  });

  // Start the game
  initGame();
  gameLoop();
});
```
