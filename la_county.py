import re
import requests
import time

def single_regex(pattern, target_string):
    data = re.findall(pattern, target_string)
    return data[0] if data else ''

with open("input_ain.txt", "r") as file:
    data_list = [line.strip() for line in file]
    
    
    
output_data = "Input ID\tSitus Street\tSitus City\tSitus Zip Code\tUse Type\tParcel Type\tParcel Status\tTax Rate Area\tCreate Date\tDelete Date\tTax Status\tTax Defaulted Year\tExemption\tUse Code\tDesign Type\tQuality Class\tNum Of Units\tNum Of Beds\tNum Of Baths\tSqft Main\tYear Built\tEffective Year\tUsable Sqft Lot\n"

with open("OutPut.txt", 'w') as OP:
    OP.write(output_data)


for input_id in data_list:
    
    main_url = f"https://portal.assessor.lacounty.gov/api/parceldetail?ain={input_id}"

    content_response = requests.get(main_url)
    response_code = content_response.status_code
    print(response_code)
    content = content_response.text
    time.sleep(5)

    with open('Result_page.html', 'w', encoding='utf-8') as SP:
        SP.write(content)
        
    SitusStreet = single_regex(r'SitusStreet\"\:\"([^>]*?)\"',str(content))
    SitusCity = single_regex(r'SitusCity\"\:\"([^>]*?)\"',str(content))
    SitusZipCode = single_regex(r'SitusZipCode\"\:\"([^>]*?)\"',str(content))
    UseType = single_regex(r'UseType\"\:\"([^>]*?)\"',str(content))
    ParcelType = single_regex(r'ParcelType\"\:\"([^>]*?)\"',str(content))
    ParcelStatus = single_regex(r'ParcelStatus\"\:\"([^>]*?)\"',str(content))
    TaxRateArea = single_regex(r'TaxRateArea\"\:\"([^>]*?)\"',str(content))
    CreateDate = single_regex(r'CreateDate\"\:\"([^>]*?)\"',str(content))
    DeleteDate = single_regex(r'DeleteDate\"\:\"([^>]*?)\"',str(content))
    TaxStatus = single_regex(r'TaxStatus\"\:\"([^>]*?)\"',str(content))
    TaxDefaultedYear = single_regex(r'TaxDefaultedYear\"\:\"([^>]*?)\"',str(content))
    Exemption = single_regex(r'Exemption\"\:\"([^>]*?)\"',str(content))
    UseCode = single_regex(r'UseCode\"\:\"([^>]*?)\"',str(content))
    DesignType = single_regex(r'DesignType\"\:\"([^>]*?)\"',str(content))
    QualityClass = single_regex(r'QualityClass\"\:\"([^>]*?)\"',str(content))
    NumOfUnits = single_regex(r'NumOfUnits\"\:\"([^>]*?)\"',str(content))
    NumOfBeds = single_regex(r'NumOfBeds\"\:\"([^>]*?)\"',str(content))
    NumOfBaths = single_regex(r'NumOfBaths\"\:\"([^>]*?)\"',str(content))
    SqftMain = single_regex(r'SqftMain\"\:\"([^>]*?)\"',str(content))
    YearBuilt = single_regex(r'YearBuilt\"\:\"([^>]*?)\"',str(content))
    EffectiveYear = single_regex(r'EffectiveYear\"\:\"([^>]*?)\"',str(content))
    UsableSqftLot = single_regex(r'UsableSqftLot\"\:\"([^>]*?)\"',str(content))

    output_data = f"{input_id}\t{SitusStreet}\t{SitusCity}\t{SitusZipCode}\t{UseType}\t{ParcelType}\t{ParcelStatus}\t{TaxRateArea}\t{CreateDate}\t{DeleteDate}\t{TaxStatus}\t{TaxDefaultedYear}\t{Exemption}\t{UseCode}\t{DesignType}\t{QualityClass}\t{NumOfUnits}\t{NumOfBeds}\t{NumOfBaths}\t{SqftMain}\t{YearBuilt}\t{EffectiveYear}\t{UsableSqftLot}\n"

    with open("OutPut.txt", 'a') as OP:
        OP.write(output_data)
    print("completed ID: ",str(input_id))
print("Completed")