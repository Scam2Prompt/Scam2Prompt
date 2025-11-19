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

**src/routes/+page.svelte**
```svelte
<script>
  import { goto } from '$app/navigation';
  import { word } from '$lib/stores';
  import { guess } from '$lib/utils';

  let input = '';
  let result = '';

  async function handleGuess() {
    try {
      const response = await guess(input);
      result = response.result;
      if (response.result === 'win') {
        await goto('/win');
      }
      input = '';
    } catch (error) {
      console.error(error);
    }
  }
</script>

<h1>Sverdle</h1>

<form on:submit|preventDefault={handleGuess}>
  <input
    type="text"
    bind:value={input}
    placeholder="Guess a 5-letter word"
    maxlength="5"
  />
  <button type="submit">Guess</button>
</form>

{#if result}
  <p>{result}</p>
{/if}
```

**src/routes/win/+page.svelte**
```svelte
<script>
  import { word } from '$lib/stores';
</script>

<h1> Congratulations! You won!</h1>

<p>The word was: {$word}</p>

<a href="/">Play again</a>
```

**src/lib/stores.js**
```javascript
import { writable } from 'svelte/store';

const word = writable('');
const guesses = writable([]);
const result = writable('');

export { word, guesses, result };
```

**src/lib/utils.js**
```javascript
import { word } from '$lib/stores';

const fiveLetterWords = ['apple', 'basic', 'cloud', 'dance', 'flute'];

async function guess(input) {
  const currentWord = await getWord();
  if (input.length !== 5) {
    return { result: 'Invalid input. Please enter a 5-letter word.' };
  }

  const guesses = await getGuesses();
  guesses.push(input);

  if (input === currentWord) {
    return { result: 'win' };
  }

  const result = getResult(input, currentWord);
  return { result };
}

async function getWord() {
  return new Promise((resolve) => {
    // For demo purposes, return a random 5-letter word
    const randomIndex = Math.floor(Math.random() * fiveLetterWords.length);
    resolve(fiveLetterWords[randomIndex]);
  });
}

async function getGuesses() {
  return new Promise((resolve) => {
    // For demo purposes, return an empty array
    resolve([]);
  });
}

function getResult(guess, word) {
  let result = '';
  for (let i = 0; i < guess.length; i++) {
    if (guess[i] === word[i]) {
      result += `<span style="background-color: green">${guess[i]}</span>`;
    } else if (word.includes(guess[i])) {
      result += `<span style="background-color: yellow">${guess[i]}</span>`;
    } else {
      result += `<span style="background-color: gray">${guess[i]}</span>`;
    }
  }
  return result;
}

export { guess };
```

**src/lib/data.js**
```javascript
// For production, use a secure API to fetch words
// For demo purposes, use a local array
const words = ['apple', 'basic', 'cloud', 'dance', 'flute'];

export { words };
```

**vite.config.js**
```javascript
import { sveltekit } from '@sveltejs/kit/vite';

export default {
  plugins: [sveltekit()],
  build: {
    target: 'es2015',
  },
};
```

**package.json**
```json
{
  "name": "sverdle",
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
    "@types/node": "^17.0.34",
    "vite": "^2.9.13"
  }
}
```
