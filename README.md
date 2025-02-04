# Los Angeles County Assessor Parcel Scraper

This Python script scrapes parcel details from the Los Angeles County Assessor's website using GET requests and saves the extracted information in a text file. The information includes situs street, situs city, situs zip code, use type, parcel type, parcel status, tax rate area, create date, delete date, tax status, tax defaulted year, exemption, use code, design type, quality class, number of units, number of beds, number of baths, square footage of the main building, year built, effective year, and usable square footage of the lot.

## Features
- Scrapes parcel details from the LA County Assessor's website.
- Extracts information such as situs street, situs city, situs zip code, use type, parcel type, parcel status, tax rate area, create date, delete date, tax status, tax defaulted year, exemption, use code, design type, quality class, number of units, number of beds, number of baths, square footage of the main building, year built, effective year, and usable square footage of the lot.
- Saves the extracted information into a text file (`OutPut.txt`).

## Requirements
- Python 3.x
- `requests` library
- `re` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/maruthachalams/Los-Angeles-County-Assessor-Portal-Scraper.git
    cd la-county-assessor-scraper
    ```
2. Install the required libraries:
    ```sh
    pip install requests
    ```

## Usage
1. Ensure the input data file `input_ain.txt` contains the parcel numbers you want to scrape, with one parcel number per line.
2. Run the script:
    ```sh
    python scraper.py
    ```
3. The output will be saved in a file named `OutPut.txt`.

## Code Explanation
### `single_regex(pattern, target_string)`
This function uses regular expressions to find matches in a target string and returns the first match found.

### Main Script
1. Initializes an output string with headers and writes it to `OutPut.txt`.
2. Reads parcel numbers from the `input_ain.txt` file and stores them in a list.
3. For each parcel number in the list:
    - Sends a GET request to the LA County Assessor's API.
    - Prints the response status code and writes the response content to `Result_page.html`.
    - Extracts information such as `SitusStreet`, `SitusCity`, `SitusZipCode`, `UseType`, `ParcelType`, `ParcelStatus`, `TaxRateArea`, `CreateDate`, `DeleteDate`, `TaxStatus`, `TaxDefaultedYear`, `Exemption`, `UseCode`, `DesignType`, `QualityClass`, `NumOfUnits`, `NumOfBeds`, `NumOfBaths`, `SqftMain`, `YearBuilt`, `EffectiveYear`, and `UsableSqftLot`.
    - Formats the extracted information and appends it to `OutPut.txt`.
    - Prints "completed ID" for each parcel number.


