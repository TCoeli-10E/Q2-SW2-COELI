from pyscript import document

def getting_allat(e):
    first_name = document.getElementById('input1').value
    last_name = document.getElementById('input2').value
    fil_grade = float(document.getElementById('filgr').value)
    pe_grade = float(document.getElementById('pegr').value)
    ict_grade = float(document.getElementById('ictgr').value)
    sci_grade = float(document.getElementById('scigr').value)
    mth_grade = float(document.getElementById('mthgr').value)
    eng_grade = float(document.getElementById('enggr').value)

    units = [5, 5, 5, 3, 1, 2]
    subjects = [sci_grade, mth_grade, eng_grade, fil_grade, pe_grade, ict_grade]

    total_units = sum(units)
    total_points = sum(g * u for g, u in zip(subjects, units))   # formula was googled
    gwa = total_points / total_units if total_units else 0   # to avoid division by zero
    if gwa > 74:
        document.getElementById('passfail').innerHTML = "you passed"
    else:
        document.getElementById('passfail').innerHTML = "you failed"

    html = f'''
    student name: {first_name} {last_name}<br>
    <strong>grades:</strong><br>
    Science: {sci_grade}<br>
    Mathematics: {mth_grade}<br>
    English: {eng_grade}<br>
    Filipino: {fil_grade}<br>
    PE: {pe_grade}<br>
    ICT: {ict_grade}<br>
    <strong>GWA:</strong> {gwa:.2f}
    '''   # i googled the decimal place thing i think
    Passd = f'''Passed'''
    faild = f'''Failed'''

    document.getElementById('output').innerHTML = html
