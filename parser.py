import os
import xml.etree.ElementTree as ET


class XMLParser:
    def __init__(self, filename):
        try:
            self.root = ET.parse(filename).getroot()
            for element in  self.root.iter():
                element.tag = element.tag.partition('}')[-1]
        except Exception as e:
            print(f'Error -> {e}')

    def get_description(self):
        try:
            author = self.root.find('./description/title-info/author/first-name').text, self.root.find('./description/title-info/author/last-name').text
            annotation = self.root.find('./description/title-info/annotation/p').text
            book_title = self.root.find('./description/title-info/book-title').text
            description = {'author': author,
                            'annotation': annotation,
                            'book-title': book_title}
            return description
        except Exception as e:
            print(f'Error -> {e}')

    def get_text(self):
        try:
            sections = self.root.findall('./body/section')
            dict_sections = []
            for child in sections:
                texts = []
                title = child.find('title')
                p_title = title.find('p').text
                p_texts = child.findall('p')
                for p_text in p_texts:
                    texts.append(p_text.text.replace('\xa0', ' '))
                dict = {'p-title': p_title,
                        'p-texts': texts}
                dict_sections.append(dict)
            return dict_sections
        except Exception as e:
            print(f'Error -> {e}')
        
                
