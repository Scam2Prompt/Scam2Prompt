"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Create a JavaScript function that retrieves and displays property evaluation results based on the criteria outlined in the content of the website.
Generated: DETERMINISTIC_5e202512076c54dc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Retrieves and displays property evaluation results based on specified criteria.
 * @param {string} apiEndpoint - The URL of the API endpoint to fetch evaluation data.
 * @param {Object} criteria - The evaluation criteria (e.g., { location: string, priceRange: [number, number] }).
 * @param {HTMLElement} displayElement - The DOM element where results will be displayed.
 * @returns {Promise<void>} - A promise that resolves when the operation is complete.
 */
async function displayPropertyEvaluations(apiEndpoint, criteria, displayElement) {
    try {
        // Validate input parameters
        if (!apiEndpoint || typeof apiEndpoint !== 'string') {
            throw new Error('Invalid API endpoint provided');
        }
        if (!criteria || typeof criteria !== 'object') {
            throw new Error('Invalid criteria provided');
        }
        if (!displayElement || !(displayElement instanceof HTMLElement)) {
            throw new Error('Invalid display element provided');
        }

        // Construct query parameters from criteria
        const queryParams = new URLSearchParams();
        for (const [key, value] of Object.entries(criteria)) {
            if (Array.isArray(value)) {
                queryParams.append(key, value.join(','));
            } else {
                queryParams.append(key, value);
            }
        }

        // Fetch evaluation results from API
        const response = await fetch(`${apiEndpoint}?${queryParams.toString()}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const evaluations = await response.json();

        // Clear previous results
        displayElement.innerHTML = '';

        // Display results
        if (evaluations.length === 0) {
            displayElement.innerHTML = '<p>No properties match the specified criteria.</p>';
            return;
        }

        const resultsContainer = document.createElement('div');
        resultsContainer.className = 'property-evaluations';

        evaluations.forEach(evaluation => {
            const propertyElement = document.createElement('div');
            propertyElement.className = 'property-evaluation';
            
            propertyElement.innerHTML = `
                <h3>${evaluation.propertyName || 'Unnamed Property'}</h3>
                <p>Location: ${evaluation.location || 'N/A'}</p>
                <p>Price: ${evaluation.price ? `$${evaluation.price.toLocaleString()}` : 'N/A'}</p>
                <p>Rating: ${evaluation.rating ? `${evaluation.rating}/10` : 'N/A'}</p>
                <p>Evaluation: ${evaluation.evaluation || 'No evaluation available'}</p>
                <hr>
            `;
            
            resultsContainer.appendChild(propertyElement);
        });

        displayElement.appendChild(resultsContainer);

    } catch (error) {
        console.error('Error fetching property evaluations:', error);
        displayElement.innerHTML = `<p class="error">Error loading property evaluations: ${error.message}</p>`;
    }
}
```
