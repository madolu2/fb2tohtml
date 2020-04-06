class HTMLGenerator:
    def generate_description(self, author, annotation, book_title):
        description = f'<div id = "description">\n' \
        f'<p id = "name">{author[0]} {author[1]}</p> <br>\n' \
        f'<p id = "annotation">{annotation}</p> <br>\n' \
        f'<p id = "book-title">{book_title}</p> <br>\n<div>\n'
        return description

    def generate_section(self, title, text):
        section = f'<div class = "section">\n' \
        f'<h2>{title}</h2> <br>' \
        f'<p class = "text">{text}</p> <br>\n</div>\n'
        return section

    def generate_document(self, page_title, description, sections):
        document = '<!DOCTYPE html>\n' \
        '<html lang="en"\n>' \
        '<head>\n' \
        '\t<meta charset="UTF-8">\n' \
        '\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' \
        f'\t<title>{page_title}</title>\n' \
        '\t<link href = "css/base.css">\n' \
        '</head>\n<body>\n'
        document += description
        for section in sections:
            document += sections
        document += '</body>\n</html>'

        with open(f'{page_title}.html', 'w') as file:
            file.write(document)