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

**SvelteKit Sverdle Implementation**
=====================================

**src/routes/+page.svelte**
```svelte
<script>
  import { Sverdle } from '$lib/Sverdle.svelte';
  import { generateRandomWord } from '$lib/utils';

  let currentWord;
  let guesses = [];
  let gameOver = false;

  async function startGame() {
    currentWord = generateRandomWord();
    guesses = [];
    gameOver = false;
  }

  async function handleGuess(guess) {
    if (gameOver) return;

    if (guess.length !== 5) {
      alert('Please enter a 5-letter word');
      return;
    }

    guesses.push(guess);

    if (guess === currentWord) {
      gameOver = true;
    }
  }

  startGame();
</script>

<Sverdle
  {currentWord}
  {guesses}
  {gameOver}
  onGuess={handleGuess}
/>
```

**src/lib/Sverdle.svelte**
```svelte
<script>
  export let currentWord;
  export let guesses;
  export let gameOver;
  export let onGuess;

  function handleSubmit(event) {
    event.preventDefault();
    const guess = event.target.guess.value.trim().toLowerCase();
    onGuess(guess);
    event.target.guess.value = '';
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="text" name="guess" placeholder="Guess a 5-letter word" />
  <button type="submit">Guess</button>

  {#if gameOver}
    <p>Congratulations! You won!</p>
  {/if}

  <ul>
    {#each guesses as guess}
      <li>
        {#each guess as letter, i}
          <span class={`letter ${guess === currentWord ? 'correct' : (currentWord.includes(letter) ? 'present' : 'absent')}`}>{letter}</span>
        {/each}
      </li>
    {/each}
  </ul>
</form>

<style>
  .letter {
    width: 20px;
    height: 20px;
    border: 1px solid #ccc;
    display: inline-block;
    text-align: center;
    line-height: 20px;
  }

  .correct {
    background-color: #0f0;
  }

  .present {
    background-color: #ff0;
  }

  .absent {
    background-color: #ccc;
  }
</style>
```

**src/lib/utils.js**
```javascript
/**
 * Generates a random 5-letter word
 * @returns {string}
 */
export function generateRandomWord() {
  const words = ['house', ' stamp', ' cloud', 'dance', 'flute']; // replace with actual word list
  return words[Math.floor(Math.random() * words.length)].trim();
}
```

**src/main.js**
```javascript
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [sveltekit()],
});
```

**package.json**
```json
{
  "name": "sverdle-sveltekit",
  "version": "1.0.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@sveltejs/kit": "^1.0.0",
    "svelte": "^3.50.1"
  },
  "devDependencies": {
    "@sveltejs/kit/vite": "^1.0.0",
    "vite": "^3.0.7"
  }
}
```
