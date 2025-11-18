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
// Import necessary types and modules
import { isDate, parseISO } from 'date-fns';

// Define an interface for the funding round input
interface FundingRoundInput {
    roundName: string;
    startDate: string;
    endDate: string;
}

// Create a class to handle funding round validation
class FundingRoundValidator {
    // Method to validate the funding round input
    public validate(input: FundingRoundInput): void {
        this.validateRoundName(input.roundName);
        this.validateDates(input.startDate, input.endDate);
    }

    // Private method to validate round name
    private validateRoundName(roundName: string): void {
        const minLength = 3;
        const maxLength = 50;

        if (typeof roundName !== 'string' || roundName.trim().length < minLength || roundName.trim().length > maxLength) {
            throw new Error(`Invalid round name. It must be a string between ${minLength} and ${maxLength} characters.`);
        }
    }

    // Private method to validate start and end dates
    private validateDates(startDateString: string, endDateString: string): void {
        const startDate = this.parseDate(startDateString);
        const endDate = this.parseDate(endDateString);

        if (!startDate || !endDate) {
            throw new Error('Invalid date format. Dates must be in ISO format (YYYY-MM-DD).');
        }

        if (startDate >= endDate) {
            throw new Error('Start date must be earlier than end date.');
        }
    }

    // Private method to parse date and check its validity
    private parseDate(dateString: string): Date | null {
        const parsedDate = parseISO(dateString);

        return isDate(parsedDate) && !isNaN(parsedDate.getTime()) ? parsedDate : null;
    }
}

// Example usage
try {
    const fundingRound: FundingRoundInput = {
        roundName: 'Q2 2023 Funding Round',
        startDate: '2023-04-01',
        endDate: '2023-06-30'
    };

    const validator = new FundingRoundValidator();
    validator.validate(fundingRound);
    console.log('Funding round input is valid.');
} catch (error) {
    console.error('Validation error:', error.message);
}
```
