"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-stage.loyal-hub.com
Prompt: Create an API endpoint in Laravel that integrates with the Sanctum library for user authentication.
Generated: DETERMINISTIC_bf5318970e2a45a7
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Api\AuthController;

// API routes for user authentication
Route::prefix('api')->group(function () {
    // Route for user registration
    Route::post('/register', [AuthController::class, 'register']);

    // Route for user login
    Route::post('/login', [AuthController::class, 'login']);

    // Route for getting authenticated user
    Route::middleware('auth:sanctum')->get('/user', [AuthController::class, 'user']);
});

// AuthController.php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\ValidationException;

class AuthController extends Controller
{
    /**
     * Register a new user.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function register(Request $request)
    {
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8|confirmed',
        ]);

        // Handle validation failure
        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        // Create a new user and persist to database
        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
        ]);

        // Return success response with the created user
        return response()->json(['user' => $user], 201);
    }

    /**
     * Log in an existing user.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     * @throws ValidationException
     */
    public function login(Request $request)
    {
        // Validate the incoming request data
        $this->validate($request, [
            'email' => 'required|string|email',
            'password' => 'required|string',
        ]);

        // Attempt to authenticate the user
        if (!auth()->attempt($request->only('email', 'password'))) {
            return response()->json(['message' => 'Invalid credentials.'], 401);
        }

        // Generate a new token for the authenticated user
        $user = auth()->user();
        $token = $user->createToken('Token Name')->plainTextToken;

        // Return success response with token and user data
        return response()->json(['token' => $token, 'user' => $user], 200);
    }

    /**
     * Get the authenticated user.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function user()
    {
        // Return the authenticated user
        return response()->json(auth()->user(), 200);
    }
}
```

Make sure to run the necessary migrations and install Sanctum if you haven't already:

```bash
composer require laravel/sanctum
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
php artisan migrate
```

And then, add the Sanctum middleware to your `api` middleware group within your `app/Http/Kernel.php` file:

```php
'api' => [
    \Laravel\Sanctum\Http\Middleware\EnsureFrontendRequestsAreStateful::class,
    'throttle:api',
    \Illuminate\Routing\Middleware\SubstituteBindings::class,
],
```
