from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Set up the Generative AI model
genai.configure(api_key="AIzaSyD101zERBMJp-Us2qlNJ2d8RZp8wBvAWME")
model = genai.GenerativeModel("gemini-1.5-flash")


def parse_learning_path(result_text):
    """Parses the AI-generated text into a dictionary."""
    lines = result_text.splitlines()
    modules = {}
    current_module = None

    for line in lines:
        if line.startswith("Module"):
            current_module = line.strip()
            modules[current_module] = []
        elif current_module and line.strip().startswith("1."):
            modules[current_module].append(line.strip()[3:])

    return modules


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_learning_path():
    search_query = request.form.get("search_query")
    ip = f"Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 6 main topics for {search_query}. The 6 main topics should be divided into modules, with the 1st module covering the basics and introduction. The topics should become more advanced as we progress to the next modules. Remember, under each module, you should give me exactly 5 subtopics for that particular module. The response you provide must be structured: first, list all 5 modules, then list all the subtopics. Remember, just give me the names of the topics and subtopics, and don't provide any additional information."

    response = model.generate_content(ip)
    response_text =response.text
    # Initialize the dictionary to store modules and their subtopics
    modules_dict = {}

    # Split the content into modules and subtopics
    modules = response_text.split('**Module')

    for module in modules[1:]:
        # Extract the module name and subtopics
        module_lines = module.strip().split('\n')
        module_name = module_lines[0].strip()  # Get module name (e.g., Module 1: Introduction to Linear Algebra)
        
        # Find the subtopics by extracting lines starting with a number
        subtopics = []
        for line in module_lines[1:]:
            if line.strip().startswith(str(len(subtopics) + 1)):
                subtopics.append(line.strip()[3:])  # Remove the numbering (e.g., "1." becomes "")
        
        # Add module and subtopics to the dictionary
        modules_dict[module_name] = subtopics
    del modules_dict['s:**']  # Removes the key 'b' and its value
    return render_template("result.html", modules=modules_dict)
if __name__ == "__main__":
    app.run(debug=True, port=5001)
