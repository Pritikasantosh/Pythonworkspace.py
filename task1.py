

def total_amount(a, b, c, d, e):
    return a + b + c + d + e


def calculate_gst(total):
    return total * 0.18


def calculate_discount(total_after_gst):
    return total_after_gst * 0.20


def calculate_bill(a, b, c, d, e):
    total = total_amount(a, b, c, d, e)
    gst = calculate_gst(total)
    total_after_gst = total + gst
    discount = calculate_discount(total_after_gst)

    return total_after_gst - discount


a, b, c, d, e = 100, 100, 100, 100, 82.20

total = total_amount(a, b, c, d, e)
gst = calculate_gst(total)
total_after_gst = total + gst
discount = calculate_discount(total_after_gst)
payable = calculate_bill(a, b, c, d, e)

print(f"Total after GST = {total_after_gst:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {payable:.2f}")





    

