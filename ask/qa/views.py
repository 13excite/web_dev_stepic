from django.shortcuts import render
from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')
def question_ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            ask = form.save()
            url = reverse('question_detail', args=[ask.id])
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, 'ask.html', {
        'form': form
    })
