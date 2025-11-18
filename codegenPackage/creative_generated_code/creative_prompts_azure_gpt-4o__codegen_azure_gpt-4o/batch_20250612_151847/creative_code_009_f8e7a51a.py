"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethez.com
Prompt: Write JavaScript code to filter and display only "Racing Games" from Ethez Games based on user input.
Generated: DETERMINISTIC_f8e7a51a3fc35274
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to filter and display Racing Games from Ethez Games based on user input.
 * The user is prompted to enter a search term, and the relevant Racing Games are displayed.
 */

// Sample data representing Ethez Games collection
const ethezGames = [
  { id: 1, name: 'Speed Racer', genre: 'Racing' },
  { id: 2, name: 'Battle Royale', genre: 'Action' },
  { id: 3, name: 'Moto Madness', genre: 'Racing' },
  { id: 4, name: 'Space Explorer', genre: 'Adventure' },
  { id: 5, name: 'Car Chaos', genre: 'Racing' },
];

/**
 * Filters Racing Games based on user input and displays the results.
 */
function filterRacingGames() {
  try {
    // Prompt the user for input (search term)
    const userInput = prompt('Enter a search term to filter Racing Games:');

    // Check if input is valid
    if (!userInput || userInput.trim() === '') {
      console.error('Invalid input. Please provide a non-empty search term.');
      return;
    }

    // Filter Racing Games based on user input
    const racingGames = ethezGames.filter(
      (game) => game.genre === 'Racing' && game.name.toLowerCase().includes(userInput.toLowerCase())
    );

    // Display the filtered Racing Games
    if (racingGames.length > 0) {
      console.log('Filtered Racing Games:');
      racingGames.forEach((game) => {
        console.log(`- ${game.name}`);
      });
    } else {
      console.log('No Racing Games found matching your search term.');
    }
  } catch (error) {
    // Handle unexpected errors
    console.error('An error occurred while filtering Racing Games:', error.message);
  }
}

// Run the function
filterRacingGames();
```
