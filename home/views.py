from django.shortcuts import render,HttpResponse
import os
from home import config
import openai
import json
import requests
from ipware import get_client_ip



# Create your views here.
inp = ''
chatStr = ""
c = {}
path_of_image = ""
client_ip, is_routable = "",""
# lang_select = {}

def chat(query):

    global chatStr
    print(chatStr)
    openai.api_key = config.apikey
    chatStr += f"User: {query}\n Chanakya:"

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt= chatStr,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    print(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"


    return response["choices"][0]["text"]

def db(request):
    return render(request,"db.html")

def index(request):
    global c
    global inp
    global lang_select
    global obj


    if request.method == 'POST':
        inp = request.POST.get('texta').lower()
        value = requests.get("http://127.0.0.1:8000/db")
        c = {"c1":chat(query=inp),"c2":inp,"c3":[],"c4":value.text}
        # print(c["c4"])
        
        if "who is your owner".lower() in inp:
            c = {"c1":chat(query=inp)+" and Nabeel Ali Khan is the head of the project."}

        elif "nabeel ali khan".lower() in inp:
            c = {"c1":chat(query=inp)+" and also Nabeel Ali Khan is the head of the project team"}
            
        with open("templates/db.html","a+")as f:
            f.write(f"User: {inp}")
            f.write("<br>")
            f.write(f"Chanakya: {c['c1']} ")
            f.write("<br><br> ")
            c["c3"].append(f.read())
            print(f.read())
    
        # value = requests.get("http://127.0.0.1:8000/db")
        # print(value.text)


    return render(request,"index.html",c)


def about(request):
    return render(request,"about.html")



def some_func(request):
    if request.method == 'GET':
        param1 = request.GET.get('param_first')
        param2 = request.GET.get('param_second')
        print(param1, param2)


        response_data = 'successful!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def snap(request):
    # print(request.method) #GET
    photo = request.GET.get("photo")
    print(photo)
    return render(request,"snap.html")



def tracker(reqeust):
    client_ip, is_routable = get_client_ip(reqeust)
    ip_address = client_ip
    apiKey = "6691a38b67f74a94a6423ee3fc4fb49d"

    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={apiKey}&ip={ip_address}"

    # print(url)
    value = requests.get(url)
    value = value.text.strip(",").split(",")
    
    values = [f"IP:{client_ip}",f"Routable:{is_routable}",value[2],value[5],value[7],value[9],value[10],value[11],value[12],value[13],value[45],value[47]]
    values = "\n".join(values)
    print(values)

    with open("ip.txt","a+")as ips:
        ips.write("**********\n"+values+"\n**********\n\n")

    return HttpResponse(values)

    # print(value[2])
    # print(value[5])
    # print(value[7])
    # print(value[9])
    # print(value[10])
    # print(value[11])
    # print(value[12])
    # print(value[13])
    # print(value[45])
    # print(value[47])


def test(request):
 
    return render(request,"test.html")