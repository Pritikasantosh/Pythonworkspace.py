

# Calculate total electricity charge
def total_amount(a, b, c, d, e):
    return a + b + c + d + e


# Calculate 10% service charge
def service_charge(total):
    return total * 0.10


# Calculate 5% discount
def discount(total_after_service):
    return total_after_service * 0.05


# Main calculation function
def calculate_bill(a, b, c, d, e):
    total = total_amount(a, b, c, d, e)
    service = service_charge(total)
    total_after_service = total + service
    discount_amount = discount(total_after_service)

    return total_after_service - discount_amount


# Supply values directly as arguments
a = 200
b = 150
c = 100
d = 250
e = 300

# Calculate bill details
total = total_amount(a, b, c, d, e)
service = service_charge(total)
total_after_service = total + service
discount_amount = discount(total_after_service)
final_amount = calculate_bill(a, b, c, d, e)

# Display results
print(f"Total electricity charge = {total:.2f}")
print(f"Service charge = {service:.2f}")
print(f"Total after service charge = {total_after_service:.2f}")
print(f"Discount = {discount_amount:.2f}")
print(f"Final payable amount = {final_amount:.2f}")





    

