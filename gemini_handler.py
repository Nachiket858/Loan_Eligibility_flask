# gemini_handler.py

from typing import Literal, List
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI


GOOGLE_API_KEY = "AIzaSyCsdxUIjuY8_91Ayri6FLnUdhppSVC6UuY"


# Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # or gemini-2.0-flash-lite if enabled for you
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2
)

# Pydantic schema for structured output
class LoanEvaluation(BaseModel):
    result: Literal["Likely Approved", "Guaranteed Approval", "Needs Improvement"] = Field(
        description="Final loan eligibility evaluation"
    )
    feedback: List[str] = Field(
        description="List of improvement suggestions for approval"
    )

# Wrap model with structured output
evaluation_model = model.with_structured_output(LoanEvaluation)

def check_loan_eligibility(loan_type: str, user_data: dict) -> dict:
    """
    Takes loan type + user data, calls Gemini with structured output,
    returns dict with result + feedback.
    """
    prompt = f"""
You are a loan eligibility predictor.

Loan Type: {loan_type}
User Data: {user_data}

Evaluate the loan eligibility.
"""
    print(f"promt:::::::::{prompt}")
    response = evaluation_model.invoke(prompt)
    print("r====================================================================================")
    print(response)
    return response.dict()
