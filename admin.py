from flask import Flask, request, jsonify

app = Flask(__name__)

# مفتاح الأمان المعتمد
SECRET_KEY = "Bin_Al_Walid_Secure_Fortress_2026"

@app.route('/verify', methods=['POST'])
def verify_access():
    data = request.json
    user_key = data.get('key')
    
    if user_key == SECRET_KEY:
        return jsonify({"status": "success", "message": "تم التحقق بنجاح"})
    else:
        return jsonify({"status": "error", "message": "مفتاح أمان غير صحيح"}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)
