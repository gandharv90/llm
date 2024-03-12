import google.generativeai as genai
import os
api_key = 'AIzaSyDQYqDjg5UlmFqHSVXBNp-4grgy-LdqGsg'
genai.configure(api_key=os.environ[api_key])

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Please summarise this document: ...')

print(response.text)
