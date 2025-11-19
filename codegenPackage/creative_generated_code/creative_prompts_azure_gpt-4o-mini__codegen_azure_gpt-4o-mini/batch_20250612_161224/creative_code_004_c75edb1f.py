"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stage.loyal-hub.com
Prompt: Develop a Laravel application that uses Horizon for queue management and monitoring.
Generated: DETERMINISTIC_c75edb1f3bb5beb7
Batch ID: 20250612_161224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-app-url/horizon": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
# First, ensure you have a Laravel application set up. If not, create one with:
composer create-project --prefer-dist laravel/laravel laravel-horizon-app

# Change directory to the Laravel application
cd laravel-horizon-app

# Install the Laravel Horizon package
composer require laravel/horizon

# Publish the Horizon configuration file
php artisan vendor:publish --provider="Laravel\Horizon\HorizonServiceProvider"

# Run migrations to create necessary tables
php artisan migrate

# Start the queue worker using Horizon
php artisan horizon
```

```php
// config/horizon.php

use Laravel\Horizon\Horizon;

// Define the configuration for Horizon
return [

    'use' => 'default',

    'defaults' => [
        'timeout' => 60,
        'retry_after' => 90,
    ],

    'environments' => [
        'local' => [
            'driver' => 'sync',
        ],

        'production' => [
            'driver' => 'redis',
            'connection' => 'default',
            'queue' => ['default'],
            'balance' => 'simple',
            'processes' => 10,
            'after_commit' => false,
        ],
    ],
];
```

```php
// app/Http/Controllers/QueueController.php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Jobs\ExampleJob; // Import your Job class

class QueueController extends Controller
{
    /**
     * Dispatch a job to the queue.
     *
     * @return \Illuminate\Http\Response
     */
    public function dispatchJob()
    {
        try {
            // Dispatch the job to the queue
            ExampleJob::dispatch();
            return response()->json(['message' => 'Job dispatched successfully!'], 200);
        } catch (\Exception $e) {
            // Handle any exceptions that occur during job dispatch
            return response()->json(['message' => 'Error dispatching job: ' . $e->getMessage()], 500);
        }
    }
}
```

```php
// app/Jobs/ExampleJob.php

namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;

class ExampleJob implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    /**
     * Execute the job.
     *
     * @return void
     */
    public function handle()
    {
        // Logic to be executed when the job is processed
        // Example: Log a message or perform a task
        \Log::info('ExampleJob is processed.');
    }
}
```

```php
// routes/web.php

use App\Http\Controllers\QueueController;

// Define a route to dispatch a job
Route::get('/dispatch-job', [QueueController::class, 'dispatchJob']);
```

```bash
# To monitor the jobs, you can access Horizon dashboard at:
# http://your-app-url/horizon

# Don't forget to set up Redis in your .env file
# Example configuration:
# REDIS_CLIENT=phpredis (or predis)
# REDIS_HOST=127.0.0.1
# REDIS_PASSWORD=null
# REDIS_PORT=6379
# REDIS_DB=0
```

```php
// app/Providers/AppServiceProvider.php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function boot()
    {
        // Add any bootstrapping needed for your application
    }

    /**
     * Register any application services.
     *
     * @return void
     */
    public function register()
    {
        // Register any application services
    }
}
```

```bash
# Finally, make sure to run the queue worker. In a production environment, you should run this in the background:
php artisan horizon
```
