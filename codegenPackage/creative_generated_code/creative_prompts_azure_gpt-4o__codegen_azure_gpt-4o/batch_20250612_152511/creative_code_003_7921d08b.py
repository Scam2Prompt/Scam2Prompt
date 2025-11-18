"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-stage.loyal-hub.com
Prompt: Write a Laravel API using Sanctum for authentication and include code for issuing and verifying tokens.
Generated: DETERMINISTIC_7921d08b1d6c2973
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

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;

// API Routes
Route::middleware('api')->group(function () {
    // Public routes
    Route::post('/register', [AuthController::class, 'register']);
    Route::post('/login', [AuthController::class, 'login']);

    // Protected routes (require authentication via Sanctum)
    Route::middleware('auth:sanctum')->group(function () {
        Route::get('/user', [AuthController::class, 'user']);
        Route::post('/logout', [AuthController::class, 'logout']);
    });
});
```

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Validator;
use App\Models\User;

class AuthController extends Controller
{
    /**
     * Handle user registration.
     */
    public function register(Request $request)
    {
        // Validate input data
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8|confirmed',
        ]);

        // Return validation errors if validation fails
        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        // Create a new user record
        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
        ]);

        // Return success response
        return response()->json([
            'message' => 'User registered successfully.',
            'user' => $user,
        ], 201);
    }

    /**
     * Handle user login and issue token.
     */
    public function login(Request $request)
    {
        // Validate input data
        $validator = Validator::make($request->all(), [
            'email' => 'required|string|email',
            'password' => 'required|string',
        ]);

        // Return validation errors if validation fails
        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        // Find user by email
        $user = User::where('email', $request->email)->first();

        // Verify password and issue token
        if ($user && Hash::check($request->password, $user->password)) {
            $token = $user->createToken('auth_token')->plainTextToken;

            // Return success response with token
            return response()->json([
                'message' => 'Login successful.',
                'token' => $token,
            ], 200);
        }

        // Return error response for invalid credentials
        return response()->json(['message' => 'Invalid credentials.'], 401);
    }

    /**
     * Retrieve authenticated user details.
     */
    public function user(Request $request)
    {
        // Return authenticated user
        return response()->json([
            'user' => $request->user(),
        ], 200);
    }

    /**
     * Handle user logout and revoke tokens.
     */
    public function logout(Request $request)
    {
        // Revoke all tokens for the authenticated user
        $request->user()->tokens()->delete();

        // Return success response
        return response()->json(['message' => 'Logged out successfully.'], 200);
    }
}
```

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens, HasFactory;

    /**
     * The attributes that are mass assignable.
     */
    protected $fillable = [
        'name',
        'email',
        'password',
    ];

    /**
     * The attributes that should be hidden for serialization.
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * The attributes that should be cast to native types.
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
    ];
}
```

```bash
# Run these commands in the terminal to set up Sanctum
composer require laravel/sanctum
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
php artisan migrate

# Add Sanctum middleware to the `api` guard in `config/auth.php`
# 'guards' => [
#     'api' => [
#         'driver' => 'sanctum',
#         'provider' => null,
#     ],
# ],
```
