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
use App\Models\User;

class SubscriptionController extends Controller
{
    /**
     * Show the subscription page.
     *
     * @return \Illuminate\View\View
     */
    public function showSubscriptionPage()
    {
        return view('subscription');
    }

    /**
     * Handle subscription creation.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function subscribe(Request $request)
    {
        $request->validate([
            'payment_method' => 'required|string', // Payment method ID from Stripe
        ]);

        $user = $request->user();

        try {
            // Subscribe the user to a plan named 'premium'
            $user->newSubscription('default', 'premium')
                ->create($request->payment_method);

            return redirect()->route('dashboard')->with('success', 'Subscription created successfully!');
        } catch (\Exception $e) {
            // Handle errors during subscription creation
            return redirect()->back()->withErrors(['error' => $e->getMessage()]);
        }
    }

    /**
     * Cancel the user's subscription.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function cancelSubscription(Request $request)
    {
        $user = $request->user();

        try {
            // Cancel the user's subscription
            $user->subscription('default')->cancel();

            return redirect()->route('dashboard')->with('success', 'Subscription canceled successfully!');
        } catch (\Exception $e) {
            // Handle errors during subscription cancellation
            return redirect()->back()->withErrors(['error' => $e->getMessage()]);
        }
    }

    /**
     * Resume the user's subscription after cancellation.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function resumeSubscription(Request $request)
    {
        $user = $request->user();

        try {
            // Resume the user's subscription
            $user->subscription('default')->resume();

            return redirect()->route('dashboard')->with('success', 'Subscription resumed successfully!');
        } catch (\Exception $e) {
            // Handle errors during subscription resumption
            return redirect()->back()->withErrors(['error' => $e->getMessage()]);
        }
    }
}
```

```blade
<!-- resources/views/subscription.blade.php -->

@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Manage Subscription</h1>

    <!-- Subscription Form -->
    <form action="{{ route('subscribe') }}" method="POST">
        @csrf
        <div class="form-group">
            <label for="payment_method">Payment Method</label>
            <input type="text" id="payment_method" name="payment_method" class="form-control" required>
            <small class="form-text text-muted">Enter your Stripe payment method ID.</small>
        </div>
        <button type="submit" class="btn btn-primary">Subscribe</button>
    </form>

    <!-- Cancel Subscription -->
    <form action="{{ route('cancel.subscription') }}" method="POST" style="margin-top: 20px;">
        @csrf
        <button type="submit" class="btn btn-danger">Cancel Subscription</button>
    </form>

    <!-- Resume Subscription -->
    <form action="{{ route('resume.subscription') }}" method="POST" style="margin-top: 20px;">
        @csrf
        <button type="submit" class="btn btn-success">Resume Subscription</button>
    </form>
</div>
@endsection
```

```php
// routes/web.php

use App\Http\Controllers\SubscriptionController;

Route::middleware(['auth'])->group(function () {
    Route::get('/subscription', [SubscriptionController::class, 'showSubscriptionPage'])->name('subscription');
    Route::post('/subscribe', [SubscriptionController::class, 'subscribe'])->name('subscribe');
    Route::post('/cancel-subscription', [SubscriptionController::class, 'cancelSubscription'])->name('cancel.subscription');
    Route::post('/resume-subscription', [SubscriptionController::class, 'resumeSubscription'])->name('resume.subscription');
});
```
