from django.shortcuts import render, redirect
from .models import Food, Consume
from user.models import UserData
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    user = request.user
    if request.method == 'POST':
        user_consumed_food = request.POST.get('food_consumed')
        consumed_food_obj = Food.objects.get(name=user_consumed_food)
        consume = Consume(food_consumed=consumed_food_obj, user=user)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    user = UserData.objects.get(user=user)
    goal = user.calories_goal

    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food, 'goal': goal})

@login_required
def delete(request, id):
    consume = Consume.objects.get(id=id)
    if request.method == 'POST':
        return redirect('/')

    consume.delete()
    return redirect('/')
