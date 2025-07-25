import math 
car_name=input("Enter car name:")
car_variant=input("Enter variant:")
on_road_price=int(input("Enter On_Road_Price:"))
down_payment=int(input("Enter Down_Payment:"))
bank_interest_rate=int(input("Enter bank interest rate:"))
loan_period_in_years=int(input("Enter loan period (in years): "))

total_amount=on_road_price-down_payment
rate_in_months=((bank_interest_rate)/12)/100
loan_period_in_months=loan_period_in_years*12

#emi=(P x R x (1+R)^N / [(1+R)^N-1])

emi=(total_amount*rate_in_months*((1+rate_in_months)**loan_period_in_months))/(((1+rate_in_months)**loan_period_in_months)-1)

print("For",car_name,"and variant",car_variant,":")
print("With")
print("On_Road_Price:",on_road_price,",")
print("Down_Payment :",down_payment,",")
print("Bank Interest Rate:",bank_interest_rate,",")
print("and Loan period:",loan_period_in_years,"years")
print("")
print("Total amount is:",total_amount)
print("")
print("EMI (per month) is :",math.ceil(emi))