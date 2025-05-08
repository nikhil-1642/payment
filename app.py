from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = request.form.get('amount')
        upi_id = "9390286430@ibl"
        name = "Nikhil"
        note = "Payment via UPI"

        if not amount or float(amount) <= 0:
            return "Enter a valid amount."

        upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={note}"

        # Make sure static folder exists
        os.makedirs("static", exist_ok=True)

        # Generate QR code
        qr = qrcode.make(upi_url)
        qr_path = os.path.join("static", "qr.png")
        qr.save(qr_path)

        return render_template('pay.html', qr_path=qr_path, amount=amount, name=name, upi_url=upi_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
