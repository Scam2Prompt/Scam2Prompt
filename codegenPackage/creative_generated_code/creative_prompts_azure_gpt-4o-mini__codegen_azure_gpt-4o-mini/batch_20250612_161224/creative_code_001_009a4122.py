"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stage.loyal-hub.com
Prompt: Write a PHP script that integrates with Laravel's Cashier library for handling subscription billing.
Generated: DETERMINISTIC_009a4122e1bf12c1
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
use App\Models\User;
use Laravel\Cashier\Cashier;
use Laravel\Cashier\Exceptions\IncompletePayment;
use Laravel\Cashier\Subscription;

// Define routes for the subscription management
Route::middleware(['auth:sanctum'])->group(function () {
    
    // Route to create a new subscription
    Route::post('/subscribe', function (Request $request) {
        // Validate incoming request data
        $request->validate([
            'plan' => 'required|string|in:monthly,yearly', // Allowed plans
        ]);

        // Get the authenticated user
        $user = $request->user();

        // Subscribe the user to the specified plan
        try {
            $user->newSubscription('default', $request->plan)->create($request->paymentMethodId);
            return response()->json(['message' => 'Subscription created successfully.'], 201);
        } catch (IncompletePayment $exception) {
            return response()->json(['error' => 'Payment was incomplete.'], 422);
        } catch (\Exception $exception) {
            return response()->json(['error' => 'An error occurred while creating the subscription.'], 500);
        }
    });

    // Route to cancel a subscription
    Route::post('/cancel-subscription', function (Request $request) {
        // Get the authenticated user
        $user = $request->user();

        // Cancel the user's subscription
        try {
            $subscription = $user->subscription('default');
            
            if ($subscription) {
                $subscription->cancel();
                return response()->json(['message' => 'Subscription canceled successfully.'], 200);
            } else {
                return response()->json(['error' => 'No active subscription found.'], 404);
            }

        } catch (\Exception $exception) {
            return response()->json(['error' => 'An error occurred while canceling the subscription.'], 500);
        }
    });

    // Route to resume a subscription
    Route::post('/resume-subscription', function (Request $request) {
        // Get the authenticated user
        $user = $request->user();

        // Resume the user's subscription
        try {
            $subscription = $user->subscription('default');

            if ($subscription && $subscription->onGracePeriod()) {
                $subscription->resume();
                return response()->json(['message' => 'Subscription resumed successfully.'], 200);
            } else {
                return response()->json(['error' => 'No subscription on grace period found.'], 404);
            }

        } catch (\Exception $exception) {
            return response()->json(['error' => 'An error occurred while resuming the subscription.'], 500);
        }
    });

    // Route to get subscription details
    Route::get('/subscription', function (Request $request) {
        // Get the authenticated user
        $user = $request->user();

        // Retrieve subscription details
        try {
            $subscription = $user->subscription('default');

            if ($subscription) {
                return response()->json(['subscription' => $subscription], 200);
            } else {
                return response()->json(['error' => 'No subscription found.'], 404);
            }

        } catch (\Exception $exception) {
            return response()->json(['error' => 'An error occurred while retrieving subscription details.'], 500);
        }
    });
});
```
