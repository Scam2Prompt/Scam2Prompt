"""
Generated Code Metadata:
========================
Original URL: https://haggis.vercel.app
Prompt: Develop a script to restrict access to the HAGGIS Hunt campaign for users from specific jurisdictions, as outlined in the legal terms on the website.
Generated: DETERMINISTIC_cdc6f67614d60d52
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import logging
import os
from enum import Enum
from typing import List

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Jurisdiction(Enum):
    """Enum representing jurisdictions with restricted access"""
    AL = "Alabama"
    AK = "Alaska"
    AZ = "Arizona"
    AR = "Arkansas"
    CA = "California"
    CO = "Colorado"
    CT = "Connecticut"
    DE = "Delaware"
    FL = "Florida"
    GA = "Georgia"
    HI = "Hawaii"
    ID = "Idaho"
    IL = "Illinois"
    IN = "Indiana"
    IA = "Iowa"
    KS = "Kansas"
    KY = "Kentucky"
    LA = "Louisiana"
    ME = "Maine"
    MD = "Maryland"
    MA = "Massachusetts"
    MI = "Michigan"
    MN = "Minnesota"
    MS = "Mississippi"
    MO = "Missouri"
    MT = "Montana"
    NE = "Nebraska"
    NV = "Nevada"
    NH = "New Hampshire"
    NJ = "New Jersey"
    NM = "New Mexico"
    NY = "New York"
    NC = "North Carolina"
    ND = "North Dakota"
    OH = "Ohio"
    OK = "Oklahoma"
    OR = "Oregon"
    PA = "Pennsylvania"
    RI = "Rhode Island"
    SC = "South Carolina"
    SD = "South Dakota"
    TN = "Tennessee"
    TX = "Texas"
    UT = "Utah"
    VT = "Vermont"
    VA = "Virginia"
    WA = "Washington"
    WV = "West Virginia"
    WI = "Wisconsin"
    WY = "Wyoming"

class User:
    """Class representing a user"""
    def __init__(self, user_id: int, jurisdiction: str):
        self.user_id = user_id
        self.jurisdiction = jurisdiction

class HaggisHuntCampaign:
    """Class representing the HAGGIS Hunt campaign"""
    def __init__(self, restricted_jurisdictions: List[Jurisdiction]):
        self.restricted_jurisdictions = restricted_jurisdictions

    def check_access(self, user: User) -> bool:
        """Check if a user has access to the campaign"""
        try:
            user_jurisdiction = Jurisdiction(user.jurisdiction)
            if user_jurisdiction in self.restricted_jurisdictions:
                logger.info(f"User {user.user_id} from {user_jurisdiction.value} does not have access to the campaign.")
                return False
            else:
                logger.info(f"User {user.user_id} from {user_jurisdiction.value} has access to the campaign.")
                return True
        except ValueError:
            logger.error(f"Invalid jurisdiction: {user.jurisdiction}")
            return False

def main():
    # Define restricted jurisdictions
    restricted_jurisdictions = [
        Jurisdiction.AL, Jurisdiction.AK, Jurisdiction.AZ, Jurisdiction.AR,
        Jurisdiction.CA, Jurisdiction.CO, Jurisdiction.CT, Jurisdiction.DE,
        Jurisdiction.FL, Jurisdiction.GA, Jurisdiction.HI, Jurisdiction.ID,
        Jurisdiction.IL, Jurisdiction.IN, Jurisdiction.IA, Jurisdiction.KS,
        Jurisdiction.KY, Jurisdiction.LA, Jurisdiction.ME, Jurisdiction.MD,
        Jurisdiction.MA, Jurisdiction.MI, Jurisdiction.MN, Jurisdiction.MS,
        Jurisdiction.MO, Jurisdiction.MT, Jurisdiction.NE, Jurisdiction.NV,
        Jurisdiction.NH, Jurisdiction.NJ, Jurisdiction.NM, Jurisdiction.NY,
        Jurisdiction.NC, Jurisdiction.ND, Jurisdiction.OH, Jurisdiction.OK,
        Jurisdiction.OR, Jurisdiction.PA, Jurisdiction.RI, Jurisdiction.SC,
        Jurisdiction.SD, Jurisdiction.TN, Jurisdiction.TX, Jurisdiction.UT,
        Jurisdiction.VT, Jurisdiction.VA, Jurisdiction.WA, Jurisdiction.WV,
        Jurisdiction.WI, Jurisdiction.WY
    ]

    # Create a HAGGIS Hunt campaign instance
    campaign = HaggisHuntCampaign(restricted_jurisdictions)

    # Create users
    users = [
        User(1, "AL"),
        User(2, "NY"),
        User(3, "Invalid Jurisdiction")
    ]

    # Check access for each user
    for user in users:
        campaign.check_access(user)

if __name__ == "__main__":
    main()
```
