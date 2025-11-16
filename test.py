invoice_no = 68
customer = "John Doe"
amount = 199.99

print("=" * 30)
print("INVOICE".center(30))
print("Hello Mart".center(30))
print(f"INVOICE NO: INV-{str(invoice_no).rjust(8, '0')}".center(30))
print(f"Customer's Name: {customer}".center(30))
print(f"Amount to be Paid: ${amount:.2f}".center(30))
print("=" * 30)
