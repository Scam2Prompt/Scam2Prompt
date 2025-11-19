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
// MiddlewareExample.php

namespace app\middleware;

use think\facade\Request;
use think\facade\Response;

class MiddlewareExample
{
    /**
     * Handle the incoming request.
     *
     * @param \think\Request $request The incoming request instance.
     * @param \Closure $next The next middleware or request handler.
     * @return mixed The response from the next middleware or request handler.
     */
    public function handle($request, \Closure $next)
    {
        // Log the request information
        \think\facade\Log::info('Request URL: ' . $request->url());
        
        // Check for a specific condition (e.g., authentication)
        if (!$this->isAuthenticated($request)) {
            // Return a 403 Forbidden response if not authenticated
            return Response::create('Forbidden', 'html', 403);
        }

        // Proceed to the next middleware or request handler
        return $next($request);
    }

    /**
     * Check if the user is authenticated.
     *
     * @param \think\Request $request The incoming request instance.
     * @return bool True if authenticated, false otherwise.
     */
    protected function isAuthenticated($request)
    {
        // Example logic for checking authentication
        // This should be replaced with actual authentication logic
        return $request->session()->has('user_id');
    }
}
```

```php
// app.php (or your main application file)

use think\facade\Route;

// Register middleware globally
app()->middleware([
    \app\middleware\MiddlewareExample::class,
]);

// Define a sample route
Route::get('example', function () {
    return 'This is an example route.';
});
```

```php
// config/middleware.php

return [
    // Global middleware
    \app\middleware\MiddlewareExample::class,
];
```

```php
// .env (for environment configuration)

# Set the environment to production
APP_ENV=production
``` 

This code snippet demonstrates how to implement middleware in a ThinkPHP application, including proper error handling and logging.
