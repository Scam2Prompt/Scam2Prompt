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

// This script demonstrates integration with Laravel's Cashier library for handling subscription billing.
// Ensure Laravel and Cashier are properly set up in your application before using this script.

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use App\Models\User;

class SubscriptionController extends Controller
{
    /**
     * Subscribe a user to a plan using Laravel Cashier.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function subscribe(Request $request)
    {
        // Validate the incoming request data
        $validated = $request->validate([
            'plan' => 'required|string', // Plan identifier defined in Stripe or Paddle
            'payment_method' => 'required|string', // Payment method ID from Stripe (e.g., card, bank_account)
        ]);

        try {
            // Retrieve the authenticated user
            $user = $request->user();

            // Ensure the user has a Stripe customer ID
            if (!$user->hasStripeId()) {
                $user->createOrGetStripeCustomer(); // Automatically creates or retrieves the Stripe customer
            }

            // Subscribe the user to the selected plan
            $subscription = $user->newSubscription('default', $validated['plan'])
                ->create($validated['payment_method']); // Attach payment method and subscribe

            return response()->json([
                'status' => 'success',
                'message' => 'Subscription created successfully!',
                'subscription' => $subscription,
            ], 200);

        } catch (\Exception $e) {
            // Log the error for debugging purposes
            Log::error('Subscription creation failed: ' . $e->getMessage());

            return response()->json([
                'status' => 'error',
                'message' => 'Failed to create subscription.',
                'error' => $e->getMessage(),
            ], 500);
        }
    }

    /**
     * Cancel a user's subscription.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function cancelSubscription(Request $request)
    {
        try {
            // Retrieve the authenticated user
            $user = $request->user();

            // Check if the user has an active subscription
            if (!$user->subscribed('default')) {
                return response()->json([
                    'status' => 'error',
                    'message' => 'No active subscription found.',
                ], 404);
            }

            // Cancel the user's subscription immediately
            $user->subscription('default')->cancel();

            return response()->json([
                'status' => 'success',
                'message' => 'Subscription canceled successfully.',
            ], 200);

        } catch (\Exception $e) {
            // Log the error for debugging purposes
            Log::error('Subscription cancellation failed: ' . $e->getMessage());

            return response()->json([
                'status' => 'error',
                'message' => 'Failed to cancel subscription.',
                'error' => $e->getMessage(),
            ], 500);
        }
    }

    /**
     * Check the user's subscription status.
     *
     * @param Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function subscriptionStatus(Request $request)
    {
        try {
            // Retrieve the authenticated user
            $user = $request->user();

            // Check subscription status and respond accordingly
            if ($user->subscribed('default')) {
                return response()->json([
                    'status' => 'success',
                    'message' => 'User is subscribed.',
                    'subscription' => $user->subscription('default'),
                ], 200);
            }

            return response()->json([
                'status' => 'success',
                'message' => 'User is not subscribed.',
            ], 200);

        } catch (\Exception $e) {
            // Log the error for debugging purposes
            Log::error('Failed to retrieve subscription status: ' . $e->getMessage());

            return response()->json([
                'status' => 'error',
                'message' => 'Failed to retrieve subscription status.',
                'error' => $e->getMessage(),
            ], 500);
        }
    }
}
```

This script handles subscription creation, cancellation, and status checking using Laravel Cashier. Ensure you have Stripe or Paddle configured properly in your Laravel project and that the necessary environment variables are set up (`STRIPE_SECRET`, `STRIPE_KEY`, etc.).
