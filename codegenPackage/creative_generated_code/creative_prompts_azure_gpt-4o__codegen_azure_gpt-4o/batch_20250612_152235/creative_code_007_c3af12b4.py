"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-pay-five.vercel.app
Prompt: Write SvelteKit code to implement a simple game like "Sverdle" by editing the `src/routes/+page.svelte` file.
Generated: DETERMINISTIC_c3af12b462722418
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```svelte
<script lang="ts">
  import { onMount } from 'svelte';

  // Constants
  const MAX_ATTEMPTS = 6;
  const WORD_LENGTH = 5;
  const TARGET_WORD = 'svelte'; // Target word for the game (should ideally be randomly selected from a word list)
  const allowedWords = ['svelte', 'react', 'solid', 'vuejs', 'angular']; // Example allowed words list

  // Game state variables
  let attempts: string[] = [];
  let currentGuess = '';
  let gameOver = false;
  let gameMessage = '';

  // Helper function: Validate the guess
  function validateGuess(guess: string): boolean {
    return guess.length === WORD_LENGTH && allowedWords.includes(guess.toLowerCase());
  }

  // Helper function: Compare guess with target word
  function compareGuess(guess: string): string[] {
    const result: string[] = [];
    for (let i = 0; i < WORD_LENGTH; i++) {
      if (guess[i] === TARGET_WORD[i]) {
        result.push('correct'); // Correct position
      } else if (TARGET_WORD.includes(guess[i])) {
        result.push('present'); // Correct letter, wrong position
      } else {
        result.push('absent'); // Letter not in target word
      }
    }
    return result;
  }

  // Function: Handle user submission
  function handleSubmit() {
    if (gameOver) {
      gameMessage = 'Game is over. Refresh to play again!';
      return;
    }

    if (!validateGuess(currentGuess)) {
      gameMessage = `Invalid guess! Ensure it's a ${WORD_LENGTH}-letter word from the allowed words list.`;
      return;
    }

    attempts.push(currentGuess);

    if (currentGuess === TARGET_WORD) {
      gameMessage = 'Congratulations! You guessed the word!';
      gameOver = true;
    } else if (attempts.length >= MAX_ATTEMPTS) {
      gameMessage = `Game over! The correct word was: ${TARGET_WORD}`;
      gameOver = true;
    } else {
      gameMessage = `Attempt ${attempts.length} submitted. Keep guessing!`;
    }

    currentGuess = ''; // Reset current guess
  }

  // Function: Track user input and enforce word length
  function handleInput(event: Event) {
    const inputValue = (event.target as HTMLInputElement).value.toLowerCase();
    if (inputValue.length <= WORD_LENGTH) {
      currentGuess = inputValue;
    }
  }

  // Initialize game state when the component is mounted
  onMount(() => {
    attempts = [];
    currentGuess = '';
    gameOver = false;
    gameMessage = 'Welcome to Sverdle! Start guessing the word.';
  });
</script>

<style>
  .guess-result {
    display: flex;
    gap: 0.5rem;
  }

  .letter {
    width: 2rem;
    height: 2rem;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid #ccc;
    font-weight: bold;
    text-transform: uppercase;
  }

  .correct {
    background-color: green;
    color: white;
  }

  .present {
    background-color: orange;
    color: white;
  }

  .absent {
    background-color: gray;
    color: white;
  }
</style>

<div id="game">
  <h1>Sverdle</h1>
  <p>{gameMessage}</p>

  {#if gameOver}
    <button on:click={() => location.reload()}>Play Again</button>
  {:else}
    <form on:submit|preventDefault={handleSubmit}>
      <input
        type="text"
        bind:value={currentGuess}
        on:input={handleInput}
        maxlength={WORD_LENGTH}
        placeholder={`Enter a ${WORD_LENGTH}-letter word`}
        disabled={gameOver}
      />
      <button type="submit">Submit Guess</button>
    </form>
  {/if}

  <div class="attempts">
    {#each attempts as attempt}
      <div class="guess-result">
        {#each compareGuess(attempt) as result, i}
          <div class="letter {result}">{attempt[i]}</div>
        {/each}
      </div>
    {/each}
  </div>
</div>
```
