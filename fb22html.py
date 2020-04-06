import xmlparser
import html_generator


xmlp = xmlparser.XMLParser('filename.fb2')
htmlgen = html_generator.HTMLGenerator()

xml_description = xmlp.get_description()
xml_texts = xmlp.get_text()
sections = []

description = htmlgen.generate_description(xml_description['author'], xml_description['annotation'], xml_description['book_title'])
for xml_text in xml_texts:
    section = htmlgen.generate_section(xml_text['p-title'], xml_text['p-text'])
    sections.append(section)

htmlgen.generate_document(xml_description['book-title'], description, sections)
