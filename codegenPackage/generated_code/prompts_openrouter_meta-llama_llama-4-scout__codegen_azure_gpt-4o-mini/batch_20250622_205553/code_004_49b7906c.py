"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: "Create a ThinkPHP middleware that handles cross-domain requests and provides a JSON response."
Generated: DETERMINISTIC_49b7906c4f0767ea
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
namespace app\middleware;

use think\facade\Response;
use think\facade\Request;

class CorsMiddleware
{
    /**
     * Handle cross-domain requests.
     *
     * @param \Closure $next The next middleware or request handler.
     * @return mixed The response from the next middleware or request handler.
     */
    public function handle($request, \Closure $next)
    {
        // Allow cross-origin requests
        header('Access-Control-Allow-Origin: *'); // Change '*' to specific domains in production
        header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS');
        header('Access-Control-Allow-Headers: Content-Type, Authorization');

        // Handle preflight requests
        if ($request->isOptions()) {
            return Response::create('', 'json', 200);
        }

        // Proceed to the next middleware or request handler
        try {
            $response = $next($request);
        } catch (\Exception $e) {
            // Log the error and return a JSON response
            // You can use a logging mechanism here
            return Response::create([
                'status' => 'error',
                'message' => 'An error occurred: ' . $e->getMessage()
            ], 'json', 500);
        }

        // Return the response
        return $response;
    }
}
```
