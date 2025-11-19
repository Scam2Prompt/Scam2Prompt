"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-stage.loyal-hub.com
Prompt: Generate a code snippet that demonstrates how to use Laravel's Cashier library for handling subscription billing in a web application.
Generated: DETERMINISTIC_44b6f50bc4dc2c86
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

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Laravel\Cashier\Subscription;

class SubscriptionController extends Controller
{
    /**
     * Display the subscription page.
     *
     * @return \Illuminate\View\View
     */
    public function index()
    {
        return view('subscriptions.index', [
            'user' => Auth::user(),
        ]);
    }

    /**
     * Create a new subscription for the authenticated user.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function subscribe(Request $request)
    {
        // Validate the request input
        $request->validate([
            'plan' => 'required|string|in:monthly,yearly', // Assumes 'monthly' and 'yearly' are valid plans
        ]);

        try {
            // Retrieve the authenticated user
            $user = Auth::user();

            // Create the subscription
            $user->newSubscription('default', $request->plan)->create($request->payment_method);

            // Redirect back with success message
            return redirect()->route('subscriptions.index')->with('success', 'Subscription created successfully!');
        } catch (\Exception $e) {
            // Log the error for debugging
            \Log::error('Subscription error: ' . $e->getMessage());

            // Redirect back with error message
            return redirect()->route('subscriptions.index')->withErrors(['error' => 'Failed to create subscription.']);
        }
    }

    /**
     * Cancel the user's subscription.
     *
     * @return \Illuminate\Http\RedirectResponse
     */
    public function cancel()
    {
        try {
            // Retrieve the authenticated user
            $user = Auth::user();

            // Cancel the active subscription
            $subscription = $user->subscription('default');
            if ($subscription) {
                $subscription->cancel();
            }

            // Redirect back with success message
            return redirect()->route('subscriptions.index')->with('success', 'Subscription canceled successfully!');
        } catch (\Exception $e) {
            // Log the error for debugging
            \Log::error('Cancellation error: ' . $e->getMessage());

            // Redirect back with error message
            return redirect()->route('subscriptions.index')->withErrors(['error' => 'Failed to cancel subscription.']);
        }
    }

    /**
     * Resume the user's cancelled subscription.
     *
     * @return \Illuminate\Http\RedirectResponse
     */
    public function resume()
    {
        try {
            // Retrieve the authenticated user
            $user = Auth::user();

            // Resume the subscription if it is canceled
            $subscription = $user->subscription('default');
            if ($subscription && $subscription->onGracePeriod()) {
                $subscription->resume();
            }

            // Redirect back with success message
            return redirect()->route('subscriptions.index')->with('success', 'Subscription resumed successfully!');
        } catch (\Exception $e) {
            // Log the error for debugging
            \Log::error('Resume error: ' . $e->getMessage());

            // Redirect back with error message
            return redirect()->route('subscriptions.index')->withErrors(['error' => 'Failed to resume subscription.']);
        }
    }
}
```

```blade
<!-- resources/views/subscriptions/index.blade.php -->
@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Manage Your Subscription</h1>

    @if(session('success'))
        <div class="alert alert-success">{{ session('success') }}</div>
    @endif

    @if($errors->any())
        <div class="alert alert-danger">
            <ul>
                @foreach ($errors->all() as $error)
                    <li>{{ $error }}</li>
                @endforeach
            </ul>
        </div>
    @endif

    <form action="{{ route('subscriptions.subscribe') }}" method="POST">
        @csrf
        <div class="form-group">
            <label for="plan">Choose a subscription plan:</label>
            <select name="plan" id="plan" required>
                <option value="">Select a plan</option>
                <option value="monthly">Monthly</option>
                <option value="yearly">Yearly</option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Subscribe</button>
    </form>

    <form action="{{ route('subscriptions.cancel') }}" method="POST" style="margin-top: 20px;">
        @csrf
        <button type="submit" class="btn btn-danger">Cancel Subscription</button>
    </form>

    <form action="{{ route('subscriptions.resume') }}" method="POST" style="margin-top: 20px;">
        @csrf
        <button type="submit" class="btn btn-warning">Resume Subscription</button>
    </form>
</div>
@endsection
```

**Note:** Make sure to adjust the routes in your `web.php` file and include the necessary middleware for authentication. This code assumes you have set up Laravel Cashier and configured your payment gateway (like Stripe).
