from django.shortcuts import render
from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import UserData


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, you are logged in')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def set_goal(request):
    if request.method == 'POST':
        user_goal = request.POST.get('set-goal')
        user = request.user
        set_user_goal = UserData.objects.get(user=user)
        set_user_goal.calories_goal = int(user_goal)
        set_user_goal.save()
        return redirect('home')

    return render(request, 'user/set-goal.html')


