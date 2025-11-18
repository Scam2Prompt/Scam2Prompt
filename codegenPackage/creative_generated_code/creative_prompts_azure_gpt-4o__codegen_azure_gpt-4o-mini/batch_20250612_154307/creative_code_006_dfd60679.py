"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptocity.fun
Prompt: Generate a Laravel script to manage background jobs using Horizon. Include code for setting up a Redis queue and monitoring job execution.
Generated: DETERMINISTIC_dfd60679a64389b1
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\JobController;
use Illuminate\Support\Facades\Artisan;

// Define the routes for managing background jobs
Route::middleware('web')->group(function () {
    // Route to display the job form
    Route::get('/jobs', [JobController::class, 'index'])->name('jobs.index');

    // Route to create a new job
    Route::post('/jobs', [JobController::class, 'store'])->name('jobs.store');
});

// Artisan command to set up Redis queue
Artisan::command('horizon:install', function () {
    // Publish Horizon assets
    Artisan::call('vendor:publish', ['--provider' => 'Laravel\Horizon\HorizonServiceProvider']);
    $this->info('Horizon assets published successfully.');
})->describe('Install Horizon');

// JobController to manage background jobs
namespace App\Http\Controllers;

use App\Jobs\ExampleJob;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class JobController extends Controller
{
    /**
     * Display the job management page.
     *
     * @return \Illuminate\View\View
     */
    public function index()
    {
        return view('jobs.index');
    }

    /**
     * Store a new job in the queue.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function store(Request $request)
    {
        // Validate the request data
        $request->validate([
            'data' => 'required|string|max:255',
        ]);

        try {
            // Dispatch a new job to the queue
            ExampleJob::dispatch($request->input('data'));

            // Log job dispatch success
            Log::info('Job dispatched successfully', ['data' => $request->input('data')]);
            return redirect()->back()->with('success', 'Job has been dispatched successfully!');
        } catch (\Exception $e) {
            // Log any errors that occur during job dispatch
            Log::error('Error dispatching job: ' . $e->getMessage());
            return redirect()->back()->with('error', 'Failed to dispatch the job.');
        }
    }
}

// Create a job class for background processing
namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;
use Illuminate\Support\Facades\Log;

class ExampleJob implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    protected $data;

    /**
     * Create a new job instance.
     *
     * @param  string  $data
     * @return void
     */
    public function __construct($data)
    {
        $this->data = $data;
    }

    /**
     * Execute the job.
     *
     * @return void
     */
    public function handle()
    {
        // Perform the task with the job data
        Log::info('Processing job with data: ' . $this->data);
        
        // Simulate a long-running task
        sleep(5);

        // Log completion of the job
        Log::info('Job completed successfully with data: ' . $this->data);
    }
}

// Configuration for Redis queue (config/queue.php)
'connections' => [
    'redis' => [
        'driver' => 'redis',
        'connection' => 'default',
        'queue' => 'default',
        'retry_after' => 90,
        'block_for' => null,
    ],
],

// Setting up Redis in .env
REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

// Ensure Laravel Horizon is running in the background
// Run the following command to start Horizon
// php artisan horizon
```
