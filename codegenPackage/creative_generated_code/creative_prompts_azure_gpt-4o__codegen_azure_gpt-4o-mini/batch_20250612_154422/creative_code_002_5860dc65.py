"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Generate a PHP-based solution for a "三三制直销软件" (three-track direct selling system) that enables simple replication and fast network expansion, as described on JieyaSoft.
Generated: DETERMINISTIC_5860dc65310e2dc3
Batch ID: 20250612_154422
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
 * Three-Track Direct Selling System (三三制直销软件)
 * This PHP script provides a basic structure for a 3-track direct selling system,
 * allowing for simple replication and fast network expansion.
 */

class DirectSellingSystem {
    private $users = []; // Store registered users

    /**
     * Register a new user in the system
     *
     * @param string $name User's name
     * @return string Success or error message
     */
    public function registerUser($name) {
        if (empty($name)) {
            return "Error: User name cannot be empty.";
        }

        // Check if user already exists
        if (isset($this->users[$name])) {
            return "Error: User already exists.";
        }

        // Register the user
        $this->users[$name] = [
            'name' => $name,
            'referrals' => []
        ];

        return "Success: User {$name} registered successfully.";
    }

    /**
     * Add a referral for a user
     *
     * @param string $referrer Name of the referrer
     * @param string $referral Name of the referral
     * @return string Success or error message
     */
    public function addReferral($referrer, $referral) {
        if (!isset($this->users[$referrer])) {
            return "Error: Referrer does not exist.";
        }

        if (count($this->users[$referrer]['referrals']) >= 3) {
            return "Error: Cannot add more than 3 referrals.";
        }

        if (isset($this->users[$referral])) {
            return "Error: Referral user already exists.";
        }

        // Add referral
        $this->users[$referrer]['referrals'][] = $referral;
        $this->registerUser($referral); // Automatically register the referral

        return "Success: Referral {$referral} added under {$referrer}.";
    }

    /**
     * Display the user structure in a formatted way
     *
     * @return string Formatted user structure
     */
    public function displayUsers() {
        $output = "User Structure:\n";
        foreach ($this->users as $user) {
            $output .= "User: {$user['name']}\n";
            if (!empty($user['referrals'])) {
                $output .= "  Referrals: " . implode(', ', $user['referrals']) . "\n";
            } else {
                $output .= "  Referrals: None\n";
            }
        }
        return $output;
    }
}

// Example usage
$system = new DirectSellingSystem();

// Register users
echo $system->registerUser("Alice") . "\n";
echo $system->registerUser("Bob") . "\n";
echo $system->registerUser("Charlie") . "\n";

// Add referrals
echo $system->addReferral("Alice", "Bob") . "\n";
echo $system->addReferral("Alice", "Charlie") . "\n";
echo $system->addReferral("Alice", "David") . "\n"; // Trying to add a fourth referral

// Display user structure
echo $system->displayUsers();
?>
```
