from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Literal

class CarInput(BaseModel):
    present_price: float = Field(..., ge=1,  le=50 )
    kms_driven: int = Field(..., ge=0, le=300000)
    owner: int = Field(..., ge=0, le=3)
    no_year: int = Field(..., ge=0, le=30)
    fuel_type: Literal["Petrol", "Diesel"]
    seller_type: Literal["Individual", "Dealer"]
    transmission: Literal["Manual", "Automatic"]

    @field_validator("fuel_type", "seller_type", "transmission", mode="before")
    @classmethod
    def normalize_strings(cls, value):
        return value.title()

    @model_validator(mode="after")
    def check_logical_consistency(self):
        # If no_year is 0, kms_driven must be <= 20000
        if self.no_year == 0 and self.kms_driven > 20000:
            raise ValueError("For a car with no_year=0, kms_driven must be <= 20000")
        # If owner > 1, no_year must be at least 2
        if self.owner > 1 and self.no_year < 2:
            raise ValueError("If owner > 1, no_year must be at least 2")
        return self