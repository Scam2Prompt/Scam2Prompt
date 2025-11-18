"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stage.loyal-hub.com
Prompt: Write a Laravel code snippet using the Sanctum library to implement API token authentication for a mobile application.
Generated: DETERMINISTIC_81fed5862f281f85
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\User;
use Illuminate\Support\Facades\Validator;

class AuthController extends Controller
{
    /**
     * Handle user registration and issue an API token.
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

        // Return validation errors if any
        if ($validator->fails()) {
            return response()->json($validator->errors(), 422);
        }

        // Create a new user instance
        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => bcrypt($request->password),
        ]);

        // Issue API token for the newly created user
        $token = $user->createToken('MobileAppToken')->plainTextToken;

        // Return success response with token
        return response()->json(['token' => $token], 201);
    }

    /**
     * Handle user authentication and issue an API token.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function login(Request $request)
    {
        // Validate the incoming request data
        $credentials = $request->validate([
            'email' => 'required|string|email',
            'password' => 'required|string',
        ]);

        // Attempt to authenticate the user
        if (Auth::attempt($credentials)) {
            $user = Auth::user();
            // Issue API token
            $token = $user->createToken('MobileAppToken')->plainTextToken;

            // Return success response with token
            return response()->json(['token' => $token], 200);
        }

        // Return unauthorized response if authentication fails
        return response()->json(['message' => 'Unauthorized'], 401);
    }

    /**
     * Handle user logout and revoke the API token.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function logout(Request $request)
    {
        // Revoke the user's current token
        $request->user()->currentAccessToken()->delete();

        // Return success response
        return response()->json(['message' => 'Logged out successfully'], 200);
    }
}
```

```php
// In routes/api.php

use App\Http\Controllers\Auth\AuthController;

Route::post('register', [AuthController::class, 'register']);
Route::post('login', [AuthController::class, 'login']);
Route::middleware('auth:sanctum')->post('logout', [AuthController::class, 'logout']);
```

```php
// In User model (App\Models\User.php)

// Add the HasApiTokens trait to the User model
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens, Notifiable;

    // Other model properties and methods...
}
```

```php
// In config/sanctum.php

// Ensure to set the stateful domains correctly for your mobile application
'stateful' => explode(',', env('SANCTUM_STATEFUL_DOMAINS', 'localhost')),
```

```php
// In .env

// Ensure you have the proper Sanctum configurations
SANCTUM_STATEFUL_DOMAINS=localhost
SESSION_DOMAIN=localhost
```

```php
// Run the following command to publish Sanctum's configuration
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
```
