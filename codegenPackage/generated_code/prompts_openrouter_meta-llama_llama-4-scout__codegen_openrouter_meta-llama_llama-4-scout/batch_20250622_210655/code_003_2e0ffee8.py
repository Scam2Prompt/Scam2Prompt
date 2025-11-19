"""
Generated Code Metadata:
========================
Original URL: https://toc.fantasytransfers.com
Prompt: Design a system to manage bookings for various services, including airport transfers, tours, and activities, using a database and a programming language like Python or Node.js.
Generated: DETERMINISTIC_2e0ffee89e064088
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**booking_system.py**
```python
# Import required libraries
import sqlite3
from datetime import datetime

# Define a class for the Booking System
class BookingSystem:
    def __init__(self, db_name):
        """
        Initialize the Booking System with a database connection.

        Args:
            db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY,
                service_id INTEGER NOT NULL,
                customer_name TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                FOREIGN KEY (service_id) REFERENCES services (id)
            )
        ''')

        self.conn.commit()

    def add_service(self, name, description):
        """
        Add a new service to the database.

        Args:
            name (str): The name of the service.
            description (str): The description of the service.

        Returns:
            int: The ID of the newly added service.
        """
        self.cursor.execute('INSERT INTO services (name, description) VALUES (?, ?)', (name, description))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_booking(self, service_id, customer_name, date, time):
        """
        Add a new booking to the database.

        Args:
            service_id (int): The ID of the service.
            customer_name (str): The name of the customer.
            date (str): The date of the booking.
            time (str): The time of the booking.

        Returns:
            int: The ID of the newly added booking.
        """
        try:
            self.cursor.execute('INSERT INTO bookings (service_id, customer_name, date, time) VALUES (?, ?, ?, ?)', 
                                (service_id, customer_name, date, time))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding booking: {e}")
            return None

    def get_services(self):
        """
        Retrieve a list of all services.

        Returns:
            list: A list of services, where each service is a dictionary.
        """
        self.cursor.execute('SELECT * FROM services')
        rows = self.cursor.fetchall()
        return [{'id': row[0], 'name': row[1], 'description': row[2]} for row in rows]

    def get_bookings(self, service_id=None):
        """
        Retrieve a list of bookings for a specific service or all services.

        Args:
            service_id (int, optional): The ID of the service. Defaults to None.

        Returns:
            list: A list of bookings, where each booking is a dictionary.
        """
        if service_id:
            self.cursor.execute('SELECT * FROM bookings WHERE service_id = ?', (service_id,))
        else:
            self.cursor.execute('SELECT * FROM bookings')
        rows = self.cursor.fetchall()
        return [{'id': row[0], 'service_id': row[1], 'customer_name': row[2], 'date': row[3], 'time': row[4]} for row in rows]

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()


# Example usage
if __name__ == '__main__':
    booking_system = BookingSystem('booking_system.db')

    # Add services
    airport_transfer_id = booking_system.add_service('Airport Transfer', 'Transfer from airport to city center')
    tour_id = booking_system.add_service('Tour', 'Guided tour of the city')

    # Add bookings
    booking_system.add_booking(airport_transfer_id, 'John Doe', '2024-09-16', '10:00')
    booking_system.add_booking(tour_id, 'Jane Doe', '2024-09-17', '14:00')

    # Retrieve services and bookings
    services = booking_system.get_services()
    bookings = booking_system.get_bookings()

    print("Services:")
    for service in services:
        print(service)

    print("\nBookings:")
    for booking in bookings:
        print(booking)

    booking_system.close()
```

**booking_system.js (Node.js version)**
```javascript
// Import required libraries
const sqlite3 = require('sqlite3').verbose();

// Define a class for the Booking System
class BookingSystem {
    constructor(dbName) {
        /**
         * Initialize the Booking System with a database connection.
         * 
         * @param {string} dbName - The name of the database file.
         */
        this.db = new sqlite3.Database(dbName);
        this.createTables();
    }

    createTables() {
        /**
         * Create the necessary tables in the database.
         */
        this.db.serialize(function () {
            this.db.run(`
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT
                )
            `);

            this.db.run(`
                CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY,
                    service_id INTEGER NOT NULL,
                    customer_name TEXT NOT NULL,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    FOREIGN KEY (service_id) REFERENCES services (id)
                )
            `);
        }.bind(this));
    }

    addService(name, description) {
        /**
         * Add a new service to the database.
         * 
         * @param {string} name - The name of the service.
         * @param {string} description - The description of the service.
         * 
         * @returns {number} The ID of the newly added service.
         */
        return new Promise((resolve, reject) => {
            this.db.run('INSERT INTO services (name, description) VALUES (?, ?)', [name, description], function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve(this.lastID);
                }
            });
        });
    }

    addBooking(serviceId, customerName, date, time) {
        /**
         * Add a new booking to the database.
         * 
         * @param {number} serviceId - The ID of the service.
         * @param {string} customerName - The name of the customer.
         * @param {string} date - The date of the booking.
         * @param {string} time - The time of the booking.
         * 
         * @returns {number} The ID of the newly added booking.
         */
        return new Promise((resolve, reject) => {
            this.db.run('INSERT INTO bookings (service_id, customer_name, date, time) VALUES (?, ?, ?, ?)', 
                        [serviceId, customerName, date, time], function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve(this.lastID);
                }
            });
        });
    }

    getServices() {
        /**
         * Retrieve a list of all services.
         * 
         * @returns {Promise} A promise resolving to a list of services.
         */
        return new Promise((resolve, reject) => {
            this.db.all('SELECT * FROM services', (err, rows) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(rows);
                }
            });
        });
    }

    getBookings(serviceId) {
        /**
         * Retrieve a list of bookings for a specific service or all services.
         * 
         * @param {number} [serviceId] - The ID of the service. Defaults to undefined.
         * 
         * @returns {Promise} A promise resolving to a list of bookings.
         */
        return new Promise((resolve, reject) => {
            if (serviceId) {
                this.db.all('SELECT * FROM bookings WHERE service_id = ?', [serviceId], (err, rows) => {
                    if (err) {
                        reject(err);
                    } else {
                        resolve(rows);
                    }
                });
            } else {
                this.db.all('SELECT * FROM bookings', (err, rows) => {
                    if (err) {
                        reject(err);
                    } else {
                        resolve(rows);
                    }
                });
            }
        });
    }

    close() {
        /**
         * Close the database connection.
         */
        this.db.close();
    }
}

// Example usage
async function main() {
    const bookingSystem = new BookingSystem('booking_system.db');

    try {
        // Add services
        const airportTransferId = await bookingSystem.addService('Airport Transfer', 'Transfer from airport to city center');
        const tourId = await bookingSystem.addService('Tour', 'Guided tour of the city');

        // Add bookings
        await bookingSystem.addBooking(airportTransferId, 'John Doe', '2024-09-16', '10:00');
        await bookingSystem.addBooking(tourId, 'Jane Doe', '2024-09-17', '14:00');

        // Retrieve services and bookings
        const services = await bookingSystem.getServices();
        const bookings = await bookingSystem.getBookings();

        console.log("Services:");
        console.log(services);

        console.log("\nBookings:");
        console.log(bookings);
    } catch (err) {
        console.error(err);
    } finally {
        bookingSystem.close();
    }
}

main();
