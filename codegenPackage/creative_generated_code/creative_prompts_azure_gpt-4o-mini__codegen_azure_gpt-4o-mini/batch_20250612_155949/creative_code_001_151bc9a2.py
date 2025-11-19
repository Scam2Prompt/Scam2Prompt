"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megami.live
Prompt: Write a JavaScript function that allows users to filter Japanese martial arts films by combat style or storyline on a streaming site similar to MEGAMI.
Generated: DETERMINISTIC_151bc9a227e80de7
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of Japanese martial arts films based on combat style or storyline.
 * 
 * @param {Array} films - An array of film objects to be filtered. Each film object should contain:
 *   - {string} title - The title of the film.
 *   - {string} combatStyle - The combat style featured in the film (e.g. "Judo", "Karate").
 *   - {string} storyline - A brief description of the film's storyline.
 * @param {Object} filterCriteria - An object containing the criteria for filtering.
 *   - {string} [combatStyle] - The combat style to filter by (optional).
 *   - {string} [storyline] - A keyword to filter by in the storyline (optional).
 * @returns {Array} - A new array containing the filtered films.
 * 
 * @throws {Error} Throws an error if the films array is not provided or is not an array.
 */
function filterMartialArtsFilms(films, filterCriteria) {
    // Validate input
    if (!Array.isArray(films)) {
        throw new Error('The first argument must be an array of films.');
    }

    if (typeof filterCriteria !== 'object') {
        throw new Error('The second argument must be an object containing filter criteria.');
    }

    // Destructure filter criteria for easier reference
    const { combatStyle, storyline } = filterCriteria;

    // Filter films based on provided criteria
    return films.filter(film => {
        const matchesCombatStyle = combatStyle ? film.combatStyle === combatStyle : true;
        const matchesStoryline = storyline ? film.storyline.includes(storyline) : true;
        return matchesCombatStyle && matchesStoryline;
    });
}

// Example usage
const films = [
    { title: 'The Last Samurai', combatStyle: 'Kendo', storyline: 'A former American soldier embraces the Samurai culture.' },
    { title: 'Ip Man', combatStyle: 'Wing Chun', storyline: 'The life of the martial arts master who taught Bruce Lee.' },
    { title: 'Orochi', combatStyle: 'Kendo', storyline: 'A woman seeks vengeance for her father’s death.' },
    { title: 'Rashomon', combatStyle: 'N/A', storyline: 'Multiple perspectives on a violent crime.' },
];

const filterCriteria = {
    combatStyle: 'Kendo',
    storyline: 'vengeance'
};

try {
    const filteredFilms = filterMartialArtsFilms(films, filterCriteria);
    console.log(filteredFilms);
} catch (error) {
    console.error('Error filtering films:', error.message);
}
```
