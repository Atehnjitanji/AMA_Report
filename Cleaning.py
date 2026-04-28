import re

def remove_clutter(year:str) -> str:
    if not year or str(year).lower() == 'nan':
        return ''
    return year

def just_year(year: str) -> str:
    output = re.findall('[0-9]+/[0-9]+/[0-9]+', year)
    i = 0
    final = ''
    if output and len(output) > 1:
        while i < 2:
            output[i] = output[i].split('/')
            i += 1
        if len(output[0][2]) == len(output[1][2]):
            if output[0][2] < output[1][2]:
                final = year_format(output[0][2])
            else:
                final = year_format(output[1][2])
        else:
            a = year_format(output[0][2])
            b = year_format(output[1][2])
            if a < b:
                final = a
            else:
                final = b
    elif len(output) == 1:
        output[0] = output[0].split('/')
        final = year_format(output[0][2])
    elif len(re.findall('[0-9]{2,4}',year)) == 1:
        return year_format(re.findall('[0-9]{2,4}',year)[0])
    elif re.findall('[0-9]+-.+-[0-9]{2,4}', year):
        output = re.findall('[0-9]+-.+-[0-9]{2,4}', year)
        output = output[0].split('-')
        return year_format(output[2])
    elif re.findall('[0-9]{4}',year):
        output = re.findall('[0-9]{4}',year)
        output.sort()
        return output[0]
    return final

def year_format(year:str) -> str:
    output = re.findall('[0-9]{2,4}',year)
    if not output:
        return ''
    output = add_19(output[0])
    return output

def add_19(year:str) -> str:
    output = "19"
    if len(year) == 2:
        output = output + year
        return output
    return year

'''def exit_year(year: str) -> str:
    year_clean = remove_clutter(year)
    year_clean = year_format(year_clean)
    return year_clean'''




