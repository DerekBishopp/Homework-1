__author__ = 'Derek'
a = ''
l = ''
b = ''
i = ''
f = ''
c = ''
z = ''
def menu():
    global choice
    print('1. Input employee first name.')
    print('2. Input employee last name.')
    print('3. Input employee DOB')
    print('4. Input employee SS#')
    print('5. Input street address.')
    print('6. Input employee city.')
    print('7. Input employee zip.')
    print('8. Print out employee information.')
    print('9. Quit')
    choice = input('Choice: ')
    return choice


def formatname(s):
    return s .title()

def firstname():
    global a
    n = input(str('First Name: '))
    a = ''+n.strip().title()


def lastname():
    global l
    n = input(str('Last Name: '))
    l = ''+n.strip().title()


def DOB():
    global b
    m = input('Month: ').strip()
    d = input('Day: ').strip()
    y = input('Year: ').strip()
    if int(m)<12 and int(m)>1 and int(d)>1 and int(d)<31 and int(y)>1900 and int(y)<2014:
        b =''+ m+'/'+d+'/'+y
    else:
        return print('YOU DON GOOFED')+DOB()

def SS():
    global i
    q = input('First Three Digits: ').strip()
    s = input('Next Two Digits: ').strip()
    t = input('Last Four Digits: ').strip()
    i = q + '-' + s + '-' + t


def street():
    global f
    n = input('Street Number: ').strip()
    s = input('Street Name: ').strip().title()
    f =n + ' ' + s


def city():
    global c
    c = ''+input('City: ').strip().title()


def zipcode():
    global z
    z = ''+input('Zip: ').strip()


def printinfo():
    print('First name: '+a)
    print('Last name: '+l)
    print('DOB: '+b)
    print('SS# '+i)
    print('Address: '+f)
    print('City: '+c)
    print('Zipcode: '+z)

def main():
    menu()
    while choice != '9' :
        if choice == '1':
            firstname()
            menu()
        elif choice == '2':
            lastname()
            menu()
        elif choice == '3':
            DOB()
            menu()
        elif choice == '4':
            SS()
            menu()
        elif choice == '5':
            street()
            menu()
        elif choice == '6':
            city()
            menu()
        elif choice == '7':
            zipcode()
            menu()
        else:
            printinfo()
            menu()
main()
