import requests

pars_res_list=[]
response=requests.get("https://bank.gov.ua/ua/markets/exchangerate")
response_text=response.text
response_parse=response_text.split("<span>")
for parse_elem_2 in response_parse:
    if parse_elem_2.startswith("$"):
        for parse_elem_2 in parse_elem_2.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                pars_res_list.append(parse_elem_2)

AUD=pars_res_list[0]
print(f"AUD - {AUD}")

AZN=pars_res_list[1]
print(f"AZN - {AZN}")

BYN=pars_res_list[2]
print(f"BYN - {BYN}")

BGN=pars_res_list[3]
print(f"BGN - {BGN}")

KRW=pars_res_list[4]
print(f"KRW - {KRW}")

HKD=pars_res_list[5]
print(f"HKD - {HKD}")

DKK=pars_res_list[6]
print(f"DKK - {DKK}")

USD=pars_res_list[7]
print(f"USD - {USD}")

EUR=pars_res_list[8]
print(f"Avalanche - {EUR}")


