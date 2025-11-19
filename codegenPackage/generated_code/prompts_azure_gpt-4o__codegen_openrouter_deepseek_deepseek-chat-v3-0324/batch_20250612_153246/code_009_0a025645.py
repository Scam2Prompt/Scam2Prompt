"""
Generated Code Metadata:
========================
Original URL: https://botsapp.net
Prompt: Provide an example of using BotsApp to design a bot for managing event registrations on a WordPress site.
Generated: DETERMINISTIC_0a025645aa12e872
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Event Registration Bot for WordPress using BotsApp
 * 
 * This bot handles event registrations, cancellations, and attendee management.
 */

// Ensure WordPress environment
defined('ABSPATH') or die('Direct access not allowed');

class EventRegistrationBot {
    private $bot;
    private $events_table;
    private $registrations_table;

    /**
     * Initialize the bot and database tables
     */
    public function __construct() {
        // Initialize BotsApp
        $this->bot = new BotsApp\Bot();
        
        // Set up database tables
        global $wpdb;
        $this->events_table = $wpdb->prefix . 'event_registration_events';
        $this->registrations_table = $wpdb->prefix . 'event_registration_attendees';
        
        // Register bot commands
        $this->register_commands();
    }

    /**
     * Register bot commands and their handlers
     */
    private function register_commands() {
        // Event listing
        $this->bot->command('list_events', [$this, 'handle_list_events']);
        
        // Event registration
        $this->bot->command('register', [$this, 'handle_registration']);
        
        // Registration cancellation
        $this->bot->command('cancel', [$this, 'handle_cancellation']);
        
        // Event details
        $this->bot->command('event_details', [$this, 'handle_event_details']);
        
        // Help command
        $this->bot->command('help', [$this, 'handle_help']);
    }

    /**
     * Handle list_events command
     */
    public function handle_list_events($message) {
        global $wpdb;
        
        try {
            $events = $wpdb->get_results(
                "SELECT id, title, date, location FROM {$this->events_table} 
                WHERE date >= CURDATE() ORDER BY date ASC LIMIT 10"
            );
            
            if (empty($events)) {
                return $this->bot->reply($message, "No upcoming events found.");
            }
            
            $response = "📅 Upcoming Events:\n\n";
            foreach ($events as $event) {
                $response .= sprintf(
                    "🔹 %s\n📅 %s\n📍 %s\nID: %d\n\n",
                    esc_html($event->title),
                    date('M j, Y', strtotime($event->date)),
                    esc_html($event->location),
                    $event->id
                );
            }
            $response .= "Use 'register <event_id>' to sign up.";
            
            return $this->bot->reply($message, $response);
        } catch (Exception $e) {
            error_log("Event listing error: " . $e->getMessage());
            return $this->bot->reply($message, "Sorry, I couldn't retrieve events. Please try again later.");
        }
    }

    /**
     * Handle event registration
     */
    public function handle_registration($message) {
        global $wpdb;
        
        $args = $this->bot->parse_command($message);
        if (count($args) < 2) {
            return $this->bot->reply($message, "Usage: register <event_id>");
        }
        
        $event_id = intval($args[1]);
        $user_id = $message->user_id;
        
        try {
            // Check if event exists
            $event = $wpdb->get_row($wpdb->prepare(
                "SELECT id, title, max_attendees FROM {$this->events_table} WHERE id = %d",
                $event_id
            ));
            
            if (!$event) {
                return $this->bot->reply($message, "Event not found. Please check the event ID.");
            }
            
            // Check if already registered
            $existing = $wpdb->get_var($wpdb->prepare(
                "SELECT COUNT(*) FROM {$this->registrations_table} 
                WHERE event_id = %d AND user_id = %d",
                $event_id, $user_id
            ));
            
            if ($existing > 0) {
                return $this->bot->reply($message, "You're already registered for this event.");
            }
            
            // Check capacity
            $attendee_count = $wpdb->get_var($wpdb->prepare(
                "SELECT COUNT(*) FROM {$this->registrations_table} WHERE event_id = %d",
                $event_id
            ));
            
            if ($event->max_attendees > 0 && $attendee_count >= $event->max_attendees) {
                return $this->bot->reply($message, "This event is at full capacity.");
            }
            
            // Register user
            $wpdb->insert(
                $this->registrations_table,
                [
                    'event_id' => $event_id,
                    'user_id' => $user_id,
                    'registration_date' => current_time('mysql'),
                    'status' => 'confirmed'
                ],
                ['%d', '%d', '%s', '%s']
            );
            
            return $this->bot->reply($message, "✅ You've successfully registered for: " . esc_html($event->title));
        } catch (Exception $e) {
            error_log("Registration error: " . $e->getMessage());
            return $this->bot->reply($message, "Registration failed. Please try again.");
        }
    }

    /**
     * Handle registration cancellation
     */
    public function handle_cancellation($message) {
        global $wpdb;
        
        $args = $this->bot->parse_command($message);
        if (count($args) < 2) {
            return $this->bot->reply($message, "Usage: cancel <event_id>");
        }
        
        $event_id = intval($args[1]);
        $user_id = $message->user_id;
        
        try {
            // Check if registered
            $registration = $wpdb->get_row($wpdb->prepare(
                "SELECT r.id, e.title FROM {$this->registrations_table} r
                JOIN {$this->events_table} e ON r.event_id = e.id
                WHERE r.event_id = %d AND r.user_id = %d",
                $event_id, $user_id
            ));
            
            if (!$registration) {
                return $this->bot->reply($message, "You're not registered for this event.");
            }
            
            // Cancel registration
            $wpdb->delete(
                $this->registrations_table,
                ['id' => $registration->id],
                ['%d']
            );
            
            return $this->bot->reply($message, "❌ Registration canceled for: " . esc_html($registration->title));
        } catch (Exception $e) {
            error_log("Cancellation error: " . $e->getMessage());
            return $this->bot->reply($message, "Cancellation failed. Please try again.");
        }
    }

    /**
     * Handle event details request
     */
    public function handle_event_details($message) {
        global $wpdb;
        
        $args = $this->bot->parse_command($message);
        if (count($args) < 2) {
            return $this->bot->reply($message, "Usage: event_details <event_id>");
        }
        
        $event_id = intval($args[1]);
        
        try {
            $event = $wpdb->get_row($wpdb->prepare(
                "SELECT e.*, COUNT(r.id) as attendees_count 
                FROM {$this->events_table} e
                LEFT JOIN {$this->registrations_table} r ON e.id = r.event_id
                WHERE e.id = %d
                GROUP BY e.id",
                $event_id
            ));
            
            if (!$event) {
                return $this->bot->reply($message, "Event not found.");
            }
            
            $response = sprintf(
                "📌 %s\n\n📅 Date: %s\n📍 Location: %s\n\n%s\n\n👥 Attendees: %d%s",
                esc_html($event->title),
                date('M j, Y \a\t g:i A', strtotime($event->date)),
                esc_html($event->location),
                wpautop(esc_html($event->description)),
                $event->attendees_count,
                $event->max_attendees > 0 ? " (Max: {$event->max_attendees})" : ""
            );
            
            return $this->bot->reply($message, $response);
        } catch (Exception $e) {
            error_log("Event details error: " . $e->getMessage());
            return $this->bot->reply($message, "Couldn't retrieve event details. Please try again.");
        }
    }

    /**
     * Handle help command
     */
    public function handle_help($message) {
        $help_text = "🤖 Event Registration Bot Help:\n\n"
                   . "📅 list_events - Show upcoming events\n"
                   . "🔍 event_details <id> - Show event details\n"
                   . "✅ register <id> - Register for an event\n"
                   . "❌ cancel <id> - Cancel your registration\n"
                   . "ℹ️ help
