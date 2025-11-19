"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Write a code snippet that demonstrates how to implement middleware in a ThinkPHP application, referencing the middleware files listed in the content.
Generated: DETERMINISTIC_183f00dcfeae24b1
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Middleware class for logging requests
namespace app\middleware;

use think\Request;
use think\Response;

class LogRequest
{
    /**
     * Handle incoming requests and log necessary information.
     *
     * @param Request $request The current HTTP request instance
     * @param \Closure $next The next middleware/handler in the stack
     * @return Response The response from the next middleware/handler
     */
    public function handle(Request $request, \Closure $next)
    {
        // Log request details (method and URL)
        error_log('Request Method: ' . $request->method());
        error_log('Request URL: ' . $request->url());

        // Proceed to the next middleware/handler
        return $next($request);
    }
}

// Middleware class for authentication
namespace app\middleware;

use think\Request;
use think\Response;

class AuthMiddleware
{
    /**
     * Handle incoming requests and perform authentication checks.
     *
     * @param Request $request The current HTTP request instance
     * @param \Closure $next The next middleware/handler in the stack
     * @return Response The response from the next middleware/handler
     */
    public function handle(Request $request, \Closure $next)
    {
        // Check for user authentication (this is a simplistic example)
        if (!$request->session('user_id')) {
            return response('Unauthorized', 401);
        }

        // Proceed to the next middleware/handler
        return $next($request);
    }
}

// Registering the middleware in the application
namespace app\http;

use think\middleware\LoadLangpack;
use think\middleware\CheckRoute;
use think\middleware\SessionInit;

return [
    // Global Middleware
    'global' => [
        LoadLangpack::class,
        SessionInit::class,
        \app\middleware\LogRequest::class,
        \app\middleware\AuthMiddleware::class,
    ],

    // Middleware for specific routes
    'route' => [
        'admin/*' => [
            \app\middleware\AuthMiddleware::class,
        ],
    ],
];
```
