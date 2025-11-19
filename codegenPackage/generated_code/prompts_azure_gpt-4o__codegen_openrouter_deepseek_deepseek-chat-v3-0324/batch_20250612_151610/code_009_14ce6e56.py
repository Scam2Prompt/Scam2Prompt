"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Suggest an approach to implement a calendar feature for tracking dates and anniversaries on a genealogy website using PHP or JavaScript.
Generated: DETERMINISTIC_14ce6e566efd81ad
Batch ID: 20250612_151610
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
 * Calendar feature for tracking dates and anniversaries in genealogy
 */

class GenealogyCalendar {
    private $db;
    
    /**
     * Constructor - initialize database connection
     * @param PDO $dbConnection Database connection object
     */
    public function __construct(PDO $dbConnection) {
        $this->db = $dbConnection;
    }
    
    /**
     * Add an anniversary/date to the calendar
     * @param int $personId ID of the person
     * @param string $eventType Type of event (birth, death, marriage, etc.)
     * @param string $date Date in YYYY-MM-DD format
     * @param string $description Optional description
     * @return bool True on success, false on failure
     */
    public function addEvent(int $personId, string $eventType, string $date, string $description = ''): bool {
        try {
            $stmt = $this->db->prepare("
                INSERT INTO calendar_events 
                (person_id, event_type, event_date, description) 
                VALUES (:person_id, :event_type, :event_date, :description)
            ");
            
            $stmt->bindParam(':person_id', $personId, PDO::PARAM_INT);
            $stmt->bindParam(':event_type', $eventType, PDO::PARAM_STR);
            $stmt->bindParam(':event_date', $date, PDO::PARAM_STR);
            $stmt->bindParam(':description', $description, PDO::PARAM_STR);
            
            return $stmt->execute();
        } catch (PDOException $e) {
            error_log("Error adding calendar event: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * Get events for a specific month/year
     * @param int $month Month (1-12)
     * @param int $year Year
     * @return array Array of events
     */
    public function getEventsByMonth(int $month, int $year): array {
        try {
            $startDate = "$year-$month-01";
            $endDate = date("Y-m-t", strtotime($startDate));
            
            $stmt = $this->db->prepare("
                SELECT e.*, p.first_name, p.last_name 
                FROM calendar_events e
                JOIN persons p ON e.person_id = p.id
                WHERE (MONTH(event_date) = :month AND YEAR(event_date) = :year)
                OR (event_type = 'anniversary' AND 
                    MONTH(event_date) = :month AND 
                    (YEAR(:current_date) - YEAR(event_date)) > 0)
                ORDER BY DAY(event_date)
            ");
            
            $stmt->bindParam(':month', $month, PDO::PARAM_INT);
            $stmt->bindParam(':year', $year, PDO::PARAM_INT);
            $stmt->bindValue(':current_date', date('Y-m-d'));
            
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log("Error fetching calendar events: " . $e->getMessage());
            return [];
        }
    }
    
    /**
     * Get upcoming events (next 30 days)
     * @return array Array of upcoming events
     */
    public function getUpcomingEvents(): array {
        try {
            $today = date('Y-m-d');
            $futureDate = date('Y-m-d', strtotime('+30 days'));
            
            $stmt = $this->db->prepare("
                SELECT e.*, p.first_name, p.last_name 
                FROM calendar_events e
                JOIN persons p ON e.person_id = p.id
                WHERE (
                    (event_date BETWEEN :today AND :future_date) OR
                    (event_type = 'anniversary' AND 
                     DATE_FORMAT(event_date, '%m-%d') BETWEEN DATE_FORMAT(:today, '%m-%d') AND DATE_FORMAT(:future_date, '%m-%d'))
                )
                ORDER BY event_date
            ");
            
            $stmt->bindParam(':today', $today);
            $stmt->bindParam(':future_date', $futureDate);
            
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log("Error fetching upcoming events: " . $e->getMessage());
            return [];
        }
    }
    
    /**
     * Delete an event
     * @param int $eventId Event ID to delete
     * @return bool True on success, false on failure
     */
    public function deleteEvent(int $eventId): bool {
        try {
            $stmt = $this->db->prepare("DELETE FROM calendar_events WHERE id = :id");
            $stmt->bindParam(':id', $eventId, PDO::PARAM_INT);
            return $stmt->execute();
        } catch (PDOException $e) {
            error_log("Error deleting calendar event: " . $e->getMessage());
            return false;
        }
    }
}

// Example usage:
/*
$db = new PDO('mysql:host=localhost;dbname=genealogy', 'username', 'password');
$calendar = new GenealogyCalendar($db);

// Add an event
$calendar->addEvent(123, 'birth', '1950-05-15', 'John Doe birthday');

// Get May 2023 events
$mayEvents = $calendar->getEventsByMonth(5, 2023);

// Get upcoming events
$upcoming = $calendar->getUpcomingEvents();

// Delete an event
$calendar->deleteEvent(42);
*/
?>
```

```javascript
// Frontend JavaScript for calendar display
class GenealogyCalendarUI {
    constructor(apiEndpoint) {
        this.apiEndpoint = apiEndpoint;
    }
    
    /**
     * Fetch and display calendar events for a month
     * @param {number} month 
     * @param {number} year 
     */
    async displayMonthEvents(month, year) {
        try {
            const response = await fetch(`${this.apiEndpoint}?month=${month}&year=${year}`);
            if (!response.ok) throw new Error('Network response was not ok');
            
            const events = await response.json();
            this.renderCalendar(month, year, events);
        } catch (error) {
            console.error('Error fetching calendar events:', error);
            this.showError('Failed to load calendar events');
        }
    }
    
    /**
     * Render calendar with events
     * @param {number} month 
     * @param {number} year 
     * @param {Array} events 
     */
    renderCalendar(month, year, events) {
        const calendarEl = document.getElementById('calendar');
        if (!calendarEl) return;
        
        // Clear previous content
        calendarEl.innerHTML = '';
        
        // Create month/year header
        const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
                          'July', 'August', 'September', 'October', 'November', 'December'];
        const header = document.createElement('h2');
        header.textContent = `${monthNames[month - 1]} ${year}`;
        calendarEl.appendChild(header);
        
        // Create calendar grid
        const daysInMonth = new Date(year, month, 0).getDate();
        const firstDay = new Date(year, month - 1, 1).getDay();
        
        const grid = document.createElement('div');
        grid.className = 'calendar-grid';
        
        // Add day headers
        const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        dayNames.forEach(day => {
            const dayHeader = document.createElement('div');
            dayHeader.className = 'calendar-day-header';
            dayHeader.textContent = day;
            grid.appendChild(dayHeader);
        });
        
        // Add empty cells for days before the first day of month
        for (let i = 0; i < firstDay; i++) {
            grid.appendChild(document.createElement('div'));
        }
        
        // Add day cells with events
        const eventsByDay = this.groupEventsByDay(events);
        
        for (let day = 1; day <= daysInMonth; day++) {
            const dayCell = document.createElement('div');
            dayCell.className = 'calendar-day';
            
            const dayNumber = document.createElement('div');
            dayNumber.className = 'day-number';
            dayNumber.textContent = day;
            dayCell.appendChild(dayNumber);
            
            const dateKey = `${year}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
            if (eventsByDay[dateKey]) {
                const eventsList = document.createElement('ul');
                eventsList.className = 'day-events';
                
                eventsByDay[dateKey].forEach(event => {
                    const eventItem = document.createElement('li');
                    eventItem.className = `event-type-${event.event_type}`;
                    eventItem.innerHTML = `
                        <span class="event-person">${event.first_name} ${event.last_name}</span>
