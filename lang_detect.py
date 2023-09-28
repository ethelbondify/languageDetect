import re
from langdetect import detect
from bs4 import BeautifulSoup
from itertools import count

# Aspose conversion to html
# import aspose.words as aw

# First document tested 
doc = aw.Document("Vonovia_Draw_Down_2020_Final_Terms-1-8.pdf")    # please edit this place
doc.save("aspose_output1.html")
# url1 = "aspose_output1.html"    # url here indicates the path to the file local storage
url2 = "Vonovia_Draw_Down_2020_Final_Terms-pages-1-8.html"
# url3 = "Sample_multiligual_text.html"
page = open(url2)       # replace url with the path to the local storage of the HTML file

#  Another document to test 
# doc = aw.Document("Sample_multiligual_text.pdf")
# doc.save("aspose_output2.html")
# url = "aspose_output2.html"
# page = open(url)


# HTML document containing multilingual text
# html_doc = '''
# <html>
# <body>
#     <p>Hello, this is English text.</p>
#     <p>Hola, este es un texto en Español.</p>
#     <p>Bonjour, ceci est un texte en Français.</p>
#     <p>Привет, это текст на русском языке.</p>
#     <p>こんにちは、これは日本語のテキストです。</p>
#     <p>你好，这是中文文本。</p>
# </body>
# </html>
# '''

# Function to generate a unique ID for each detected language
def generate_id():
    for i in count():
        yield f"lang-{i}"

# Detect languages and add inline CSS styles
def highlight_languages(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser') # html doc is read hear
    language_id_generator = generate_id()

    for tag in soup.find_all('p'):
        text = tag.text.strip()
        if text:
            lang = detect(text)
            ############# optional ################################
            lang_label = f"({get_language_name(lang)})"
            span_tag = BeautifulSoup(f"<span style='background-color: {get_language_color(lang)}'>{text}</span>", 'html.parser')
            label_tag = BeautifulSoup(f"<label>{lang_label}</label>", 'html.parser')
            tag.replace_with(label_tag, span_tag)

            # tag.replace_with(f"<span style='background-color: {get_language_color(lang)}'>{text}</span>")

    return soup

# Assign different colors for different languages
def get_language_color(lang):
    color_mapping = {
        'en': 'yellow',  # English
        'es': 'lightblue',  # Spanish
        'fr': 'lightgreen',  # French
        'de': 'bisque',  # German
        'it': 'chocolate',  # Italian
        'ru': 'pink',  # Russian
        'ja': 'lightgrey',  # Japanese
        'zh-cn': 'lightcoral',  # Simplified Chinese
        'nl': 'orange',  # Dutch
        'ar': 'red',  # Arabic
        # Add more language-color mappings as needed...
    }
    return color_mapping.get(lang, 'white')  # Default color for unknown languages

# Assign different colors for different languages
def get_language_name(lang):
    language_names = {
        'en': 'English',  # English
        'es': 'Español',  # Spanish
        'fr': 'Français',  # French
        'de': 'German',  # German
        'it': 'Italian',  # Italian
        'ru': 'Rusian',  # Russian
        'ja': 'Japanese',  # Japanese
        'zh-cn': 'Chinese',  # Simplified Chinese
        'nl': 'Dutch',  # Dutch
        'ar': 'Arabic',  # Arabic
        # Add more language-name mappings as needed...
    }
    return language_names.get(lang, 'Unknown')  # Default name for unknown languages

# Apply the highlighting and print the modified HTML
highlighted_html = highlight_languages(page.read())
#set encoding to UTF-8
with open('test_lang2.html', 'w', encoding = 'utf-8') as file:
    file.write(str(highlighted_html.prettify()))
