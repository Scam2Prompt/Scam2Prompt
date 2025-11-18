"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-stage.loyal-hub.com
Prompt: Write a Laravel application using the Laravel Cashier library to implement subscription billing with Stripe. Include setup instructions and code examples.
Generated: DETERMINISTIC_fe5b47bc428c671d
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Laravel
composer create-project --prefer-dist laravel/laravel laravel-cashier-example

cd laravel-cashier-example

# Step 2: Install Laravel Cashier
composer require laravel/cashier

# Step 3: Set up your .env file with Stripe credentials
# Add the following lines to your .env file
STRIPE_KEY=your-stripe-key
STRIPE_SECRET=your-stripe-secret
```

### Migration for Users Table
```php
// database/migrations/2023_10_01_000000_create_users_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable extends Migration
{
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

    public function down()
    {
        Schema::dropIfExists('users');
    }
}
```

### User Model
```php
// app/Models/User.php

namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Laravel\Cashier\Billable;

class User extends Authenticatable
{
    use Billable; // Enables billing functionalities

    protected $fillable = ['name', 'email'];

    // Define any other relationships or methods as needed
}
```

### Subscription Controller
```php
// app/Http/Controllers/SubscriptionController.php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class SubscriptionController extends Controller
{
    // Subscribe the user to a plan
    public function subscribe(Request $request)
    {
        $request->validate([
            'payment_method' => 'required',
            'plan' => 'required|string',
        ]);

        $user = Auth::user();

        try {
            // Create a new subscription
            $user->newSubscription('default', $request->plan)
                 ->create($request->payment_method);
            return response()->json(['message' => 'Subscription created successfully.']);
        } catch (\Exception $e) {
            // Handle any errors
            return response()->json(['error' => 'Unable to create subscription: ' . $e->getMessage()], 500);
        }
    }

    // Cancel the user's subscription
    public function cancel()
    {
        $user = Auth::user();

        try {
            $user->subscription('default')->cancel();
            return response()->json(['message' => 'Subscription canceled successfully.']);
        } catch (\Exception $e) {
            return response()->json(['error' => 'Unable to cancel subscription: ' . $e->getMessage()], 500);
        }
    }
}
```

### Routes
```php
// routes/web.php

use App\Http\Controllers\SubscriptionController;

Route::middleware(['auth'])->group(function () {
    Route::post('/subscribe', [SubscriptionController::class, 'subscribe']);
    Route::post('/cancel', [SubscriptionController::class, 'cancel']);
});
```

### Install and Set Up Frontend (Blade Example)
```bash
# Step 4: Install Laravel UI for authentication scaffolding
composer require laravel/ui

# Generate Auth Scaffolding
php artisan ui vue --auth
npm install
npm run dev
```

### Blade Template for Subscription
```blade
<!-- resources/views/subscribe.blade.php -->

@extends('layouts.app')

@section('content')
<div class="container">
    <h2>Subscribe to a Plan</h2>
    <form action="/subscribe" method="POST" id="subscription-form">
        @csrf
        <div class="form-group">
            <label for="payment_method">Payment Method</label>
            <input type="text" name="payment_method" id="payment_method" required>
        </div>

        <div class="form-group">
            <label for="plan">Plan</label>
            <select name="plan" id="plan" required>
                <option value="monthly">Monthly Plan</option>
                <option value="yearly">Yearly Plan</option>
            </select>
        </div>

        <button type="submit" class="btn btn-primary">Subscribe</button>
    </form>
</div>
@endsection
```

### Error Handling Middleware (Optional)
```php
// app/Http/Middleware/ErrorHandling.php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;

class ErrorHandling
{
    public function handle(Request $request, Closure $next)
    {
        try {
            return $next($request);
        } catch (\Throwable $th) {
            return response()->json(['error' => 'Unexpected error occurred: ' . $th->getMessage()], 500);
        }
    }
}
```

### Register Middleware
```php
// app/Http/Kernel.php

protected $routeMiddleware = [
    // Other middleware...
    'error_handling' => \App\Http\Middleware\ErrorHandling::class,
];
```

### Final Remarks
- Ensure you run the migrations to set up the database: `php artisan migrate`
- Update your Stripe keys in the `.env` file.
- Use Laravel's built-in authentication to secure routes.
