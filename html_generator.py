class HTMLGenerator:
    def generate_description(self, author, annotation, book_title):
        description = f'<div id = "description">\n' \
        f'<p id = "name">{author[0]} {author[1]}</p> <br>\n' \
        f'<p id = "annotation">{annotation}</p> <br>\n' \
        f'<p id = "book-title">{book_title}</p> <br>\n<div>\n'
        return description

    def generate_section(self, title, text, sub_section = False):
        if sub_section:
            section = f'<div class = "sub-section">\n'
            for t in title:
                section += f'<h3>{t}</h3>\n'
            section += f'{text}\n</div>\n'
        else:
            section = f'<div class = "section">\n'
            for t in title:
                section += f'<h2>{t}</h2>\n'
            section += f'{text}\n</div>\n'
        return section

    def wrap_paragraph(self, paragraphs):
        wrapped_paragraphs = ''
        for paragraph in paragraphs:
            if paragraph:
                wrapped_paragraphs += (f'<p>{paragraph}</p>\n')
        return wrapped_paragraphs

    def generate_document(self, page_title, description, sections):
        document = '<!DOCTYPE html>\n' \
        '<html lang="en"\n>' \
        '<head>\n' \
        '\t<meta charset="UTF-8">\n' \
        '\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' \
        f'\t<title>{page_title}</title>\n' \
        '\t<link rel="stylesheet" href="../css/base.css">\n' \
        '</head>\n<body>\n'
        document += description
        for section in sections:
            document += section
        document += '</body>\n</html>'
        return document, page_title