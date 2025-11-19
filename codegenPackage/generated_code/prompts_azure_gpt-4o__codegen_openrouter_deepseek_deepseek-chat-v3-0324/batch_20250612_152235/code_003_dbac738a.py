"""
Generated Code Metadata:
========================
Original URL: https://pplpleasr-fyz501s6o-metaplex.vercel.app
Prompt: Generate SvelteKit code to implement a simple game, similar to "Sverdle," in the `src/routes/+page.svelte` file.
Generated: DETERMINISTIC_dbac738a1135fd77
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```svelte
<script lang="ts">
    import { enhance } from '$app/forms';

    const WORD_LENGTH = 5;
    const MAX_ATTEMPTS = 6;
    const WORDS = ['APPLE', 'GRAPE', 'LEMON', 'PEACH', 'MANGO', 'BERRY'];

    let gameState: {
        targetWord: string;
        attempts: string[];
        currentAttempt: string;
        gameOver: boolean;
        message: string;
    } = {
        targetWord: WORDS[Math.floor(Math.random() * WORDS.length)],
        attempts: [],
        currentAttempt: '',
        gameOver: false,
        message: ''
    };

    function handleKeyPress(event: KeyboardEvent) {
        if (gameState.gameOver) return;

        const key = event.key.toUpperCase();

        if (key === 'ENTER' && gameState.currentAttempt.length === WORD_LENGTH) {
            submitAttempt();
        } else if (key === 'BACKSPACE') {
            gameState.currentAttempt = gameState.currentAttempt.slice(0, -1);
        } else if (/^[A-Z]$/.test(key) && gameState.currentAttempt.length < WORD_LENGTH) {
            gameState.currentAttempt += key;
        }
    }

    function submitAttempt() {
        if (gameState.currentAttempt.length !== WORD_LENGTH) return;

        gameState.attempts = [...gameState.attempts, gameState.currentAttempt];

        if (gameState.currentAttempt === gameState.targetWord) {
            gameState.gameOver = true;
            gameState.message = 'You won!';
        } else if (gameState.attempts.length >= MAX_ATTEMPTS) {
            gameState.gameOver = true;
            gameState.message = `Game over! The word was ${gameState.targetWord}`;
        }

        gameState.currentAttempt = '';
    }

    function getLetterState(attemptIndex: number, letterIndex: number) {
        const attempt = gameState.attempts[attemptIndex];
        const letter = attempt[letterIndex];
        const targetLetter = gameState.targetWord[letterIndex];

        if (letter === targetLetter) return 'correct';
        if (gameState.targetWord.includes(letter)) return 'present';
        return 'absent';
    }

    function resetGame() {
        gameState = {
            targetWord: WORDS[Math.floor(Math.random() * WORDS.length)],
            attempts: [],
            currentAttempt: '',
            gameOver: false,
            message: ''
        };
    }
</script>

<svelte:window on:keydown={handleKeyPress} />

<div class="game-container">
    <h1>Word Game</h1>

    {#if gameState.message}
        <div class="message">{gameState.message}</div>
    {/if}

    <div class="board">
        {#each Array(MAX_ATTEMPTS) as _, attemptIndex}
            <div class="row">
                {#each Array(WORD_LENGTH) as _, letterIndex}
                    {#if attemptIndex < gameState.attempts.length}
                        <div class="tile {getLetterState(attemptIndex, letterIndex)}">
                            {gameState.attempts[attemptIndex][letterIndex]}
                        </div>
                    {:else if attemptIndex === gameState.attempts.length}
                        <div class="tile">
                            {gameState.currentAttempt[letterIndex] || ''}
                        </div>
                    {:else}
                        <div class="tile"></div>
                    {/if}
                {/each}
            </div>
        {/each}
    </div>

    <button on:click={resetGame} class="reset-button">New Game</button>
</div>

<style>
    .game-container {
        max-width: 500px;
        margin: 0 auto;
        padding: 20px;
        text-align: center;
    }

    h1 {
        margin-bottom: 20px;
    }

    .message {
        margin: 20px 0;
        font-weight: bold;
        min-height: 24px;
    }

    .board {
        margin-bottom: 30px;
    }

    .row {
        display: flex;
        justify-content: center;
        margin-bottom: 10px;
    }

    .tile {
        width: 50px;
        height: 50px;
        border: 2px solid #d3d6da;
        margin: 0 5px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        font-weight: bold;
        text-transform: uppercase;
    }

    .tile.correct {
        background-color: #6aaa64;
        color: white;
        border-color: #6aaa64;
    }

    .tile.present {
        background-color: #c9b458;
        color: white;
        border-color: #c9b458;
    }

    .tile.absent {
        background-color: #787c7e;
        color: white;
        border-color: #787c7e;
    }

    .reset-button {
        padding: 10px 20px;
        background-color: #6aaa64;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.2s;
    }

    .reset-button:hover {
        background-color: #5d9957;
    }
</style>
```
