from flask import Flask, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename
import os
import uuid
from weasyprint import HTML

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form.to_dict()

    # Save uploaded photo
    photo = request.files['photo']
    filename = f"{uuid.uuid4().hex}_{secure_filename(photo.filename)}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    photo.save(filepath)
    photo_url = url_for('static', filename=filename)
    data['photo_url'] = filepath

    # Select the template
    template = data.get("template", "resume_template1") + ".html"

    # Render HTML with data
    rendered = render_template(template, **data)

    # Generate PDF
    pdf_path = f"{uuid.uuid4().hex}_resume.pdf"
    HTML(string=rendered, base_url='.').write_pdf(pdf_path)

    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
