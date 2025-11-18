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
// AllowCrossDomain.php

namespace app\middleware;

use think\facade\Request;
use think\Response;

class AllowCrossDomain
{
    /**
     * Handle an incoming request.
     *
     * @param  \think\Request  $request
     * @param  \Closure  $next
     * @return \think\Response
     */
    public function handle(Request $request, \Closure $next)
    {
        // Set CORS headers
        $response = $next($request);

        // Allow all domains (for development only, restrict in production)
        $response->header([
            'Access-Control-Allow-Origin' => '*',
            'Access-Control-Allow-Methods' => 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers' => 'X-Requested-With, Content-Type, Authorization',
            'Access-Control-Max-Age' => '86400',
        ]);

        // Handle preflight request
        if ($request->isOptions()) {
            return $response;
        }

        return $response;
    }
}
```

```php
// In your application middleware configuration

return [
    // Other middleware
    \app\middleware\AllowCrossDomain::class,
];
```

```php
// If you want to handle errors specifically for CORS

namespace app\middleware;

use think\exception\HttpException;

class AllowCrossDomain
{
    // ... (rest of the code)

    public function handle(Request $request, \Closure $next)
    {
        try {
            // Set CORS headers
            $response = $next($request);
            // CORS settings...
            return $response;
        } catch (HttpException $e) {
            // Log error (optional)
            // \think\facade\Log::error($e->getMessage());

            // Return a JSON response for error handling
            return json(['error' => 'Internal Server Error'], 500);
        }
    }
}
```

This code defines a middleware class `AllowCrossDomain` for handling CORS in a ThinkPHP application. It includes comments to describe the purpose of each section, and it handles errors gracefully.
