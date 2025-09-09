# gemini_handler.py

from typing import Literal, List
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI


GOOGLE_API_KEY = "AIzaSyCsdxUIjuY8_91Ayri6FLnUdhppSVC6UuY"


# Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2
)

# Pydantic schema for structured output
class LoanEvaluation(BaseModel):
    result: Literal["Likely Approved", "Guaranteed Approval", "Needs Improvement"] = Field(
        description="Final loan eligibility evaluation"
    )
    feedback: List[str] = Field(
         default_factory=lambda: ["No specific feedback provided."],
        description=" List of improvement suggestions for approval "
    )

# Wrap model with structured output
evaluation_model = model.with_structured_output(LoanEvaluation)

def check_loan_eligibility(loan_type: str, user_data: dict) -> dict:
    
    # Calculate monthly disposable income
    monthly_income = 0
    if 'annual_income' in user_data:
        monthly_income = float(user_data['annual_income']) / 12
    elif 'monthly_income' in user_data:
        monthly_income = float(user_data['monthly_income'])
    elif 'business_turnover' in user_data:
        monthly_income = float(user_data['business_turnover']) * float(user_data['profit_margin']) / 100 / 12
    elif 'annual_family_income' in user_data:
        monthly_income = float(user_data['annual_family_income']) / 12

    other_expenses = float(user_data.get('other_expenses', 0))
    disposable_income = monthly_income - other_expenses

    prompt = f"""
You are a loan eligibility predictor. Consider the following calculations:

Monthly Income: ₹{monthly_income:,.2f}
Monthly Other Expenses: ₹{other_expenses:,.2f}
Monthly Disposable Income: ₹{disposable_income:,.2f}

Loan Type: {loan_type}
User Data: {user_data}

Based on the monthly disposable income and other factors, evaluate the loan eligibility.

"""
    print(f"promt:::::::::{prompt}")
    response = evaluation_model.invoke(prompt)
    print("r====================================================================================")
    print(response)
    return response
