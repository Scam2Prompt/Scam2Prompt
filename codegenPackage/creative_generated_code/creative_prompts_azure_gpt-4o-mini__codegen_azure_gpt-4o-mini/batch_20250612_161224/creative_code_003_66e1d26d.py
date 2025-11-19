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
// Step 1: Install Laravel Sanctum via Composer
// Run the following command in your terminal
// composer require laravel/sanctum

// Step 2: Publish the Sanctum configuration
// Run the following command to publish the Sanctum configuration file
// php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"

// Step 3: Run the migrations to create the necessary tables
// Run the following command to migrate
// php artisan migrate

// Step 4: Add Sanctum's middleware to your api middleware group within your app/Http/Kernel.php file
protected $middlewareGroups = [
    'api' => [
        \Laravel\Sanctum\Http\Middleware\EnsureFrontendRequestsAreStateful::class,
        'throttle:api',
        \Illuminate\Routing\Middleware\SubstituteBindings::class,
    ],
];

// Step 5: Use the Sanctum's HasApiTokens trait in your User model
namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens;

    // User model properties and methods
    protected $fillable = ['name', 'email', 'password'];
    protected $hidden = ['password', 'remember_token'];
}

// Step 6: Set up authentication routes in your routes/api.php
use App\Http\Controllers\AuthController;
use Illuminate\Support\Facades\Route;

Route::post('/register', [AuthController::class, 'register']);
Route::post('/login', [AuthController::class, 'login']);
Route::middleware('auth:sanctum')->get('/user', [AuthController::class, 'getUser']);

// Step 7: Create an AuthController to handle authentication
namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\ValidationException;

class AuthController extends Controller
{
    // Register a new user
    public function register(Request $request)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|confirmed|min:8',
        ]);

        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
        ]);

        return response()->json(['user' => $user], 201);
    }

    // Log in a user and issue a token
    public function login(Request $request)
    {
        $request->validate([
            'email' => 'required|string|email',
            'password' => 'required|string',
        ]);

        $user = User::where('email', $request->email)->first();

        // Check if the user exists and the password matches
        if (!$user || !Hash::check($request->password, $user->password)) {
            throw ValidationException::withMessages([
                'email' => ['The provided credentials are incorrect.'],
            ]);
        }

        // Create a token for the user
        $token = $user->createToken('YourAppName')->plainTextToken;

        return response()->json(['token' => $token]);
    }

    // Get the authenticated user
    public function getUser(Request $request)
    {
        return response()->json($request->user());
    }
}

// Step 8: Ensure your User model is properly configured for API authentication
// (This is already done with the HasApiTokens trait)

// Step 9: Test the API authentication
// Use Postman or any API testing tool to test the registration and login routes.
```
