"""
Generated Code Metadata:
========================
Original URL: https://helium-git-fork-sultanpeyek-feature-bonfida-twi-4d5276-metaplex.vercel.app
Prompt: Provide an example of a SvelteKit project setup that includes a custom route similar to the Sverdle app mentioned on the webpage.
Generated: DETERMINISTIC_a073d4da212ac5ab
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```svelte
<!-- src/routes/+layout.svelte -->
<script>
    import '../app.css';
</script>

<slot />
```

```svelte
<!-- src/routes/+page.svelte -->
<script>
    import { page } from '$app/stores';
</script>

<h1>Welcome to My SvelteKit App</h1>

<p>Current route: {$page.url.pathname}</p>

<a href="/custom-game">Play Custom Game</a>
```

```svelte
<!-- src/routes/custom-game/+page.svelte -->
<script>
    let guesses = [];
    let currentGuess = '';
    const answer = 'SVELTE';

    function handleSubmit() {
        if (currentGuess.length !== 6) return;
        guesses = [...guesses, currentGuess];
        currentGuess = '';
    }
</script>

<h1>Custom Word Game</h1>

<form on:submit|preventDefault={handleSubmit}>
    <input
        type="text"
        bind:value={currentGuess}
        maxlength="6"
        placeholder="Enter 6-letter word"
    />
    <button type="submit">Submit</button>
</form>

{#if guesses.length > 0}
    <div class="guesses">
        {#each guesses as guess}
            <div class="guess">
                {#each guess.split('') as letter, i}
                    <span
                        class:correct={letter === answer[i]}
                        class:present={answer.includes(letter) && letter !== answer[i]}
                    >
                        {letter}
                    </span>
                {/each}
            </div>
        {/each}
    </div>
{/if}

<style>
    .guesses {
        margin-top: 2rem;
    }
    .guess {
        display: flex;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .guess span {
        display: inline-block;
        width: 2rem;
        height: 2rem;
        line-height: 2rem;
        text-align: center;
        border: 1px solid #ccc;
    }
    .correct {
        background-color: #4ade80;
        color: white;
    }
    .present {
        background-color: #fbbf24;
        color: white;
    }
</style>
```

```javascript
// src/routes/custom-game/+page.server.js
export function load() {
    return {
        meta: {
            title: 'Custom Game',
            description: 'Play a custom word game'
        }
    };
}
```

```javascript
// svelte.config.js
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    kit: {
        // adapter: adapter()
    },
    preprocess: vitePreprocess()
};

export default config;
```

```javascript
// package.json
{
    "name": "sveltekit-custom-route-example",
    "version": "0.0.1",
    "private": true,
    "scripts": {
        "dev": "vite dev",
        "build": "vite build",
        "preview": "vite preview",
        "check": "svelte-kit sync && svelte-check --tsconfig ./tsconfig.json",
        "check:watch": "svelte-kit sync && svelte-check --tsconfig ./tsconfig.json --watch"
    },
    "devDependencies": {
        "@sveltejs/kit": "^1.0.0",
        "svelte": "^3.55.0",
        "svelte-check": "^2.10.2",
        "typescript": "^4.9.3",
        "vite": "^4.0.0"
    }
}
```
