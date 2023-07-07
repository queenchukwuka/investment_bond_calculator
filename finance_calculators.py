import math

# The program menu
to_invest = print("investment - to calculate the amount of money you'll earn on your investment")
to_repay = print("bond - to calculate the amount you'll have to pay on a home loan")

# to select the option from the program menu
choice = input("Enter either 'investment' or 'bond' to proceed: ")

# If the user is choosing 'investment'
if choice == "INVESTMENT" or choice == "Investment" or choice == "investment":
    print("You have chosen the 'investment' option.")

    # when the user chooses the investment option
    P = int(input("Enter the amount of money you are depositing: "))

    # asking the user to select the interest rate
    r = float(input("Enter the percentage interest rate(number only): "))/100

    # the period of investment
    t = int(input("Enter the number of years of investment: "))

    # user to select the type of interest
    interest = input("Please select 'simple' or 'compound' interest: ")

    if interest == "simple" or interest == "Simple" or interest == "SIMPLE":
        print(P*(1 + r*t))       # when simple interest is calculated as A = P*(1 + r*t)


        # when the user selects compoud interest
    elif interest == "COMPOUND" or interest == "compound" or interest == "Compound":
        print(P * math.pow((1+r),t))

# when the user selects 'bond'
elif choice == "Bond" or choice == "BOND" or choice == "bond":
    print("You have selected bond as your choice")

    # to enter the present house value
    P = int(input("Enter the present value of house: "))

    # period for bond repayment
    n = int(input("Enter the number of months for repayment: "))

    # to input the yearly interest rate
    yearly_interest= float(input("Enter the monthly interest(number only): "))/100

     # to input the monthly interest
    i = float(yearly_interest)/12

    # to calculate the bond repayment
    if choice == "Bond" or choice == "BOND" or choice == "bond":
        print(float(i * P)/(1 - (1 + i)**(-n)))


# when the user selects an option other than 'investment' or 'bond' 
else:
    print("You have not chosen a valid option, please select a valid option to proceed.")






