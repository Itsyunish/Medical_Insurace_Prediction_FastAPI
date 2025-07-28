from pydantic import BaseModel, Field, computed_field
from pydantic.functional_validators import BeforeValidator
from typing import Annotated, Literal

# Function to normalize strings
def clean_string(v: str) -> str:
    return v.strip().lower()

# Type alias for normalized string
NormalizedStr = Annotated[str, BeforeValidator(clean_string)]

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user")]
    sex: Annotated[NormalizedStr, Literal['male', 'female'], Field(..., description="Gender of the user")]
    bmi: Annotated[float, Field(..., description="BMI of the user")]
    children: Annotated[int, Field(..., ge=0, le=5, description="Number of children")]
    smoker: Annotated[NormalizedStr, Literal['yes', 'no'], Field(..., description="Are you a smoker?")]
    region: Annotated[NormalizedStr, Literal['southwest', 'southeast', 'northwest', 'northeast'], Field(..., description="Region")]
    

    @computed_field
    @property
    def bmi_category(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'
