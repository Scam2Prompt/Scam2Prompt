"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-pay-five.vercel.app
Prompt: Can you provide a code example for implementing Sverdle in a new SvelteKit project based on the guidance from solana-pay-five.vercel.app?
Generated: DETERMINISTIC_d3ce0236df1b1099
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/routes/sverdle/+page.svelte
<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let guesses = [];
  let answer = '';
  let currentGuess = '';
  const totalGuesses = 6;
  const wordLength = 5;

  // Initialize the game
  onMount(() => {
    startNewGame();
  });

  // Start a new game and generate random 5-letter word
  function startNewGame() {
    // Example static word list, replace this with dynamic fetching if needed
    const wordList = ['apple', 'grape', 'berry', 'peach', 'lemon'];
    const randomIndex = Math.floor(Math.random() * wordList.length);
    answer = wordList[randomIndex];
    guesses = [];
    currentGuess = '';
  }

  // Handle input from user
  function handleInput(event) {
    const input = event.target.value;
    if (input.length <= wordLength) {
      currentGuess = input;
    }
  }

  // Submit the current guess
  function submitGuess() {
    if (currentGuess.length !== wordLength) {
      alert('Guess must be 5 letters.');
      return;
    }
    if (guesses.length >= totalGuesses) {
      alert('No more guesses allowed.');
      return;
    }

    const result = evaluateGuess(currentGuess);
    guesses.push({ word: currentGuess, result });
    currentGuess = '';

    if (currentGuess === answer) {
      alert('You won!');
      startNewGame();
    } else if (guesses.length === totalGuesses) {
      alert(`Game over! The correct word was "${answer}".`);
      startNewGame();
    }
  }

  // Evaluate how well the guess matches the answer
  function evaluateGuess(guess) {
    // Result array, where 'correct' = correct letter and position,
    // 'misplaced' = correct letter but wrong position, 'wrong' = incorrect letter
    const result = new Array(wordLength).fill('wrong');
    const answerChars = answer.split('');
    const guessChars = guess.split('');

    // First pass: Check for correct letters in the correct positions
    guessChars.forEach((char, index) => {
      if (char === answerChars[index]) {
        result[index] = 'correct';
        answerChars[index] = null; // Mark as used
      }
    });

    // Second pass: Check for correct letters in wrong positions
    guessChars.forEach((char, index) => {
      if (result[index] === 'wrong' && answerChars.includes(char)) {
        result[index] = 'misplaced';
        answerChars[answerChars.indexOf(char)] = null; // Mark as used
      }
    });

    return result;
  }
</script>

<style>
  .guess {
    display: flex;
    margin-bottom: 10px;
  }
  .letter {
    width: 2em;
    height: 2em;
    margin: 0 5px;
    text-align: center;
    font-size: 1.5em;
    border: 1px solid #ccc;
    line-height: 2em;
  }
  .correct {
    background-color: green;
    color: white;
  }
  .misplaced {
    background-color: yellow;
    color: black;
  }
  .wrong {
    background-color: red;
    color: white;
  }
</style>

<main>
  <h1>Sverdle</h1>
  <div>
    {#each guesses as { word, result }}
      <div class="guess">
        {#each word as letter, index}
          <div class="letter {result[index]}">{letter}</div>
        {/each}
      </div>
    {/each}
  </div>
  <input type="text" bind:value={currentGuess} maxlength={wordLength} on:input={handleInput} />
  <button on:click={submitGuess}>Submit</button>
</main>
```
