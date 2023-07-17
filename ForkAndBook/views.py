from django.shortcuts import render, redirect
from ForkAndBook.models import Student, Menu, Employee, FoodBook
from django.contrib import messages
# Create your views here.

def loginpage(request):
    if request.method == 'POST':
        sID = request.POST['StudID']
        spass = request.POST['StudPass']

        student = None

        if sID and spass:
            try:
                student = Student.objects.get(StudID=sID, StudPass=spass)
            except Student.DoesNotExist:
                return render(request, "loginpage.html")

        if sID and spass == spass:
            request.session['StudID'] = student.StudID
            return redirect('homeStudent')

    # Check if there is a success message from deleteStudent view
    success_messages1 = messages.get_messages(request)
    dict = {
        'message': success_messages1,
    }
    return render(request, "loginpage.html", dict)

def loginpage2(request):
    if request.method == 'POST':
        eID = request.POST['EmployeeID']
        epass = request.POST['EmployeePass']

        student = None

        if eID and epass:
            try:
                employee = Employee.objects.get(EmployeeID=eID, EmployeePass=epass)
            except Student.DoesNotExist:
                return render(request, "loginpage2.html")

        if eID and epass == epass:
            request.session['EmployeeID'] = employee.EmployeeID
            return redirect('homeEmployee')

    # Check if there is a success message from deleteEmployee view
    success_messages2 = messages.get_messages(request)
    dict = {
        'message': success_messages2,
    }
    return render(request, "loginpage2.html", dict)


def registerpage(request):
    if request.method =='POST':
        sID=request.POST['StudID']
        sname=request.POST['StudName']
        sphone=request.POST['StudPhone']
        spass=request.POST['StudPass']
        if Student.objects.filter(StudID = sID).exists() == True:
            dict = {
                'message':'Account with student ID {0} already exists'.format(sID),
                'all':all,
            }
            return render(request, 'registerpage.html', dict)
        else:
            data=Student(StudID=sID, StudName=sname, StudPhone=sphone, StudPass=spass)
            data.save()
            dict={
                'message' : 'New  Student has been saved'
            }

        return render(request,"registerpage.html",dict)
    else:
        return render(request,"registerpage.html")
    
def registerpage2(request):
    if request.method =='POST':
        eID=request.POST['EmployeeID']
        ename=request.POST['EmployeeName']
        ephone=request.POST['EmployeePhone']
        epass=request.POST['EmployeePass']
        if Employee.objects.filter(EmployeeID = eID).exists() == True:
            dict = {
                'message':'Account with employee ID {0} already exists'.format(eID),
                'all':all,
            }
            return render(request, 'registerpage2.html', dict)
        else:
            data=Employee(EmployeeID=eID, EmployeeName=ename, EmployeePhone=ephone, EmployeePass=epass)
            data.save()
            dict={
                'message' : 'New  Employee has been saved'
            }

        return render(request,"registerpage2.html",dict)
    else:
        return render(request,"registerpage2.html")


def homeStudent(request):
    sID = request.session.get('StudID')
    student = Student.objects.get(StudID=sID)
    foodbook_entries = FoodBook.objects.filter(StudID=student)

    dict = {
        'student': student,
        'foodbook_entries': foodbook_entries,
    }
    return render(request, "homeStudent.html", dict)




def homeEmployee(request):
    eID = request.session.get('EmployeeID')
    employee = Employee.objects.get(EmployeeID=eID)
    assigned_menus = Menu.objects.filter(EmployeeID=employee)
    
    student_foodbooks = FoodBook.objects.filter(MenuID__in=assigned_menus)
    
    dict = {
        'employee': employee,
        'assigned_menus': assigned_menus,
        'student_foodbooks': student_foodbooks,
    }
    return render(request, "homeEmployee.html", dict)




def studentUpdate(request):
    if request.method == 'POST':
        # Get the current student object
        sID = request.session.get('StudID')
        student = Student.objects.get(StudID=sID)

        # Update the student data based on the form inputs
        student.StudName = request.POST['StudName']
        student.StudPhone = request.POST['StudPhone']
        student.save()

        # Redirect to the homeStudent page or display a success message
        return redirect('homeStudent')
    else:
        # Render the studentUpdate template for GET requests
        sID = request.session.get('StudID')
        student = Student.objects.get(StudID=sID)
        dict = {
            'student': student,
        }
        return render(request, "studentUpdate.html", dict)
    
def employeeUpdate(request):
    if request.method == 'POST':
        # Get the current employee object
        eID = request.session.get('EmployeeID')
        employee = Employee.objects.get(EmployeeID=eID)

        # Update the employee data based on the form inputs
        employee.EmployeeName = request.POST['EmployeeName']
        employee.EmployeePhone = request.POST['EmployeePhone']
        employee.save()

        # Redirect to the homeEmployee page or display a success message
        return redirect('homeEmployee')
    else:
        # Render the employeeUpdate template for GET requests
        eID = request.session.get('EmployeeID')
        employee = Employee.objects.get(EmployeeID=eID)
        dict = {
            'employee': employee,
        }
        return render(request, "employeeUpdate.html", dict)
    

