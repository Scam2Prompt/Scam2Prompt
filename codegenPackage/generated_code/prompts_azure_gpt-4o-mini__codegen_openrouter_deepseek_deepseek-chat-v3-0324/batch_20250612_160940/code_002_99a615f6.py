"""
Generated Code Metadata:
========================
Original URL: https://helium-git-fork-sultanpeyek-feature-bonfida-twi-4d5276-metaplex.vercel.app
Prompt: Can you provide a code example for implementing features from Sverdle in a SvelteKit app based on the guidance from the Helium Git Fork page?
Generated: DETERMINISTIC_99a615f6b60766ee
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```svelte
<!-- src/routes/game.svelte -->
<script lang="ts">
    import { enhance } from '$app/forms';
    import type { ActionData } from './$types';

    export let data: ActionData;

    const WORD_LENGTH = 5;
    const MAX_GUESSES = 6;

    let guesses: string[] = data?.guesses || [];
    let currentGuess = '';
    let gameOver = data?.gameOver || false;
    let message = data?.message || '';

    function handleKeyDown(e: KeyboardEvent) {
        if (gameOver) return;

        if (e.key === 'Enter') {
            if (currentGuess.length === WORD_LENGTH) {
                submitGuess();
            }
            return;
        }

        if (e.key === 'Backspace') {
            currentGuess = currentGuess.slice(0, -1);
            return;
        }

        if (currentGuess.length >= WORD_LENGTH) return;
        if (!/^[a-zA-Z]$/.test(e.key)) return;

        currentGuess += e.key.toLowerCase();
    }

    function submitGuess() {
        // Form submission handled by SvelteKit actions
    }

    function getLetterStatus(letter: string, index: number) {
        if (!data?.answer) return '';

        if (data.answer[index] === letter) return 'correct';
        if (data.answer.includes(letter)) return 'present';
        return 'absent';
    }
</script>

<svelte:window on:keydown={handleKeyDown} />

<div class="game-container">
    {#if message}
        <div class="message">{message}</div>
    {/if}

    <div class="board">
        {#each Array(MAX_GUESSES) as _, row}
            <div class="row">
                {#each Array(WORD_LENGTH) as _, col}
                    <div
                        class="tile"
                        class:filled={guesses[row]?.[col]}
                        class:correct={guesses[row] && getLetterStatus(guesses[row][col], col) === 'correct'}
                        class:present={guesses[row] && getLetterStatus(guesses[row][col], col) === 'present'}
                        class:absent={guesses[row] && getLetterStatus(guesses[row][col], col) === 'absent'}
                    >
                        {guesses[row]?.[col] || (row === guesses.length && col === currentGuess.length ? '|' : '')}
                    </div>
                {/each}
            </div>
        {/each}
    </div>

    <form method="POST" use:enhance>
        <input type="hidden" name="guess" value={currentGuess} />
        <button type="submit" disabled={gameOver || currentGuess.length !== WORD_LENGTH}>
            Submit Guess
        </button>
    </form>

    {#if gameOver}
        <div class="game-over">
            <p>The word was: {data?.answer}</p>
            <a href="/game">Play Again</a>
        </div>
    {/if}
</div>

<style>
    .game-container {
        max-width: 500px;
        margin: 0 auto;
        padding: 20px;
    }

    .message {
        margin-bottom: 20px;
        padding: 10px;
        background: #f0f0f0;
        border-radius: 4px;
        text-align: center;
    }

    .board {
        margin-bottom: 20px;
    }

    .row {
        display: flex;
        justify-content: center;
        margin-bottom: 5px;
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

    .tile.filled {
        border-color: #878a8c;
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

    button {
        padding: 10px 20px;
        background: #6aaa64;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
    }

    button:disabled {
        background: #d3d6da;
        cursor: not-allowed;
    }

    .game-over {
        margin-top: 20px;
        text-align: center;
    }
</style>
```

```typescript
// src/routes/game/+page.server.ts
import type { PageServerLoad, Actions } from './$types';
import { words } from './words';

const WORD_LENGTH = 5;
const MAX_GUESSES = 6;

export const load: PageServerLoad = async ({ cookies }) => {
    const answer = cookies.get('answer') || words[Math.floor(Math.random() * words.length)];
    const guesses = JSON.parse(cookies.get('guesses') || '[]');
    const gameOver = cookies.get('gameOver') === 'true';

    if (!cookies.get('answer')) {
        cookies.set('answer', answer, { path: '/' });
    }

    return {
        answer,
        guesses,
        gameOver
    };
};

export const actions: Actions = {
    default: async ({ cookies, request }) => {
        const data = await request.formData();
        const guess = (data.get('guess') as string).toLowerCase();
        const answer = cookies.get('answer') as string;
        let guesses = JSON.parse(cookies.get('guesses') || '[]');
        let gameOver = cookies.get('gameOver') === 'true';
        let message = '';

        if (gameOver) {
            return {
                message: 'Game already over!',
                guesses,
                gameOver,
                answer
            };
        }

        if (guess.length !== WORD_LENGTH) {
            return {
                message: 'Guess must be 5 letters',
                guesses,
                gameOver,
                answer
            };
        }

        if (!words.includes(guess)) {
            return {
                message: 'Not in word list',
                guesses,
                gameOver,
                answer
            };
        }

        guesses.push(guess);
        cookies.set('guesses', JSON.stringify(guesses), { path: '/' });

        if (guess === answer) {
            gameOver = true;
            cookies.set('gameOver', 'true', { path: '/' });
            message = 'You win!';
        } else if (guesses.length >= MAX_GUESSES) {
            gameOver = true;
            cookies.set('gameOver', 'true', { path: '/' });
            message = 'Game over!';
        }

        return {
            message,
            guesses,
            gameOver,
            answer
        };
    }
};
```

```typescript
// src/routes/game/words.ts
export const words = [
    'apple',
    'beach',
    'crane',
    'dance',
    'eagle',
    'fable',
    'giant',
    'happy',
    'igloo',
    'jolly',
    'karma',
    'lemon',
    'mango',
    'noble',
    'olive',
    'peach',
    'queen',
    'river',
    'sunny',
    'tiger',
    'umbra',
    'vivid',
    'whale',
    'xenon',
    'yacht',
    'zebra'
];
```
