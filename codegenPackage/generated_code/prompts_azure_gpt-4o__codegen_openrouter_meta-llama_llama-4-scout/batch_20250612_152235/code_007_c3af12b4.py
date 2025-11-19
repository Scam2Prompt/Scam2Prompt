"""
Generated Code Metadata:
========================
Original URL: https://solana-pay-five.vercel.app
Prompt: Write SvelteKit code to implement a simple game like "Sverdle" by editing the `src/routes/+page.svelte` file.
Generated: DETERMINISTIC_c3af12b462722418
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```svelte
<script>
  // Import required modules
  import { invalidateAll, formData } from '$app/forms';
  import { fail } from '@sveltejs/kit';

  // Initialize game state
  let word = '';
  let guesses = [];
  let currentGuess = '';
  let result = '';
  const maxGuesses = 6;
  const wordLength = 5;

  // Generate a random 5-letter word (replace with API call or dictionary)
  const dictionary = ['apple', 'table', 'chair', 'basic', 'cloud'];
  word = dictionary[Math.floor(Math.random() * dictionary.length)];

  // Function to handle form submission
  async function handleSubmit() {
    // Check if input is valid
    if (currentGuess.length !== wordLength) {
      result = `Please enter a ${wordLength}-letter word.`;
      return;
    }

    // Check if input is a valid word (replace with dictionary check)
    if (!dictionary.includes(currentGuess)) {
      result = 'Invalid word. Please try again.';
      return;
    }

    // Add guess to list
    guesses = [...guesses, currentGuess];

    // Check if user won
    if (currentGuess === word) {
      result = ' Congratulations, you won!';
      return;
    }

    // Check if user ran out of guesses
    if (guesses.length >= maxGuesses) {
      result = `Game over. The word was ${word}.`;
      return;
    }

    // Reset current guess
    currentGuess = '';
  }

  // Function to handle key press
  function handleKeyPress(event) {
    // Check if input is a letter
    if (event.key.match(/[a-z]/i)) {
      // Append letter to current guess
      currentGuess += event.key.toLowerCase();
    } else if (event.key === 'Backspace') {
      // Remove last letter from current guess
      currentGuess = currentGuess.slice(0, -1);
    } else if (event.key === 'Enter') {
      // Submit form on Enter key press
      handleSubmit();
    }
  }

  // Add event listener for key presses
  document.addEventListener('keydown', handleKeyPress);

  // Clean up event listener on destroy
  onDestroy(() => {
    document.removeEventListener('keydown', handleKeyPress);
  });
</script>

<style>
  .guess {
    display: flex;
    gap: 5px;
  }

  .letter {
    width: 30px;
    height: 30px;
    border: 1px solid #ccc;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 18px;
  }

  .correct {
    background-color: #0f0;
  }

  .present {
    background-color: #ff0;
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <input
    type="text"
    bind:value={currentGuess}
    maxlength={wordLength}
    placeholder="Guess a 5-letter word"
  />
  <button type="submit">Guess</button>
</form>

{#if result}
  <p>{result}</p>
{/if}

<ul>
  {#each guesses as guess}
    <li class="guess">
      {#each guess as letter}
        <div class="letter">
          {letter}
          {#if letter === word[guesses.indexOf(guess)]}
            <span class="correct"></span>
          {/if}
          {#if word.includes(letter) && letter !== word[guesses.indexOf(guess)]}
            <span class="present"></span>
          {/if}
        </div>
      {/each}
    </li>
  {/each}
</ul>
```
