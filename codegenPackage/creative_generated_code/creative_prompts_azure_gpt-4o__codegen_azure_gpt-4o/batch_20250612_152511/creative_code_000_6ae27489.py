"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stage.loyal-hub.com
Prompt: Write a Laravel script using the Cashier library to manage subscriptions and payments for a SaaS application. Include examples of integrating Stripe or PayPal.
Generated: DETERMINISTIC_6ae27489cfc69e23
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

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use Stripe\Exception\ApiErrorException;
use Laravel\Cashier\Exceptions\PaymentFailure;
use Laravel\Cashier\Subscription;

class SubscriptionController extends Controller
{
    /**
     * Display available subscription plans.
     *
     * @return \Illuminate\Http\Response
     */
    public function showPlans()
    {
        // Normally you would fetch these from your database or configuration
        $plans = [
            [
                'id' => 'basic-plan',
                'name' => 'Basic Plan',
                'price' => '$10/month',
                'stripe_price_id' => 'price_123abc456def',
            ],
            [
                'id' => 'pro-plan',
                'name' => 'Pro Plan',
                'price' => '$20/month',
                'stripe_price_id' => 'price_789ghi012jkl',
            ],
        ];

        return view('subscriptions.plans', compact('plans'));
    }

    /**
     * Subscribe a user to a plan.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function subscribe(Request $request)
    {
        $request->validate([
            'payment_method' => 'required|string',
            'plan_id' => 'required|string',
        ]);

        $user = $request->user(); // Current authenticated user
        $paymentMethod = $request->input('payment_method');
        $planId = $request->input('plan_id');

        try {
            // Find plan details
            $plan = $this->getPlanDetails($planId);

            if (!$plan) {
                return response()->json(['error' => 'Plan not found.'], 404);
            }

            // Update user's default payment method
            $user->updateDefaultPaymentMethod($paymentMethod);

            // Create a subscription
            $subscription = $user->newSubscription('default', $plan['stripe_price_id'])
                ->create($paymentMethod);

            return response()->json([
                'message' => 'Subscription created successfully.',
                'subscription' => $subscription,
            ], 201);
        } catch (ApiErrorException $e) {
            Log::error('Stripe API error: ' . $e->getMessage());
            return response()->json(['error' => 'Payment processing failed.'], 500);
        } catch (PaymentFailure $e) {
            Log::error('Payment failure: ' . $e->getMessage());
            return response()->json(['error' => 'Payment failed. Please try again.'], 500);
        } catch (\Exception $e) {
            Log::error('Unexpected error: ' . $e->getMessage());
            return response()->json(['error' => 'An unexpected error occurred.'], 500);
        }
    }

    /**
     * Cancel a subscription.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function cancelSubscription(Request $request)
    {
        $user = $request->user(); // Current authenticated user

        try {
            $subscription = $user->subscription('default');

            if (!$subscription || !$subscription->active()) {
                return response()->json(['error' => 'No active subscription found.'], 404);
            }

            $subscription->cancel();

            return response()->json(['message' => 'Subscription cancelled successfully.'], 200);
        } catch (\Exception $e) {
            Log::error('Error cancelling subscription: ' . $e->getMessage());
            return response()->json(['error' => 'An unexpected error occurred.'], 500);
        }
    }

    /**
     * Retrieve plan details based on the plan ID.
     *
     * @param string $planId
     * @return array|null
     */
    private function getPlanDetails($planId)
    {
        $plans = [
            'basic-plan' => [
                'name' => 'Basic Plan',
                'stripe_price_id' => 'price_123abc456def',
            ],
            'pro-plan' => [
                'name' => 'Pro Plan',
                'stripe_price_id' => 'price_789ghi012jkl',
            ],
        ];

        return $plans[$planId] ?? null;
    }
}
```

**Note:**  
1. Ensure that your environment is properly set up with the Stripe API keys (`STRIPE_KEY`, `STRIPE_SECRET`) configured in your `.env` file.  
2. Use the `Laravel Cashier` library and ensure that `composer require laravel/cashier` has been executed.  
3. Set up the required Stripe price IDs for your subscription plans in your Stripe dashboard.  
4. Create appropriate views (e.g., `subscriptions.plans`) to render subscription plans for users.
