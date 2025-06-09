# AutoResume – Intelligent Resume Generator
#### Video Demo:  <https://youtu.be/your-video-link-here>
#### Description:

AutoResume is a web-based application designed to help users effortlessly generate professional, polished resumes in PDF format by simply filling out a form. Whether you're a student, fresher, or working professional, AutoResume streamlines the resume creation process and eliminates the need for complex design tools or writing templates from scratch.

### 💡 Key Features:

- **Simple Form Interface**: Users can enter their details through a clean and intuitive web form.
- **Photo Upload**: Option to include a professional-looking photo in the resume.
- **Template Styling**: Modern and minimalistic resume templates that adapt well to professional use.
- **PDF Resume Generation**: Automatically generates a downloadable PDF version of the resume.
- **Responsive Design**: Works smoothly across desktops and mobile devices.
- **Modular Code Structure**: Designed for easy scalability and future enhancements like multiple templates, font styles, etc.

### 🚀 How It Works:

1. **User Input**: The user fills out a web form with details such as name, contact info, education, work experience, skills, languages, references, and summary.
2. **Template Rendering**: Data is inserted dynamically into a pre-styled HTML/CSS resume template.
3. **PDF Conversion**: Using a PDF library (like `xhtml2pdf`, `WeasyPrint`, or `reportlab`), the HTML content is converted into a downloadable PDF.
4. **Output**: The user can view and download their resume instantly.

### 🛠️ Technologies Used:

- **Frontend**: HTML5, CSS3, Bootstrap
- **Backend**: Python (Flask Framework)
- **PDF Generation**: `xhtml2pdf` / `WeasyPrint`
- **Other Libraries**: Flask-WTF (optional), Jinja2 for templating

### ✅ Future Improvements:

- Support for multiple resume templates
- Auto-save user data and profile creation
- Dark mode toggle for the form interface
- Option to import data from LinkedIn
- Mobile-friendly resume preview

### 🙋‍♂️ Target Users:

- College students applying for internships
- Fresh graduates looking for job opportunities
- Freelancers and gig workers creating quick portfolios

### 📦 Installation & Run Locally:

```bash
git clone https://github.com/Sankarshan77/AutoResume.git
cd autoresume
pip install -r requirements.txt
python app.py



