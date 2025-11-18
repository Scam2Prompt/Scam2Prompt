"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Create a single-elimination tournament bracket generator for slowpitch softball playoffs in JavaScript, following the features described on Slo-Pitch Central.
Generated: DETERMINISTIC_8f23ec30ebe04b8a
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Single-Elimination Tournament Bracket Generator
 * Author: [Your Name]
 * Description: Generates a single-elimination tournament bracket for slowpitch softball playoffs.
 * Features:
 * - Accepts a list of teams
 * - Handles odd number of teams by adding a bye
 * - Displays matchups for each round
 * - Generates bracket until the winner is determined
 */

/**
 * Generates a single-elimination tournament bracket.
 * @param {Array<string>} teams - List of team names participating in the playoffs.
 * @returns {Array<Array<string>>} Bracket rounds as an array of arrays.
 */
function generateTournamentBracket(teams) {
  // Validate input
  if (!Array.isArray(teams) || teams.length === 0) {
    throw new Error('Input must be a non-empty array of team names.');
  }

  // Add 'Bye' if the number of teams is odd
  if (teams.length % 2 !== 0) {
    teams.push('Bye');
  }

  const rounds = [];

  // Generate rounds until one team remains
  while (teams.length > 1) {
    const round = [];
    for (let i = 0; i < teams.length; i += 2) {
      const team1 = teams[i];
      const team2 = teams[i + 1];
      round.push(`${team1} vs ${team2}`);
    }
    rounds.push(round);

    // Advance winners (for simplicity, we assume the first team of each match advances)
    teams = teams.filter((team, index) => index % 2 === 0);
  }

  return rounds;
}

/**
 * Prints the tournament bracket rounds.
 * @param {Array<Array<string>>} bracket - Tournament rounds as an array of arrays.
 */
function printBracket(bracket) {
  console.log('Tournament Bracket:');
  bracket.forEach((round, index) => {
    console.log(`Round ${index + 1}:`);
    round.forEach(match => {
      console.log(`  ${match}`);
    });
  });
}

// Example usage
try {
  const teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'];
  const bracket = generateTournamentBracket(teams);
  printBracket(bracket);
} catch (error) {
  console.error('Error:', error.message);
}
```
