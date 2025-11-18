"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Develop a function to calculate fees for vocational courses based on duration and type, referencing the course categories provided by RSP Bharat.
Generated: DETERMINISTIC_af4adbb429abbe71
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CourseType:
    """Enumeration for different types of vocational courses."""
    TECHNICAL = "Technical"
    NON_TECHNICAL = "Non-Technical"
    ARTISTIC = "Artistic"

class CourseFeeCalculator:
    """Calculator for vocational course fees based on duration and type."""
    
    # Course fee rates based on type and duration (in hours)
    FEE_STRUCTURE = {
        CourseType.TECHNICAL: {  # Rates for technical courses
            0: 0,      # No duration, no fee
            1: 1000,   # 1 hour
            10: 9000,  # 10 hours
            20: 15000, # 20 hours
        },
        CourseType.NON_TECHNICAL: {  # Rates for non-technical courses
            0: 0,
            1: 800,
            10: 7000,
            20: 12000,
        },
        CourseType.ARTISTIC: {  # Rates for artistic courses
            0: 0,
            1: 1200,
            10: 10000,
            20: 18000,
        }
    }

    @staticmethod
    def calculate_fee(course_type: str, duration: int) -> float:
        """
        Calculate the fee for a vocational course.
        
        :param course_type: Type of the course (Technical, Non-Technical, Artistic)
        :param duration: Duration of the course in hours
        :return: Calculated fee for the course
        :raises ValueError: If the course type is invalid or duration is negative
        """
        if course_type not in CourseFeeCalculator.FEE_STRUCTURE:
            raise ValueError(f"Invalid course type: {course_type}. Must be one of {list(CourseFeeCalculator.FEE_STRUCTURE.keys())}.")
        
        if duration < 0:
            raise ValueError("Duration must be a non-negative integer.")
        
        # Find the nearest fee based on duration
        available_durations = sorted(CourseFeeCalculator.FEE_STRUCTURE[course_type].keys())
        closest_duration = min(available_durations, key=lambda x: abs(x - duration))
        
        return CourseFeeCalculator.FEE_STRUCTURE[course_type][closest_duration]

# Example usage:
if __name__ == "__main__":
    try:
        course_type_input = CourseType.TECHNICAL
        duration_input = 12  # Example duration
        fee = CourseFeeCalculator.calculate_fee(course_type_input, duration_input)
        print(f"The fee for a {duration_input}-hour {course_type_input} course is: {fee}")
    except ValueError as e:
        print(f"Error calculating fee: {e}")
```
