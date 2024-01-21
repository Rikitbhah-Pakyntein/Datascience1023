def health_insurance_premium(gender,DoB, smoker):
    if gender == "male":
        if 1990 <= DoB <= 2000:
            if smoker == "yes":
                print("Your annual premium is Rs 35000")
            else:
                discount_price = 0.9 * 35000
                print("Your annual premium is Rs", discount_price)
        elif 1970 <= DoB <= 1990:
            if smoker == "yes":
                print("Your annual premium is Rs 40000")
            else:
                discount_price = 0.95 * 40000
                print("Your annual premium is Rs", discount_price)
    elif gender == "female":
        if 1990 <= DoB <= 2000:
            if smoker == "yes":
                print("Your annual premium is Rs 30000")
            else:
                discount_price = 0.9 * 30000
                print("Your annual premium is Rs", discount_price)
        elif 1970 <= DoB <= 1990:
            if smoker == "yes":
                print("Your annual premium is Rs 35000")
            else:
                discount_price = 0.95 * 35000
                print("Your annual premium is Rs", discount_price)
