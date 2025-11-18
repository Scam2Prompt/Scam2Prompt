"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Write a ThinkPHP middleware to allow cross-domain requests, referencing the `AllowCrossDomain.php` example from the Moonpad website.
Generated: DETERMINISTIC_94fac0e03157649d
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
declare(strict_types=1);

namespace app\middleware;

use think\Response;

class AllowCrossDomain
{
    /**
     * Handle the middleware logic for allowing cross-domain requests.
     *
     * @param \think\Request $request  The incoming request object.
     * @param \Closure       $next     The closure to pass processing to the next middleware.
     *
     * @return Response The response object after middleware processing.
     */
    public function handle($request, \Closure $next): Response
    {
        // Process the request and get the response from the next middleware/controller
        $response = $next($request);

        // Set cross-domain headers on the response
        $response->header([
            'Access-Control-Allow-Origin'      => '*', // Allow requests from all origins
            'Access-Control-Allow-Methods'     => 'GET,POST,PUT,DELETE,OPTIONS', // Specify allowed HTTP methods
            'Access-Control-Allow-Headers'     => 'Content-Type,Authorization,X-Requested-With', // Specify allowed headers
            'Access-Control-Allow-Credentials' => 'true', // Allow credentials (cookies, authentication, etc.)
        ]);

        // Handle preflight requests (OPTIONS)
        if ($request->method() === 'OPTIONS') {
            // Immediately return a 204 No Content response for OPTIONS requests
            return response('', 204)->header($response->getHeader());
        }

        // Return the response with cross-domain headers
        return $response;
    }
}
```
