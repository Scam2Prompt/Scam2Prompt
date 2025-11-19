"""
Generated Code Metadata:
========================
Original URL: https://stage.loyal-hub.com
Prompt: Write a Laravel script using the Cashier library to manage subscriptions and payments for a SaaS application. Include examples of integrating Stripe or PayPal.
Generated: DETERMINISTIC_6ae27489cfc69e23
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\User;
use Laravel\Cashier\Cashier;
use Laravel\Cashier\Exceptions\IncompletePayment;
use Stripe\Exception\CardException;

class SubscriptionController extends Controller
{
    /**
     * Display the subscription form.
     *
     * @return \Illuminate\View\View
     */
    public function showSubscriptionForm()
    {
        return view('subscription.form');
    }

    /**
     * Create a new subscription for the authenticated user.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function createSubscription(Request $request)
    {
        // Validate the incoming request data
        $request->validate([
            'payment_method' => 'required|string',
            'plan' => 'required|string',
        ]);

        $user = Auth::user();

        try {
            // Create a new subscription for the user
            $user->newSubscription('default', $request->plan)
                ->create($request->payment_method);

            return redirect()->route('home')->with('success', 'Subscription created successfully!');
        } catch (CardException $e) {
            // Handle card errors
            return redirect()->back()->withErrors(['payment_method' => $e->getMessage()]);
        } catch (IncompletePayment $e) {
            // Handle incomplete payment errors
            return redirect()->route('payment.confirm', $e->payment->id);
        } catch (\Exception $e) {
            // Handle any other errors
            return redirect()->back()->withErrors(['error' => 'An error occurred while creating the subscription.']);
        }
    }

    /**
     * Show the payment confirmation page.
     *
     * @param  string  $paymentId
     * @return \Illuminate\View\View
     */
    public function confirmPayment($paymentId)
    {
        return view('payment.confirm', compact('paymentId'));
    }

    /**
     * Handle the payment confirmation.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  string  $paymentId
     * @return \Illuminate\Http\RedirectResponse
     */
    public function handlePaymentConfirmation(Request $request, $paymentId)
    {
        // Validate the incoming request data
        $request->validate([
            'payment_method' => 'required|string',
        ]);

        $user = Auth::user();

        try {
            // Confirm the payment
            $user->charge($request->payment_method, $paymentId);

            return redirect()->route('home')->with('success', 'Payment confirmed successfully!');
        } catch (CardException $e) {
            // Handle card errors
            return redirect()->back()->withErrors(['payment_method' => $e->getMessage()]);
        } catch (\Exception $e) {
            // Handle any other errors
            return redirect()->back()->withErrors(['error' => 'An error occurred while confirming the payment.']);
        }
    }

    /**
     * Cancel the user's subscription.
     *
     * @return \Illuminate\Http\RedirectResponse
     */
    public function cancelSubscription()
    {
        $user = Auth::user();

        try {
            // Cancel the user's subscription
            $user->subscription('default')->cancel();

            return redirect()->route('home')->with('success', 'Subscription canceled successfully!');
        } catch (\Exception $e) {
            // Handle any errors
            return redirect()->back()->withErrors(['error' => 'An error occurred while canceling the subscription.']);
        }
    }
}
```

### Notes:
- Ensure you have the necessary routes defined in your `web.php` file for the methods in this controller.
- Make sure to set up your views (`subscription.form`, `payment.confirm`) to handle the forms and display messages.
- This code assumes you have already set up Laravel Cashier and configured your Stripe or PayPal credentials in your `.env` file.
