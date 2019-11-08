from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic, Post
from django.http import HttpResponse, Http404
from .forms import NewTopicForm
# Create your views here.
# 处理应用程序request/response

def home(request):
    # return HttpResponse('Hello, World!')
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards}) #context意思
    # boards_names = list()
    # for board in boards:
    #     boards_names.append(board.name)
    # response_html = '<br>'.join(boards_names)
    # return HttpResponse(response_html)
def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'boards/topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: 临时使用一个账号作为登录账户

    if request.method=='POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit = False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by=user
            )
            return redirect('board_topics',pk = board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})
        # subject=request.POST['subject']
        # message = request.POST['message']
        #
        # user = User.objects.first()  # TODO: 临时使用一个账号作为登录账户
        #
        # topic = Topic.objects.create(
        #     subject=subject,
        #     board=board,
        #     starter=user
        # )
        #
        # post = Post.objects.create(
        #     message=message,
        #     topic=topic,
        #     created_by=user
        # )
        # return redirect('board_topics',pk=board.pk)  # TODO:redirect to the created topic page
    # return render(request, 'boards/new_topic.html', {'board': board})
