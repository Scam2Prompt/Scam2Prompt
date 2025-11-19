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

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;
use Illuminate\Support\Facades\Auth;

class AuthController extends Controller
{
    /**
     * Register a new user.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function register(Request $request)
    {
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8',
        ]);

        // If validation fails, return a response with errors
        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        // Create a new user record
        $user = \App\Models\User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => bcrypt($request->password), // Hash the password before storing it
        ]);

        // Return a success response
        return response()->json(['message' => 'User registered successfully', 'user' => $user], 201);
    }

    /**
     * Login a user and issue a Sanctum token.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function login(Request $request)
    {
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'email' => 'required|string|email',
            'password' => 'required|string',
        ]);

        // If validation fails, return a response with errors
        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        // Attempt to authenticate the user
        if (!Auth::attempt($request->only('email', 'password'))) {
            return response()->json(['message' => 'Invalid credentials'], 401);
        }

        // Retrieve the authenticated user
        $user = Auth::user();

        // Generate a Sanctum token for the user
        $token = $user->createToken('API Token')->plainTextToken;

        // Return the token in the response
        return response()->json(['message' => 'Login successful', 'token' => $token], 200);
    }

    /**
     * Logout the authenticated user and revoke their tokens.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function logout()
    {
        // Retrieve the authenticated user
        $user = Auth::user();

        // Revoke all tokens for the user
        $user->tokens()->delete();

        // Return a success response
        return response()->json(['message' => 'Logout successful'], 200);
    }
}
```

### Notes:
1. Ensure Sanctum is properly configured in your Laravel application (`composer require laravel/sanctum` and follow installation/setup instructions in the Laravel documentation).
2. Use the following routes in your `routes/api.php` file to map the controller methods:
```php
use App\Http\Controllers\API\AuthController;

Route::post('/register', [AuthController::class, 'register']);
Route::post('/login', [AuthController::class, 'login']);
Route::post('/logout', [AuthController::class, 'logout'])->middleware('auth:sanctum');
```
3. Make sure your `User` model includes the `HasApiTokens` trait:
```php
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens, Notifiable;
}
```
