# Tangkap galat

def iniString(str):
    try:
        nilai = int(str)
    except ValueError:
        nilai = float(str)
    return nilai
