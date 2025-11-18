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
use Illuminate\Support\Facades\Auth;
use App\Models\User;
use Laravel\Cashier\Exceptions\IncompletePayment;
use Laravel\Cashier\Cashier;

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
     * Create a new subscription for the user.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function subscribe(Request $request)
    {
        // Validate the incoming request data
        $request->validate([
            'payment_method' => 'required',
            'plan' => 'required|in:monthly,yearly', // Ensure only allowed plans
        ]);

        try {
            // Get the authenticated user
            $user = Auth::user();

            // Create or update the user's payment method
            $user->createOrUpdateStripeCustomer($request->payment_method);

            // Subscribe the user to the selected plan
            $user->newSubscription('default', $request->plan)->create($request->payment_method);

            return redirect()->route('subscription.success')->with('success', 'Subscription created successfully!');
        } catch (IncompletePayment $exception) {
            // Handle the case where the payment was incomplete
            return redirect()->route('subscription.form')->withErrors(['payment' => $exception->getMessage()]);
        } catch (\Exception $exception) {
            // Handle any other exceptions that occur
            return redirect()->route('subscription.form')->withErrors(['error' => 'An error occurred. Please try again.']);
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
            return redirect()->route('subscription.index')->with('success', 'Your subscription has been canceled.');
        }

        return redirect()->route('subscription.index')->withErrors(['error' => 'No active subscription found.']);
    }
}
```

### Migration for creating Users Table with Cashier Fields

```php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->string('stripe_id')->nullable();
            $table->string('card_brand')->nullable();
            $table->string('card_last_four')->nullable();
            $table->timestamp('trial_ends_at')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('users');
    }
}
```

### Blade View for Subscription Form (`resources/views/subscription/form.blade.php`)

```blade
@extends('layouts.app')

@section('content')
<div class="container">
    <h2>Subscribe to Our Service</h2>

    @if ($errors->any())
        <div class="alert alert-danger">
            <ul>
                @foreach ($errors->all() as $error)
                    <li>{{ $error }}</li>
                @endforeach
            </ul>
        </div>
    @endif

    <form action="{{ route('subscribe') }}" method="POST" id="subscription-form">
        @csrf
        <div class="form-group">
            <label for="plan">Select Plan</label>
            <select name="plan" id="plan" required>
                <option value="monthly">Monthly</option>
                <option value="yearly">Yearly</option>
            </select>
        </div>
        <div class="form-group">
            <label for="payment_method">Payment Method</label>
            <input type="text" name="payment_method" id="payment_method" required placeholder="Enter your payment method details">
        </div>
        <button type="submit" class="btn btn-primary">Subscribe</button>
    </form>
</div>
@endsection
```

### Blade View for Subscription Success (`resources/views/subscription/success.blade.php`)

```blade
@extends('layouts.app')

@section('content')
<div class="container">
    <h2>Subscription Successful!</h2>
    <p>Thank you for subscribing to our service. Your payment has been processed.</p>
</div>
@endsection
```

### Route Definitions (`routes/web.php`)

```php
use App\Http\Controllers\SubscriptionController;

Route::middleware(['auth'])->group(function () {
    Route::get('/subscribe', [SubscriptionController::class, 'showSubscriptionForm'])->name('subscription.form');
    Route::post('/subscribe', [SubscriptionController::class, 'subscribe'])->name('subscribe');
    Route::get('/subscription/success', [SubscriptionController::class, 'subscriptionSuccess'])->name('subscription.success');
    Route::post('/subscription/cancel', [SubscriptionController::class, 'cancelSubscription'])->name('subscription.cancel');
});
```

### Environment Configuration for Stripe (`.env`)

```env
STRIPE_KEY=your_stripe_public_key
STRIPE_SECRET=your_stripe_secret_key
```

### Additional Notes
- Ensure that the Laravel Cashier package is installed and configured in your Laravel application.
- The views assume a Bootstrap-based layout for styling purposes; adjust as needed based on your application's design.
