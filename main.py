from input_details import get_user_details
from eligibility_check import check_eligibility

def main():
    age, annual_income, credit_score = get_user_details()
    result = check_eligibility(age, annual_income, credit_score)
    print(result)

if __name__ == "__main__":
    main()
