
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
def count(request):
    data=request.GET['fulltextarea']
    lst=data.split()
    length=len(lst)
    worddictionary={}
    for words in lst:
        if words in worddictionary:
            worddictionary[words] +=1
        else:
            worddictionary[words]=1
    sorted_list= sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'word':data,'len':length,'text':sorted_list})

