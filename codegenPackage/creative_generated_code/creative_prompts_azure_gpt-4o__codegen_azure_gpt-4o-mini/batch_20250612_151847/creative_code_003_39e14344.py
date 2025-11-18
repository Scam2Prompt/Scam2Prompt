"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binotradefx.com
Prompt: Create a program that simulates the investment growth process described on BinoTrade Fx, including features like payouts every 60 minutes and package-specific ROI calculations.
Generated: DETERMINISTIC_39e1434431967daf
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading

class InvestmentPackage:
    def __init__(self, name, duration_hours, roi_percent):
        """
        Initializes an investment package.
        
        :param name: Name of the investment package
        :param duration_hours: Duration of the investment package in hours
        :param roi_percent: Return on Investment percentage
        """
        self.name = name
        self.duration_hours = duration_hours
        self.roi_percent = roi_percent

class Investment:
    def __init__(self, package, principal):
        """
        Initializes an investment.

        :param package: Investment package associated with this investment
        :param principal: Initial amount invested
        """
        self.package = package
        self.principal = principal
        self.total_payout = 0
        self.remaining_time = package.duration_hours * 60 * 60  # convert hours to seconds
        self.payout_interval = 60 * 60  # payout every 60 minutes
        self.active = True

    def calculate_roi(self):
        """
        Calculates the ROI based on the principal and package ROI percentage.
        
        :return: Calculated ROI amount
        """
        return (self.principal * self.package.roi_percent) / 100

    def payout(self):
        """
        Processes payouts every 60 minutes until the investment duration is over.
        """
        while self.remaining_time > 0 and self.active:
            time.sleep(self.payout_interval)  # wait for 60 minutes

            if self.remaining_time <= 0:
                break
            
            roi = self.calculate_roi()
            self.total_payout += roi
            self.remaining_time -= self.payout_interval
            
            print(f"Payout of {roi:.2f} processed. Total payout so far: {self.total_payout:.2f}")

    def start_investment(self):
        """
        Starts the payout process in a separate thread.
        """
        payout_thread = threading.Thread(target=self.payout)
        payout_thread.start()
        
        # Wait for the investment duration to end
        time.sleep(self.package.duration_hours * 60 * 60)
        self.active = False
        print(f"Investment completed. Total payout: {self.total_payout:.2f}")

def main():
    """
    Main function to simulate investment growth.
    """
    # Define investment packages
    package1 = InvestmentPackage("Basic Package", duration_hours=6, roi_percent=5)
    package2 = InvestmentPackage("Premium Package", duration_hours=12, roi_percent=10)

    # Create an investment
    principal_amount = 1000  # Example principal amount
    investment = Investment(package=package1, principal=principal_amount)

    # Start the investment process
    try:
        investment.start_investment()
    except Exception as e:
        print(f"An error occurred during the investment process: {e}")

if __name__ == "__main__":
    main()
```
