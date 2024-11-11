import pymupdf
import json
import os
import datetime
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import Config


class PDFParserUniversal:

    def __init__(self, doc):
        self.doc = doc
        self.toc = doc.get_toc()
        self.structure_file_path = None
        self.structure = self.process_toc()

    def process_toc(self) -> dict:
        structure = {}
        current_chapter = None
        
        for item in self.toc:
            level, title, page = item
            if level == 1:
                current_chapter = title
                structure[current_chapter] = {"page": page, "sections": {}}
            elif level == 2:
                structure[current_chapter]["sections"][title] = {"page": page, "subsections": {}}
            elif level == 3:
                structure[current_chapter]["sections"][list(structure[current_chapter]["sections"])[-1]]["subsections"][title] = {"page": page}
        
        return structure

    def save_structure(self, structure_filepath):
        json_formatted_structure = json.dumps(
            self.structure,
            indent=4,
            separators=(',', ': '),
            ensure_ascii=False
        )
        with open(structure_filepath, "w+", encoding="utf-8") as f:
            f.write(json_formatted_structure)
        
      
    
if __name__ == "__main__":
    doc = pymupdf.open(os.path.join(Config.DATA_PATH, Config.FILE_NAME))
    pp = PDFParserUniversal(doc=doc)
    extracted_file_name = f'structure_universal_{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")}.json'
    pp.save_structure(os.path.join(Config.EXTRACTED_DATA_PATH, extracted_file_name))