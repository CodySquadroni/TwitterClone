from django.shortcuts import render, redirect
from .models import Profile
from .forms import AccountCreationForm
from django.contrib import messages


# Create your views here.


def account_creation(request):
    if request.method == "POST":
        form = AccountCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, fr'Welcome to the party {username}! You successfully created your account!')
            return redirect('login')

    else:
        form = AccountCreationForm

    return render(request, 'users/register.html', {'form': form})


def profiles_list(request):
    # my_profile = Profile.objects.get(id=profile_id)
    profiles = Profile.objects.exclude(user=request.user)

    # return render(request, 'users/profile.html')
    return render(request, 'users/profiles_list.html', {'profiles': profiles})


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)

        # Post FOrm Logic
        if request.method == 'POST':
            # Get current user
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST["follow"]
            # Decide to follow or unfollow
            if action == "unfollow":
                print("TEST")
                print(current_user_profile)
                current_user_profile.follows.remove(profile.user)

            elif action == "follow":
                print("TEST")
                print(current_user_profile)
                current_user_profile.follows.add(profile.user)

        return render(request, 'users/profile.html', {'profile': profile})

    else:
        messages.success(request, ('You must be logged in'))
        return redirect('tweets/index.html')
