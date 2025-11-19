"""
Generated Code Metadata:
========================
Original URL: https://haynatural.oil.ph
Prompt: Generate a list of 10 different use cases for Hay Natural Oil, including code snippets in PHP that demonstrate how to integrate this information into a web application.
Generated: DETERMINISTIC_061649180f4fee71
Batch ID: 20250622_210703
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
 * Hay Natural Oil Use Cases Web Application Integration
 * 
 * This file demonstrates 10 different use cases for Hay Natural Oil
 * and shows how to integrate them into a web application.
 */

class HayNaturalOilUseCases {
    /**
     * Get all use cases with descriptions
     * 
     * @return array Array of use cases with details
     */
    public static function getAllUseCases() {
        return [
            [
                'id' => 1,
                'title' => 'Skin Moisturizer',
                'description' => 'Hay Natural Oil can be used as a natural moisturizer for dry skin.',
                'instructions' => 'Apply a few drops to clean skin and massage gently.'
            ],
            [
                'id' => 2,
                'title' => 'Hair Conditioner',
                'description' => 'Deep conditions hair and adds shine.',
                'instructions' => 'Apply to damp hair, leave for 30 minutes, then rinse.'
            ],
            [
                'id' => 3,
                'title' => 'Massage Oil',
                'description' => 'Perfect for aromatherapy and relaxation massages.',
                'instructions' => 'Warm slightly before application for better absorption.'
            ],
            [
                'id' => 4,
                'title' => 'Cuticle Treatment',
                'description' => 'Nourishes dry cuticles and promotes healthy nail growth.',
                'instructions' => 'Apply directly to cuticles before bedtime.'
            ],
            [
                'id' => 5,
                'title' => 'Lip Balm',
                'description' => 'Natural alternative to commercial lip balms.',
                'instructions' => 'Apply a small amount to lips as needed.'
            ],
            [
                'id' => 6,
                'title' => 'After-Sun Care',
                'description' => 'Soothes sunburned skin and helps restore moisture.',
                'instructions' => 'Apply gently to affected areas after sun exposure.'
            ],
            [
                'id' => 7,
                'title' => 'Makeup Remover',
                'description' => 'Effectively removes makeup while nourishing skin.',
                'instructions' => 'Apply to cotton pad and wipe gently over face.'
            ],
            [
                'id' => 8,
                'title' => 'Bath Oil',
                'description' => 'Adds moisture to skin during bathing.',
                'instructions' => 'Add 5-10 drops to warm bath water.'
            ],
            [
                'id' => 9,
                'title' => 'Aromatherapy',
                'description' => 'Can be used in diffusers for relaxation.',
                'instructions' => 'Add 3-5 drops to your diffuser with water.'
            ],
            [
                'id' => 10,
                'title' => 'Scar Treatment',
                'description' => 'Helps reduce appearance of scars over time.',
                'instructions' => 'Massage into scar area twice daily.'
            ]
        ];
    }

    /**
     * Get a specific use case by ID
     * 
     * @param int $id Use case ID
     * @return array|null Returns the use case or null if not found
     */
    public static function getUseCaseById($id) {
        $useCases = self::getAllUseCases();
        foreach ($useCases as $case) {
            if ($case['id'] == $id) {
                return $case;
            }
        }
        return null;
    }

    /**
     * Display use cases in HTML format
     * 
     * @return string HTML formatted list of use cases
     */
    public static function displayUseCases() {
        $useCases = self::getAllUseCases();
        $html = '<div class="use-cases-container">';
        $html .= '<h2>Hay Natural Oil Use Cases</h2>';
        $html .= '<ul class="use-cases-list">';
        
        foreach ($useCases as $case) {
            $html .= sprintf(
                '<li class="use-case-item">
                    <h3>%s</h3>
                    <p><strong>Description:</strong> %s</p>
                    <p><strong>Instructions:</strong> %s</p>
                </li>',
                htmlspecialchars($case['title']),
                htmlspecialchars($case['description']),
                htmlspecialchars($case['instructions'])
            );
        }
        
        $html .= '</ul>';
        $html .= '</div>';
        
        return $html;
    }

    /**
     * Get use cases as JSON
     * 
     * @return string JSON encoded use cases
     */
    public static function getUseCasesJson() {
        return json_encode(self::getAllUseCases(), JSON_PRETTY_PRINT);
    }
}

// Example usage in a web application:

// Display all use cases
echo HayNaturalOilUseCases::displayUseCases();

// Get specific use case
/*
$useCase = HayNaturalOilUseCases::getUseCaseById(3);
if ($useCase) {
    echo "<h2>{$useCase['title']}</h2>";
    echo "<p>{$useCase['description']}</p>";
    echo "<p><strong>Instructions:</strong> {$useCase['instructions']}</p>";
} else {
    echo "<p>Use case not found.</p>";
}
*/

// Get JSON data for API response
/*
header('Content-Type: application/json');
echo HayNaturalOilUseCases::getUseCasesJson();
*/
?>
```
