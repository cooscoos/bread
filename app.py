"""A simple Flask app that serves Markdown pages"""
from typing import Dict
from flask import Flask, render_template, request
import markdown

# Create a Flask app
app = Flask(__name__)

# List of pages
pages: Dict[str, str] = {
    "Beginner Wholewheat Loaf": "beginner_wholewheat_loaf.md",
    "Beginner White Loaf": "beginner_white_loaf.md",
    "Sprouted Spelt Loaf": "sprouted_spelt.md",
}


@app.route('/')
def home():
    """Home route: renders the home page"""
    return render_template('home.html', pages=pages.keys())


@app.route('/<name>')
def page(name: str) -> str:
    """Page route: renders the requested page"""

    # Read in the Markdown file
    with open(pages[name], 'r', encoding='utf-8') as file:
        raw_markdown = file.read()

    # Replace relative markdown links with urls
    raw_markdown = replace_links(raw_markdown)
    content = markdown.markdown(raw_markdown, extensions=['extra', 'tables'])
    return render_template('page.html', name=name, content=content)


def replace_links(raw_markdown: str) -> str:
    """Replace relative markdown links with Flask URLs"""
    for webpage, filename in pages.items():
        # Construct the URL manually using the request object
        url = f"{request.url_root}{webpage.replace(' ', '%20')}"
        # Replace Markdown links with Flask URLs
        raw_markdown = raw_markdown.replace(f'](./{filename})', f']({url})')
    return raw_markdown


if __name__ == "__main__":
    # Run at localhost:5000
    app.run(host='0.0.0.0', debug=False)  # Set debug=True for development
