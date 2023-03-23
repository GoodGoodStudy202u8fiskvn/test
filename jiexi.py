import re

def parse_text(text):
    lines = text.strip().split('\n')#将文本内容去除空格，按'\n'分割转换成list
    parsed = {
        'name': lines[0].strip(),
        'lei': lines[1].strip(),
        'sub_fund': []
    }

    fund1 = None
    for line in lines[2:]:
        if not line.strip():
            continue

        if re.match(r'\d+\.', line):
            fund1 = {
                'title': line.split('.', 1)[1].strip(),
                'isin': []
            }

            if fund1:
                parsed['sub_fund'].append(fund1)

        else:
            fund1['isin'].append(line.strip())

    if fund1:
        parsed['sub_fund'].append(fund1)

    return parsed

long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

parsed_text = parse_text(long_text)
print(parsed_text)