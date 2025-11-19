"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Write a JavaScript function that tracks the progress of athletes in a mentorship program, incorporating elements of discipline and character building as emphasized by Team DGA.
Generated: DETERMINISTIC_1d33ec80196c5997
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Class representing an athlete in the mentorship program.
 */
class Athlete {
    constructor(name, discipline, character) {
        this.name = name; // Name of the athlete
        this.discipline = discipline; // Discipline level (1-10)
        this.character = character; // Character level (1-10)
        this.progress = []; // Array to track progress over time
    }

    /**
     * Updates the athlete's discipline and character levels.
     * @param {number} discipline - New discipline level (1-10).
     * @param {number} character - New character level (1-10).
     */
    updateProgress(discipline, character) {
        if (this.validateLevel(discipline) && this.validateLevel(character)) {
            this.discipline = discipline;
            this.character = character;
            this.progress.push({ discipline, character, date: new Date() });
        } else {
            throw new Error('Discipline and character levels must be between 1 and 10.');
        }
    }

    /**
     * Validates the level input.
     * @param {number} level - The level to validate.
     * @returns {boolean} - True if valid, false otherwise.
     */
    validateLevel(level) {
        return Number.isInteger(level) && level >= 1 && level <= 10;
    }

    /**
     * Retrieves the athlete's progress history.
     * @returns {Array} - Array of progress records.
     */
    getProgressHistory() {
        return this.progress;
    }
}

/**
 * Class representing the mentorship program.
 */
class MentorshipProgram {
    constructor() {
        this.athletes = []; // Array to hold athletes in the program
    }

    /**
     * Adds a new athlete to the program.
     * @param {string} name - Name of the athlete.
     * @param {number} discipline - Initial discipline level (1-10).
     * @param {number} character - Initial character level (1-10).
     */
    addAthlete(name, discipline, character) {
        const newAthlete = new Athlete(name, discipline, character);
        this.athletes.push(newAthlete);
    }

    /**
     * Updates an athlete's progress based on their name.
     * @param {string} name - Name of the athlete.
     * @param {number} discipline - New discipline level (1-10).
     * @param {number} character - New character level (1-10).
     */
    updateAthleteProgress(name, discipline, character) {
        const athlete = this.athletes.find(a => a.name === name);
        if (athlete) {
            athlete.updateProgress(discipline, character);
        } else {
            throw new Error(`Athlete with name ${name} not found.`);
        }
    }

    /**
     * Retrieves the progress history of an athlete.
     * @param {string} name - Name of the athlete.
     * @returns {Array} - Array of progress records.
     */
    getAthleteProgressHistory(name) {
        const athlete = this.athletes.find(a => a.name === name);
        if (athlete) {
            return athlete.getProgressHistory();
        } else {
            throw new Error(`Athlete with name ${name} not found.`);
        }
    }
}

// Example usage:
try {
    const program = new MentorshipProgram();
    program.addAthlete('John Doe', 7, 8);
    program.updateAthleteProgress('John Doe', 8, 9);
    console.log(program.getAthleteProgressHistory('John Doe'));
} catch (error) {
    console.error(error.message);
}
```
