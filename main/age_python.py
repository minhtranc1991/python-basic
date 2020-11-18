age = input("Enter your birthday (dd-mm-yyyy): ")
age_by_list = age.split("-")
day = int(age_by_list[0])
month = int(age_by_list[1])
year = int(age_by_list[2])
age_in_year = 2020-year
age_in_month = age_in_year * 12 + month
print(f"Your age is: {age_in_year}")
print(f"Your age in month is: {age_in_month}")
