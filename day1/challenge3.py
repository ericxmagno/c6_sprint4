from bs4 import BeautifulSoup
from IPython import embed

def generate_html():
    return """
        <html>
        <head></head>
        <body>
            <a href="/a.html">A</a>
            <a href="/b.html">B</a>
            <a href="/c.html">C</a>
            <a href="/d.html">D</a>
        </body>
    """

def main():
    html_doc = generate_html()
    # embed()
    soup = BeautifulSoup(html_doc, 'html.parser')
    div_elements = soup.find_all('a')

    for e in div_elements:
        print(e.get_text())
        print(e.get('href'))

if __name__ == "__main__":
    main()