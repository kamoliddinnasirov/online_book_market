from django.shortcuts import render





def index(request):
    text_head = 'Bu bosh sahifa'
    text_body = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
    context = {"text_head": text_head, "text_body": text_body}
    return render(request, 'index.html', context)

