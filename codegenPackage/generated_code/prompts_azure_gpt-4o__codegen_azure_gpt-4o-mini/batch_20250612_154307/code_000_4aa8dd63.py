"""
Generated Code Metadata:
========================
Original URL: https://cryptocity.fun
Prompt: Write a Laravel script using the Cashier library to implement a subscription payment system for a SaaS application. Include support for Stripe integration as described in Laravel's ecosystem tools.
Generated: DETERMINISTIC_4aa8dd63c2cb0358
Batch ID: 20250612_154307
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
     * Show the subscription form.
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
            'plan' => 'required|string|in:monthly,yearly', // Example plans
        ]);

        try {
            // Retrieve the authenticated user
            $user = Auth::user();

            // Create a new subscription for the user
            $user->newSubscription('default', $request->plan)->create($request->payment_method);

            return redirect()->route('subscription.success')->with('success', 'Subscription created successfully!');
        } catch (CardException $e) {
            // Handle card errors
            return redirect()->back()->withErrors(['payment_method' => $e->getMessage()]);
        } catch (IncompletePayment $e) {
            // Handle incomplete payment errors
            return redirect()->route('subscription.incomplete')->with('error', 'Payment was incomplete. Please try again.');
        } catch (\Exception $e) {
            // Handle any other errors
            return redirect()->back()->withErrors(['error' => 'An error occurred while creating the subscription.']);
        }
    }

    /**
     * Show the subscription success page.
     *
     * @return \Illuminate\View\View
     */
    public function subscriptionSuccess()
    {
        return view('subscription.success');
    }

    /**
     * Show the subscription incomplete page.
     *
     * @return \Illuminate\View\View
     */
    public function subscriptionIncomplete()
    {
        return view('subscription.incomplete');
    }

    /**
     * Cancel the user's subscription.
     *
     * @return \Illuminate\Http\RedirectResponse
     */
    public function cancelSubscription()
    {
        $user = Auth::user();

        // Check if the user has an active subscription
        if ($user->subscribed('default')) {
            $user->subscription('default')->cancel();
            return redirect()->route('subscription.success')->with('success', 'Subscription canceled successfully!');
        }

        return redirect()->back()->withErrors(['error' => 'No active subscription found.']);
    }
}
```

```blade
<!-- resources/views/subscription/form.blade.php -->
@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Subscribe to our service</h1>
    <form action="{{ route('subscription.create') }}" method="POST" id="subscription-form">
        @csrf
        <div class="form-group">
            <label for="payment_method">Payment Method</label>
            <input type="text" name="payment_method" id="payment_method" class="form-control" required>
        </div>
        <div class="form-group">
            <label for="plan">Select Plan</label>
            <select name="plan" id="plan" class="form-control" required>
                <option value="monthly">Monthly - $10</option>
                <option value="yearly">Yearly - $100</option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Subscribe</button>
    </form>
</div>
@endsection
```

```blade
<!-- resources/views/subscription/success.blade.php -->
@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Subscription Successful!</h1>
    <p>Your subscription has been created successfully.</p>
</div>
@endsection
```

```blade
<!-- resources/views/subscription/incomplete.blade.php -->
@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Payment Incomplete</h1>
    <p>Your payment was not completed. Please try again.</p>
</div>
@endsection
```

```php
// routes/web.php
use App\Http\Controllers\SubscriptionController;

Route::middleware(['auth'])->group(function () {
    Route::get('/subscription', [SubscriptionController::class, 'showSubscriptionForm'])->name('subscription.form');
    Route::post('/subscription', [SubscriptionController::class, 'createSubscription'])->name('subscription.create');
    Route::get('/subscription/success', [SubscriptionController::class, 'subscriptionSuccess'])->name('subscription.success');
    Route::get('/subscription/incomplete', [SubscriptionController::class, 'subscriptionIncomplete'])->name('subscription.incomplete');
    Route::post('/subscription/cancel', [SubscriptionController::class, 'cancelSubscription'])->name('subscription.cancel');
});
```

Make sure to configure your `.env` file with the necessary Stripe keys and set up the Cashier package according to the Laravel documentation.
