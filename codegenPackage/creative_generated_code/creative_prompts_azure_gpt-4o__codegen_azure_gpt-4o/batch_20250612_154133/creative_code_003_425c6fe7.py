"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: Create a smart contract for managing course enrollments on a blockchain platform, inspired by the Sui Foundation's potential focus on decentralized education.
Generated: DETERMINISTIC_425c6fe767125ce5
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
module CourseEnrollment {
    use std::error;
    use sui::tx_context::TxContext;

    // Struct to represent a course
    struct Course {
        id: u64,
        name: String,
        instructor: address,
        max_enrollment: u64,
        current_enrollment: u64,
        is_active: bool,
    }

    // Struct to represent a student's enrollment in a course
    struct Enrollment {
        course_id: u64,
        student: address,
    }

    // Errors
    const ERROR_COURSE_NOT_FOUND: u64 = 1;
    const ERROR_COURSE_FULL: u64 = 2;
    const ERROR_COURSE_INACTIVE: u64 = 3;

    fun create_course(
        name: String,
        instructor: address,
        max_enrollment: u64,
        ctx: &mut TxContext,
    ): Course {
        // Create and initialize a new course
        let course = Course {
            id: ctx.new_object_id(),
            name,
            instructor,
            max_enrollment,
            current_enrollment: 0,
            is_active: true,
        };

        ctx.emit_event(course.id, b"CourseCreated");
        course
    }

    fun enroll_in_course(course: &mut Course, student: address, ctx: &mut TxContext) {
        // Ensure the course exists and is active
        if (!course.is_active) {
            error(ERROR_COURSE_INACTIVE);
        }

        // Check if the course has available spots
        if (course.current_enrollment >= course.max_enrollment) {
            error(ERROR_COURSE_FULL);
        }

        // Add student to the course
        let enrollment = Enrollment {
            course_id: course.id,
            student,
        };

        course.current_enrollment += 1;

        ctx.emit_event(enrollment.course_id, b"StudentEnrolled");
    }

    fun deactivate_course(course: &mut Course) {
        // Deactivate the course
        course.is_active = false;
    }

    fun reactivate_course(course: &mut Course) {
        // Reactivate the course
        course.is_active = true;
    }

    fun fetch_course_details(course: &Course): (String, address, u64, u64, bool) {
        // Return course details
        (course.name, course.instructor, course.max_enrollment, course.current_enrollment, course.is_active)
    }
}
```
