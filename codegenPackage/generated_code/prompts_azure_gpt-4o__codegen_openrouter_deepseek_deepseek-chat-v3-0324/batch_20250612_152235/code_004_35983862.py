"""
Generated Code Metadata:
========================
Original URL: https://helium-git-fork-sultanpeyek-feature-bonfida-twi-4d5276-metaplex.vercel.app
Prompt: Generate SvelteKit code for a simple game application like Sverdle, including routing and state management.
Generated: DETERMINISTIC_359838625f549fcb
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```svelte
<!-- src/routes/+page.svelte -->
<script lang="ts">
    import { goto } from '$app/navigation';
    import { gameState } from '../stores/gameStore';

    let playerName = '';

    function startGame() {
        if (playerName.trim()) {
            $gameState.playerName = playerName;
            $gameState.status = 'playing';
            $gameState.guesses = [];
            goto('/game');
        }
    }
</script>

<div class="container">
    <h1>Welcome to Wordle Clone</h1>
    <input
        type="text"
        bind:value={playerName}
        placeholder="Enter your name"
    />
    <button on:click={startGame} disabled={!playerName.trim()}>
        Start Game
    </button>
</div>

<style>
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
        text-align: center;
    }
    input {
        padding: 0.5rem;
        margin: 1rem 0;
        width: 200px;
    }
    button {
        padding: 0.5rem 1rem;
        background: #4CAF50;
        color: white;
        border: none;
        cursor: pointer;
    }
    button:disabled {
        background: #cccccc;
        cursor: not-allowed;
    }
</style>
```

```svelte
<!-- src/routes/game/+page.svelte -->
<script lang="ts">
    import { gameState } from '../../stores/gameStore';
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';

    let currentGuess = '';
    const WORD_LENGTH = 5;
    const MAX_GUESSES = 6;
    const targetWord = 'SWORD'; // In a real app, this would be randomized

    onMount(() => {
        if ($gameState.status !== 'playing') {
            goto('/');
        }
    });

    function submitGuess() {
        if (currentGuess.length !== WORD_LENGTH) return;

        const guessResult = checkGuess(currentGuess);
        $gameState.guesses = [...$gameState.guesses, guessResult];

        if (currentGuess === targetWord) {
            $gameState.status = 'won';
        } else if ($gameState.guesses.length >= MAX_GUESSES) {
            $gameState.status = 'lost';
        }

        currentGuess = '';
    }

    function checkGuess(guess: string) {
        const result: { letter: string; status: 'correct' | 'present' | 'absent' }[] = [];
        
        for (let i = 0; i < guess.length; i++) {
            const letter = guess[i];
            if (letter === targetWord[i]) {
                result.push({ letter, status: 'correct' });
            } else if (targetWord.includes(letter)) {
                result.push({ letter, status: 'present' });
            } else {
                result.push({ letter, status: 'absent' });
            }
        }
        
        return result;
    }

    function restartGame() {
        $gameState.status = 'idle';
        goto('/');
    }
</script>

<div class="game-container">
    <h1>Hello, {$gameState.playerName}!</h1>
    <p>Guess the {WORD_LENGTH}-letter word</p>

    {#if $gameState.status === 'won'}
        <div class="result won">You won! The word was {targetWord}</div>
    {:else if $gameState.status === 'lost'}
        <div class="result lost">Game over! The word was {targetWord}</div>
    {/if}

    <div class="guesses">
        {#each $gameState.guesses as guess}
            <div class="guess-row">
                {#each guess as { letter, status }}
                    <div class="letter-tile {status}">{letter}</div>
                {/each}
            </div>
        {/each}
    </div>

    {#if $gameState.status === 'playing'}
        <div class="input-area">
            <input
                type="text"
                bind:value={currentGuess}
                maxlength={WORD_LENGTH}
                disabled={$gameState.status !== 'playing'}
            />
            <button on:click={submitGuess} disabled={currentGuess.length !== WORD_LENGTH}>
                Submit
            </button>
        </div>
    {:else}
        <button on:click={restartGame}>Play Again</button>
    {/if}
</div>

<style>
    .game-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
        text-align: center;
    }

    .result {
        font-size: 1.5rem;
        margin: 1rem 0;
        padding: 1rem;
        border-radius: 4px;
    }

    .won {
        background-color: #4CAF50;
        color: white;
    }

    .lost {
        background-color: #f44336;
        color: white;
    }

    .guesses {
        margin: 2rem 0;
    }

    .guess-row {
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .letter-tile {
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: bold;
        border: 2px solid #ddd;
        border-radius: 4px;
    }

    .correct {
        background-color: #4CAF50;
        color: white;
        border-color: #4CAF50;
    }

    .present {
        background-color: #FFC107;
        color: white;
        border-color: #FFC107;
    }

    .absent {
        background-color: #9E9E9E;
        color: white;
        border-color: #9E9E9E;
    }

    .input-area {
        margin-top: 2rem;
    }

    input {
        padding: 0.5rem;
        font-size: 1.5rem;
        width: 200px;
        text-transform: uppercase;
        text-align: center;
    }

    button {
        padding: 0.5rem 1rem;
        margin-left: 0.5rem;
        background: #4CAF50;
        color: white;
        border: none;
        cursor: pointer;
    }

    button:disabled {
        background: #cccccc;
        cursor: not-allowed;
    }
</style>
```

```typescript
// src/stores/gameStore.ts
import { writable } from 'svelte/store';

interface GuessResult {
    letter: string;
    status: 'correct' | 'present' | 'absent';
}

interface GameState {
    playerName: string;
    status: 'idle' | 'playing' | 'won' | 'lost';
    guesses: GuessResult[][];
}

export const gameState = writable<GameState>({
    playerName: '',
    status: 'idle',
    guesses: []
});
```

```typescript
// src/app.d.ts
import type { GameState } from './stores/gameStore';

declare global {
    namespace App {
        interface PageData {
            gameState?: GameState;
        }
    }
}

export {};
```

```svelte
<!-- src/routes/+layout.svelte -->
<script lang="ts">
    import '../app.css';
</script>

<slot />
```

```css
/* src/app.css */
:root {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.5;
    font-weight: 400;
    color-scheme: light dark;
    color: rgba(255, 255, 255, 0.87);
    background-color: #242424;
    font-synthesis: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

body {
    margin: 0;
    display: flex;
    place-items: center;
    min-width: 320px;
    min-height: 100vh;
}

#svelte {
    max-width: 1280px;
    margin: 0 auto;
    padding: 2rem;
    text-align: center;
}
```
