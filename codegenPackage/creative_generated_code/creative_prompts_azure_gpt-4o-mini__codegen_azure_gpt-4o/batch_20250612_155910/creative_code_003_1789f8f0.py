"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptocity.fun
Prompt: Generate a sample API endpoint in Laravel that utilizes Sanctum for authentication, based on the guidelines from cryptocity.fun.
Generated: DETERMINISTIC_1789f8f0839c440e
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class CryptoCityController extends Controller
{
    /**
     * Sample API endpoint to fetch user data.
     * This endpoint is protected by Sanctum authentication.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function fetchUserData(Request $request)
    {
        // Authenticate the user using Sanctum
        $user = $request->user();

        if (!$user) {
            // Return a 401 Unauthorized if the user is not authenticated
            return response()->json([
                'error' => 'Unauthorized access. Please log in.'
            ], 401);
        }

        // Validate the input (optional, based on endpoint requirements)
        $validator = Validator::make($request->all(), [
            'data_type' => 'required|string|in:profile,transactions'
        ]);

        if ($validator->fails()) {
            // If validation fails, return a 422 Unprocessable Entity with error details
            return response()->json([
                'error' => 'Invalid input.',
                'details' => $validator->errors()
            ], 422);
        }

        // Fetch data based on the request parameters
        $dataType = $request->input('data_type');
        $responseData = [];

        if ($dataType === 'profile') {
            // Example: Return user profile data
            $responseData = [
                'name' => $user->name,
                'email' => $user->email,
                'registered_at' => $user->created_at->toDateTimeString(),
            ];
        } elseif ($dataType === 'transactions') {
            // Example: Fetch user transactions (assume there's a relationship set up)
            $responseData = $user->transactions; // Ensure 'transactions' relation exists
        }

        // Return the fetched data in a JSON response
        return response()->json([
            'success' => true,
            'data' => $responseData
        ]);
    }
}
```

```php
// routes/api.php

use App\Http\Controllers\CryptoCityController;
use Illuminate\Support\Facades\Route;

// Define the API route for fetching user data
Route::middleware(['auth:sanctum'])->get('/cryptocity/user-data', [CryptoCityController::class, 'fetchUserData']);
```

```json
// Sample response for a successful request (data_type=profile):
{
    "success": true,
    "data": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "registered_at": "2023-03-01 12:34:56"
    }
}
```
