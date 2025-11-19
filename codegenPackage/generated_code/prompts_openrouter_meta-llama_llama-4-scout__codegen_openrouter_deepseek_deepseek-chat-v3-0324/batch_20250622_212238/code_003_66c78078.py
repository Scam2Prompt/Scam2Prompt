"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Develop a simple grading system in JavaScript that assigns grades based on marks, with categories similar to the Fiji Mathematics Competition (Prize, Distinction, Credit, Pass, Participation).
Generated: DETERMINISTIC_66c780784b52f193
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple grading system based on marks with categories similar to Fiji Mathematics Competition.
 * Categories: Prize, Distinction, Credit, Pass, Participation.
 */

class GradingSystem {
    /**
     * Initialize grading system with custom thresholds
     * @param {Object} thresholds - Grade thresholds (defaults to FMC standard)
     */
    constructor(thresholds = {
        prize: 90,
        distinction: 75,
        credit: 60,
        pass: 40
    }) {
        this.thresholds = thresholds;
        this.validateThresholds();
    }

    /**
     * Validate that thresholds are in correct order and values
     * @throws {Error} If thresholds are invalid
     */
    validateThresholds() {
        const { prize, distinction, credit, pass } = this.thresholds;
        
        if (prize <= distinction || distinction <= credit || credit <= pass) {
            throw new Error('Invalid thresholds: must be prize > distinction > credit > pass');
        }
        
        if (pass < 0 || prize > 100) {
            throw new Error('Thresholds must be between 0 and 100');
        }
    }

    /**
     * Determine grade based on marks
     * @param {number} marks - Student's marks (0-100)
     * @returns {string} Grade category
     * @throws {Error} If marks are invalid
     */
    getGrade(marks) {
        if (typeof marks !== 'number' || isNaN(marks)) {
            throw new Error('Marks must be a number');
        }
        
        if (marks < 0 || marks > 100) {
            throw new Error('Marks must be between 0 and 100');
        }

        const { prize, distinction, credit, pass } = this.thresholds;

        if (marks >= prize) {
            return 'Prize';
        } else if (marks >= distinction) {
            return 'Distinction';
        } else if (marks >= credit) {
            return 'Credit';
        } else if (marks >= pass) {
            return 'Pass';
        } else {
            return 'Participation';
        }
    }

    /**
     * Get all grades with their thresholds
     * @returns {Object} Grade thresholds mapping
     */
    getGradeThresholds() {
        return {
            Prize: `>= ${this.thresholds.prize}`,
            Distinction: `${this.thresholds.distinction}-${this.thresholds.prize - 1}`,
            Credit: `${this.thresholds.credit}-${this.thresholds.distinction - 1}`,
            Pass: `${this.thresholds.pass}-${this.thresholds.credit - 1}`,
            Participation: `< ${this.thresholds.pass}`
        };
    }
}

// Example usage:
// const fmcGrading = new GradingSystem();
// console.log(fmcGrading.getGrade(85)); // "Distinction"
// console.log(fmcGrading.getGradeThresholds());
```
