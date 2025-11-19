"""
Generated Code Metadata:
========================
Original URL: https://nftbuy.site
Prompt: Generate a code snippet that creates a simple HTML5 game similar to the "Zombie Mission 13" featured on NFTBuy, focusing on player controls and enemy interactions.
Generated: DETERMINISTIC_37d9ca547585c003
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zombie Mission</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: #222;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
        }
        #gameCanvas {
            border: 2px solid #444;
            background-color: #111;
        }
        #gameUI {
            position: absolute;
            color: white;
            padding: 10px;
            font-size: 18px;
        }
        #healthBar {
            width: 200px;
            height: 20px;
            background-color: #333;
            margin-bottom: 10px;
        }
        #healthFill {
            height: 100%;
            width: 100%;
            background-color: #ff3333;
            transition: width 0.3s;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="800" height="600"></canvas>
    <div id="gameUI">
        <div id="healthBar">
            <div id="healthFill"></div>
        </div>
        <div>Score: <span id="score">0</span></div>
        <div>Ammo: <span id="ammo">30</span></div>
    </div>

    <script>
        // Game variables
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const scoreElement = document.getElementById('score');
        const ammoElement = document.getElementById('ammo');
        const healthFill = document.getElementById('healthFill');

        // Player properties
        const player = {
            x: canvas.width / 2,
            y: canvas.height / 2,
            radius: 20,
            speed: 5,
            health: 100,
            maxHealth: 100,
            ammo: 30,
            maxAmmo: 30,
            color: '#3498db',
            lastShot: 0,
            reloadTime: 1000,
            isReloading: false
        };

        // Bullets array
        let bullets = [];
        const bulletSpeed = 10;
        const bulletRadius = 5;

        // Zombies array
        let zombies = [];
        const zombieSpeed = 1.5;
        const zombieRadius = 25;
        let zombieSpawnRate = 2000; // ms
        let lastZombieSpawn = 0;

        // Game state
        let score = 0;
        let gameOver = false;
        let keys = {
            ArrowUp: false,
            ArrowDown: false,
            ArrowLeft: false,
            ArrowRight: false
        };

        // Event listeners
        window.addEventListener('keydown', (e) => {
            if (keys.hasOwnProperty(e.key)) {
                keys[e.key] = true;
            }
            if (e.key === 'r' && !player.isReloading) {
                reload();
            }
        });

        window.addEventListener('keyup', (e) => {
            if (keys.hasOwnProperty(e.key)) {
                keys[e.key] = false;
            }
        });

        canvas.addEventListener('click', (e) => {
            if (!gameOver && !player.isReloading && player.ammo > 0) {
                shoot(e);
            }
        });

        // Main game loop
        function gameLoop(timestamp) {
            if (gameOver) {
                displayGameOver();
                return;
            }

            // Clear canvas
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Update and draw player
            updatePlayer();
            drawPlayer();

            // Update and draw bullets
            updateBullets();
            drawBullets();

            // Spawn and update zombies
            spawnZombies(timestamp);
            updateZombies();
            drawZombies();

            // Check collisions
            checkCollisions();

            // Update UI
            updateUI();

            requestAnimationFrame(gameLoop);
        }

        // Player functions
        function updatePlayer() {
            // Movement
            if (keys.ArrowUp && player.y - player.radius > 0) {
                player.y -= player.speed;
            }
            if (keys.ArrowDown && player.y + player.radius < canvas.height) {
                player.y += player.speed;
            }
            if (keys.ArrowLeft && player.x - player.radius > 0) {
                player.x -= player.speed;
            }
            if (keys.ArrowRight && player.x + player.radius < canvas.width) {
                player.x += player.speed;
            }
        }

        function drawPlayer() {
            ctx.beginPath();
            ctx.arc(player.x, player.y, player.radius, 0, Math.PI * 2);
            ctx.fillStyle = player.color;
            ctx.fill();
            ctx.closePath();
        }

        // Bullet functions
        function shoot(e) {
            const rect = canvas.getBoundingClientRect();
            const mouseX = e.clientX - rect.left;
            const mouseY = e.clientY - rect.top;

            const angle = Math.atan2(mouseY - player.y, mouseX - player.x);
            const velocity = {
                x: Math.cos(angle) * bulletSpeed,
                y: Math.sin(angle) * bulletSpeed
            };

            bullets.push({
                x: player.x,
                y: player.y,
                radius: bulletRadius,
                velocity: velocity
            });

            player.ammo--;
            player.lastShot = Date.now();
            if (player.ammo <= 0) {
                reload();
            }
        }

        function updateBullets() {
            for (let i = bullets.length - 1; i >= 0; i--) {
                bullets[i].x += bullets[i].velocity.x;
                bullets[i].y += bullets[i].velocity.y;

                // Remove bullets that are out of bounds
                if (bullets[i].x < 0 || bullets[i].x > canvas.width ||
                    bullets[i].y < 0 || bullets[i].y > canvas.height) {
                    bullets.splice(i, 1);
                }
            }
        }

        function drawBullets() {
            ctx.fillStyle = '#f1c40f';
            bullets.forEach(bullet => {
                ctx.beginPath();
                ctx.arc(bullet.x, bullet.y, bullet.radius, 0, Math.PI * 2);
                ctx.fill();
                ctx.closePath();
            });
        }

        function reload() {
            if (player.isReloading) return;
            
            player.isReloading = true;
            setTimeout(() => {
                player.ammo = player.maxAmmo;
                player.isReloading = false;
            }, player.reloadTime);
        }

        // Zombie functions
        function spawnZombies(timestamp) {
            if (timestamp - lastZombieSpawn > zombieSpawnRate) {
                let x, y;
                // Spawn from edges
                if (Math.random() < 0.5) {
                    x = Math.random() < 0.5 ? 0 : canvas.width;
                    y = Math.random() * canvas.height;
                } else {
                    x = Math.random() * canvas.width;
                    y = Math.random() < 0.5 ? 0 : canvas.height;
                }

                zombies.push({
                    x: x,
                    y: y,
                    radius: zombieRadius,
                    speed: zombieSpeed,
                    health: 100,
                    color: '#27ae60'
                });

                lastZombieSpawn = timestamp;
                // Increase spawn rate as score increases
                zombieSpawnRate = Math.max(500, 2000 - score * 10);
            }
        }

        function updateZombies() {
            zombies.forEach(zombie => {
                // Move towards player
                const angle = Math.atan2(player.y - zombie.y, player.x - zombie.x);
                zombie.x += Math.cos(angle) * zombie.speed;
                zombie.y += Math.sin(angle) * zombie.speed;
            });
        }

        function drawZombies() {
            zombies.forEach(zombie => {
                ctx.beginPath();
                ctx.arc(zombie.x, zombie.y, zombie.radius, 0, Math.PI * 2);
                ctx.fillStyle = zombie.color;
                ctx.fill();
                ctx.closePath();
            });
        }

        // Collision detection
        function checkCollisions() {
            // Bullet-zombie collisions
            for (let i = bullets.length - 1; i >= 0; i--) {
                for (let j = zombies.length - 1; j >= 0; j--) {
                    const dx = bullets[i].x - zombies[j].x;
                    const dy = bullets[i].y - zombies[j].y;
                    const distance = Math.sqrt(dx * dx + dy * dy);

                    if (distance < bullets[i].radius + zombies[j].radius) {
                        // Hit zombie
                        zombies[j].health -= 50;
                        bullets
