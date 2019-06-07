from django.http import HttpResponse
from django.shortcuts import render
from secrets import randbelow

def count(request):
    return render(request, 'coutwords.html')

def cresultrs(request):
    content = request.GET['content']
    content_words = content.split()
    content_words_count = {}

    for word in content_words:
        if word in content_words_count:
            content_words_count[word] += 1
        else:
            content_words_count[word] = 1


    count_of_words = content_words_count.items()


    return render(request, 'counted_word_results.html', {'content':content,'count_of_words':count_of_words})
