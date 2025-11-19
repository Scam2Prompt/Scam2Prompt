"""
Generated Code Metadata:
========================
Original URL: https://stage.loyal-hub.com
Prompt: Create a Laravel application using the Dusk library to automate browser testing. Include examples of writing and executing test cases.
Generated: DETERMINISTIC_3a7358a0e88eb790
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Laravel Dusk Browser Testing Example**
=====================================================

**Step 1: Install Laravel and Dusk**

First, create a new Laravel project and install Dusk:

```bash
composer create-project --prefer-dist laravel/laravel dusk-example
cd dusk-example
composer require --dev laravel/dusk
php artisan dusk:install
```

**Step 2: Configure Dusk**

Publish the Dusk configuration:

```bash
php artisan vendor:publish --provider="Laravel\Dusk\DuskServiceProvider"
```

**Step 3: Write Test Cases**

Create a new test case in `tests/Browser/ExampleTest.php`:

```php
// tests/Browser/ExampleTest.php

namespace Tests\Browser;

use Tests\DuskTestCase;
use Laravel\Dusk\Browser;
use Illuminate\Foundation\Testing\DatabaseMigrations;

class ExampleTest extends DuskTestCase
{
    /**
     * A basic browser test example.
     *
     * @return void
     */
    public function testBasicExample()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/')
                    ->assertTitle('Dusk Example')
                    ->assertSee('Laravel');
        });
    }

    /**
     * Test login functionality.
     *
     * @return void
     */
    public function testLogin()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/login')
                    ->type('email', 'example@example.com')
                    ->type('password', 'password')
                    ->press('Login')
                    ->assertPathIs('/home');
        });
    }

    /**
     * Test form submission.
     *
     * @return void
     */
    public function testFormSubmission()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/form')
                    ->type('name', 'John Doe')
                    ->type('email', 'john@example.com')
                    ->press('Submit')
                    ->assertSee('Form submitted successfully');
        });
    }
}
```

**Step 4: Create Test Routes and Views**

Create routes in `routes/web.php`:

```php
// routes/web.php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/login', function () {
    return view('login');
});

Route::get('/home', function () {
    return view('home');
});

Route::get('/form', function () {
    return view('form');
});
```

Create views in `resources/views/`:

```php
<!-- resources/views/welcome.blade.php -->

<h1>Dusk Example</h1>

<p>Welcome to Laravel!</p>
```

```php
<!-- resources/views/login.blade.php -->

<h1>Login</h1>

<form>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Login">
</form>
```

```php
<!-- resources/views/home.blade.php -->

<h1>Home</h1>

<p>Welcome to your dashboard!</p>
```

```php
<!-- resources/views/form.blade.php -->

<h1>Form</h1>

<form>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <input type="submit" value="Submit">
</form>
```

**Step 5: Run Test Cases**

Run the test cases using the following command:

```bash
php artisan dusk
```

You can also run a specific test case:

```bash
php artisan dusk --class=ExampleTest
```
