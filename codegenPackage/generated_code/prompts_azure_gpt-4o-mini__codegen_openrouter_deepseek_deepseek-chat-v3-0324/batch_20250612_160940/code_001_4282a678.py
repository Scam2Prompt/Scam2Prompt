"""
Generated Code Metadata:
========================
Original URL: https://pplpleasr-fyz501s6o-metaplex.vercel.app
Prompt: What are the steps to set up a new SvelteKit app and include Sverdle functionality?
Generated: DETERMINISTIC_4282a67837ed8a3c
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# Step 1: Create a new SvelteKit project
npm create svelte@latest my-sverdle-app
cd my-sverdle-app
npm install

# Step 2: Install required dependencies
npm install --save-dev @types/node

# Step 3: Create game components and logic
mkdir -p src/lib/game
touch src/lib/game/{Game.svelte,Keyboard.svelte,Square.svelte,WordRow.svelte,words.ts,game.ts}

# Step 4: Add words.ts (word list)
cat << 'EOF' > src/lib/game/words.ts
export const WORDS = [
    'apple', 'beach', 'candy', 'dance', 'eagle',
    'fairy', 'ghost', 'happy', 'igloo', 'jolly',
    'koala', 'lemon', 'mango', 'ninja', 'olive',
    'peach', 'queen', 'robot', 'sunny', 'tiger',
    'umbra', 'vivid', 'whale', 'xerox', 'yacht', 'zebra'
];
EOF

# Step 5: Add game.ts (game logic)
cat << 'EOF' > src/lib/game/game.ts
import { WORDS } from './words';

export const MAX_GUESSES = 6;
export const WORD_LENGTH = 5;

export type LetterState = 'correct' | 'present' | 'absent';

export interface Guess {
    word: string;
    evaluation: LetterState[];
}

export function getRandomWord(): string {
    return WORDS[Math.floor(Math.random() * WORDS.length)];
}

export function evaluateGuess(guess: string, answer: string): LetterState[] {
    const evaluation: LetterState[] = Array(WORD_LENGTH).fill('absent');
    const answerLetters = answer.split('');
    const guessLetters = guess.split('');

    // Check for correct letters first
    for (let i = 0; i < WORD_LENGTH; i++) {
        if (guessLetters[i] === answerLetters[i]) {
            evaluation[i] = 'correct';
            answerLetters[i] = ''; // Mark as used
        }
    }

    // Check for present letters
    for (let i = 0; i < WORD_LENGTH; i++) {
        if (evaluation[i] === 'correct') continue;
        
        const index = answerLetters.indexOf(guessLetters[i]);
        if (index !== -1) {
            evaluation[i] = 'present';
            answerLetters[index] = ''; // Mark as used
        }
    }

    return evaluation;
}
EOF

# Step 6: Add Square.svelte
cat << 'EOF' > src/lib/game/Square.svelte
<script lang="ts">
    export let letter: string;
    export let state: 'correct' | 'present' | 'absent' | 'empty' = 'empty';
</script>

<div
    class="square"
    class:correct={state === 'correct'}
    class:present={state === 'present'}
    class:absent={state === 'absent'}
>
    {letter}
</div>

<style>
    .square {
        width: 50px;
        height: 50px;
        border: 2px solid #d3d6da;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 2rem;
        font-weight: bold;
        text-transform: uppercase;
    }

    .correct {
        background-color: #6aaa64;
        color: white;
        border-color: #6aaa64;
    }

    .present {
        background-color: #c9b458;
        color: white;
        border-color: #c9b458;
    }

    .absent {
        background-color: #787c7e;
        color: white;
        border-color: #787c7e;
    }
</style>
EOF

# Step 7: Add WordRow.svelte
cat << 'EOF' > src/lib/game/WordRow.svelte
<script lang="ts">
    import Square from './Square.svelte';
    import type { LetterState } from './game';

    export let word: string;
    export let evaluation: LetterState[];
    export let isActive = false;
</script>

<div class="row">
    {#each Array(5) as _, i}
        <Square
            letter={word[i] || ''}
            state={evaluation?.[i] || 'empty'}
        />
    {/each}
</div>

<style>
    .row {
        display: flex;
        gap: 5px;
        margin-bottom: 5px;
    }
</style>
EOF

# Step 8: Add Keyboard.svelte
cat << 'EOF' > src/lib/game/Keyboard.svelte
<script lang="ts">
    import { onMount } from 'svelte';
    import type { LetterState } from './game';

    export let onKeyPress: (key: string) => void;
    export let letterStates: Record<string, LetterState> = {};

    const rows = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ['Enter', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Backspace']
    ];

    onMount(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if (e.key === 'Enter') {
                onKeyPress('Enter');
            } else if (e.key === 'Backspace') {
                onKeyPress('Backspace');
            } else if (/^[a-z]$/i.test(e.key)) {
                onKeyPress(e.key.toUpperCase());
            }
        };

        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
    });
</script>

<div class="keyboard">
    {#each rows as row}
        <div class="row">
            {#each row as key}
                <button
                    class="key"
                    class:correct={letterStates[key.toLowerCase()] === 'correct'}
                    class:present={letterStates[key.toLowerCase()] === 'present'}
                    class:absent={letterStates[key.toLowerCase()] === 'absent'}
                    on:click={() => onKeyPress(key)}
                >
                    {#if key === 'Backspace'}
                        ⌫
                    {:else}
                        {key}
                    {/if}
                </button>
            {/each}
        </div>
    {/each}
</div>

<style>
    .keyboard {
        margin-top: 20px;
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .row {
        display: flex;
        justify-content: center;
        gap: 5px;
    }

    .key {
        min-width: 30px;
        height: 50px;
        border: none;
        border-radius: 4px;
        background-color: #d3d6da;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0 10px;
    }

    .key:hover {
        background-color: #c0c3c7;
    }

    .correct {
        background-color: #6aaa64;
        color: white;
    }

    .present {
        background-color: #c9b458;
        color: white;
    }

    .absent {
        background-color: #787c7e;
        color: white;
    }
</style>
EOF

# Step 9: Add Game.svelte (main component)
cat << 'EOF' > src/lib/game/Game.svelte
<script lang="ts">
    import { onMount } from 'svelte';
    import WordRow from './WordRow.svelte';
    import Keyboard from './Keyboard.svelte';
    import { getRandomWord, evaluateGuess, MAX_GUESSES, WORD_LENGTH, type LetterState } from './game';

    let answer: string = '';
    let guesses: { word: string; evaluation: LetterState[] }[] = [];
    let currentGuess = '';
    let gameOver = false;
    let message = '';
    let letterStates: Record<string, LetterState> = {};

    onMount(() => {
        startNewGame();
    });

    function startNewGame() {
        answer = getRandomWord();
        guesses = [];
        currentGuess = '';
        gameOver = false;
        message = '';
        letterStates = {};
    }

    function handleKeyPress(key: string) {
        if (gameOver) return;

        if (key === 'Enter') {
            if (currentGuess.length === WORD_LENGTH) {
                const evaluation = evaluateGuess(currentGuess, answer);
                guesses = [...guesses, { word: currentGuess, evaluation }];
                
                // Update letter states
                currentGuess.split('').forEach((letter, i) => {
                    const currentState = letterStates[letter];
