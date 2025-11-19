"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Generate a code snippet that demonstrates how to use Laravel's Cashier library for handling subscription billing in a web application.
Generated: DETERMINISTIC_44b6f50bc4dc2c86
Batch ID: 20250612_161224
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
use Illuminate\Support\Facades\Validator;
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
    public function createSubscription(Request $request)
    {
        // Validate the incoming request
        $validator = Validator::make($request->all(), [
            'payment_method' => 'required|string',
            'plan' => 'required|string|in:basic,premium',
        ]);

        if ($validator->fails()) {
            return redirect()->back()->withErrors($validator)->withInput();
        }

        $user = $request->user();

        try {
            // Add payment method to the user
            $user->createOrGetStripeCustomer();
            $user->updateDefaultPaymentMethod($request->payment_method);

            // Subscribe the user to the selected plan
            $user->newSubscription('default', $request->plan)->create($request->payment_method);

            return redirect()->route('dashboard')->with('success', 'Subscription created successfully!');
        } catch (\Exception $e) {
            // Handle errors gracefully
            return redirect()->back()->with('error', 'Failed to create subscription: ' . $e->getMessage());
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
            // Cancel the subscription
            $user->subscription('default')->cancel();

            return redirect()->route('dashboard')->with('success', 'Subscription canceled successfully!');
        } catch (\Exception $e) {
            // Handle errors gracefully
            return redirect()->back()->with('error', 'Failed to cancel subscription: ' . $e->getMessage());
        }
    }

    /**
     * Resume a canceled subscription.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function resumeSubscription(Request $request)
    {
        $user = $request->user();

        try {
            // Resume the subscription
            $user->subscription('default')->resume();

            return redirect()->route('dashboard')->with('success', 'Subscription resumed successfully!');
        } catch (\Exception $e) {
            // Handle errors gracefully
            return redirect()->back()->with('error', 'Failed to resume subscription: ' . $e->getMessage());
        }
    }
}
```

```blade
<!-- resources/views/subscription.blade.php -->
@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Manage Your Subscription</h1>

    @if(session('success'))
        <div class="alert alert-success">{{ session('success') }}</div>
    @endif

    @if(session('error'))
        <div class="alert alert-danger">{{ session('error') }}</div>
    @endif

    <form action="{{ route('subscription.create') }}" method="POST">
        @csrf
        <div class="form-group">
            <label for="payment_method">Payment Method</label>
            <input type="text" name="payment_method" id="payment_method" class="form-control" required>
        </div>
        <div class="form-group">
            <label for="plan">Select Plan</label>
            <select name="plan" id="plan" class="form-control" required>
                <option value="basic">Basic</option>
                <option value="premium">Premium</option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Subscribe</button>
    </form>

    <form action="{{ route('subscription.cancel') }}" method="POST" class="mt-3">
        @csrf
        <button type="submit" class="btn btn-danger">Cancel Subscription</button>
    </form>

    <form action="{{ route('subscription.resume') }}" method="POST" class="mt-3">
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
    Route::get('/subscription', [SubscriptionController::class, 'showSubscriptionPage'])->name('subscription.page');
    Route::post('/subscription/create', [SubscriptionController::class, 'createSubscription'])->name('subscription.create');
    Route::post('/subscription/cancel', [SubscriptionController::class, 'cancelSubscription'])->name('subscription.cancel');
    Route::post('/subscription/resume', [SubscriptionController::class, 'resumeSubscription'])->name('subscription.resume');
});
```
