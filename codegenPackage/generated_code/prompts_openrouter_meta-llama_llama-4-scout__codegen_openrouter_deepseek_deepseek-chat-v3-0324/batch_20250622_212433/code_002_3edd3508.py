"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: "Write a code snippet in JavaScript to create a scheduling system for classes in a dental education institution, considering a mixed modality schedule with varying class days and times, such as those listed for INESO's specializations."
Generated: DETERMINISTIC_3edd3508e6a62cf1
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Class Scheduling System for Dental Education Institution
 * Supports mixed modality schedules with varying class days and times
 */

class ClassSchedule {
  /**
   * @param {Object} config - Configuration for the schedule system
   * @param {string} config.institutionName - Name of the institution
   * @param {Array} config.specializations - List of available specializations
   */
  constructor(config) {
    this.institutionName = config.institutionName || 'Dental Education Institution';
    this.specializations = config.specializations || [];
    this.schedules = {};
    this.initializeSchedules();
  }

  /**
   * Initialize schedules for each specialization
   */
  initializeSchedules() {
    this.specializations.forEach(spec => {
      this.schedules[spec] = {
        classes: [],
        modalities: []
      };
    });
  }

  /**
   * Add a class to a specialization's schedule
   * @param {string} specialization - Name of the specialization
   * @param {Object} classInfo - Class information
   * @param {string} classInfo.name - Class name
   * @param {string} classInfo.modality - Class modality (e.g., 'in-person', 'online', 'hybrid')
   * @param {Array} classInfo.days - Days of the week (e.g., ['Mon', 'Wed'])
   * @param {string} classInfo.startTime - Start time (e.g., '09:00')
   * @param {string} classInfo.endTime - End time (e.g., '11:00')
   * @param {string} classInfo.instructor - Instructor name
   * @returns {boolean} True if class was added successfully
   */
  addClass(specialization, classInfo) {
    if (!this.schedules[specialization]) {
      console.error(`Specialization "${specialization}" not found`);
      return false;
    }

    if (!this.validateClassInfo(classInfo)) {
      console.error('Invalid class information');
      return false;
    }

    const schedule = this.schedules[specialization];
    schedule.classes.push(classInfo);

    // Track unique modalities
    if (!schedule.modalities.includes(classInfo.modality)) {
      schedule.modalities.push(classInfo.modality);
    }

    return true;
  }

  /**
   * Validate class information before adding to schedule
   * @param {Object} classInfo - Class information to validate
   * @returns {boolean} True if class info is valid
   */
  validateClassInfo(classInfo) {
    const requiredFields = ['name', 'modality', 'days', 'startTime', 'endTime', 'instructor'];
    for (const field of requiredFields) {
      if (!classInfo[field]) {
        console.error(`Missing required field: ${field}`);
        return false;
      }
    }

    if (!Array.isArray(classInfo.days) || classInfo.days.length === 0) {
      console.error('Days must be a non-empty array');
      return false;
    }

    if (!this.validateTimeFormat(classInfo.startTime) || !this.validateTimeFormat(classInfo.endTime)) {
      console.error('Invalid time format. Use HH:MM');
      return false;
    }

    return true;
  }

  /**
   * Validate time format (HH:MM)
   * @param {string} time - Time string to validate
   * @returns {boolean} True if time format is valid
   */
  validateTimeFormat(time) {
    return /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/.test(time);
  }

  /**
   * Get all classes for a specialization
   * @param {string} specialization - Name of the specialization
   * @returns {Array} List of classes or empty array if not found
   */
  getClasses(specialization) {
    if (!this.schedules[specialization]) {
      console.error(`Specialization "${specialization}" not found`);
      return [];
    }
    return this.schedules[specialization].classes;
  }

  /**
   * Get all modalities for a specialization
   * @param {string} specialization - Name of the specialization
   * @returns {Array} List of modalities or empty array if not found
   */
  getModalities(specialization) {
    if (!this.schedules[specialization]) {
      console.error(`Specialization "${specialization}" not found`);
      return [];
    }
    return this.schedules[specialization].modalities;
  }

