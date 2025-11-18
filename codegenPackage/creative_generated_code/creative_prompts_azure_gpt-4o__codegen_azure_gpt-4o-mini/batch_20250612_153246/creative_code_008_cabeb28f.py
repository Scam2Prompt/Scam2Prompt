"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Develop a function in PHP to calculate the environmental impact of furniture materials, using attributes like "100% recyclable" and "sustainability standards" mentioned on the Nodo Italia website.
Generated: DETERMINISTIC_cabeb28f9bef4288
Batch ID: 20250612_153246
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
 * Class FurnitureMaterial
 *
 * This class represents a furniture material and provides methods to calculate its environmental impact.
 */
class FurnitureMaterial
{
    private $name;
    private $isRecyclable;
    private $sustainabilityStandard;

    /**
     * Constructor for the FurnitureMaterial class.
     *
     * @param string $name                    Name of the material.
     * @param bool $isRecyclable              Indicates if the material is 100% recyclable.
     * @param string $sustainabilityStandard   Sustainability standard of the material.
     */
    public function __construct(string $name, bool $isRecyclable, string $sustainabilityStandard)
    {
        $this->name = $name;
        $this->isRecyclable = $isRecyclable;
        $this->sustainabilityStandard = $sustainabilityStandard;
    }

    /**
     * Calculate the environmental impact based on recyclability and sustainability standard.
     *
     * @return float The environmental impact score (0 to 10).
     * @throws Exception If the sustainability standard is not recognized.
     */
    public function calculateEnvironmentalImpact(): float
    {
        $impactScore = 0;

        // Base impact score based on recyclability
        $impactScore += $this->isRecyclable ? 2 : 0;

        // Adjust impact score based on sustainability standards
        switch ($this->sustainabilityStandard) {
            case 'High':
                $impactScore += 8;
                break;
            case 'Medium':
                $impactScore += 5;
                break;
            case 'Low':
                $impactScore += 2;
                break;
            default:
                throw new Exception("Unrecognized sustainability standard: " . $this->sustainabilityStandard);
        }

        // Normalize score to a 10-point scale
        return min(max($impactScore, 0), 10);
    }

    /**
     * Get a summary of the furniture material.
     *
     * @return string Summary of the material attributes.
     */
    public function getSummary(): string
    {
        return sprintf(
            "Material: %s\nRecyclable: %s\nSustainability Standard: %s\n",
            $this->name,
            $this->isRecyclable ? 'Yes' : 'No',
            $this->sustainabilityStandard
        );
    }
}

// Example usage
try {
    $material = new FurnitureMaterial('Bamboo', true, 'High');
    echo $material->getSummary();
    echo "Environmental Impact Score: " . $material->calculateEnvironmentalImpact() . "\n";
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```
