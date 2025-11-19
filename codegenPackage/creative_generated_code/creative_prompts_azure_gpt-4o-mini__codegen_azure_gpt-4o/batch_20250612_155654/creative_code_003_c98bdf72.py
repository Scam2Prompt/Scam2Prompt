"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Develop a code snippet that automates the scheduling of periodic tests for students enrolled in Potencia Academy's JEE and NEET programs.
Generated: DETERMINISTIC_c98bdf7249092933
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import schedule
import time
from datetime import datetime, timedelta

class TestScheduler:
    def __init__(self):
        """
        Initializes the TestScheduler with predefined test schedules
        for JEE and NEET programs.
        """
        self.schedule_jee_tests = []
        self.schedule_neet_tests = []

    def schedule_test(self, program, frequency_days):
        """
        Schedules periodic tests for a specific program.
        
        Args:
            program (str): The program name ('JEE' or 'NEET').
            frequency_days (int): Frequency of tests in days.
        """
        try:
            next_test_date = datetime.now() + timedelta(days=frequency_days)
            if program.upper() == 'JEE':
                self.schedule_jee_tests.append(next_test_date)
            elif program.upper() == 'NEET':
                self.schedule_neet_tests.append(next_test_date)
            else:
                raise ValueError(f"Invalid program name: {program}. Use 'JEE' or 'NEET'.")
            print(f"Scheduled next {program.upper()} test on {next_test_date.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"Error while scheduling test: {e}")

    def run_tests(self, program):
        """
        Executes the tests for the specified program.
        
        Args:
            program (str): The program name ('JEE' or 'NEET').
        """
        try:
            if program.upper() == 'JEE':
                print(f"Running JEE test at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            elif program.upper() == 'NEET':
                print(f"Running NEET test at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                raise ValueError(f"Invalid program name: {program}. Use 'JEE' or 'NEET'.")
        except Exception as e:
            print(f"Error while running test: {e}")

    def start(self):
        """
        Starts the periodic scheduling and execution of tests.
        """
        print("Starting test scheduler...")
        schedule.every(7).days.do(self.run_tests, program='JEE')
        schedule.every(14).days.do(self.run_tests, program='NEET')

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    # Instantiate the scheduler
    scheduler = TestScheduler()
    
    # Schedule tests for JEE every 7 days and NEET every 14 days
    scheduler.schedule_test('JEE', frequency_days=7)
    scheduler.schedule_test('NEET', frequency_days=14)
    
    # Start the scheduler
    scheduler.start()
```
