#customer monthly electricity bill, -->no of units consumed , multiple features , and billing rules 

units=int(input("Enter the total Electricitiy Units Consumed by the Customer:  "))

if units<0:
    print("units Can not be less Than Zero(0) (Negative Numeric values.) , Please Enter units again")

else:
    discount=0 #Defalut discount
    surcharge=0#Defaut surcharge

    if units>=0 and units<=100:
        RPU=5  #(RPU=Rate PER Units)
        ConsumptionBill=RPU*units

        if units<=50:
            discount=5
            discountAmount=(ConsumptionBill*5) /100
            ConsumptionBill=ConsumptionBill-  discountAmount# 5% Discount
        else:
            PeakHourUnits=int(input(f"Enter Peak Hour Units Consumed by the Customer from {units} units: "))
            PeakHourCharge=2 #(Extra PeakHourCharge per units above 50 units)
            ConsumptionBill+=PeakHourCharge*PeakHourUnits

        print("\n*************************************** Consumption is Low ********************************\n")



    elif units>=101 and units<=200:
        RPU=7
        ConsumptionBill=5*100+RPU*(units-100)
        PeakHourUnits=int(input(f"Enter Peak Hour Units Consumed by the Customer from {units} units: "))
        PeakHourCharge=2 #(Extra PeakHourCharge per units above 50 units)
        ConsumptionBill+=PeakHourCharge*PeakHourUnits

        print("\n*************************************** Consumption is Medium ********************************\n")



    elif units>=201 and units<=300:
        RPU=10
        ConsumptionBill=5*100+7*100+RPU*(units-200)
        PeakHourUnits=int(input(f"Enter Peak Hour Units Consumed by the Customer from {units} units: "))
        PeakHourCharge=2 #(Extra PeakHourCharge per units above 50 units)
        ConsumptionBill+=PeakHourCharge*PeakHourUnits

        print("\n*************************************** Consumption is Medium ********************************\n")


    elif units>=301:
        RPU=15
        ConsumptionBill=5*100+7*100+10*100+RPU*(units-300)
        PeakHourUnits=int(input(f"Enter Peak Hour Units Consumed by the Customer from {units} units: "))
        PeakHourCharge=2 #(Extra PeakHourCharge per units above 50 units)
        ConsumptionBill+=PeakHourCharge*PeakHourUnits
        if units>=500:
            surcharge=10
            surchargeamount=(ConsumptionBill*10) /100
            ConsumptionBill=ConsumptionBill+surchargeamount

        print("\n*************************************** Consumption is High ********************************\n")


    PaymentDelayed=input("Is the Payement of Bill Delayed ? (T or F)")

    FixedMeterCharge=50

    LatePaymentPenalty=0

    if PaymentDelayed=="T" or PaymentDelayed=="t":
        LatePaymentPenalty=100

    FinalBill=ConsumptionBill+FixedMeterCharge+LatePaymentPenalty

    # if units<=50:
    #      RPUD=5  #(RPUD=Rate Per Unit Discount)
    # elif units>=500:
    #      RPUSC=10 #(RPUSC=Rate PEr Units Surcharge)


    print("================================================================================================")

    print(f"Total units Consumed By The Customer                                       : {units}")
    print(f"Rate PER Units Applied                                                     : {RPU} \n")

    if units<=50:
        print(f"                                                  Discount and Discount Ammount For less than 50 units Consumed           ")
        print(f"                                                                Discount   : {discount}")
        print(f"                                                         Discount Amount   : {discountAmount} \n")

    elif units>50:
        print(f"                                                  PeakHourUnits and PeakHourCharge For Greater than 50 units Consumed    ")
        print(f"                                                           PeakHourUnits   : {PeakHourUnits}")
        print(f"                                                          PeakHourCharge   : {PeakHourCharge} \n")
        
        if units>=500:
            print(f"                                              Surcharge and Surchargeamount For greater than 500 units Consumed      ")
            print(f"                                                               Surcharge   : {surcharge}")
            print(f"                                                         Surchargeamount   : {surchargeamount} \n")



    print(f"                                                        ConsumptionBill    : {ConsumptionBill}")
    print(f"                                                        FixedMeterCharge   : {FixedMeterCharge}")
    print(f"                                                      LatePaymentPenalty   : {LatePaymentPenalty}")
    print(f"Amount Payable ------------------------------------>           FinalBill   : {FinalBill}")

    print("================================================================================================")


























# Project Definition: Electricity Bill Calculator

# The Electricity Bill Calculator is a Python mini project designed to demonstrate the use of conditional and nested statements in a practical, real-world application. The program calculates a customer’s monthly electricity bill based on the number of units consumed, incorporating multiple features and billing rules to reflect real-world scenarios.

# Features and Functionalities:
# 	1.	Accepts user input for the total electricity units consumed.
# 	2.	Uses if, elif, and else statements to apply tiered billing based on consumption slabs:
# 	•	0 – 100 units → ₹5/unit
# 	•	101 – 200 units → ₹7/unit
# 	•	201 – 300 units → ₹10/unit
# 	•	Above 300 units → ₹15/unit
# 	3.	Implements nested conditions to handle additional charges or discounts within slabs.
# 	4.	Adds a fixed meter charge of ₹50 to every bill.
# 	5.	Applies a 10% surcharge if total units exceed 500 units.
# 	6.	Provides a 5% discount if consumption is below 50 units as a low-usage incentive.
# 	7.	Includes extra charges for peak-hour consumption: ₹2/unit for units consumed during peak hours above 50 units.
# 	8.	Handles edge cases, such as exactly hitting slab limits or zero consumption.
# 	9.	Offers custom messages to indicate low, medium, or high consumption.
# 	10.	Calculates and displays a final formatted bill, showing total amount, surcharge, discounts, and fixed charges.
# 	11.	Can optionally add a late payment penalty of ₹100 if payment is delayed.
# 	12.	Ensures user input validation, allowing only non-negative numeric entries.
