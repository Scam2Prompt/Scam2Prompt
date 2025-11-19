"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Explain how to implement event broadcasting in Laravel using the Echo library, and provide a code example.
Generated: DETERMINISTIC_880ad3619cf3329b
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
// Step 1: Create an Event
// Run the following Artisan command to create a new event
// php artisan make:event UserRegistered

namespace App\Events;

use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

class UserRegistered
{
    use Dispatchable, SerializesModels;

    public $user;

    /**
     * Create a new event instance.
     *
     * @param  \App\Models\User  $user
     * @return void
     */
    public function __construct($user)
    {
        $this->user = $user;
    }
}

// Step 2: Create a Listener
// Run the following Artisan command to create a new listener
// php artisan make:listener SendWelcomeEmail

namespace App\Listeners;

use App\Events\UserRegistered;
use Illuminate\Support\Facades\Mail;

class SendWelcomeEmail
{
    /**
     * Handle the event.
     *
     * @param  UserRegistered  $event
     * @return void
     */
    public function handle(UserRegistered $event)
    {
        // Send a welcome email to the registered user
        Mail::to($event->user->email)->send(new \App\Mail\WelcomeEmail($event->user));
    }
}

// Step 3: Register the Event and Listener
// In the EventServiceProvider, register the event and listener

namespace App\Providers;

use App\Events\UserRegistered;
use App\Listeners\SendWelcomeEmail;
use Illuminate\Foundation\Support\Providers\EventServiceProvider as ServiceProvider;

class EventServiceProvider extends ServiceProvider
{
    protected $listen = [
        UserRegistered::class => [
            SendWelcomeEmail::class,
        ],
    ];
}

// Step 4: Broadcasting the Event
// Update the event to implement the ShouldBroadcast interface

namespace App\Events;

use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

class UserRegistered implements ShouldBroadcast
{
    use Dispatchable, SerializesModels;

    public $user;

    public function __construct($user)
    {
        $this->user = $user;
    }

    public function broadcastOn()
    {
        return ['user-registered'];
    }
}

// Step 5: Trigger the Event
// In your controller, trigger the event when a user registers

namespace App\Http\Controllers;

use App\Events\UserRegistered;
use App\Models\User;
use Illuminate\Http\Request;

class AuthController extends Controller
{
    public function register(Request $request)
    {
        // Validate the request
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8|confirmed',
        ]);

        // Create the user
        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => bcrypt($request->password),
        ]);

        // Fire the UserRegistered event
        event(new UserRegistered($user));

        return response()->json(['message' => 'User registered successfully!'], 201);
    }
}

// Step 6: Set up Laravel Echo
// In your JavaScript file, set up Laravel Echo to listen for the event

import Echo from 'laravel-echo';
import Pusher from 'pusher-js';

window.Pusher = Pusher;

window.Echo = new Echo({
    broadcaster: 'pusher',
    key: 'your-pusher-key',
    cluster: 'your-pusher-cluster',
    encrypted: true,
});

// Listen for the event
window.Echo.channel('user-registered')
    .listen('UserRegistered', (e) => {
        console.log('User registered:', e.user);
    });
```

Make sure to replace `'your-pusher-key'` and `'your-pusher-cluster'` with your actual Pusher credentials. Also, ensure that you have set up Pusher in your Laravel application and configured the broadcasting settings in `config/broadcasting.php`.
