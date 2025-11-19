"""
Generated Code Metadata:
========================
Original URL: https://stethtoken.net
Prompt: Generate a .NET code snippet for Xbox game development.
Generated: DETERMINISTIC_ad64c6e653d76b15
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using System;

namespace XboxGameDevelopment
{
    /// <summary>
    /// This is the main type for your game.
    /// </summary>
    public class Game1 : Game
    {
        private GraphicsDeviceManager _graphics;
        private SpriteBatch _spriteBatch;

        // Game objects
        private Texture2D _playerTexture;
        private Vector2 _playerPosition;

        public Game1()
        {
            _graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
            IsMouseVisible = true;
        }

        /// <summary>
        /// Allows the game to perform any initialization it needs to before starting to run.
        /// This is where it can query for any required services and load any non-graphic
        /// related game data.  Calling base.Initialize will enumerate through any components
        /// and initialize them.
        /// </summary>
        protected override void Initialize()
        {
            // Initialize graphics settings
            _graphics.PreferredBackBufferWidth = 800;
            _graphics.PreferredBackBufferHeight = 480;
            _graphics.ApplyChanges();

            base.Initialize();
        }

        /// <summary>
        /// LoadContent will be called once per game and is the place to load
        /// all of your content.
        /// </summary>
        protected override void LoadContent()
        {
            _spriteBatch = new SpriteBatch(GraphicsDevice);

            // Load player texture
            try
            {
                _playerTexture = Content.Load<Texture2D>("player");
            }
            catch (ContentLoadException ex)
            {
                Console.WriteLine($"Error loading player texture: {ex.Message}");
            }

            // Initialize player position
            _playerPosition = new Vector2(GraphicsDevice.Viewport.Width / 2, GraphicsDevice.Viewport.Height / 2);
        }

        /// <summary>
        /// UnloadContent will be called once per game and is the place to unload
        /// game-specific content.
        /// </summary>
        protected override void UnloadContent()
        {
            // Unload player texture
            _playerTexture?.Dispose();
        }

        /// <summary>
        /// Allows the game to run logic such as updating the world,
        /// checking for collisions, gathering input, and playing audio.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Update(GameTime gameTime)
        {
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
                Exit();

            // Update player position based on input
            var keyboardState = Keyboard.GetState();
            if (keyboardState.IsKeyDown(Keys.Up))
                _playerPosition.Y -= 5;
            if (keyboardState.IsKeyDown(Keys.Down))
                _playerPosition.Y += 5;
            if (keyboardState.IsKeyDown(Keys.Left))
                _playerPosition.X -= 5;
            if (keyboardState.IsKeyDown(Keys.Right))
                _playerPosition.X += 5;

            base.Update(gameTime);
        }

        /// <summary>
        /// This is called when the game should draw itself.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(Color.CornflowerBlue);

            // Draw player
            _spriteBatch.Begin();
            _spriteBatch.Draw(_playerTexture, _playerPosition, Color.White);
            _spriteBatch.End();

            base.Draw(gameTime);
        }
    }
}
```

```csharp
using System;

namespace XboxGameDevelopment
{
    public static class Program
    {
        [STAThread]
        static void Main()
        {
            try
            {
                using (var game = new Game1())
                    game.Run();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error running game: {ex.Message}");
            }
        }
    }
}
```
