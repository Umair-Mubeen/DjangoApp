from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee


def Index(request):
    try:
        if 'UserName' not in request.session:
            return render(request, 'login.html')
        else:
            return HttpResponseRedirect('Dashboard')
    except Exception as e:
        return HttpResponse(str(e))


def login(request):
    try:
        if request.method == 'POST':
            user = request.POST['user']
            pwd = request.POST['pwd']
            Emp = Employee.objects.filter(Emp_Name=user, Emp_Pwd=pwd).exists()
            if Emp is True:
                if 'UserName' not in request.session:
                    request.session['UserName'] = user
                print("Login SuccessFully !")
                return HttpResponseRedirect('Dashboard')
            else:
                return HttpResponse("Invalid UserName Or Password  !")
        else:
            return HttpResponse('Method shall be POST rather than GET !')
    except Exception as e:
        return HttpResponse(e)


def registration(request):
    try:
        if 'UserName' not in request.session:
            return HttpResponseRedirect('/')

        ID = request.GET.get('Id')
        if ID is None:
            return render(request, 'registration.html',
                          {"EmpID": "", "Emp_Name": "", "Emp_Email": "", "Emp_Age": "", "EmpAddress": "",
                           "EmpDesignation": "", "Type": "", "Emp_PWD": ""})
        else:
            Emp = Employee.objects.get(pk=ID)

            return render(request, 'registration.html', {
                "EmpID": ID,
                "Emp_Name": Emp.Emp_Name,
                "Emp_Email": Emp.Emp_Email,
                "Emp_Age": Emp.Emp_Age,
                "EmpAddress": Emp.EmpAddress,
                "EmpDesignation": Emp.Emp_Designation,
                "Type": "hidden",
                "Emp_PWD": Emp.Emp_Pwd

            })




    except Exception as e:
        return HttpResponse(str(e))


def AddUser(request):
    try:
        if 'UserName' not in request.session:
            return HttpResponseRedirect('/')

        if request.method == 'POST':

            hd_Id = request.POST['hd_Id']
            emp_name = request.POST['emp_name']
            emp_email = request.POST['emp_email']
            emp_age = request.POST['emp_age']
            emp_address = request.POST['emp_address']
            emp_designation = request.POST['emp_designation']
            emp_pwd = request.POST['emp_pwd']
            # Insert the new Record in Db
            if hd_Id == "":
                Emp = Employee()
                Emp.Emp_Name = emp_name
                Emp.Emp_Email = emp_email
                Emp.Emp_Age = emp_age
                Emp.EmpAddress = emp_address
                Emp.Emp_Designation = emp_designation
                Emp.Emp_Pwd = emp_pwd
                Emp.save()
                return HttpResponseRedirect("ManageUsers")

            # update the current object row
            if hd_Id is not None:
                Emp = Employee.objects.get(pk=hd_Id)
                Emp.Emp_Name = emp_name
                Emp.Emp_Email = emp_email
                Emp.Emp_Age = emp_age
                Emp.EmpAddress = emp_address
                Emp.Emp_Designation = emp_designation
                Emp.Emp_Pwd = emp_pwd
                Emp.save()
                return HttpResponseRedirect("ManageUsers")


        else:
            return HttpResponse("Method Shall be Post rather than Get")
    except Exception as e:
        return HttpResponse("Error => " + str(e))


def FetchUser(request):
    try:
        if 'UserName' not in request.session:
            return HttpResponseRedirect('/')

        Emp = Employee.objects.all()
        for res in Emp:
            print(res.Emp_Name)
        return render(request, 'ManageUsers.html', {'EmpList': Emp})

    except Exception as e:
        return HttpResponse(e)


def DeleteUser(request):
    try:
        if 'UserName' not in request.session:
            return HttpResponseRedirect('/')

        ID = request.GET.get('Id')
        Emp = Employee.objects.get(pk=ID)
        Emp.delete()
        return HttpResponseRedirect("ManageUsers")
    except Exception as e:
        return HttpResponse(e)


def Dashboard(request):
    if 'UserName' not in request.session:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'Dashboard.html', {'return_url': request.build_absolute_uri})
    # request.path get url without query parameters
    # request.get_full_[ath with query parameters
    # requet.build_absolute_uri gives you relative url


def AddEditInward(request):
    if 'UserName' not in request.session:
        return HttpResponseRedirect('/')

    return_url = request.GET['return_url']
    return HttpResponse(return_url)


def Logout(request):
    if 'UserName' not in request.session:
        return HttpResponseRedirect('/')

    del request.session['UserName']
    return HttpResponseRedirect('Dashboard')


def IsUserLoggedIn(request):
    if request.session['UserName'] is not None:
        return True
    else:
        return False
