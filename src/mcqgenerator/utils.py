import os
import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
            
        except Exception as e:
            raise Exception("error reading the PDF file")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "unsupported file format only pdf and text file suppoted"
            )

import json

def get_table_data(quiz_str):
    try:
        if not quiz_str:
            raise ValueError("Empty quiz string received.")
        quiz_dict = json.loads(quiz_str)  # Keep this
        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value.get("mcq", "")
            options = value.get("options", {})
            quiz_table_data.append({
                "MCQ": mcq,
                "Option_A": options.get("a", ""),
                "Option_B": options.get("b", ""),
                "Option_C": options.get("c", ""),
                "Option_D": options.get("d", ""),
                "Correct": value.get("correct", "")
            })

        return quiz_table_data
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return None



