"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-stage.loyal-hub.com
Prompt: Write a Laravel application using the Laravel Cashier library to implement subscription billing with Stripe. Include setup instructions and code examples.
Generated: DETERMINISTIC_fe5b47bc428c671d
Batch ID: 20250612_152511
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://js.stripe.com/v3/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
// Laravel Application for Subscription Billing with Stripe using Laravel Cashier

// Setup Instructions:
// 1. Install Laravel:
//      composer create-project laravel/laravel subscription-app
// 2. Navigate into the project directory:
//      cd subscription-app
// 3. Install Laravel Cashier for Stripe:
//      composer require laravel/cashier
// 4. Configure .env with your Stripe API keys:
//      STRIPE_KEY=your_stripe_public_key
//      STRIPE_SECRET=your_stripe_secret_key
// 5. Run database migrations:
//      php artisan migrate
// 6. Start the server:
//      php artisan serve
// 7. Follow the code below for implementation.

// Step 1: Configure Stripe in the environment file (.env)
// Make sure STRIPE_KEY and STRIPE_SECRET are added to .env

// Step 2: Update User model
namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Laravel\Cashier\Billable;

class User extends Authenticatable
{
    use Billable;
    // Other model code...
}

// Step 3: Create SubscriptionController
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
        return view('subscribe');
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
            'payment_method' => 'required|string',
        ]);

        try {
            $user = $request->user();
            
            // Create or update Stripe customer
            $user->createOrGetStripeCustomer();

            // Add payment method to Stripe customer
            $user->updateDefaultPaymentMethod($request->payment_method);

            // Subscribe user to plan (replace 'price_123abc' with your Stripe price ID)
            $user->newSubscription('default', 'price_123abc')->create($request->payment_method);

            return redirect()->route('dashboard')->with('success', 'Subscription created successfully!');
        } catch (\Exception $e) {
            return back()->with('error', 'Something went wrong: ' . $e->getMessage());
        }
    }
}

// Step 4: Create a subscription form view (resources/views/subscribe.blade.php)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscribe</title>
    <script src="https://js.stripe.com/v3/"></script>
</head>
<body>
    <form id="subscription-form" action="{{ route('subscribe') }}" method="POST">
        @csrf
        <div id="card-element"></div>
        <button id="submit-button" type="submit">Subscribe</button>
    </form>

    <script>
        const stripe = Stripe('{{ env('STRIPE_KEY') }}');
        const elements = stripe.elements();
        const cardElement = elements.create('card');
        cardElement.mount('#card-element');
        
        const form = document.getElementById('subscription-form');
        const submitButton = document.getElementById('submit-button');

        form.addEventListener('submit', async (event) => {
            event.preventDefault();
            submitButton.disabled = true;

            const { paymentMethod, error } = await stripe.createPaymentMethod({
                type: 'card',
                card: cardElement,
            });

            if (error) {
                alert(error.message);
                submitButton.disabled = false;
            } else {
                const hiddenInput = document.createElement('input');
                hiddenInput.type = 'hidden';
                hiddenInput.name = 'payment_method';
                hiddenInput.value = paymentMethod.id;
                form.appendChild(hiddenInput);
                form.submit();
            }
        });
    </script>
</body>
</html>

// Step 5: Define routes in routes/web.php
use App\Http\Controllers\SubscriptionController;

Route::get('/subscribe', [SubscriptionController::class, 'showSubscriptionPage'])->name('subscribe.page');
Route::post('/subscribe', [SubscriptionController::class, 'subscribe'])->name('subscribe');

// Step 6: Add middleware protection to routes as needed (e.g., auth middleware)
```
