"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stage.loyal-hub.com
Prompt: Explain how to implement Laravel Sanctum for API authentication in a new project.
Generated: DETERMINISTIC_66e1d26d4f77cf60
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

// Step 1: Install Laravel Sanctum via Composer
// Command: composer require laravel/sanctum

// Step 2: Publish Sanctum configuration file and migration
// Command: php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"

// Step 3: Run the database migration to create the personal_access_tokens table
// Command: php artisan migrate

// Step 4: Update the 'config/auth.php' file
return [
    'guards' => [
        'web' => [
            'driver' => 'session',
            'provider' => 'users',
        ],
        'api' => [
            'driver' => 'sanctum', // Set Sanctum as the driver for API requests
            'provider' => 'users',
        ],
    ],
    // Other configurations...
];

// Step 5: Add Sanctum middleware to 'app/Http/Kernel.php'
protected $middlewareGroups = [
    'api' => [
        \Laravel\Sanctum\Http\Middleware\EnsureFrontendRequestsAreStateful::class, // Handles cookie-based authentication
        'throttle:api',
        \Illuminate\Routing\Middleware\SubstituteBindings::class,
    ],
];

// Step 6: Enable Sanctum in the User model
namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens; // Provides methods for token generation
    use Notifiable;

    protected $fillable = [
        'name',
        'email',
        'password',
    ];

    protected $hidden = [
        'password',
        'remember_token',
    ];
}

// Step 7: Create a route for user login and token generation
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use App\Models\User;

Route::post('/login', function (Request $request) {
    $request->validate([
        'email' => 'required|email',
        'password' => 'required',
    ]);

    $user = User::where('email', $request->email)->first();

    if (!$user || !Hash::check($request->password, $user->password)) {
        return response()->json([
            'message' => 'Invalid credentials'
        ], 401);
    }

    // Generate a new token for the authenticated user
    $token = $user->createToken('API Token')->plainTextToken;

    return response()->json([
        'access_token' => $token,
        'token_type' => 'Bearer',
    ]);
});

// Step 8: Protect API routes using Sanctum middleware
Route::middleware(['auth:sanctum'])->group(function () {
    Route::get('/user', function (Request $request) {
        return $request->user(); // Returns the authenticated user's details
    });

    // Add more authenticated routes here...
});

// Step 9: Handle token revocation (optional)
Route::post('/logout', function (Request $request) {
    $request->user()->tokens()->delete(); // Deletes all tokens for the authenticated user

    return response()->json([
        'message' => 'Logged out successfully'
    ]);
});
```
