"""
* This is a currency converter program.
* This uses the Exchange Rates API to get real-time exchange rates.
* Free version only allows EUR to be the base currency
* To enable conversions between all currencies,
    1) EUR/user_input_currency exchange rate is calculated
    2) EUR/user_quoted_currency exchange rate is calculated
    3) user_input_currency/user_quoted_currency is calculated by
        (EUR/user_quoted_currency) / (EUR/user_input_currency)
* Program is optimized to minimise the API calls
"""

import requests

# setting up API key and base URL
api_key  = "13538ac5e9be3fe26154a91ecf6fc404"
base_url = "http://api.exchangeratesapi.io/v1/"
endpoint = "latest" # fetches latest rates from the dataset

def display_all_codes():
    params = {
        "access_key" : api_key,
    }
    response = requests.get(base_url + "symbols", params = params)

    data = response.json()

    # Accessing symbols and printing key-value pairs in groups of two with fixed width
    symbol_pairs = data['symbols'].items()
    for index, (key, value) in enumerate(symbol_pairs):
        print(f"{key.ljust(5)}: {value.ljust(30)}", end='\t')
        # Print new line after every two pairs
        if (index + 1) % 2 == 0:
            print()

def generate_exchange_rates(currency_code):
    params = {
        "access_key" : api_key,
        "base" : "EUR",
        "symbols" : currency_code
    }
    try:
        response = requests.get(base_url + endpoint, params = params)

        data = response.json()

        # extracting the rates from the JSON content
        exchange_rate = data["rates"][currency_code]
        return exchange_rate

    except (requests.RequestException, KeyError) as e:
        print(f"Error: {e}")
        return None


print("*** REAL-TIME CURRENCY CONVERTER ***")

# to monitor the API calls
api_calls = 0

# exchange rates against EUR
base_currency_code = input("Enter the base currency code ['help' to get all codes]: ").upper()
if base_currency_code == "EUR":
    base_exchange_rate_EUR = 1
elif base_currency_code == "HELP":
    display_all_codes()
    api_calls += 1
    base_currency_code = input("Enter the base currency code: ").upper()
    if base_currency_code == "EUR":
        base_exchange_rate_EUR = 1
    else:
        base_exchange_rate_EUR = generate_exchange_rates(base_currency_code)
        api_calls += 1
else:
    base_exchange_rate_EUR = generate_exchange_rates(base_currency_code)
    api_calls += 1

# end if API calling errors
if (base_exchange_rate_EUR is None):
    print("Program terminated due to failed API requests.")
    quit()

quoted_curreny_code = input("Enter the output currency code: ").upper()
if quoted_curreny_code == "EUR":
    quoted_exchange_rate_EUR = 1
elif quoted_curreny_code == base_currency_code:
    quoted_exchange_rate_EUR = base_exchange_rate_EUR
else:
    quoted_exchange_rate_EUR = generate_exchange_rates(quoted_curreny_code)
    api_calls += 1

# end if API calling errors
if (quoted_exchange_rate_EUR is None):
    print("Program terminated due to failed API requests.")
    quit()

# exchange rates against the base and quoted currencies
final_exchange_rate = round(quoted_exchange_rate_EUR / base_exchange_rate_EUR, 6)

#calculating the amount to quoted currency
amount = int(input("Enter the amount to convert: "))
converted_amount = round(amount * final_exchange_rate, 2)

# printing output values
print(f"Exchange rate of {base_currency_code} to {quoted_curreny_code} is {final_exchange_rate}")
print(f"{amount} {base_currency_code} = {converted_amount} {quoted_curreny_code}")

#printing the number of API calls
print_api_calls = input("See the number of API calls? [y/n]: ")
if print_api_calls.lower() == "y":
    print(api_calls)

print("Thank you for using the program...")