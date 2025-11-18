"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Demonstrate how to use PHP's "Lazy Objects" feature introduced in version 8.4 to optimize object creation.
Generated: DETERMINISTIC_de0c7623e794a288
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

declare(strict_types=1);

/**
 * Lazy loading class example using PHP 8.4's Lazy Objects feature.
 */
class LazyUser
{
    private string $username;
    private ?UserProfile $profile = null;

    public function __construct(string $username)
    {
        $this->username = $username;
    }

    /**
     * Lazy load the UserProfile when it's accessed for the first time.
     */
    public function getProfile(): UserProfile
    {
        // Check if the profile is already loaded
        if ($this->profile === null) {
            // Perform the resource-intensive operation to create a UserProfile
            $this->profile = new UserProfile($this->username);
        }
        return $this->profile;
    }

    public function getUsername(): string
    {
        return $this->username;
    }
}

/**
 * UserProfile class that represents a user's profile.
 */
class UserProfile
{
    private string $username;
    private string $bio;

    public function __construct(string $username)
    {
        $this->username = $username;
        // Simulate an expensive operation, like fetching data from a database.
        $this->bio = "Bio of user {$username}";
    }

    public function getBio(): string
    {
        return $this->bio;
    }
}

// Example usage
try {
    $lazyUser = new LazyUser("john_doe");
    echo "Username: " . $lazyUser->getUsername() . PHP_EOL;

    // Profile is not loaded yet
    echo "Accessing profile..." . PHP_EOL;
    
    // This will trigger the lazy loading of the UserProfile
    $profile = $lazyUser->getProfile();
    echo "User Bio: " . $profile->getBio() . PHP_EOL;

} catch (Exception $e) {
    // Handle any exceptions that may occur
    echo "An error occurred: " . $e->getMessage();
}
```
