"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Using the information from SMKN 1 Kadipaten's website, write a script in PHP to automate the generation of student exam schedules based on predefined tokens and dates.
Generated: DETERMINISTIC_9de3ce55725970e0
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Student Exam Schedule Generator for SMKN 1 Kadipaten
 * 
 * This script automates the generation of student exam schedules based on predefined tokens and dates.
 * It reads input data, processes it, and outputs a structured exam schedule.
 */

class ExamScheduleGenerator {
    private $tokens;
    private $dates;
    private $schedule;

    /**
     * Constructor
     * 
     * @param array $tokens Predefined tokens for exam types
     * @param array $dates  Predefined exam dates
     */
    public function __construct(array $tokens, array $dates) {
        $this->tokens = $tokens;
        $this->dates = $dates;
        $this->schedule = [];
    }

    /**
     * Validate input data
     * 
     * @param array $data Input data to validate
     * @throws InvalidArgumentException If data is invalid
     */
    private function validateInput(array $data) {
        if (empty($data)) {
            throw new InvalidArgumentException("Input data cannot be empty");
        }

        foreach ($data as $item) {
            if (!isset($item['class']) || !isset($item['subject']) || !isset($item['token'])) {
                throw new InvalidArgumentException("Missing required fields in input data");
            }

            if (!in_array($item['token'], $this->tokens)) {
                throw new InvalidArgumentException("Invalid token: " . $item['token']);
            }
        }
    }

    /**
     * Generate schedule based on input data
     * 
     * @param array $data Input data containing class, subject, and token
     * @return array Generated schedule
     */
    public function generate(array $data) {
        try {
            $this->validateInput($data);
            
            foreach ($data as $item) {
                $tokenIndex = array_search($item['token'], $this->tokens);
                if ($tokenIndex !== false && isset($this->dates[$tokenIndex])) {
                    $this->schedule[] = [
                        'class' => $item['class'],
                        'subject' => $item['subject'],
                        'date' => $this->dates[$tokenIndex],
                        'token' => $item['token']
                    ];
                }
            }

            return $this->schedule;
        } catch (Exception $e) {
            error_log("Error generating schedule: " . $e->getMessage());
            return [];
        }
    }

    /**
     * Output schedule in HTML format
     * 
     * @return string HTML formatted schedule
     */
    public function toHTML() {
        if (empty($this->schedule)) {
            return '<p>No schedule data available</p>';
        }

        $html = '<table border="1" cellpadding="8" cellspacing="0" style="width:100%; border-collapse:collapse;">';
        $html .= '<thead><tr><th>Class</th><th>Subject</th><th>Date</th><th>Exam Type</th></tr></thead>';
        $html .= '<tbody>';

        foreach ($this->schedule as $item) {
            $html .= sprintf(
                '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>',
                htmlspecialchars($item['class']),
                htmlspecialchars($item['subject']),
                htmlspecialchars($item['date']),
                htmlspecialchars($item['token'])
            );
        }

        $html .= '</tbody></table>';
        return $html;
    }
}

// Example usage:
try {
    // Predefined tokens and dates (should be configured based on SMKN 1 Kadipaten's requirements)
    $tokens = ['UTS', 'UAS', 'UKK'];
    $dates = ['2023-10-15', '2023-12-10', '2024-03-05'];

    // Sample input data (should be replaced with actual data from the website)
    $inputData = [
        ['class' => 'X TKJ 1', 'subject' => 'Matematika', 'token' => 'UTS'],
        ['class' => 'X TKJ 2', 'subject' => 'Bahasa Inggris', 'token' => 'UAS'],
        ['class' => 'XI MM 1', 'subject' => 'Pemrograman Web', 'token' => 'UKK'],
    ];

    $generator = new ExamScheduleGenerator($tokens, $dates);
    $schedule = $generator->generate($inputData);

    // Output the schedule
    header('Content-Type: text/html; charset=utf-8');
    echo $generator->toHTML();

} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    echo "An error occurred while generating the schedule. Please try again later.";
}
?>
```
