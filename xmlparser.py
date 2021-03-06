import xml.etree.ElementTree as ET
import sys


class XMLParser:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.root = ET.parse(filename).getroot()
            for element in  self.root.iter():
                element.tag = element.tag.partition('}')[-1]
        except AttributeError as e:
            self.logging('__init__', e)

    def logging(self, module, exceprion):
        with open('log.txt', 'a') as logfile:
            import datetime
            logfile.write(f'{datetime.datetime.now()} Error in {module} {self.filename} -> {exceprion}\n')

    def get_description(self):
        try:
            author = self.root.find('.//author/first-name').text, self.root.find('.//author/last-name').text
            annotation = self.root.find('.//annotation/p').text
            book_title = self.root.find('.//book-title').text
            description = {'author': author,
                            'annotation': annotation,
                            'book-title': book_title}
            return description
        except AttributeError as e:
            self.logging('get_description', e)

    def get_text(self):
        try:
            bodys = self.root.findall('body')
            #Get all sections from book
            sections = bodys[0].findall('.//section')
            #Create array for sections
            sections_array = []
            for section in sections:
                subsections_array = []
                #Create section.p and subsection.p arrays
                stexts = []
                stitles = []
                subsection_dict = None
                #Find section.title
                section_title = section.find('title')
                #If title == None -> title = '---'
                if section_title:
                    section_title = section_title.findall('p')
                    for stitle in section_title:
                        stitles.append(stitle.text)
                else:
                    stitles = ''
                #Find all section.p
                section_texts = section.findall('p')
                for section_text in section_texts:
                    stexts.append(section_text.text)
                #Find all subsections
                subsections = section.findall('section')
                #Find subsection.title and all subsection.p
                for subsection in subsections:
                    subtexts = []
                    subtitles = []
                    subsection_title = subsection.find('title')
                    #If title == None -> title = '---'
                    if subsection_title:
                        subsection_title = subsection_title.findall('p')
                        for stitle in subsection_title:
                            subtitles.append(stitle.text)
                    else:
                        subsection_title = ''
                    
                    subsection_texts = subsection.findall('p')
                    if subsection_texts:
                        #Fill subsection.p array
                        for subsection_text in subsection_texts:
                            subtexts.append(subsection_text.text)
                        subsection_dict = {'subsection-title': subtitles,
                                        'subsection-texts': subtexts}
                        subsections_array.append(subsection_dict)
                        
                section_dict = {'section-title': stitles,
                        'section-texts': stexts,
                        'subsections': subsections_array}
                #Fill section.p array
                sections_array.append(section_dict)
            return sections_array
        except AttributeError as e:
            self.logging('get_text', e)
        
                
