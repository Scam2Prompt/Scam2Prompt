"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stage.loyal-hub.com
Prompt: Develop a Laravel application that uses Horizon for queue management and monitoring.
Generated: DETERMINISTIC_c75edb1f3bb5beb7
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for setting up a Laravel application with Horizon for queue management and monitoring:

### Installation

Run the following commands to install Laravel and Horizon:

```bash
composer create-project laravel/laravel horizon-app
cd horizon-app
composer require laravel/horizon
```

---

### `config/app.php`

Ensure the `providers` array includes Horizon service provider:

```php
'providers' => [
    // Other providers...
    Laravel\Horizon\HorizonServiceProvider::class,
],
```

---

### `config/horizon.php`

(Optional) Customize Horizon configuration if needed:

```php
return [
    'use' => 'default',
    'prefix' => 'horizon',
    'middleware' => ['web'],
];
```

---

### Register Horizon routes in `routes/web.php`

```php
use Illuminate\Support\Facades\Route;

// Horizon Dashboard Routes
Route::middleware(['auth'])->group(function () {
    // Horizon dashboard will be accessible only to authenticated users
    Route::get('/horizon', function () {
        return redirect('/horizon');
    });
});
```

---

### `app/Console/Kernel.php`

Ensure Horizon listens to the queues properly:

```php
protected function schedule(Schedule $schedule)
{
    // Schedule Horizon to monitor queues
    $schedule->command('horizon:snapshot')->everyFiveMinutes();
}
``
