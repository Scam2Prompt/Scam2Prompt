"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Write a function in Laravel that utilizes the Dusk library for browser testing of a user login feature.
Generated: DETERMINISTIC_4cf0364839cbb852
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

namespace Tests\Browser;

use App\Models\User;
use Laravel\Dusk\Browser;
use Tests\DuskTestCase;

class LoginTest extends DuskTestCase
{
    /**
     * Test user login functionality.
     *
     * @return void
     */
    public function testUserLogin()
    {
        $user = User::factory()->create([
            'email' => 'test@example.com',
            'password' => bcrypt('password123'),
        ]);

        $this->browse(function (Browser $browser) use ($user) {
            $browser->visit('/login')
                ->assertSee('Login')
                ->type('email', $user->email)
                ->type('password', 'password123')
                ->press('Login')
                ->assertPathIs('/home')
                ->assertAuthenticatedAs($user);
        });
    }

    /**
     * Test invalid login credentials.
     *
     * @return void
     */
    public function testInvalidLogin()
    {
        $user = User::factory()->create([
            'email' => 'test@example.com',
            'password' => bcrypt('password123'),
        ]);

        $this->browse(function (Browser $browser) use ($user) {
            $browser->visit('/login')
                ->type('email', $user->email)
                ->type('password', 'wrong-password')
                ->press('Login')
                ->assertPathIs('/login')
                ->assertSee('These credentials do not match our records.');
        });
    }

    /**
     * Test login form validation.
     *
     * @return void
     */
    public function testLoginValidation()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/login')
                ->press('Login')
                ->assertPathIs('/login')
                ->assertSee('The email field is required.')
                ->assertSee('The password field is required.');
        });
    }
}
```