def studentDelete(request):
    # Get the current student object
    sID = request.session.get('StudID')
    student = Student.objects.get(StudID=sID)

    if request.method == 'POST':
        # Delete the student data from the database
        student.delete()

        # Clear the session and redirect to the login page
        request.session.clear()
        messages.success(request, 'Student data deleted successfully.')
        return redirect('loginpage')

    dict = {
        'student': student,
    }
    return render(request, 'studentDelete.html', dict)

def employeeDelete(request):
    # Get the current employee object
    eID = request.session.get('EmployeeID')
    employee = Employee.objects.get(EmployeeID=eID)

    if request.method == 'POST':
        # Delete the employee data from the database
        employee.delete()

        # Clear the session and redirect to the login page
        request.session.clear()
        messages.success(request, 'Employee data deleted successfully.')
        return redirect('loginpage2')

    dict = {
        'employee': employee,
    }
    return render(request, 'employeeDelete.html', dict)

def choosepage(request):
    return render(request, 'choosepage.html')


def BigCubeMenu(request):
    menus = Menu.objects.all()[:4]  # Limit the query to retrieve only four menu items
    dict = {
        'menu': menus,
    }
    return render(request, 'BigCubeMenu.html', dict)

def KhemahBiruMenu(request):
    all_menus = Menu.objects.all()  # Retrieve all menu items
    remaining_menus = all_menus[4:]  # Exclude the first four items
    
    dict = {
        'menu': remaining_menus,
    }
    return render(request, 'KhemahBiruMenu.html', dict)

def registerMenu(request):
    eID = request.session.get('EmployeeID')
    employee = Employee.objects.get(EmployeeID=eID)

    if request.method == 'POST':
        mID = request.POST['MenuID']
        mname = request.POST['MenuName']
        mprice = request.POST['MenuPrice']

        if Menu.objects.filter(MenuID=mID).exists():
            dict = {
                'message': 'Menu with Menu ID {0} already exists'.format(mID),
                'all': all,
                'employee': employee,
            }
            return render(request, 'homeEmployee.html', dict)
        else:
            data = Menu(MenuID=mID, MenuName=mname, MenuPrice=mprice, EmployeeID=employee)
            data.save()
            
            # Set the MenuID in the session
            request.session['MenuID'] = mID

            # Redirect to the BigCubeMenu page
            return redirect('homeEmployee')

    return render(request, "registerMenu.html", {'employee': employee})

def addFood(request, menu_id):
    sID = request.session.get('StudID')
    eID = request.session.get('EmployeeID')
    student = Student.objects.get(StudID=sID)
    menu = Menu.objects.get(MenuID=menu_id)
    employee = Employee.objects.get(EmployeeID=eID)

    # Check if the menu item already exists in the student's FoodBook
    foodbook_entry = FoodBook.objects.filter(StudID=student, MenuID=menu, EmployeeID=employee).first()
    if foodbook_entry:
        # If the item exists, update the quantity by incrementing it
        foodbook_entry.Quant += 1
        foodbook_entry.save()
    else:
        # If the item doesn't exist, create a new entry with quantity 1
        foodbook_entry = FoodBook(StudID=student, MenuID=menu, EmployeeID=employee, Quant=1)
        foodbook_entry.save()

    return redirect('homeStudent')


def deleteFood(request, food_id):
    foodbook_entry = FoodBook.objects.get(id=food_id)
    foodbook_entry.delete()
    return redirect('homeStudent')


def deleteMenu(request, menu_id):
    if request.method == 'POST':
        menu = Menu.objects.get(MenuID=menu_id)
        menu.delete()
        return redirect('BigCubeMenu')
    else:
        return redirect('homeEmployee')


def approveFood(request, food_id):
    foodbook_entry = FoodBook.objects.get(id=food_id)
    foodbook_entry.Status = 'Approved'
    foodbook_entry.save()
    return redirect('homeEmployee')

def rejectFood(request, food_id):
    foodbook_entry = FoodBook.objects.get(id=food_id)
    student_id = foodbook_entry.StudID_id
    foodbook_entry.delete()

    # Update the corresponding student's FoodBook entry to display 'Rejected'
    student = Student.objects.get(StudID=student_id)
    rejected_foodbook_entry = FoodBook.objects.filter(StudID=student, MenuID=foodbook_entry.MenuID).first()
    if rejected_foodbook_entry:
        rejected_foodbook_entry.Status = 'Rejected'
        rejected_foodbook_entry.save()

    return redirect('homeEmployee')