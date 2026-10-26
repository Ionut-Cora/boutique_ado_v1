from django.shortcuts import render
from .models import UserProfile


def profile(request):
    """Display the user's profile."""
    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
