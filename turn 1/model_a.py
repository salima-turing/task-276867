from flask import Flask, request, jsonify

app = Flask(__name__)

REGULATORY_DATA = {
    "drug_names": ["Avastin", "Ceritinib", "Imfinzi"],
    "indications": ["Cancer", "Metastatic Cancer", "Immune Suppression"]
}


@app.route('/compliance_check', methods=['POST'])
def compliance_check():
    try:
        data = request.get_json()
        drug_name = data.get('drug_name')
        indication = data.get('indication')

        is_compliant = perform_compliance_check(drug_name, indication)

        response = {
            "drug_name": drug_name,
            "indication": indication,
            "is_compliant": is_compliant
        }
        return jsonify(response), 200
    except KeyError as e:
        return jsonify(error=str(e)), 400


def perform_compliance_check(drug_name, indication):
    is_compliant_drug = drug_name in REGULATORY_DATA["drug_names"]
    is_compliant_indication = indication in REGULATORY_DATA["indications"]

    return is_compliant_drug and is_compliant_indication


if __name__ == '__main__':
    app.run(debug=True)
