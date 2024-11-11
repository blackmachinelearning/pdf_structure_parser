import pymupdf
import re
import json
import os
import datetime
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import Config

from config import Config


class PDFParser:

    def __init__(self, doc):
        self.doc = doc
        self.toc = doc.get_toc()
        self.structure_file_path = None
        self.structure = self.structurize_doc()


    def structurize_doc(self) -> dict:
        structure = {}
        current_chapter = ""
        current_section = ""
        current_subsection = ""
        for ind, i in enumerate(self.toc):
            if re.match(pattern=r"Глава \d+", string=i[1]):
                current_chapter = re.search(pattern=r'\d+', string=i[1]).group()
                structure[current_chapter] = {
                    "title": "",
                    "sections": {},
                    "page": i[2],
                }

            elif structure.get(current_chapter) and structure.get(current_chapter)["title"] == "":
                structure.get(current_chapter)["title"] = i[1]
            elif current_chapter != "":
                chapter = structure[current_chapter]
                if re.match(pattern=f'{current_chapter}\.', string=i[1]):
                    section_parts = i[1].split(" ")
                    if len(section_parts[0].split(".")) < 3:
                        current_section = section_parts[0]
                        chapter["sections"][current_section] = {
                            "title": ' '.join(section_parts[1:]),
                            "subsections": {},
                            "page": i[2],
                        }
                    else:
                        current_subsection = section_parts[0]
                        chapter["sections"][current_section]["subsections"][current_subsection] = {
                            "title": ' '.join(section_parts[1:]),
                            "page": i[2],
                        }
        return structure
    

    def save_structure(self, structure_filepath):
        self.structure_file_path = structure_filepath
        json_formatted_structure = json.dumps(
            self.structure,
            sort_keys=True,
            indent=4,
            separators=(',', ': '),
            ensure_ascii=False
        )
        with open(self.structure_file_path, "w+", encoding="utf-8") as f:
            f.write(json_formatted_structure)

    
if __name__ == "__main__":
    doc = pymupdf.open(os.path.join(Config.DATA_PATH, Config.FILE_NAME))
    pp = PDFParser(doc=doc)
    extracted_file_name = f'structure_{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")}.json'
    pp.save_structure(os.path.join(Config.EXTRACTED_DATA_PATH, extracted_file_name))