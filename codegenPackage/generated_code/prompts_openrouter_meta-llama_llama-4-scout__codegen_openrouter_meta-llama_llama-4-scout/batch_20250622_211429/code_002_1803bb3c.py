"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-52--gracious-swanson-bcc8c1.netlify.app
Prompt: Recommend a tech stack for a Melbourne-based front-end engineer working on a new project, considering React and VueJS.
Generated: DETERMINISTIC_1803bb3cca416c01
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// tech-stack-recommender.js

/**
 * Recommends a tech stack for a front-end engineer project.
 * 
 * @param {string} projectType - Type of project (e.g., web application, mobile application).
 * @param {string} engineerLocation - Location of the engineer (e.g., Melbourne).
 * @param {string[]} preferredFrameworks - List of preferred frameworks (e.g., React, VueJS).
 * @returns {object} Recommended tech stack.
 */
function recommendTechStack(projectType, engineerLocation, preferredFrameworks) {
    try {
        // Define a map of project types to recommended tech stacks
        const projectTypeStacks = {
            'web application': {
                'React': ['Create React App', 'Webpack', 'Babel', 'ESLint'],
                'VueJS': ['Vue CLI', 'Webpack', 'Babel', 'ESLint']
            },
            'mobile application': {
                'React': ['React Native', 'Expo', 'Jest'],
                'VueJS': ['NativeScript-Vue', 'Vue CLI', 'Jest']
            }
        };

        // Define a map of engineer locations to recommended deployment platforms
        const locationPlatforms = {
            'Melbourne': 'AWS'
        };

        // Validate input parameters
        if (!projectType || !engineerLocation || !preferredFrameworks) {
            throw new Error('Invalid input parameters');
        }

        // Filter preferred frameworks based on project type
        const filteredFrameworks = preferredFrameworks.filter(framework => 
            projectTypeStacks[projectType] && projectTypeStacks[projectType][framework]
        );

        // If no frameworks match the project type, throw an error
        if (filteredFrameworks.length === 0) {
            throw new Error(`No matching frameworks found for project type: ${projectType}`);
        }

        // Recommend a tech stack for each filtered framework
        const recommendedStacks = filteredFrameworks.map(framework => ({
            framework,
            buildTool: projectTypeStacks[projectType][framework][0],
            bundler: projectTypeStacks[projectType][framework][1],
            transpiler: projectTypeStacks[projectType][framework][2],
            linter: projectTypeStacks[projectType][framework][3],
            deploymentPlatform: locationPlatforms[engineerLocation]
        }));

        return recommendedStacks;
    } catch (error) {
        console.error(error.message);
        return [];
    }
}

// Example usage
const projectType = 'web application';
const engineerLocation = 'Melbourne';
const preferredFrameworks = ['React', 'VueJS'];

const recommendedStacks = recommendTechStack(projectType, engineerLocation, preferredFrameworks);
console.log(recommendedStacks);
```
