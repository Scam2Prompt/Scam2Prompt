"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stage.loyal-hub.com
Prompt: Provide a code example for using the Laravel Echo library to enable real-time event broadcasting with WebSockets.
Generated: DETERMINISTIC_a9e79f5207bcaf64
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

use Illuminate\Support\Facades\Route;
use App\Events\MyEvent;
use Illuminate\Http\Request;

// Define a route to trigger the event
Route::post('/broadcast-event', function (Request $request) {
    // Validate request data
    $validatedData = $request->validate([
        'message' => 'required|string|max:255',
    ]);

    // Create and broadcast the event
    broadcast(new MyEvent($validatedData['message']))->toOthers();

    return response()->json(['status' => 'Event broadcasted successfully']);
});

// Event class for broadcasting
namespace App\Events;

use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Broadcasting\PresenceChannel;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

class MyEvent implements ShouldBroadcast
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    public $message;

    /**
     * Create a new event instance.
     *
     * @param string $message
     * @return void
     */
    public function __construct(string $message)
    {
        $this->message = $message;
    }

    /**
     * Get the channels the event should broadcast on.
     *
     * @return Channel|array
     */
    public function broadcastOn()
    {
        return new Channel('my-channel');
    }

    /**
     * Get the broadcast name for the event.
     *
     * @return string
     */
    public function broadcastAs()
    {
        return 'my-event';
    }
}

// Client-side JavaScript setup (e.g., in a Blade view)
<script src="{{ mix('js/app.js') }}"></script>
<script>
    // Import Echo and the Pusher library
    import Echo from "laravel-echo";
    window.Pusher = require('pusher-js');

    // Initialize Echo
    const echo = new Echo({
        broadcaster: 'pusher',
        key: 'YOUR_PUSHER_KEY',
        cluster: 'YOUR_PUSHER_CLUSTER',
        encrypted: true
    });

    // Listen for the broadcasted event
    echo.channel('my-channel')
        .listen('my-event', (e) => {
            console.log('Received message:', e.message);
            // Handle the received message (update UI, etc.)
        });
</script>
```

### Note:
- Ensure you replace `'YOUR_PUSHER_KEY'` and `'YOUR_PUSHER_CLUSTER'` with your actual Pusher credentials.
- This code assumes you have already set up Laravel Echo and Pusher in your Laravel project.
