"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: "Develop a code snippet in PHP to display business hours (e.g., Seg a Sex, das 07:30 às 17:30) in a user-friendly format on a website."
Generated: DETERMINISTIC_31aeab885b69d58d
Batch ID: 20250622_212822
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
 * Business Hours Display Class
 * Formats and displays business hours in a user-friendly way
 */
class BusinessHoursDisplay
{
    /**
     * @var array $hours Business hours configuration
     * Format: ['day' => ['open' => 'HH:MM', 'close' => 'HH:MM'], ...]
     */
    private $hours;

    /**
     * @var array $dayNames Translated day names
     */
    private $dayNames = [
        'Mon' => 'Seg',
        'Tue' => 'Ter',
        'Wed' => 'Qua',
        'Thu' => 'Qui',
        'Fri' => 'Sex',
        'Sat' => 'Sáb',
        'Sun' => 'Dom'
    ];

    /**
     * Constructor
     * @param array $hours Business hours configuration
     */
    public function __construct(array $hours)
    {
        $this->hours = $hours;
    }

    /**
     * Formats hours for display
     * @param string $open Opening time
     * @param string $close Closing time
     * @return string Formatted time range
     */
    private function formatTimeRange(string $open, string $close): string
    {
        return "das {$open} às {$close}";
    }

    /**
     * Groups consecutive days with same hours
     * @return array Grouped days with their hours
     */
    private function groupDays(): array
    {
        $grouped = [];
        $previous = null;
        $currentGroup = [];

        foreach ($this->hours as $day => $times) {
            $key = $times['open'] . '-' . $times['close'];
            
            if ($key === $previous) {
                $currentGroup[] = $day;
            } else {
                if (!empty($currentGroup)) {
                    $grouped[] = [
                        'days' => $currentGroup,
                        'times' => $this->hours[$currentGroup[0]]
                    ];
                }
                $currentGroup = [$day];
                $previous = $key;
            }
        }

        if (!empty($currentGroup)) {
            $grouped[] = [
                'days' => $currentGroup,
                'times' => $this->hours[$currentGroup[0]]
            ];
        }

        return $grouped;
    }

    /**
     * Formats day range string
     * @param array $days Array of days in the group
     * @return string Formatted day range
     */
    private function formatDayRange(array $days): string
    {
        if (count($days) === 1) {
            return $this->dayNames[$days[0]];
        }

        $firstDay = $this->dayNames[$days[0]];
        $lastDay = $this->dayNames[end($days)];

        return "{$firstDay} a {$lastDay}";
    }

    /**
     * Generates the formatted business hours display
     * @return string HTML formatted business hours
     */
    public function display(): string
    {
        try {
            $groupedDays = $this->groupDays();
            $output = '<ul class="business-hours">';

            foreach ($groupedDays as $group) {
                $dayRange = $this->formatDayRange($group['days']);
                $timeRange = $this->formatTimeRange(
                    $group['times']['open'],
                    $group['times']['close']
                );

                $output .= "<li>{$dayRange}, {$timeRange}</li>";
            }

            $output .= '</ul>';
            return $output;
        } catch (Exception $e) {
            error_log("Error displaying business hours: " . $e->getMessage());
            return '<p>Horário indisponível no momento.</p>';
        }
    }
}

// Example usage:
/*
$businessHours = [
    'Mon' => ['open' => '07:30', 'close' => '17:30'],
    'Tue' => ['open' => '07:30', 'close' => '17:30'],
    'Wed' => ['open' => '07:30', 'close' => '17:30'],
    'Thu' => ['open' => '07:30', 'close' => '17:30'],
    'Fri' => ['open' => '07:30', 'close' => '17:30'],
    'Sat' => ['open' => '09:00', 'close' => '13:00'],
    'Sun' => ['open' => '09:00', 'close' => '13:00']
];

$display = new BusinessHoursDisplay($businessHours);
echo $display->display();
*/
?>
```
