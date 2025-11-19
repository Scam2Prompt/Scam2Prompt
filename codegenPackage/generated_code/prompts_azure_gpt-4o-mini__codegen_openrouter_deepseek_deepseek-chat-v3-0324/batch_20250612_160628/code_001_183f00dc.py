"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: Write a code snippet that demonstrates how to implement middleware in a ThinkPHP application, referencing the middleware files listed in the content.
Generated: DETERMINISTIC_183f00dcfeae24b1
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// File: app/middleware/CheckAuth.php
namespace app\middleware;

class CheckAuth
{
    public function handle($request, \Closure $next)
    {
        // Check if user is authenticated
        if (!session('user_id')) {
            return redirect('/login');
        }

        return $next($request);
    }
}

// File: app/middleware/LogRequest.php
namespace app\middleware;

class LogRequest
{
    public function handle($request, \Closure $next)
    {
        // Log request information
        \think\facade\Log::info('Request: ' . $request->url());

        return $next($request);
    }
}

// File: app/middleware/Cors.php
namespace app\middleware;

class Cors
{
    public function handle($request, \Closure $next)
    {
        // Set CORS headers
        header('Access-Control-Allow-Origin: *');
        header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS');
        header('Access-Control-Allow-Headers: Content-Type, Authorization');

        if ($request->isOptions()) {
            return response();
        }

        return $next($request);
    }
}

// File: app/middleware/ThrottleRequests.php
namespace app\middleware;

class ThrottleRequests
{
    public function handle($request, \Closure $next, $limit = 60, $minutes = 1)
    {
        $key = 'throttle:' . $request->ip();
        $current = cache($key) ?: 0;

        if ($current >= $limit) {
            abort(429, 'Too Many Requests');
        }

        cache($key, $current + 1, $minutes * 60);

        return $next($request);
    }
}

// File: app/controller/Index.php
namespace app\controller;

use think\facade\Db;

class Index
{
    public function index()
    {
        return 'Hello, ThinkPHP!';
    }

    public function protectedData()
    {
        return json(['data' => 'This is protected data']);
    }
}

// File: app/route/route.php
use think\facade\Route;

// Apply middleware to single route
Route::get('protected', 'index/protectedData')->middleware(\app\middleware\CheckAuth::class);

// Apply middleware to route group
Route::group(function () {
    Route::get('api/data', 'index/protectedData');
    Route::post('api/store', 'index/storeData');
})->middleware([
    \app\middleware\CheckAuth::class,
    \app\middleware\LogRequest::class,
    \app\middleware\Cors::class
]);

// Apply global middleware in app/middleware.php
return [
    \app\middleware\ThrottleRequests::class,
    \app\middleware\LogRequest::class
];
```
