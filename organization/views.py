from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Organization, CustomUser, Role # type: ignore
from .forms import OrganizationForm, UserForm
from django.shortcuts import render

@login_required
def organization_list(request):
    if not request.user.is_superuser:
        return redirect('user_list')
    organizations = Organization.objects.all()
    return render(request, 'organization/organization_list.html', {'organizations': organizations})

@login_required
def organization_create(request):
    if not request.user.is_superuser:
        return redirect('user_list')
    form = OrganizationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('organization_list')
    return render(request, 'organization/organization_form.html', {'form': form})

@login_required
def user_list(request):
    users = CustomUser.objects.filter(organization=request.user.organization)
    return render(request, 'organization/user_list.html', {'users': users})

@login_required
def user_create(request):
    if request.user.role.name != 'Admin':
        return redirect('user_list')
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'organization/user_form.html', {'form': form})

# @login_required
# def assign_role(request, user_id):
#     user = get_object_or_404(CustomUser, id=user_id)
#     if request.user.role.name != 'Admin' or user.organization != request.user.organization:
#         return redirect('user_list')
#     if request.method == 'POST':
#         role_id = request.POST.get('role')
#         role = get_object_or_404(Role, id=role_id)
#         user.role = role
#         user.save()
#         return redirect('user_list')
#     roles = Role.objects.all()
#     return render(request, 'organization/assign_role.html', {'user': user, 'roles': roles})

@login_required
def assign_role(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    # SAFELY check role and organization match
   # if not request.user.role or request.user.role.name != 'Admin' or user.organization != request.user.organization:
   #     return redirect('user_list')

    if request.method == 'POST':
        role_id = request.POST.get('role')
        role = get_object_or_404(Role, id=role_id)
        user.role = role
        user.save()
        return redirect('user_list')

    roles = Role.objects.all()
    return render(request, 'organization/assign_role.html', {'user': user, 'roles': roles})



@login_required
def dashboard(request):
 #   return render(request, 'users/dashboard.html')
     return render(request, 'organization/dashboard.html')
      










# views.py 
# def home(request):
#    # return render(request, 'home.html')  # Ensure this template exists
#      return render(request, 'multi_org_management/home.html')
 