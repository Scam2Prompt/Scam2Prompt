"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonaeac.com
Prompt: Write a function in JavaScript to dynamically display membership levels and their corresponding earning percentages (e.g., 1% for Premium Member, 1.2% for Professional Member) as described on bonaeac.com.
Generated: DETERMINISTIC_34fcff5b46ecd3ad
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A function to display membership levels and their corresponding earning percentages.
 * The function creates a dynamic HTML structure to present the data.
 * 
 * @param {Array} membershipData - An array of objects, where each object contains 
 *                                  the membership level and its earning percentage.
 */
function displayMembershipLevels(membershipData) {
    // Validate input: Check if membershipData is an array
    if (!Array.isArray(membershipData)) {
        console.error('Invalid input: membershipData should be an array.');
        return;
    }

    // Create a container for the membership levels
    const container = document.createElement('div');
    container.className = 'membership-levels';

    // Iterate over the membership data to create HTML elements
    membershipData.forEach(member => {
        // Validate each member object
        if (typeof member.level !== 'string' || typeof member.earningPercentage !== 'number') {
            console.error('Invalid membership data: Each member should have a level (string) and earningPercentage (number).');
            return;
        }

        // Create a div for each membership level
        const memberDiv = document.createElement('div');
        memberDiv.className = 'membership-level';

        // Create a paragraph for the membership level
        const levelParagraph = document.createElement('p');
        levelParagraph.textContent = `Membership Level: ${member.level}`;

        // Create a paragraph for the earning percentage
        const earningParagraph = document.createElement('p');
        earningParagraph.textContent = `Earning Percentage: ${member.earningPercentage}%`;

        // Append the paragraphs to the member div
        memberDiv.appendChild(levelParagraph);
        memberDiv.appendChild(earningParagraph);

        // Append the member div to the container
        container.appendChild(memberDiv);
    });

    // Append the container to the body or a specific element in the DOM
    document.body.appendChild(container);
}

// Sample membership data
const membershipLevels = [
    { level: 'Premium Member', earningPercentage: 1.0 },
    { level: 'Professional Member', earningPercentage: 1.2 }
];

// Call the function to display membership levels
displayMembershipLevels(membershipLevels);
```
