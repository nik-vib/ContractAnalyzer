import spacy
from nltk.sem import logic
from nltk.tokenize import sent_tokenize
from difflib import SequenceMatcher

# Sample contract text
contract_text = """
This Agreement is made between Company XYZ and Company ABC for the sale and purchase of goods. 
Company XYZ agrees to deliver the goods within 10 business days. 
Company ABC agrees to pay the invoice within 30 days of receiving the goods.
"""

# Load English tokenizer, tagger, parser, and NER
nlp = spacy.load("en_core_web_sm")

# Preprocess contract text to extract meaningful clauses
def preprocess_contract(text):
    doc = nlp(text)
    clauses = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
    return clauses

# Unification function
def unify(query, clause):
    try:
        # Perform unification
        unification = logic.Expression.fromstring(query).unify(logic.Expression.fromstring(clause))
        return unification
    except Exception as e:
        return None

# Resolution function
def resolve(query, contract_clauses):
    try:
        query_tokens = query.lower().split()
        
        for clause in contract_clauses:
            clause_tokens = clause.lower().split()
            if all(token in clause_tokens for token in query_tokens):
                print(f"Match found for query '{query}':")
                print(f"Matched clause: {clause}")
                return
        
        print(f"No match found for query '{query}'")
    except Exception as e:
        print("Error occurred while resolving the query:", e)

# Main function
def main():
    print("Welcome to the Contract Analysis Assistant!")
    # Preprocess contract text
    contract_clauses = preprocess_contract(contract_text)
    
    while True:
        print("\nAvailable commands:")
        print("1. Analyze clause")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            query = input("Enter the clause to analyze: ")
            resolve(query, contract_clauses)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
