"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Create a smart contract for managing course enrollments on a blockchain platform, inspired by the Sui Foundation's potential focus on decentralized education.
Generated: DETERMINISTIC_425c6fe767125ce5
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Smart contract for managing course enrollments on a blockchain platform
//! Inspired by decentralized education initiatives

use sui::object::{UID, ID};
use sui::transfer;
use sui::tx_context::TxContext;
use sui::event;
use sui::balance::{Balance, Supply};
use sui::coin::Coin;
use sui::dynamic_field;
use std::string::String;

/// Course object representing an educational course
struct Course has key, store {
    id: UID,
    name: String,
    description: String,
    instructor: String,
    max_capacity: u64,
    current_enrollment: u64,
    price: u64,
    active: bool
}

/// Enrollment object representing a student's enrollment in a course
struct Enrollment has key, store {
    id: UID,
    course_id: ID,
    student_address: address,
    enrollment_date: u64,
    completed: bool
}

/// Certificate object issued upon course completion
struct Certificate has key, store {
    id: UID,
    course_id: ID,
    student_address: address,
    completion_date: u64,
    certificate_hash: String
}

/// Error types for the enrollment process
enum EnrollmentError {
    ECourseFull,
    ECourseInactive,
    EInsufficientFunds,
    EAlreadyEnrolled,
    ENotEnrolled,
    ECourseNotFound,
    ENotCompleted
}

/// Module containing all course enrollment functions
module course_enrollment::enrollment {
    use sui::object;
    use sui::transfer;
    use sui::tx_context::TxContext;
    use sui::event;
    use std::string;
    use sui::balance;
    use sui::coin;
    use sui::dynamic_field;
    use course_enrollment::enrollment::{Course, Enrollment, Certificate, EnrollmentError};

    /// Event emitted when a new course is created
    struct CourseCreated has copy, drop {
        course_id: ID,
        name: String,
        instructor: String
    }

    /// Event emitted when a student enrolls in a course
    struct StudentEnrolled has copy, drop {
        course_id: ID,
        student_address: address
    }

    /// Event emitted when a course is completed
    struct CourseCompleted has copy, drop {
        course_id: ID,
        student_address: address,
        certificate_hash: String
    }

    /// Creates a new course
    public fun create_course(
        name: String,
        description: String,
        instructor: String,
        max_capacity: u64,
        price: u64,
        ctx: &mut TxContext
    ): Course {
        let course = Course {
            id: object::new(ctx),
            name,
            description,
            instructor,
            max_capacity,
            current_enrollment: 0,
            price,
            active: true
        };

        event::emit(CourseCreated {
            course_id: object::id(&course),
            name: copy name,
            instructor: copy instructor
        });

        course
    }

    /// Enrolls a student in a course
    public entry fun enroll(
        course: &mut Course,
        payment: Coin<SUI>,
        student_address: address,
        ctx: &mut TxContext
    ) {
        // Check course availability
        assert!(course.active, EnrollmentError::ECourseInactive);
        assert!(course.current_enrollment < course.max_capacity, EnrollmentError::ECourseFull);
        
        // Check payment
        let payment_amount = coin::value(&payment);
        assert!(payment_amount >= course.price, EnrollmentError::EInsufficientFunds);
        
        // Create enrollment record
        let enrollment = Enrollment {
            id: object::new(ctx),
            course_id: object::id(course),
            student_address,
            enrollment_date: tx_context::epoch(ctx),
            completed: false
        };

        // Update course enrollment count
        course.current_enrollment = course.current_enrollment + 1;

        // Transfer payment to course owner (simplified)
        transfer::transfer(payment, student_address);

        // Emit enrollment event
        event::emit(StudentEnrolled {
            course_id: object::id(course),
            student_address
        });

        // Transfer enrollment object to student
        transfer::transfer(enrollment, student_address);
    }

    /// Marks a course as completed and issues a certificate
    public entry fun complete_course(
        course: &mut Course,
        enrollment: &mut Enrollment,
        certificate_hash: String,
        ctx: &mut TxContext
    ) {
        assert!(enrollment.completed == false, EnrollmentError::ENotEnrolled);
        assert!(object::id(course) == enrollment.course_id, EnrollmentError::ECourseNotFound);

        enrollment.completed = true;
        course.current_enrollment = course.current_enrollment - 1;

        let certificate = Certificate {
            id: object::new(ctx),
            course_id: object::id(course),
            student_address: enrollment.student_address,
            completion_date: tx_context::epoch(ctx),
            certificate_hash
        };

        event::emit(CourseCompleted {
            course_id: object::id(course),
            student_address: enrollment.student_address,
            certificate_hash: copy certificate_hash
        });

        transfer::transfer(certificate, enrollment.student_address);
    }

    /// Toggles course active status
    public entry fun toggle_course_status(course: &mut Course) {
        course.active = !course.active;
    }

    /// Withdraws funds from course (simplified)
    public entry fun withdraw_funds(
        _course: &Course,
        _balance: &mut Balance<SUI>,
        amount: u64,
        recipient: address
    ) {
        // In a real implementation, this would transfer funds from course balance
        // Simplified for this example
        transfer::public_transfer(coin::from_balance(_balance, amount), recipient);
    }
}
```
