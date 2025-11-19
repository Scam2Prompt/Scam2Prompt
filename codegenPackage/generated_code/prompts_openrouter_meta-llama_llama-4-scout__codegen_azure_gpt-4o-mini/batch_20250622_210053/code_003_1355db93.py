"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Generate a Laravel code example that utilizes the features of Laravel v8.83.12 and PHP v7.4.30.
Generated: DETERMINISTIC_1355db9394b086f5
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
use App\Http\Controllers\UserController;
use Illuminate\Http\Request;

// Define a route for the user resource
Route::resource('users', UserController::class);

// UserController.php
namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class UserController extends Controller
{
    /**
     * Display a listing of the users.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        // Retrieve all users from the database
        $users = User::all();
        return response()->json($users);
    }

    /**
     * Store a newly created user in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8|confirmed',
        ]);

        // Handle validation failure
        if ($validator->fails()) {
            return response()->json($validator->errors(), 422);
        }

        // Create a new user instance
        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => bcrypt($request->password), // Hash the password
        ]);

        // Return a response with the created user
        return response()->json($user, 201);
    }

    /**
     * Display the specified user.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        // Find the user by ID or fail
        $user = User::findOrFail($id);
        return response()->json($user);
    }

    /**
     * Update the specified user in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'name' => 'sometimes|required|string|max:255',
            'email' => 'sometimes|required|string|email|max:255|unique:users,email,' . $id,
            'password' => 'sometimes|required|string|min:8|confirmed',
        ]);

        // Handle validation failure
        if ($validator->fails()) {
            return response()->json($validator->errors(), 422);
        }

        // Find the user by ID or fail
        $user = User::findOrFail($id);

        // Update user attributes
        $user->name = $request->name ?? $user->name;
        $user->email = $request->email ?? $user->email;
        if ($request->filled('password')) {
            $user->password = bcrypt($request->password); // Hash the new password
        }
        $user->save();

        // Return a response with the updated user
        return response()->json($user);
    }

    /**
     * Remove the specified user from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        // Find the user by ID or fail
        $user = User::findOrFail($id);
        $user->delete(); // Delete the user

        // Return a response indicating successful deletion
        return response()->json(['message' => 'User deleted successfully.'], 204);
    }
}
```

Make sure to run the necessary migrations to create the `users` table and include the `User` model in your application.
