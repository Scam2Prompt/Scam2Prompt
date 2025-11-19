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
// File: app/middleware/AuthMiddleware.php

namespace app\middleware;

use think\Request;
use think\Response;

/**
 * Authentication Middleware
 */
class AuthMiddleware
{
    /**
     * @param Request $request
     * @param \Closure $next
     * @return Response
     */
    public function handle(Request $request, \Closure $next)
    {
        // Authentication logic here
        // For demonstration purposes, assume authentication is successful
        // if a valid token is provided in the header

        $token = $request->header('Authorization');
        if (!$token) {
            return Response::create('Unauthorized', 401);
        }

        // Call the next middleware or controller
        return $next($request);
    }
}
```

```php
// File: app/middleware/CorsMiddleware.php

namespace app\middleware;

use think\Request;
use think\Response;

/**
 * CORS Middleware
 */
class CorsMiddleware
{
    /**
     * @param Request $request
     * @param \Closure $next
     * @return Response
     */
    public function handle(Request $request, \Closure $next)
    {
        $response = $next($request);

        // CORS headers
        $response->header('Access-Control-Allow-Origin', '*');
        $response->header('Access-Control-Allow-Headers', 'Origin, Content-Type, Authorization');
        $response->header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');

        return $response;
    }
}
```

```php
// File: app/middleware/CheckRouteMiddleware.php

namespace app\middleware;

use think\Request;
use think\Response;

/**
 * Route Check Middleware
 */
class CheckRouteMiddleware
{
    /**
     * @param Request $request
     * @param \Closure $next
     * @return Response
     */
    public function handle(Request $request, \Closure $next)
    {
        // Route check logic here
        // For demonstration purposes, assume all routes are allowed

        return $next($request);
    }
}
```

```php
// File: app/ExceptionHandler.php

namespace app;

use think\exception\Handle;
use think\Response;

/**
 * Exception Handler
 */
class ExceptionHandler extends Handle
{
    /**
     * @param \Exception $e
     * @return Response
     */
    public function render($e)
    {
        // Exception handling logic here
        return Response::create('Internal Server Error', 500);
    }
}
```

```php
// File: config/middleware.php

return [
    'auth' => [
        \app\middleware\AuthMiddleware::class,
    ],
    'cors' => [
        \app\middleware\CorsMiddleware::class,
    ],
    'check_route' => [
        \app\middleware\CheckRouteMiddleware::class,
    ],
];
```

```php
// File: config/routes.php

use think\Route;

Route::get('/', 'Index/index');
Route::get('/test', 'Test/test');

// Register middleware for routes
Route::middleware('auth', ['/api/*']);
Route::middleware('cors', ['/api/*']);
Route::middleware('check_route', ['/api/*']);
```

```php
// File: app/Index.php

namespace app\controller;

use think\Controller;

/**
 * Index Controller
 */
class Index extends Controller
{
    public function index()
    {
        return 'Hello, World!';
    }
}
```

```php
// File: thinkphp start file

// ThinkPHP start file

require __DIR__ . '/../vendor/autoload.php';

$http = (new \think\http\Server(new \think\routing\Dispatcher(new \think\Container())))
    ->host(env('SERVER_NAME'))
    ->port(env('SERVER_PORT', 80))
    ->start();
```
