from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/books'
COVER_FOLDER = 'static/covers'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COVER_FOLDER, exist_ok=True)

# Homepage
@app.route('/')
def index():
    books = []
    for filename in os.listdir(UPLOAD_FOLDER):
        if filename.endswith(".pdf"):
            title = filename.replace('.pdf','')
            cover_path = os.path.join(COVER_FOLDER, f"{title}.jpg")
            if os.path.exists(cover_path):
                cover = f"static/covers/{title}.jpg"   # use uploaded cover
            else:
                cover = 'static/images/java_logo.jpg'  # default cover if no custom one

            books.append({
                'title': title,
                'file': f'static/books/{filename}',
                'cover': cover
            })
    return render_template('index.html', books=books)

# Upload book + cover
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        book_file = request.files['book']
        cover_file = request.files['cover']

        if book_file and book_file.filename.endswith('.pdf'):
            # Save PDF
            book_path = os.path.join(UPLOAD_FOLDER, book_file.filename)
            book_file.save(book_path)

            # Save cover (if provided)
            if cover_file and cover_file.filename.endswith(('.jpg', '.png', '.jpeg')):
                # Ensure cover name matches book name
                title = book_file.filename.replace('.pdf','')
                cover_path = os.path.join(COVER_FOLDER, f"{title}.jpg")
                cover_file.save(cover_path)

            return redirect(url_for('index'))

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
