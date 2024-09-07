from flask import Flask, render_template, request
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code = None
    entered_text = ""  

    if request.method == 'POST':
        entered_text = request.form.get('data')

        
        if entered_text:
            img = qrcode.make(entered_text)
            buf = BytesIO()
            img.save(buf, format='PNG')
            buf.seek(0)

            
            qr_code = base64.b64encode(buf.getvalue()).decode('utf-8')
 
    return render_template('index.html', qr_code=qr_code, entered_text=entered_text)

if __name__ == '__main__':
    app.run(debug=True)


