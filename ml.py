import PyPDF2
import spacy

# Open the PDF file
pdf_file = open('wildlife_conservation.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Extract text from each page
text = ''
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text += page.extractText()

# Close the PDF file
pdf_file.close()

# Load the English language model in spaCy
nlp = spacy.load('en_core_web_sm')

# Process the text with spaCy
doc = nlp(text)

# Define a function to answer questions
def answer_question(question):
    # Process the question with spaCy
    question_doc = nlp(question)
    
    # Find the most similar sentence in the document
    max_similarity = 0
    best_sentence = None
    for sentence in doc.sents:
        similarity = question_doc.similarity(sentence)
        if similarity > max_similarity:
            max_similarity = similarity
            best_sentence = sentence
    
    # Extract the answer from the sentence
    answer = best_sentence.text
    
    return answer

# Test the question-answering model
question = "What is the definition of conservation?"
answer = answer_question(question)
print(answer)