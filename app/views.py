
from multiprocessing import context
from re import template
from django.contrib import admin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
# Create your views here.

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]
job_description = [
    "First Job Description",
    "Second Job Description",
   " Third Job Description", 
]
#def hello(request):
    #return HttpResponse("Hello World")
def hello(request):
    template=loader.get_template('app/hello.html')
    context={"name" : "django"}
    return HttpResponse(template.render(context, request))

def job_list(request):
    list_of_jobs = "<ul>"
    for j in job_title:
        job_id = job_title.index(j)
        detail_url = reverse('jobs_detail' , args=(job_id ,))
        list_of_jobs += f"<li> <a href='job/{job_id}' > {j} </a> </li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)

def job_detail(request, id):
    try:
        
        if id == 0:
            return redirect(reverse('jobs_home'))
        return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        return  HttpResponse(return_html)
    except:
        return HttpResponseNotFound('NOT FOUND')
    