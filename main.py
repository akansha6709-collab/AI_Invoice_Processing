import pymupdf
import pytesseract
doc = pymupdf.open("sample-invoice.pdf")

print(len(doc))
print(doc[0])

text = doc[0].get_text()
print(text)


lines = text.splitlines()
print(lines)

print("Number of lines:", len(lines))

# clean text

clean_lines = [line.strip()for line in lines]
print(clean_lines)

print(clean_lines[:10])
print("Empty lines:",clean_lines.count(""))

clean_lines = [line for line in clean_lines if line != ""]
print(clean_lines)

for line in clean_lines:
    if line.startswith("INV-"):
        invoice_number = line
        print(invoice_number)


for line in clean_lines:
    if "September" in line:
        invoice_date = line
        print(line)

for line in clean_lines:
    if "Subtotal" in line:
        index = clean_lines.index(line)
        subtotal = clean_lines[index+1]
        subtotal = clean_lines[index + 1]
        print(subtotal)

for line in clean_lines:
    if "GST at 18%" in line:
        tax = line.split("₹")[1]
        print(tax)


for line in clean_lines:
    if "Total due" in line:
        total = line.split("₹")[1]
        print(total)


print(clean_lines[:5])
vendor_name = clean_lines[0]
print(vendor_name)


subtotal = subtotal.replace("₹","").replace(",","")
print(subtotal)

subtotal = float(subtotal)
print(subtotal)
print(type(subtotal))


tax = tax.replace(",","")
print(tax)

tax = float(tax)
print(tax)
print(type(tax))

total_amount = total.replace(",","")
print(total_amount)

total_amount = float(total_amount)
print(total_amount)
print(type(total_amount))

calculated_total = subtotal + tax
print(calculated_total)

if calculated_total == total_amount:
    print("Invoice total is correct")
else:
    print("Invoice total mismatch")


if vendor_name:
    print("Vendor name is available")
else:
    print("Vendor name is missing")

if invoice_number:
    print("Invoice number is available")
else:
    print("Invoice number is missing") 

if invoice_date:
    print("Invoice date is available")
else:
    print("Invoice date is missing")     

if subtotal:
    print("subtotal is available")
else:
    print("subtotal is missing")    

if tax:
    print("tax is available")
else:
    print("tax is missing")  

if total_amount:
    print("total amount is available")
else:
    print("total amount is missing")      

missing_fields = []

if not vendor_name:
    missing_fields.append("vendor_name")

if not invoice_number:
    missing_fields.append("invoice_number")

print(missing_fields)

if not invoice_date:
    missing_fields.append("invoice_date")

if not subtotal:
    missing_fields.append("subtotal")   

if not tax:
    missing_fields.append("tax")

if not total_amount:
    missing_fields.append("total_amount")    

print(missing_fields)

if missing_fields:
    print("Missing fields:", missing_fields)
else:
    print("All required fields are available")



# Create structured JSON output

invoice_data = {}
invoice_data["vendor_name"] = vendor_name
invoice_data["invoice_number"] = invoice_number
invoice_data["invoice_date"] = invoice_date
invoice_data["subtotal"] = subtotal
invoice_data["invoice_date"] = invoice_date
invoice_data["tax"] = tax
invoice_data["total_amount"] = total_amount
print(invoice_data)

import json
json_data = json.dumps(invoice_data, indent=4)
print(json_data)

with open("invoice_data.json", "w") as file:
    file.write(json_data)




def extract_invoice_text(pdf_path):
    try:
        doc = pymupdf.open(pdf_path)
    except Exception:
        return ""
    text = doc[0].get_text()
    if not text.strip():
        page = doc[0]
        pix = page.get_pixmap()
        image = pix.pil_image()
        text = pytesseract.image_to_string(image)
    return text

text=extract_invoice_text("sample-invoice.pdf")
print(text)
print(text[:500])


def clean_invoice_text(text):
    lines = text.splitlines()
    clean_lines = [line.strip() for line in lines]
    clean_lines = [line for line in clean_lines if line]
    return clean_lines

text = extract_invoice_text("sample-invoice.pdf")
clean_lines = clean_invoice_text(text)

print(clean_lines[:5])

def extract_invoice_fields(clean_lines):
    invoice_data = {}
    invoice_data["vendor_name"] = clean_lines[0]

    for line in clean_lines:
        if line.startswith("INV-"):
            invoice_data["invoice_number"] = line   

    for line in clean_lines:
        if "September" in line:
            invoice_data["invoice_date"] = line

    for line in clean_lines:
        if "Subtotal" in line:
            index = clean_lines.index(line)
            subtotal = float(clean_lines[index + 1].replace("₹", "").replace(",", ""))
            invoice_data["subtotal"] = subtotal
                 

    for line in clean_lines:
        if "GST at 18%" in line:
            tax = float(line.split("₹")[1].replace(",", ""))
            invoice_data["tax"] = tax

    for line in clean_lines:
        if "Total due" in line:
            total_amount = float(line.split("₹")[1].replace(",", ""))
            invoice_data["total_amount"] = total_amount

    return invoice_data


invoice_data = extract_invoice_fields(clean_lines)
print(invoice_data)


def validate_invoice(invoice_data):
    missing_fields = []

    required_fields = [
        "vendor_name",
        "invoice_number",
        "invoice_date",
        "subtotal",
        "tax",
        "total_amount"
    ]

    for field in required_fields:
        if invoice_data.get(field) is None or invoice_data.get(field) == "":
            missing_fields.append(field)

    if all(field in invoice_data for field in ["subtotal", "tax", "total_amount"]):
        calculated_total = invoice_data["subtotal"] + invoice_data["tax"]

        if calculated_total == invoice_data["total_amount"]:
            total_status = "Invoice total is correct"
        else:
            total_status = "Invoice total mismatch"
    else:
        total_status = "Cannot validate total: amount fields missing"

    validation_result = {
        "missing_fields": missing_fields,
        "total_status": total_status,
        "is_valid": len(missing_fields) == 0 and total_status == "Invoice total is correct"
    }

    return validation_result

validation_result = validate_invoice(invoice_data)
print(validation_result)

    
def save_invoice_json(invoice_data, validation_result):
    invoice_data["validation"] = validation_result
    json_data = json.dumps(invoice_data, indent=4)
    with open("invoice_data.json", "w") as file:
        file.write(json_data)

     
save_invoice_json(invoice_data, validation_result)
print("Invoice JSON saved successfully")

print(invoice_data)

test_invoice = {
    "vendor_name": "Test Vendor",
    "invoice_number": "INV-TEST-002",
    "invoice_date": "21 October 2026",
    "subtotal": 1000.0,
    "tax": 180.0,
    "total_amount": 1500.0
}
print(validate_invoice(test_invoice))

