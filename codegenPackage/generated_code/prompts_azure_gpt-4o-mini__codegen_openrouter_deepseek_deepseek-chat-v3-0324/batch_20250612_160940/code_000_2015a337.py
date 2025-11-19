"""
Generated Code Metadata:
========================
Original URL: https://helium-git-fork-sultanpeyek-feature-bonfida-twi-4d5276-metaplex.vercel.app
Prompt: How can I integrate Sverdle into my SvelteKit app using the instructions provided on the Helium Git Fork webpage?
Generated: DETERMINISTIC_2015a337dbeb0e3d
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```svelte
<script lang="ts">
    import { onMount } from 'svelte';
    import { game, initGame, type CharStatus } from 'sverdle';

    // Initialize the game on component mount
    onMount(() => {
        initGame();
    });

    // Function to handle keyboard input
    function handleKeydown(event: KeyboardEvent) {
        if (game.over) return;

        if (event.key === 'Enter') {
            game.submitGuess();
        } else if (event.key === 'Backspace') {
            game.deleteLastLetter();
        } else if (/^[A-Za-z]$/.test(event.key)) {
            game.addLetter(event.key.toUpperCase());
        }
    }

    // Add keyboard event listener when component mounts
    onMount(() => {
        window.addEventListener('keydown', handleKeydown);
        return () => {
            window.removeEventListener('keydown', handleKeydown);
        };
    });

    // Function to get tile status for styling
    function getTileStatus(letter: string, index: number): CharStatus | undefined {
        if (!game.guesses[index]) return undefined;
        return game.guesses[index].statuses[game.guesses[index].word.indexOf(letter)];
    }
</script>

<main class="game-container">
    <h1>Sverdle</h1>

    <div class="game-board">
        {#each Array(6) as _, rowIndex}
            <div class="game-row">
                {#each Array(5) as _, colIndex}
                    {#const letter = game.guesses[rowIndex]?.word[colIndex] || game.currentGuess[colIndex] || ''}
                    <div
                        class="game-tile"
                        class:filled={letter}
                        class:current-row={rowIndex === game.guesses.length && !game.over}
                        data-status={getTileStatus(letter, rowIndex)}
                    >
                        {letter}
                    </div>
                {/each}
            </div>
        {/each}
    </div>

    {#if game.over}
        <div class="game-message">
            {#if game.won}
                <p>Congratulations! You won!</p>
            {:else}
                <p>Game over! The word was: {game.answer}</p>
            {/if}
            <button on:click={initGame}>Play Again</button>
        </div>
    {/if}

    <div class="keyboard">
        {#each ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM'] as row}
            <div class="keyboard-row">
                {#if row === 'ZXCVBNM'}
                    <button class="keyboard-key wide" on:click={game.submitGuess}>ENTER</button>
                {/if}

                {#each row.split('') as key}
                    <button
                        class="keyboard-key"
                        class:used={game.usedKeys[key] === 'used'}
                        class:correct={game.usedKeys[key] === 'correct'}
                        class:present={game.usedKeys[key] === 'present'}
                        on:click={() => game.addLetter(key)}
                    >
                        {key}
                    </button>
                {/each}

                {#if row === 'ZXCVBNM'}
                    <button class="keyboard-key wide" on:click={game.deleteLastLetter}>DEL</button>
                {/if}
            </div>
        {/each}
    </div>
</main>

<style>
    .game-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        max-width: 500px;
        margin: 0 auto;
        padding: 1rem;
    }

    .game-board {
        margin: 1rem 0;
    }

    .game-row {
        display: flex;
        justify-content: center;
        margin-bottom: 0.5rem;
    }

    .game-tile {
        width: 3rem;
        height: 3rem;
        border: 2px solid #d3d6da;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 2rem;
        font-weight: bold;
        margin: 0 0.2rem;
        text-transform: uppercase;
    }

    .game-tile.filled {
        border-color: #878a8c;
    }

    .game-tile.current-row {
        border-color: #878a8c;
        animation: pulse 1s infinite;
    }

    .game-tile[data-status="correct"] {
        background-color: #6aaa64;
        color: white;
        border-color: #6aaa64;
    }

    .game-tile[data-status="present"] {
        background-color: #c9b458;
        color: white;
        border-color: #c9b458;
    }

    .game-tile[data-status="used"] {
        background-color: #787c7e;
        color: white;
        border-color: #787c7e;
    }

    .game-message {
        text-align: center;
        margin: 1rem 0;
    }

    .game-message button {
        margin-top: 1rem;
        padding: 0.5rem 1rem;
        background-color: #6aaa64;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    .keyboard {
        margin-top: 1rem;
    }

    .keyboard-row {
        display: flex;
        justify-content: center;
        margin-bottom: 0.5rem;
    }

    .keyboard-key {
        min-width: 2rem;
        height: 3rem;
        margin: 0 0.2rem;
        border: none;
        border-radius: 4px;
        background-color: #d3d6da;
        font-weight: bold;
        cursor: pointer;
        text-transform: uppercase;
    }

    .keyboard-key.wide {
        min-width: 3.5rem;
    }

    .keyboard-key.used {
        background-color: #787c7e;
        color: white;
    }

    .keyboard-key.correct {
        background-color: #6aaa64;
        color: white;
    }

    .keyboard-key.present {
        background-color: #c9b458;
        color: white;
    }

    @keyframes pulse {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
        100% {
            transform: scale(1);
        }
    }
</style>
```
