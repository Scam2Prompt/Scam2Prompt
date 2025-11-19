"""
Generated Code Metadata:
========================
Original URL: https://stage.loyal-hub.com
Prompt: Provide code examples for using Laravel Echo to implement real-time event broadcasting in a web app.
Generated: DETERMINISTIC_d837e1fbaf6daaec
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
// routes/web.php
use App\Events\MessageSent;

Route::get('/', function () {
    return view('welcome');
});

Route::post('/send-message', function (Illuminate\Http\Request $request) {
    $message = $request->input('message');

    // Broadcast the event
    broadcast(new MessageSent($message))->toOthers();

    return response()->json(['status' => 'Message broadcasted successfully']);
});

// app/Events/MessageSent.php
namespace App\Events;

use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Broadcasting\PresenceChannel;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Queue\SerializesModels;

class MessageSent implements ShouldBroadcast
{
    use InteractsWithSockets, SerializesModels;

    public $message;

    /**
     * Create a new event instance.
     *
     * @param string $message
     */
    public function __construct($message)
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
        return new Channel('messages');
    }
}

// resources/js/bootstrap.js
import Echo from 'laravel-echo';
import Pusher from 'pusher-js';

// Configure Laravel Echo with Pusher
window.Pusher = Pusher;

window.Echo = new Echo({
    broadcaster: 'pusher',
    key: process.env.MIX_PUSHER_APP_KEY,
    cluster: process.env.MIX_PUSHER_APP_CLUSTER,
    forceTLS: true
});

// Listen for the 'MessageSent' event
window.Echo.channel('messages')
    .listen('MessageSent', (event) => {
        console.log('Message received:', event.message);
    });

// resources/views/welcome.blade.php
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laravel Echo Example</title>
    <script src="{{ mix('js/app.js') }}" defer></script>
</head>
<body>
    <h1>Laravel Echo Real-Time Example</h1>
    <form id="messageForm">
        <input type="text" id="messageInput" placeholder="Enter your message">
        <button type="submit">Send Message</button>
    </form>

    <script>
        document.getElementById('messageForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const message = document.getElementById('messageInput').value;

            try {
                const response = await fetch('/send-message', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
                    },
                    body: JSON.stringify({ message })
                });

                const data = await response.json();
                console.log(data.status);
            } catch (error) {
                console.error('Error sending message:', error);
            }
        });
    </script>
</body>
</html>

// .env
MIX_PUSHER_APP_KEY=your-pusher-app-key
MIX_PUSHER_APP_CLUSTER=your-pusher-app-cluster

// webpack.mix.js
const mix = require('laravel-mix');

mix.js('resources/js/app.js', 'public/js')
   .sass('resources/sass/app.scss', 'public/css')
   .sourceMaps();
```
