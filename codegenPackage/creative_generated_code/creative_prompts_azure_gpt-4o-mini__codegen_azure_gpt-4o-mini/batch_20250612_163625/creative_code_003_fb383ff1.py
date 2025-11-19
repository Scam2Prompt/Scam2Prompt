"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Develop a function in PHP that displays occasions based on a given date, utilizing the method shared on Omidtak's site.
Generated: DETERMINISTIC_fb383ff10e11d6fd
Batch ID: 20250612_163625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Class OccasionManager
 * This class is responsible for managing and displaying occasions based on a given date.
 */
class OccasionManager
{
    /**
     * Displays occasions for the given date.
     *
     * @param string $date The date in 'Y-m-d' format.
     * @throws InvalidArgumentException If the date format is invalid.
     */
    public function displayOccasions($date)
    {
        // Validate the date format
        if (!$this->isValidDate($date)) {
            throw new InvalidArgumentException("Invalid date format. Please use 'Y-m-d' format.");
        }

        // Fetch occasions based on the date
        $occasions = $this->getOccasionsByDate($date);

        // Display the occasions
        if (empty($occasions)) {
            echo "No occasions found for the date: $date\n";
        } else {
            foreach ($occasions as $occasion) {
                echo "Occasion: $occasion on Date: $date\n";
            }
        }
    }

    /**
     * Checks if the provided date is in valid 'Y-m-d' format.
     *
     * @param string $date The date to validate.
     * @return bool True if the date is valid, false otherwise.
     */
    private function isValidDate($date)
    {
        $d = DateTime::createFromFormat('Y-m-d', $date);
        return $d && $d->format('Y-m-d') === $date;
    }

    /**
     * Gets occasions based on the provided date.
     * This method simulates fetching occasions from a data source.
     *
     * @param string $date The date to retrieve occasions for.
     * @return array An array of occasions for the specified date.
     */
    private function getOccasionsByDate($date)
    {
        // Simulated data source (could be a database or an API)
        $occasionData = [
            '2023-10-31' => ['Halloween'],
            '2023-12-25' => ['Christmas'],
            '2023-01-01' => ['New Year\'s Day'],
        ];

        return $occasionData[$date] ?? [];
    }
}

// Example usage
try {
    $occasionManager = new OccasionManager();
    $occasionManager->displayOccasions('2023-10-31'); // Replace with the desired date
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    echo "An unexpected error occurred: " . $e->getMessage() . "\n";
}
?>
```
