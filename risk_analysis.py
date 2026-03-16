def analyze_risks(values):

    risks = []

    if values.get("glucose",0) > 140:
        risks.append("Possible diabetes risk")

    if values.get("cholesterol",0) > 200:
        risks.append("Heart disease risk")

    if values.get("ldl",0) > 130:
        risks.append("High LDL cholesterol")

    if values.get("creatinine",0) > 1.3:
        risks.append("Possible kidney issue")

    if values.get("hemoglobin",15) < 12:
        risks.append("Possible anemia")

    if values.get("platelets",200000) < 150000:
        risks.append("Low platelet count")

    if not risks:
        risks.append("No major risks detected")

    return risks