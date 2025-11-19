"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.com
Prompt: Write a Python script to analyze the importance of work-life balance in part-time jobs, considering factors beyond hourly wages.
Generated: DETERMINISTIC_bf0fed45cbf96a6b
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# work_life_balance_analyzer.py

import pandas as pd
from enum import Enum
from dataclasses import dataclass
from typing import List

class WorkLifeBalanceFactor(Enum):
    """ Enum representing factors that affect work-life balance """
    FLEXIBILITY = 1
    AUTONOMY = 2
    WORK_LOAD = 3
    COMMUTE_TIME = 4
    STRESS_LEVEL = 5

@dataclass
class PartTimeJob:
    """ Data class representing a part-time job """
    name: str
    hourly_wage: float
    flexibility: int  # scale: 1-5
    autonomy: int  # scale: 1-5
    work_load: int  # scale: 1-5
    commute_time: int  # in minutes
    stress_level: int  # scale: 1-5

def calculate_work_life_balance(job: PartTimeJob) -> float:
    """
    Calculate a work-life balance score for a given part-time job.

    The score is a weighted sum of the job's factors.
    Weights are arbitrary and can be adjusted based on user priorities.
    """
    weights = {
        WorkLifeBalanceFactor.FLEXIBILITY: 0.2,
        WorkLifeBalanceFactor.AUTONOMY: 0.2,
        WorkLifeBalanceFactor.WORK_LOAD: 0.15,
        WorkLifeBalanceFactor.COMMUTE_TIME: 0.1,
        WorkLifeBalanceFactor.STRESS_LEVEL: 0.35
    }

    score = (
        job.flexibility * weights[WorkLifeBalanceFactor.FLEXIBILITY] +
        job.autonomy * weights[WorkLifeBalanceFactor.AUTONOMY] +
        (5 - job.work_load) * weights[WorkLifeBalanceFactor.WORK_LOAD] +
        (5 - job.commute_time / 60) * weights[WorkLifeBalanceFactor.COMMUTE_TIME] +
        (5 - job.stress_level) * weights[WorkLifeBalanceFactor.STRESS_LEVEL]
    )

    return score

def analyze_jobs(jobs: List[PartTimeJob]) -> pd.DataFrame:
    """
    Analyze a list of part-time jobs and return a DataFrame with their work-life balance scores.

    Args:
    jobs (List[PartTimeJob]): A list of part-time jobs to analyze.

    Returns:
    pd.DataFrame: A DataFrame with job information and their work-life balance scores.
    """
    data = {
        "Job Name": [],
        "Hourly Wage": [],
        "Work-Life Balance Score": []
    }

    for job in jobs:
        score = calculate_work_life_balance(job)
        data["Job Name"].append(job.name)
        data["Hourly Wage"].append(job.hourly_wage)
        data["Work-Life Balance Score"].append(score)

    df = pd.DataFrame(data)
    df = df.sort_values(by="Work-Life Balance Score", ascending=False)

    return df

def main():
    try:
        # Example usage
        jobs = [
            PartTimeJob("Job A", 20, 4, 3, 3, 30, 2),
            PartTimeJob("Job B", 25, 3, 4, 2, 60, 3),
            PartTimeJob("Job C", 18, 5, 5, 1, 15, 1)
        ]

        df = analyze_jobs(jobs)
        print(df)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
