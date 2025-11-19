"""
Generated Code Metadata:
========================
Original URL: https://hypersteakin.site
Prompt: Create a JavaScript function that simulates a tournament bracket for indie games, inspired by the Hyper Swap tournament featured at the HyperSteakin Gaming Summit.
Generated: DETERMINISTIC_53b0c6bc5e61d66a
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a game participant.
 */
class Participant {
  /**
   * Creates a new participant.
   * @param {string} name - The participant's name.
   */
  constructor(name) {
    this.name = name;
  }
}

/**
 * Represents a game match.
 */
class Match {
  /**
   * Creates a new match.
   * @param {Participant} participant1 - The first participant.
   * @param {Participant} participant2 - The second participant.
   */
  constructor(participant1, participant2) {
    this.participant1 = participant1;
    this.participant2 = participant2;
    this.winner = null;
  }

  /**
   * Sets the match winner.
   * @param {Participant} winner - The winning participant.
   */
  setWinner(winner) {
    if (winner !== this.participant1 && winner !== this.participant2) {
      throw new Error('Invalid winner');
    }
    this.winner = winner;
  }
}

/**
 * Simulates a tournament bracket.
 */
class TournamentBracket {
  /**
   * Creates a new tournament bracket.
   * @param {Participant[]} participants - The tournament participants.
   */
  constructor(participants) {
    if (participants.length % 2 !== 0) {
      throw new Error('Number of participants must be even');
    }
    this.participants = participants;
    this.matches = [];
    this.createMatches();
  }

  /**
   * Creates the initial matches.
   */
  createMatches() {
    for (let i = 0; i < this.participants.length; i += 2) {
      const match = new Match(this.participants[i], this.participants[i + 1]);
      this.matches.push(match);
    }
  }

  /**
   * Simulates a round of matches.
   * @param {number} roundNumber - The current round number.
   * @returns {Match[]} The matches for the next round.
   */
  simulateRound(roundNumber) {
    if (this.matches.length === 1) {
      throw new Error('Tournament is already over');
    }
    const winners = [];
    for (const match of this.matches) {
      // Simulate a match (for simplicity, assume participant1 wins)
      match.setWinner(match.participant1);
      console.log(`Round ${roundNumber}: ${match.participant1.name} beats ${match.participant2.name}`);
      winners.push(match.winner);
    }
    this.matches = [];
    for (let i = 0; i < winners.length; i += 2) {
      if (i + 1 < winners.length) {
        const match = new Match(winners[i], winners[i + 1]);
        this.matches.push(match);
      } else {
        // If there's an odd number of winners, give a bye to the last one
        console.log(`Round ${roundNumber}: ${winners[i].name} gets a bye`);
      }
    }
    return this.matches;
  }

  /**
   * Simulates the entire tournament.
   */
  simulateTournament() {
    let roundNumber = 1;
    while (this.matches.length > 1) {
      this.simulateRound(roundNumber);
      roundNumber++;
    }
    console.log(`Tournament winner: ${this.matches[0].winner.name}`);
  }
}

// Example usage:
function main() {
  const participants = [
    new Participant('John'),
    new Participant('Alice'),
    new Participant('Bob'),
    new Participant('Charlie'),
    new Participant('David'),
    new Participant('Eve'),
    new Participant('Frank'),
    new Participant('George'),
  ];
  const tournament = new TournamentBracket(participants);
  tournament.simulateTournament();
}

main();
```
