from flask import Flask, render_template, request
import google.generativeai as genai
modules_dict = {}
app = Flask(__name__)

# Set up the Generative AI model
genai.configure(api_key="AIzaSyD101zERBMJp-Us2qlNJ2d8RZp8wBvAWME")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_learning_path():
    global modules_dict
    search_query = request.form.get("search_query")
    ip = f"Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 6 main topics for {search_query}. The 6 main topics should be divided into modules, with the 1st module covering the basics and introduction. The topics should become more advanced as we progress to the next modules. Remember, under each module, you should give me exactly 5 subtopics for that particular module. The response you provide must be structured: first, list all 5 modules, then list all the subtopics. Remember, just give me the names of the topics and subtopics, and don't provide any additional information."

    response = model.generate_content(ip)
    response_text =response.text
    # Initialize the dictionary to store modules and their subtopics
    

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
    return render_template("results2.html", modules=modules_dict)
@app.route("/1")
def module_1():
    
    txt=[]
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[0]][0]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[0]][1]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[0]][2]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[0]][3]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[0]][4]).text)    


    return render_template("module1.html", modules=modules_dict[list(modules_dict.keys())[0]],text=txt)
print(modules_dict)
@app.route("/2")
def module_2():
    
    txt=[]
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[1]][0]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[1]][1]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[1]][2]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[1]][3]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[1]][4]).text)    


    return render_template("module2.html", modules=modules_dict[list(modules_dict.keys())[1]],text=txt)
@app.route("/3")
def module_3():
    
    txt=[]
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[2]][0]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[2]][1]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[2]][2]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[2]][3]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[2]][4]).text)    


    return render_template("module3.html", modules=modules_dict[list(modules_dict.keys())[2]],text=txt)
@app.route("/4")
def module_4():
    
    txt=[]
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[3]][0]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[3]][1]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[3]][2]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[3]][3]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[3]][4]).text)    


    return render_template("module4.html", modules=modules_dict[list(modules_dict.keys())[3]],text=txt)
@app.route("/5")
def module_5():
    
    txt=[]
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[4]][0]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[4]][1]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[4]][2]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[4]][3]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[4]][4]).text)    


    return render_template("module5.html", modules=modules_dict[list(modules_dict.keys())[4]],text=txt)
@app.route("/6")
def module_6():
    
    txt=[]
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[5]][0]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[5]][1]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[5]][2]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[5]][3]).text)
    txt.append(model.generate_content("Remember, tell me exactly what I ask. Don't give me any additional information. Give me exactly 300 words detailed paragraph  about "+modules_dict[list(modules_dict.keys())[5]][4]).text)    


    return render_template("module6.html", modules=modules_dict[list(modules_dict.keys())[5]],text=txt)
if __name__ == "__main__":
    app.run(debug=True, port=5001)
