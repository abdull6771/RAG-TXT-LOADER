# RAG Flask App

This project is a Retrieval-Augmented Generation (RAG) web application built with Flask. It allows users to upload and analyze text documents, leveraging modern web technologies for an interactive experience.

## Features

- **Document Upload:** Upload `.txt` files for analysis.
- **Text Analysis:** Analyze uploaded documents using RAG techniques (customize this section based on your app's capabilities).
- **Modern UI:** Responsive interface with custom CSS and JavaScript.
- **Image Support:** Static images for branding or illustration.

## Project Structure

```
app.py
static/
    css/
        styles.css
    images/
        picture.jpeg
        rag.png
    js/
        scripts.js
templates/
    about.html
    index.html
uploads/
    911_Calls_Analysis.txt
    Cover_Letter_Machine_learning_engineer.txt
    renewable_energy.txt
```

- `app.py`: Main Flask application.
- `static/`: Static assets (CSS, JS, images).
- `templates/`: HTML templates for the web interface.
- `uploads/`: Example uploaded text files.

## Getting Started

### Prerequisites

- Python 3.8+
- Flask

### Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd rag_flask_app
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```

### Running the App

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`.

## Customization

- Add or modify HTML templates in `templates/`.
- Update styles in `static/css/styles.css`.
- Add JavaScript functionality in `static/js/scripts.js`.
- Place additional images in `static/images/`.

## License

This project is provided for educational and demonstration purposes.
