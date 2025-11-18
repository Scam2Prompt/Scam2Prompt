"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptocity.fun
Prompt: Write a Laravel script using the Cashier library to implement a subscription payment system for a SaaS application. Include support for Stripe integration as described in Laravel's ecosystem tools.
Generated: DETERMINISTIC_4aa8dd63c2cb0358
Batch ID: 20250612_154307
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
use Stripe\Exception\ApiErrorException;
use App\Models\User; // Assuming User model is used to represent subscribers

class SubscriptionController extends Controller
{
    /**
     * Display the subscription page.
     *
     * @return \Illuminate\View\View
     */
    public function showSubscriptionForm()
    {
        return view('subscription.form'); // View file for subscription form
    }

    /**
     * Handle the subscription creation process.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function createSubscription(Request $request)
    {
        // Validate the input data
        $validator = Validator::make($request->all(), [
            'payment_method' => 'required|string', // Stripe Payment Method ID
            'plan' => 'required|string', // Plan ID from Stripe
        ]);

        if ($validator->fails()) {
            return redirect()->back()->withErrors($validator)->withInput();
        }

        $user = $request->user(); // Retrieve the authenticated user

        try {
            // Update Stripe payment method for the user
            $user->createOrGetStripeCustomer();
            $user->updateDefaultPaymentMethod($request->payment_method);

            // Subscribe the user to the selected plan
            $subscription = $user->newSubscription('default', $request->plan)
                ->create($request->payment_method);

            return redirect()->route('subscription.success')->with('status', 'Subscription created successfully!');
        } catch (ApiErrorException $e) {
            // Handle Stripe API errors
            return redirect()->back()->withErrors(['error' => $e->getMessage()]);
        } catch (\Exception $e) {
            // Handle other potential errors
            return redirect()->back()->withErrors(['error' => 'An unexpected error occurred. Please try again later.']);
        }
    }

    /**
     * Display the subscription success page.
     *
     * @return \Illuminate\View\View
     */
    public function subscriptionSuccess()
    {
        return view('subscription.success'); // View file for subscription success message
    }
}
```

### Notes:
- Ensure your Laravel application has installed and set up the `Laravel Cashier` package (`composer require laravel/cashier`).
- Proper migration and configuration are needed for Stripe keys (`STRIPE_KEY` and `STRIPE_SECRET`) in your `.env` file.
- The `User` model must use the `Billable` trait: `use Laravel\Cashier\Billable;`.
- Replace placeholder views (`subscription.form`, `subscription.success`) with appropriate Blade templates.
```
