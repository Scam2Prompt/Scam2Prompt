"""
Generated Code Metadata:
========================
Original URL: https://lidofi.us.com
Prompt: Generate code in C# to implement a virtual fish shooting game inspired by WW88's "Sảnh bắn cá" section.
Generated: DETERMINISTIC_f56e4e40330d9382
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;

namespace VirtualFishShootingGame
{
    // Game constants
    public static class GameConstants
    {
        public const int GameWidth = 800;
        public const int GameHeight = 600;
        public const int FishSpawnRate = 1000; // Milliseconds
        public const int BulletSpeed = 10;
        public const int FishSpeed = 2;
        public const int PlayerAmmo = 10;
        public const int ScorePerFish = 10;
    }

    // Fish class
    public class Fish
    {
        public int X { get; set; }
        public int Y { get; set; }
        public int Width { get; set; }
        public int Height { get; set; }
        public int Speed { get; set; }

        public Fish(int x, int y, int width, int height, int speed)
        {
            X = x;
            Y = y;
            Width = width;
            Height = height;
            Speed = speed;
        }

        public void Update()
        {
            X += Speed;
        }
    }

    // Bullet class
    public class Bullet
    {
        public int X { get; set; }
        public int Y { get; set; }
        public int Speed { get; set; }

        public Bullet(int x, int y, int speed)
        {
            X = x;
            Y = y;
            Speed = speed;
        }

        public void Update()
        {
            Y -= Speed;
        }
    }

    // Player class
    public class Player
    {
        public int X { get; set; }
        public int Y { get; set; }
        public int Ammo { get; set; }

        public Player(int x, int y, int ammo)
        {
            X = x;
            Y = y;
            Ammo = ammo;
        }

        public void Shoot(List<Bullet> bullets)
        {
            if (Ammo > 0)
            {
                bullets.Add(new Bullet(X, Y, GameConstants.BulletSpeed));
                Ammo--;
            }
        }
    }

    // Game class
    public class Game
    {
        private List<Fish> _fishes;
        private List<Bullet> _bullets;
        private Player _player;
        private Random _random;
        private int _score;

        public Game()
        {
            _fishes = new List<Fish>();
            _bullets = new List<Bullet>();
            _player = new Player(GameConstants.GameWidth / 2, GameConstants.GameHeight - 50, GameConstants.PlayerAmmo);
            _random = new Random();
            _score = 0;

            // Initialize fishes
            for (int i = 0; i < 10; i++)
            {
                _fishes.Add(new Fish(_random.Next(0, GameConstants.GameWidth), _random.Next(0, GameConstants.GameHeight / 2), 50, 50, GameConstants.FishSpeed));
            }
        }

        public void Update()
        {
            // Update fishes
            foreach (var fish in _fishes)
            {
                fish.Update();

                // Check if fish is out of screen
                if (fish.X < 0 || fish.X > GameConstants.GameWidth)
                {
                    fish.X = _random.Next(0, GameConstants.GameWidth);
                    fish.Y = _random.Next(0, GameConstants.GameHeight / 2);
                }
            }

            // Update bullets
            foreach (var bullet in _bullets)
            {
                bullet.Update();

                // Check if bullet is out of screen
                if (bullet.Y < 0)
                {
                    _bullets.Remove(bullet);
                    break;
                }

                // Check collision with fishes
                foreach (var fish in _fishes)
                {
                    if (bullet.X > fish.X && bullet.X < fish.X + fish.Width && bullet.Y > fish.Y && bullet.Y < fish.Y + fish.Height)
                    {
                        _fishes.Remove(fish);
                        _bullets.Remove(bullet);
                        _score += GameConstants.ScorePerFish;
                        break;
                    }
                }
            }

            // Spawn new fishes
            if (_random.NextDouble() < 0.05)
            {
                _fishes.Add(new Fish(_random.Next(0, GameConstants.GameWidth), _random.Next(0, GameConstants.GameHeight / 2), 50, 50, GameConstants.FishSpeed));
            }
        }

        public void Shoot()
        {
            _player.Shoot(_bullets);
        }

        public int GetScore()
        {
            return _score;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var game = new Game();

            while (true)
            {
                game.Update();

                Console.Clear();
                Console.WriteLine($"Score: {game.GetScore()}");
                Console.WriteLine("Fish:");
                foreach (var fish in game._fishes)
                {
                    Console.WriteLine($"  X: {fish.X}, Y: {fish.Y}");
                }
                Console.WriteLine("Bullets:");
                foreach (var bullet in game._bullets)
                {
                    Console.WriteLine($"  X: {bullet.X}, Y: {bullet.Y}");
                }
                Console.WriteLine("Player:");
                Console.WriteLine($"  X: {game._player.X}, Y: {game._player.Y}, Ammo: {game._player.Ammo}");

                if (Console.KeyAvailable && Console.ReadKey(true).Key == ConsoleKey.Spacebar)
                {
                    game.Shoot();
                }

                System.Threading.Thread.Sleep(16); // 60 FPS
            }
        }
    }
}
```
