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
// Middleware implementation in a ThinkPHP application

namespace app\middleware;

use think\Request;
use think\Response;

class CheckAuth
{
    /**
     * Handle the incoming request and check for authentication.
     *
     * @param Request  $request
     * @param \Closure $next
     * @return mixed
     */
    public function handle(Request $request, \Closure $next)
    {
        // Example authentication check
        if (!$request->header('Authorization')) {
            // Return an error response if Authorization header is missing
            return response(['error' => 'Unauthorized'], 401);
        }
        
        // Proceed to the next middleware or controller
        return $next($request);
    }
}

// Another middleware example: LogRequest
namespace app\middleware;

use think\Request;

class LogRequest
{
    /**
     * Log request details before processing.
     *
     * @param Request  $request
     * @param \Closure $next
     * @return mixed
     */
    public function handle(Request $request, \Closure $next)
    {
        // Log request information (Example: log to a file)
        file_put_contents('request.log', json_encode([
            'url' => $request->url(),
            'method' => $request->method(),
            'time' => date('Y-m-d H:i:s')
        ]) . PHP_EOL, FILE_APPEND);
        
        // Proceed to the next middleware or controller
        return $next($request);
    }
}

// Middleware registration in app\middleware.php
return [
    // Register the middlewares
    \app\middleware\CheckAuth::class,
    \app\middleware\LogRequest::class,
];

// Controller example: Applying middleware
namespace app\controller;

use think\Controller;

class User extends Controller
{
    protected $middleware = [
        \app\middleware\CheckAuth::class,
        \app\middleware\LogRequest::class,
    ];

    /**
     * Example action method.
     *
     * @return \think\Response
     */
    public function index()
    {
        return response(['message' => 'Welcome to the user index page'], 200);
    }
}
```
