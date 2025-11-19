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
 * Tracks the progress of athletes in a mentorship program with a focus on discipline and character building.
 * @class AthleteProgressTracker
 */
class AthleteProgressTracker {
    /**
     * Creates an instance of AthleteProgressTracker.
     * @param {string} programName - The name of the mentorship program.
     */
    constructor(programName) {
        this.programName = programName;
        this.athletes = new Map(); // Stores athlete data with ID as key
        this.metrics = {
            discipline: ['Attendance', 'Punctuality', 'Effort'],
            character: ['Respect', 'Teamwork', 'Leadership']
        };
    }

    /**
     * Adds a new athlete to the tracker.
     * @param {string} athleteId - Unique identifier for the athlete.
     * @param {string} name - Full name of the athlete.
     * @param {string} mentorId - ID of the assigned mentor.
     * @throws {Error} If athlete already exists.
     */
    addAthlete(athleteId, name, mentorId) {
        if (this.athletes.has(athleteId)) {
            throw new Error(`Athlete with ID ${athleteId} already exists.`);
        }

        this.athletes.set(athleteId, {
            name,
            mentorId,
            progress: {
                discipline: this._initializeMetrics('discipline'),
                character: this._initializeMetrics('character'),
                notes: []
            }
        });
    }

    /**
     * Initializes metric scores to 0.
     * @private
     * @param {string} category - 'discipline' or 'character'.
     * @returns {Object} Initialized metrics object.
     */
    _initializeMetrics(category) {
        return this.metrics[category].reduce((acc, metric) => {
            acc[metric] = 0;
            return acc;
        }, {});
    }

    /**
     * Updates an athlete's progress metrics.
     * @param {string} athleteId - ID of the athlete.
     * @param {string} category - 'discipline' or 'character'.
     * @param {string} metric - Specific metric to update.
     * @param {number} score - New score (0-100).
     * @throws {Error} If athlete doesn't exist or invalid parameters.
     */
    updateMetric(athleteId, category, metric, score) {
        if (!this.athletes.has(athleteId)) {
            throw new Error(`Athlete with ID ${athleteId} not found.`);
        }

        if (!this.metrics[category] || !this.metrics[category].includes(metric)) {
            throw new Error(`Invalid category or metric: ${category}/${metric}`);
        }

        if (score < 0 || score > 100) {
            throw new Error('Score must be between 0 and 100.');
        }

        const athlete = this.athletes.get(athleteId);
        athlete.progress[category][metric] = score;
    }

    /**
     * Adds a progress note for an athlete.
     * @param {string} athleteId - ID of the athlete.
     * @param {string} note - Progress note content.
     * @param {string} author - Author of the note (mentor ID or name).
     * @throws {Error} If athlete doesn't exist.
     */
    addProgressNote(athleteId, note, author) {
        if (!this.athletes.has(athleteId)) {
            throw new Error(`Athlete with ID ${athleteId} not found.`);
        }

        const athlete = this.athletes.get(athleteId);
        athlete.progress.notes.push({
            date: new Date().toISOString(),
            author,
            note
        });
    }

    /**
     * Gets an athlete's progress report.
     * @param {string} athleteId - ID of the athlete.
     * @returns {Object} Progress report including metrics and notes.
     * @throws {Error} If athlete doesn't exist.
     */
    getProgressReport(athleteId) {
        if (!this.athletes.has(athleteId)) {
            throw new Error(`Athlete with ID ${athleteId} not found.`);
        }

        const athlete = this.athletes.get(athleteId);
        return {
            name: athlete.name,
            mentorId: athlete.mentorId,
            progress: JSON.parse(JSON.stringify(athlete.progress)) // Deep copy
        };
    }

    /**
     * Calculates overall progress score for an athlete.
     * @param {string} athleteId - ID of the athlete.
     * @returns {number} Average score across all metrics (0-100).
     * @throws {Error} If athlete doesn't exist.
     */
    calculateOverallProgress(athleteId) {
        if (!this.athletes.has(athleteId)) {
            throw new Error(`Athlete with ID ${athleteId} not found.`);
        }

        const athlete = this.athletes.get(athleteId);
        const disciplineScores = Object.values(athlete.progress.discipline);
        const characterScores = Object.values(athlete.progress.character);
        const allScores = [...disciplineScores, ...characterScores];

        if (allScores.length === 0) return 0;

        const sum = allScores.reduce((total, score) => total + score, 0);
        return Math.round(sum / allScores.length);
    }
}

// Example usage:
// const tracker = new AthleteProgressTracker('Team DGA Mentorship');
// tracker.addAthlete('ath1', 'John Doe', 'mentor1');
// tracker.updateMetric('ath1', 'discipline', 'Attendance', 85);
// tracker.addProgressNote('ath1', 'Showing great improvement in teamwork', 'mentor1');
// console.log(tracker.getProgressReport('ath1'));
// console.log('Overall progress:', tracker.calculateOverallProgress('ath1'));
```
