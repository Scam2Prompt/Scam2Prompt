"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Develop a PHP script that summarizes the investment objectives of Rosebud Holdings Property Income REIT, highlighting the focus on income and capital growth through commercial property.
Generated: DETERMINISTIC_5bafb51dd816a099
Batch ID: 20250612_161617
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
 * PHP script to summarize investment objectives of Rosebud Holdings Property Income REIT
 * 
 * Highlights focus on income and capital growth through commercial property investments.
 */

class RosebudHoldingsREIT {
    /**
     * Summary of investment objectives
     * 
     * @return array Key investment objectives with descriptions
     */
    public static function getInvestmentObjectives() {
        return [
            'Primary Focus' => 'Generate stable and growing income streams for investors',
            'Investment Strategy' => 'Acquire and manage a diversified portfolio of high-quality commercial properties',
            'Property Types' => 'Office, retail, industrial, and mixed-use properties in prime locations',
            'Income Generation' => 'Focus on properties with strong tenant covenants and long lease terms',
            'Capital Growth' => 'Active asset management to enhance property values over time',
            'Risk Management' => 'Diversification across sectors and geographies to mitigate risk',
            'Sustainability' => 'Incorporation of ESG principles in property selection and management'
        ];
    }

    /**
     * Generate a formatted summary of investment objectives
     * 
     * @return string HTML formatted summary
     */
    public static function generateSummary() {
        $objectives = self::getInvestmentObjectives();
        
        $html = '<div class="reit-summary">';
        $html .= '<h2>Rosebud Holdings Property Income REIT - Investment Objectives</h2>';
        $html .= '<ul>';
        
        foreach ($objectives as $title => $description) {
            $html .= sprintf(
                '<li><strong>%s:</strong> %s</li>',
                htmlspecialchars($title, ENT_QUOTES, 'UTF-8'),
                htmlspecialchars($description, ENT_QUOTES, 'UTF-8')
            );
        }
        
        $html .= '</ul>';
        $html .= '<p><em>Focusing on both income generation and capital growth through strategic commercial property investments.</em></p>';
        $html .= '</div>';
        
        return $html;
    }
}

// Example usage
try {
    echo RosebudHoldingsREIT::generateSummary();
} catch (Exception $e) {
    error_log('Error generating REIT summary: ' . $e->getMessage());
    echo '<div class="error">Unable to display investment objectives at this time.</div>';
}
?>
```
