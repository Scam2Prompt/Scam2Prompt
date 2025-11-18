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
use App\Models\User;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Now create something great!
|
*/

// Route for user registration
Route::post('register', [AuthController::class, 'register']);

// Route for user login
Route::post('login', [AuthController::class, 'login']);

// Protected route example
Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

```

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use App\Models\User;
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
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8|confirmed',
        ]);

        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
        ]);

        return response()->json(['message' => 'User registered successfully.'], 201);
    }

    /**
     * Log in a user and issue a token.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     * @throws ValidationException
     */
    public function login(Request $request)
    {
        $credentials = $request->validate([
            'email' => 'required|string|email',
            'password' => 'required|string',
        ]);

        if (! $token = auth()->attempt($credentials)) {
            throw ValidationException::withMessages([
                'email' => ['The provided credentials are incorrect.'],
            ]);
        }

        return response()->json(['token' => $token], 200);
    }

    /**
     * Verify the provided token.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function verify(Request $request)
    {
        $user = auth()->user();
        
        if (!$user) {
            return response()->json(['message' => 'Unauthorized'], 401);
        }

        return response()->json(['user' => $user], 200);
    }
}
```

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Laravel\Sanctum\HasApiTokens;

class User extends Model
{
    use HasFactory, HasApiTokens;

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
```

```bash
# Ensure to run the following command to set up Sanctum and publish its configuration
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
```

```php
// In your config/auth.php, set the driver to sanctum in the api guard
'guards' => [
    'sanctum' => [
        'driver' => 'sanctum',
        'provider' => 'users',
    ],
],
```

```bash
# Don't forget to run migrations
php artisan migrate
```

```php
// In your Kernel.php, include Sanctum's middleware in the api middleware group
use Laravel\Sanctum\Http\Middleware\EnsureFrontendRequestsAreStateful;

protected $middlewareGroups = [
    'api' => [
        EnsureFrontendRequestsAreStateful::class,
        'throttle:api',
        \Illuminate\Routing\Middleware\SubstituteBindings::class,
    ],
];
```

```php
// Make sure to include Sanctum's service provider in the config/app.php
'providers' => [
    ...
    Laravel\Sanctum\SanctumServiceProvider::class,
],
```
