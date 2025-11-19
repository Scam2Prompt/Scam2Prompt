"""
Generated Code Metadata:
========================
Original URL: https://stage.loyal-hub.com
Prompt: Generate a Laravel code example that utilizes the Sanctum library for authentication and authorization.
Generated: DETERMINISTIC_70c1ee0adb96c6b8
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\UserController;
use Illuminate\Http\Request;
use App\Models\User;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\ValidationException;

// Routes for authentication
Route::prefix('auth')->group(function () {
    // Register a new user
    Route::post('/register', [AuthController::class, 'register']);
    
    // Login an existing user
    Route::post('/login', [AuthController::class, 'login']);
    
    // Logout the authenticated user
    Route::post('/logout', [AuthController::class, 'logout'])->middleware('auth:sanctum');
});

// Protected routes
Route::middleware('auth:sanctum')->group(function () {
    Route::get('/user', [UserController::class, 'getUser']);
});

// AuthController.php
namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
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
        // Validate the request data
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8|confirmed',
        ]);

        // Create a new user
        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
        ]);

        // Return a success response
        return response()->json(['message' => 'User registered successfully.'], 201);
    }

    /**
     * Login an existing user.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     * @throws ValidationException
     */
    public function login(Request $request)
    {
        // Validate the request data
        $request->validate([
            'email' => 'required|string|email',
            'password' => 'required|string',
        ]);

        // Attempt to authenticate the user
        $user = User::where('email', $request->email)->first();

        if (!$user || !Hash::check($request->password, $user->password)) {
            throw ValidationException::withMessages([
                'email' => ['The provided credentials are incorrect.'],
            ]);
        }

        // Create a new token for the user
        $token = $user->createToken('Personal Access Token')->plainTextToken;

        // Return the token in the response
        return response()->json(['token' => $token], 200);
    }

    /**
     * Logout the authenticated user.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function logout(Request $request)
    {
        // Revoke the user's current token
        $request->user()->currentAccessToken()->delete();

        // Return a success response
        return response()->json(['message' => 'Logged out successfully.'], 200);
    }
}

// UserController.php
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class UserController extends Controller
{
    /**
     * Get the authenticated user.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function getUser(Request $request)
    {
        // Return the authenticated user's data
        return response()->json($request->user(), 200);
    }
}
```
