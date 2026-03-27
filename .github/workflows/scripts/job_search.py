import os
from openai import OpenAI
import PyPDF2

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load your resumes from PDF files
def load_resumes():
    resumes = {}
    resume_files = {
        'revenue_ops': 'Lisa Janasik - Resume - Revenue Operations.pdf',
        'manager': 'Lisa Janasik - Resume - Manager.pdf',
        'account_manager': 'Lisa Janasik - Resume - Account Manager.pdf',
        'sales': 'Lisa Janasik - Resume - Sales.pdf'
    }
    
    for key, path in resume_files.items():
        try:
            with open(path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                resumes[key] = text
                print(f"Loaded {key} resume ({len(text)} characters)")
        except FileNotFoundError:
            print(f"Error: {path} not found")
        except Exception as e:
            print(f"Error reading {path}: {e}")
    
    return resumes

# Main function
def main():
    print("Loading resumes...")
    resumes = load_resumes()
    print(f"Successfully loaded {len(resumes)} resume versions")
    
    if len(resumes) == 0:
        print("ERROR: No resumes loaded!")
        return
    
    print("Job search automation is ready!")

if __name__ == "__main__":
    main()
