from django.shortcuts import render
from users.models import Users
from django.http import HttpResponse

import os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")


# Create your views here.
def signup(request):
    return render(request,'signup.html')

def insert(request):
    if request.method=='POST':
       firstname=request.POST.get('firstname')
       lastname=request.POST.get('lastname')
       email=request.POST.get('email')
       password=request.POST.get('password')
       country=request.POST.get('country')
       Users.objects.create(firstname=firstname,lastname=lastname,email=email,password=password,country=country)
       return render(request,'login.html')
    else:
        return render(request,'signup.html')
    
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if Users.objects.filter(email=email,password=password).exists():
            return render(request,'dashboard.html')
        else:
            return HttpResponse('<center><h1> Login Failed!</h1></center>')
    else:
        return render(request,'login.html')
    
def home(request):
    return render(request,'home.html')
def logout(request):
    return render(request,'login.html')


@csrf_exempt
def devgpt_view(request):
    code_output = ""
    if request.method == "POST":
        prompt = request.POST.get("prompt", "").strip()
        if prompt:
            full_prompt = f"# Task: {prompt}\n# Generate full project with files.\n\n"
            inputs = tokenizer(full_prompt, return_tensors="pt")
            outputs = model.generate(**inputs, max_new_tokens=1024, do_sample=True, temperature=0.7)
            generated = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Parse files from output
            files = parse_files_from_output(generated)

            # Write files to output directory
            base_dir = "generated_project"
            os.makedirs(base_dir, exist_ok=True)
            for filename, content in files.items():
                filepath = os.path.join(base_dir, filename)
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                with open(filepath, "w") as f:
                    f.write(content)

            code_output = "\n".join(f"Generated: {filename}" for filename in files)

    return render(request, "devgpt.html", {"code_output": code_output})

def parse_files_from_output(output):
    """
    Parse model output like:
    # file: index.html
    ...
    # file: style.css
    ...
    Into a dictionary of {filename: content}
    """
    import re
    files = {}
    parts = re.split(r"# file: (.+)", output)
    for i in range(1, len(parts), 2):
        filename = parts[i].strip()
        content = parts[i + 1].strip()
        files[filename] = content
    return files


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model once (you may move this to init if needed)
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")

@csrf_exempt
def message(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        if not prompt:
            return JsonResponse({"error": "Prompt is required"}, status=400)

        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=200)
        code = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return JsonResponse({"code": code})

    return render(request, "home.html")