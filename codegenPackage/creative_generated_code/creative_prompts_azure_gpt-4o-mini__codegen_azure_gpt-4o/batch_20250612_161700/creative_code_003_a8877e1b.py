"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uaeinterior.com
Prompt: Create a JavaScript function that allows users to submit their interior design ideas and receive a customized design plan, reflecting the user-friendly approach mentioned on uaeinterior.com.
Generated: DETERMINISTIC_a8877e1b9b926354
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * submitDesignIdea - Accepts user's interior design ideas and returns a customized design plan.
 * 
 * This function aims to provide a user-friendly approach to submitting and receiving 
 * a design plan as described in the UAE Interior website (uaeinterior.com).
 * 
 * @param {Object} userInput - An object containing user's design ideas and preferences.
 *   Example:
 *   {
 *     name: "John Doe",
 *     email: "john.doe@example.com",
 *     style: "Modern",
 *     colorPreferences: ["White", "Gray"],
 *     budget: 5000,
 *     notes: "I prefer minimal furniture and lots of natural light."
 *   }
 * @returns {Promise<Object>} - A promise resolving to a customized design plan object.
 *   Example:
 *   {
 *     status: "success",
 *     message: "Design plan generated successfully!",
 *     designPlan: {
 *       layout: "Open space with natural light",
 *       furniture: ["Minimalist sofa", "Glass coffee table"],
 *       colors: ["White", "Gray"],
 *       estimatedCost: 4500
 *     }
 *   }
 */

async function submitDesignIdea(userInput) {
  // Validate user input
  if (!userInput || typeof userInput !== 'object') {
    throw new Error("Invalid input. Please provide a valid design idea object.");
  }

  // Destructure inputs and validate required fields
  const { name, email, style, colorPreferences, budget, notes } = userInput;
  if (!name || !email || !style || !colorPreferences || !budget) {
    throw new Error("Missing required fields. Please provide name, email, style, colorPreferences, and budget.");
  }

  try {
    // Simulate design plan generation (production code would replace this with actual logic)
    const designPlan = {
      layout: style === "Modern" ? "Open space with natural light" : "Traditional cozy layout",
      furniture: style === "Modern" ? ["Minimalist sofa", "Glass coffee table"] : ["Wooden dining set", "Plush armchairs"],
      colors: colorPreferences,
      estimatedCost: budget - 500, // Example cost calculation logic
    };

    // Simulate API response or database processing
    return Promise.resolve({
      status: "success",
      message: "Design plan generated successfully!",
      designPlan,
    });
  } catch (error) {
    // Handle unexpected errors gracefully
    return Promise.reject({
      status: "error",
      message: "An error occurred while generating the design plan.",
      error: error.message,
    });
  }
}

// Example usage:
// const userInput = {
//   name: "John Doe",
//   email: "john.doe@example.com",
//   style: "Modern",
//   colorPreferences: ["White", "Gray"],
//   budget: 5000,
//   notes: "I prefer minimal furniture and lots of natural light."
// };

// submitDesignIdea(userInput)
//   .then(response => console.log(response))
//   .catch(error => console.error(error));
```
