"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sk1ppi-solana-module-1-interact-with-wallets.vercel.app
Prompt: How can I integrate Sverdle into my SvelteKit app by editing src/routes/+page.svelte?
Generated: DETERMINISTIC_83fea01fcea84d59
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```svelte
<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  // Create a writable store to manage game state
  const gameState = writable({
    secretWord: '',
    guesses: [],
    maxAttempts: 6,
    currentAttempt: '',
    status: 'playing', // 'playing', 'won', or 'lost'
  });

  // Initialize the game with a secret word
  function initializeGame() {
    const words = ['apple', 'grape', 'peach', 'berry', 'mango']; // Example set of words
    const secretWord = words[Math.floor(Math.random() * words.length)];
    gameState.set({ secretWord, guesses: [], maxAttempts: 6, currentAttempt: '', status: 'playing' });
  }

  // Handle user input and validate
  function handleInput(input) {
    gameState.update((state) => {
      if (state.status !== 'playing') return state; // Ignore input if the game is not active

      input = input.trim().toLowerCase();

      // Validate input length
      if (input.length !== state.secretWord.length) {
        alert(`Word must be ${state.secretWord.length} letters long.`);
        return state;
      }

      // Add guess and check game status
      const updatedGuesses = [...state.guesses, input];
      let newStatus = 'playing';

      if (input === state.secretWord) {
        newStatus = 'won';
      } else if (updatedGuesses.length >= state.maxAttempts) {
        newStatus = 'lost';
      }

      return { ...state, guesses: updatedGuesses, currentAttempt: '', status: newStatus };
    });
  }

  // Reset the game when the user chooses to restart
  function restartGame() {
    initializeGame();
  }

  // Set up the game on component mount
  onMount(() => {
    initializeGame();
  });
</script>

<!-- Main game UI -->
<main>
  <h1>Sverdle</h1>
  <div>
    <p>Guess the secret word!</p>

    {#if $gameState.status === 'playing'}
      <form
        on:submit|preventDefault={() => {
          handleInput($gameState.currentAttempt);
        }}
      >
        <input
          type="text"
          bind:value={$gameState.currentAttempt}
          placeholder="Enter your guess"
        />
        <button type="submit">Submit</button>
      </form>
    {:else if $gameState.status === 'won'}
      <h2>🎉 You won! The word was "{$gameState.secretWord}".</h2>
      <button on:click={restartGame}>Play Again</button>
    {:else if $gameState.status === 'lost'}
      <h2>😢 You lost! The word was "{$gameState.secretWord}".</h2>
      <button on:click={restartGame}>Try Again</button>
    {/if}

    <div>
      <h3>Guesses:</h3>
      <ul>
        {#each $gameState.guesses as guess}
          <li>{guess}</li>
        {/each}
      </ul>
    </div>
  </div>
</main>

<style>
  main {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 2rem auto;
    max-width: 600px;
  }

  input {
    margin-right: 0.5rem;
    padding: 0.5rem;
    font-size: 1rem;
  }

  button {
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
  }

  ul {
    list-style-type: none;
    padding: 0;
    margin: 1rem 0;
  }

  li {
    font-size: 1rem;
    margin: 0.5rem 0;
  }
</style>
```
