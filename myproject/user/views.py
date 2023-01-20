from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:homepage")
    form = NewUserForm()
    return render(
        request=request, template_name="user/register.html", context={"form": form}
    )
