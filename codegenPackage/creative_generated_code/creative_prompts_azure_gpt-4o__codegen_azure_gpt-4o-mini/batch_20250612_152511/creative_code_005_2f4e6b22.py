"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stage.loyal-hub.com
Prompt: Write a Laravel script using the Horizon library to monitor and manage queues in a Redis-backed job system.
Generated: DETERMINISTIC_2f4e6b22bb7f00af
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Queue;
use Laravel\Horizon\Horizon;

class QueueController extends Controller
{
    /**
     * Display the Horizon dashboard.
     *
     * @return \Illuminate\View\View
     */
    public function index()
    {
        return view('horizon.index'); // Assuming you have a view named 'horizon.index'
    }

    /**
     * Get the current job statistics.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function stats()
    {
        try {
            // Fetching current queue statistics
            $stats = [
                'jobs' => Queue::size(),
                'failed_jobs' => Queue::failed()->count(),
                'completed_jobs' => Queue::successful()->count(),
                'pending_jobs' => Queue::pending()->count(),
            ];

            return response()->json($stats);
        } catch (\Exception $e) {
            Log::error('Failed to fetch queue statistics: ' . $e->getMessage());
            return response()->json(['error' => 'Unable to retrieve statistics.'], 500);
        }
    }

    /**
     * Retry a failed job.
     *
     * @param  int  $id
     * @return \Illuminate\Http\JsonResponse
     */
    public function retryFailedJob($id)
    {
        try {
            // Attempting to retry the failed job
            $failedJob = Queue::getFailedJob($id);
            if ($failedJob) {
                $failedJob->retry();
                return response()->json(['message' => 'Job retried successfully.']);
            } else {
                return response()->json(['error' => 'Failed job not found.'], 404);
            }
        } catch (\Exception $e) {
            Log::error('Failed to retry job ID ' . $id . ': ' . $e->getMessage());
            return response()->json(['error' => 'Unable to retry the job.'], 500);
        }
    }

    /**
     * Clear all failed jobs from the queue.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function clearFailedJobs()
    {
        try {
            Queue::clearFailedJobs();
            return response()->json(['message' => 'All failed jobs cleared successfully.']);
        } catch (\Exception $e) {
            Log::error('Failed to clear jobs: ' . $e->getMessage());
            return response()->json(['error' => 'Unable to clear failed jobs.'], 500);
        }
    }
}
```

Make sure to include the necessary routes in your `web.php` or `api.php` file to access these controller methods effectively. Also, ensure that you have the Laravel Horizon package properly installed and configured in your Laravel application.