  /**
   * Find classes by day for a specialization
   * @param {string} specialization - Name of the specialization
   * @param {string} day - Day to search for (e.g., 'Mon')
   * @returns {Array} List of classes on that day
   */
  getClassesByDay(specialization, day) {
    const classes = this.getClasses(specialization);
    return classes.filter(cls => cls.days.includes(day));
  }

  /**
   * Find classes by modality for a specialization
   * @param {string} specialization - Name of the specialization
   * @param {string} modality - Modality to search for (e.g., 'online')
   * @returns {Array} List of classes with that modality
   */
  getClassesByModality(specialization, modality) {
    const classes = this.getClasses(specialization);
    return classes.filter(cls => cls.modality === modality);
  }

  /**
   * Check for schedule conflicts for a given class
   * @param {string} specialization - Name of the specialization
   * @param {Object} classInfo - Class information to check
   * @returns {boolean} True if conflict exists
   */
  hasConflict(specialization, classInfo) {
    const classes = this.getClasses(specialization);
    const days = classInfo.days;
    const start = this.timeToMinutes(classInfo.startTime);
    const end = this.timeToMinutes(classInfo.endTime);

    for (const existingClass of classes) {
      if (existingClass.name === classInfo.name) continue;

      const existingDays = existingClass.days;
      const hasDayOverlap = days.some(day => existingDays.includes(day));
      
      if (hasDayOverlap) {
        const existingStart = this.timeToMinutes(existingClass.startTime);
        const existingEnd = this.timeToMinutes(existingClass.endTime);
        
        if ((start >= existingStart && start < existingEnd) ||
            (end > existingStart && end <= existingEnd) ||
            (start <= existingStart && end >= existingEnd)) {
          return true;
        }
      }
    }

    return false;
  }

  /**
   * Convert time string to minutes since midnight
   * @param {string} time - Time string (HH:MM)
   * @returns {number} Minutes since midnight
   */
  timeToMinutes(time) {
    const [hours, minutes] = time.split(':').map(Number);
    return hours * 60 + minutes;
  }

  /**
   * Generate a weekly schedule for a specialization
   * @param {string} specialization - Name of the specialization
   * @returns {Object} Weekly schedule organized by day
   */
  generateWeeklySchedule(specialization) {
    if (!this.schedules[specialization]) {
      console.error(`Specialization "${specialization}" not found`);
      return {};
    }

    const weeklySchedule = {
      Mon: [], Tue: [], Wed: [], Thu: [], Fri: [], Sat: [], Sun: []
    };

    const classes = this.getClasses(specialization);
    classes.forEach(cls => {
      cls.days.forEach(day => {
        if (weeklySchedule[day]) {
          weeklySchedule[day].push({
            name: cls.name,
            modality: cls.modality,
            startTime: cls.startTime,
            endTime: cls.endTime,
            instructor: cls.instructor
          });
        }
      });
    });

    // Sort classes by start time for each day
    for (const day in weeklySchedule) {
      weeklySchedule[day].sort((a, b) => 
        this.timeToMinutes(a.startTime) - this.timeToMinutes(b.startTime)
      );
    }

    return weeklySchedule;
  }
}

// Example usage:
/*
const dentalSchoolSchedule = new ClassSchedule({
  institutionName: "INESO",
  specializations: [
    "Orthodontics",
    "Endodontics",
    "Periodontics",
    "Prosthodontics"
  ]
});

const orthoClass = {
  name: "Advanced Orthodontic Techniques",
  modality: "hybrid",
  days: ["Mon", "Wed"],
  startTime: "14:00",
  endTime: "16:00",
  instructor: "Dr. Smith"
};

dentalSchoolSchedule.addClass("Orthodontics", orthoClass);

const weeklySchedule = dentalSchoolSchedule.generateWeeklySchedule("Orthodontics");
console.log(weeklySchedule);
*/
```
