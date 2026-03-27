import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load your resumes
def load_resumes():
    resumes = {}
    resume_files = {
        'revenue_ops': 'revenue-operations.md',
        'manager': 'manager.md',
        'account_manager': 'account-manager.md',
        'sales': 'sales.md'
    }
    
    for key, path in resume_files.items():
        try:
            with open(path, 'r') as f:
                resumes[key] = f.read()
        except FileNotFoundError:
            print(f"Warning: {path} not found")
    
    return resumes

# Main function
def main():
    print("Loading resumes...")
    resumes = load_resumes()
    print(f"Loaded {len(resumes)} resume versions")
    print("Job search automation is ready!")

if __name__ == "__main__":
    main()
