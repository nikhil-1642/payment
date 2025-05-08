from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = request.form["amount"]
        upi_id = "9390286430@ybl"
        name = "Nikhil"

        # Generate UPI payment URI
        upi_uri = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn=Payment+via+UPI"

        # Create QR code
        qr = qrcode.make(upi_uri)

        # Ensure 'static' folder exists
        os.makedirs("static", exist_ok=True)

        # Save the QR code
        qr_path = os.path.join("static", "qr.png")
        qr.save(qr_path)

        return render_template("index.html", qr_path=qr_path, upi_uri=upi_uri)

    return render_template("index.html", qr_path=None, upi_uri=None)

if __name__ == "__main__":
    app.run(debug=True)
