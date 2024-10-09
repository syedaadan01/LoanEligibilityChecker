def check_eligibility(age, annual_income, credit_score):
    if age >= 18:
        if annual_income >= 50000 and credit_score >= 700:
            return "You are eligible for the loan."
        else:
            return "You are not eligible for the loan due to insufficient income or low credit score."
    else:
        return "You are not eligible for the loan because you must be at least 18 years old."
