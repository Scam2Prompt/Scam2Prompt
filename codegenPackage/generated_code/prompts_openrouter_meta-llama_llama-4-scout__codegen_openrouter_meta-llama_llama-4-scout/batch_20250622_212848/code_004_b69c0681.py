"""
Generated Code Metadata:
========================
Original URL: https://duchessgarden.sn
Prompt: Create a JavaScript function that implements a booking system for a beauty salon, allowing clients to reserve appointments for services like "Damp Massage du Dos" and "Manucure Pédicure".
Generated: DETERMINISTIC_b69c0681c1c34ec2
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Beauty Salon Booking System
 */

// Define a class for Service
class Service {
  /**
   * Constructor for Service
   * @param {string} name - Service name
   * @param {number} duration - Service duration in minutes
   * @param {number} price - Service price
   */
  constructor(name, duration, price) {
    this.name = name;
    this.duration = duration;
    this.price = price;
  }
}

// Define a class for Appointment
class Appointment {
  /**
   * Constructor for Appointment
   * @param {Date} date - Appointment date
   * @param {Service} service - Service for the appointment
   * @param {string} clientName - Client name
   */
  constructor(date, service, clientName) {
    this.date = date;
    this.service = service;
    this.clientName = clientName;
  }
}

// Define a class for BookingSystem
class BookingSystem {
  /**
   * Constructor for BookingSystem
   */
  constructor() {
    this.services = [];
    this.appointments = [];
  }

  /**
   * Add a service to the booking system
   * @param {Service} service - Service to add
   */
  addService(service) {
    this.services.push(service);
  }

  /**
   * Book an appointment
   * @param {Date} date - Appointment date
   * @param {string} serviceName - Service name
   * @param {string} clientName - Client name
   * @throws {Error} If service not found or date is invalid
   */
  bookAppointment(date, serviceName, clientName) {
    const service = this.services.find(s => s.name === serviceName);
    if (!service) {
      throw new Error(`Service '${serviceName}' not found`);
    }
    if (!(date instanceof Date) || isNaN(date.getTime())) {
      throw new Error('Invalid date');
    }
    const appointment = new Appointment(date, service, clientName);
    this.appointments.push(appointment);
    return appointment;
  }

  /**
   * Get all appointments
   * @returns {Appointment[]} All appointments
   */
  getAppointments() {
    return this.appointments;
  }

  /**
   * Get all services
   * @returns {Service[]} All services
   */
  getServices() {
    return this.services;
  }
}

// Example usage
function main() {
  const bookingSystem = new BookingSystem();

  // Create services
  const dampMassage = new Service("Damp Massage du Dos", 30, 40);
  const manucurePedicure = new Service("Manucure Pédicure", 60, 60);

  // Add services to the booking system
  bookingSystem.addService(dampMassage);
  bookingSystem.addService(manucurePedicure);

  try {
    // Book appointments
    const appointment1 = bookingSystem.bookAppointment(new Date('2024-09-17T10:00:00'), "Damp Massage du Dos", "John Doe");
    const appointment2 = bookingSystem.bookAppointment(new Date('2024-09-18T11:00:00'), "Manucure Pédicure", "Jane Doe");

    // Display appointments
    console.log('Appointments:');
    bookingSystem.getAppointments().forEach(appointment => {
      console.log(`Date: ${appointment.date.toLocaleString()}, Service: ${appointment.service.name}, Client: ${appointment.clientName}`);
    });

    // Display services
    console.log('\nServices:');
    bookingSystem.getServices().forEach(service => {
      console.log(`Name: ${service.name}, Duration: ${service.duration} minutes, Price: $${service.price}`);
    });
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
