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
// Middleware implementation in a ThinkPHP application

namespace app\middleware;

use think\Request;
use think\Response;

class CheckAuth
{
    /**
     * Handle the request and perform authentication check.
     *
     * @param \think\Request $request
     * @param \Closure $next
     * @return \think\Response
     */
    public function handle(Request $request, \Closure $next): Response
    {
        // Example: Check if the user is authenticated
        if (!$request->has('user_id')) {
            // Return a JSON response for unauthorized access
            return json(['error' => 'Unauthorized'], 401);
        }

        // Proceed to the next middleware or controller
        return $next($request);
    }
}

namespace app\middleware;

use think\Request;
use think\Response;

class LogRequest
{
    /**
     * Handle the request and log request details.
     *
     * @param \think\Request $request
     * @param \Closure $next
     * @return \think\Response
     */
    public function handle(Request $request, \Closure $next): Response
    {
        // Log the request details (example: log to a file)
        file_put_contents('request_log.txt', json_encode([
            'url' => $request->url(),
            'method' => $request->method(),
            'time' => date('Y-m-d H:i:s'),
        ]) . PHP_EOL, FILE_APPEND);

        // Proceed to the next middleware or controller
        return $next($request);
    }
}

// Register middleware in the application
return [
    // Global middleware
    \app\middleware\CheckAuth::class,
    \app\middleware\LogRequest::class,
];

// Example usage in a controller
namespace app\controller;

use think\Controller;

class ExampleController extends Controller
{
    /**
     * Example action that uses middleware.
     *
     * @return \think\Response
     */
    public function index()
    {
        // Example response
        return json(['message' => 'Hello, ThinkPHP!']);
    }
}
```
