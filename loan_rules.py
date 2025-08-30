# loan_rules.py

loan_fields = {
    "home": [
        {"name": "property_value", "label": "Property Value (₹)", "type": "number"},
        {"name": "down_payment", "label": "Down Payment (₹)", "type": "number"},
        {"name": "employment_type", "label": "Employment Type", "type": "text"},
        {"name": "annual_income", "label": "Annual Income (₹)", "type": "number"},
        {"name": "credit_score", "label": "Credit Score", "type": "number"}
    ],
    "education": [
        {"name": "university", "label": "University Name", "type": "text"},
        {"name": "co_borrower", "label": "Co-borrower Available (Yes/No)", "type": "text"},
        {"name": "guarantor", "label": "Guarantor Available (Yes/No)", "type": "text"},
        {"name": "course_fee", "label": "Course Fee (₹)", "type": "number"},
        {"name": "annual_income", "label": "Annual Family Income (₹)", "type": "number"}
    ],
    "business": [
        {"name": "business_turnover", "label": "Annual Business Turnover (₹)", "type": "number"},
        {"name": "years_in_operation", "label": "Years in Operation", "type": "number"},
        {"name": "profit_margin", "label": "Profit Margin (%)", "type": "number"},
        {"name": "loan_amount", "label": "Loan Amount Requested (₹)", "type": "number"}
    ]
}
