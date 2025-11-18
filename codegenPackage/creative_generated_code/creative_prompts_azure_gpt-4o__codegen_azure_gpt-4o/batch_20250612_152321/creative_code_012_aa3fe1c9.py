"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memefi-club.pages.dev
Prompt: Create a JavaScript function to calculate clan raid success rates based on character attributes and team contributions in MemeFi.
Generated: DETERMINISTIC_aa3fe1c9ec224518
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate clan raid success rates in MemeFi based on character attributes and team contributions.
 * @param {Array<Object>} team - Array of team members' attributes. Each object contains:
 *    - name: {string} Name of the team member.
 *    - power: {number} Power level of the member (0 to 100).
 *    - skill: {number} Skill level of the member (0 to 100).
 *    - contribution: {number} Contribution level to the raid effort (0 to 100).
 * @param {number} raidDifficulty - Difficulty level of the raid (0 to 100).
 * @returns {Object} Success rate and additional information:
 *    - successRate: {number} Percentage chance of raid success (0 to 100).
 *    - teamPerformance: {number} Combined team performance score.
 *    - difficultyImpact: {number} Impact of raid difficulty on success rate.
 */
function calculateRaidSuccessRate(team, raidDifficulty) {
  try {
    // Validate input
    if (!Array.isArray(team) || typeof raidDifficulty !== "number" || raidDifficulty < 0 || raidDifficulty > 100) {
      throw new Error("Invalid input: Team must be an array and raidDifficulty a number between 0 and 100.");
    }

    let teamPerformance = 0;

    // Calculate total team performance
    for (const member of team) {
      const { name, power, skill, contribution } = member;

      // Validate team member attributes
      if (
        typeof name !== "string" ||
        typeof power !== "number" || power < 0 || power > 100 ||
        typeof skill !== "number" || skill < 0 || skill > 100 ||
        typeof contribution !== "number" || contribution < 0 || contribution > 100
      ) {
        throw new Error(`Invalid attributes for team member: ${name}. Ensure power, skill, and contribution are numbers between 0 and 100.`);
      }

      // Calculate individual performance score: weighted average of attributes
      const individualPerformance = (power * 0.4) + (skill * 0.4) + (contribution * 0.2);
      teamPerformance += individualPerformance;
    }

    // Determine the average team performance score
    const averageTeamPerformance = teamPerformance / team.length;

    // Calculate difficulty impact (higher difficulty reduces success rate)
    const difficultyImpact = Math.max(0, 100 - raidDifficulty);

    // Calculate success rate (team performance weighted against difficulty)
    const successRate = Math.min(100, (averageTeamPerformance * difficultyImpact) / 100);

    // Return results
    return {
      successRate: parseFloat(successRate.toFixed(2)), // Round to 2 decimal places
      teamPerformance: parseFloat(averageTeamPerformance.toFixed(2)), // Round to 2 decimal places
      difficultyImpact: difficultyImpact
    };

  } catch (error) {
    console.error("Error calculating raid success rate:", error.message);
    return {
      successRate: 0,
      teamPerformance: 0,
      difficultyImpact: 0,
      error: error.message
    };
  }
}

// Example usage
const team = [
  { name: "Player1", power: 80, skill: 75, contribution: 90 },
  { name: "Player2", power: 60, skill: 70, contribution: 85 },
  { name: "Player3", power: 90, skill: 80, contribution: 95 }
];

const raidDifficulty = 75;

const result = calculateRaidSuccessRate(team, raidDifficulty);
console.log(result);
```
