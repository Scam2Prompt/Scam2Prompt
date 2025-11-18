"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager-bz23c2f5n-bootnode.vercel.app
Prompt: Provide code in TypeScript to validate user inputs for creating a funding round in Gitcoin's Round Manager, ensuring proper formatting for dates and round names.
Generated: DETERMINISTIC_3e913ac5dfdbf30d
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// TypeScript Code to Validate User Inputs for Creating a Funding Round in Gitcoin's Round Manager

// Define a type for user inputs
type FundingRoundInput = {
  roundName: string; // Name of the funding round
  startDate: string; // Start date in ISO format (e.g., "2023-10-01")
  endDate: string;   // End date in ISO format (e.g., "2023-10-31")
};

/**
 * Validates the format of a funding round's inputs.
 * @param inputs - The user inputs to validate.
 * @returns A boolean indicating whether the inputs are valid and an array of error messages, if any.
 */
function validateFundingRound(inputs: FundingRoundInput): { isValid: boolean; errors: string[] } {
  const errors: string[] = [];

  // Validate round name: must not be empty and can only contain alphanumeric and spaces
  const roundNamePattern = /^[a-zA-Z0-9 ]+$/;
  if (!inputs.roundName) {
    errors.push("Round name is required.");
  } else if (!roundNamePattern.test(inputs.roundName)) {
    errors.push("Round name must only contain alphanumeric characters and spaces.");
  }

  // Validate dates: must be in ISO format and properly ordered
  const isoDatePattern = /^\d{4}-\d{2}-\d{2}$/;
  if (!inputs.startDate) {
    errors.push("Start date is required.");
  } else if (!isoDatePattern.test(inputs.startDate)) {
    errors.push("Start date must be in ISO format (YYYY-MM-DD).");
  }

  if (!inputs.endDate) {
    errors.push("End date is required.");
  } else if (!isoDatePattern.test(inputs.endDate)) {
    errors.push("End date must be in ISO format (YYYY-MM-DD).");
  }

  if (inputs.startDate && inputs.endDate) {
    const startDate = new Date(inputs.startDate);
    const endDate = new Date(inputs.endDate);

    if (isNaN(startDate.getTime())) {
      errors.push("Start date is not a valid date.");
    }

    if (isNaN(endDate.getTime())) {
      errors.push("End date is not a valid date.");
    }

    if (!isNaN(startDate.getTime()) && !isNaN(endDate.getTime()) && startDate > endDate) {
      errors.push("Start date must be earlier than or equal to end date.");
    }
  }

  return {
    isValid: errors.length === 0,
    errors,
  };
}

// Example usage:
const userInput: FundingRoundInput = {
  roundName: "Gitcoin Round 2023",
  startDate: "2023-10-01",
  endDate: "2023-10-31",
};

const validationResult = validateFundingRound(userInput);

if (validationResult.isValid) {
  console.log("Input is valid.");
} else {
  console.error("Input validation failed with errors:", validationResult.errors);
}
```
