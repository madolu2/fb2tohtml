import xmlparser
import html_generator
import os


books_dir = 'books'
books = os.listdir(books_dir)
for book in books:
    #Create XMLParser and HTMLGenerator instances
    xmlp = xmlparser.XMLParser(f'{books_dir}/{book}')
    htmlgen = html_generator.HTMLGenerator()

    #Get description and texts from book
    xml_description = xmlp.get_description()
    xml_texts = xmlp.get_text()
    sections = []
    titles = []
    count = 0
    #Generate description block
    description = htmlgen.generate_description(xml_description['author'], xml_description['annotation'], xml_description['book-title'])
    for xml_text in xml_texts:
        count += 1
        section_text = ''
        titles.append(htmlgen.wrap_title(xml_text['section-title'], count))
        if xml_text['section-texts']:
            #Wrap text into <p></p> tags
            section_text = htmlgen.wrap_paragraph(xml_text['section-texts'])
        #Generate section block
        section = htmlgen.generate_section(xml_text['section-title'], section_text, count)
        sections.append(section)
        if xml_text['subsections']:
            for subsection in xml_text['subsections']:
                subsection_text = htmlgen.wrap_paragraph(subsection['subsection-texts'])
                #If book have subsections
                if subsection_text:
                    #Generate subsection block
                    section = htmlgen.generate_section(subsection['subsection-title'], subsection_text, count, sub_section=True)
                    sections.append(section)
    #Generate HTML document
    document, title = htmlgen.generate_document(xml_description['book-title'], description, sections, ''.join(titles))
    #Create *.html file
    with open(f'html_library/{title}.html', 'w', encoding='utf-8') as file:
        file.write(document)