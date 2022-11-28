#include <iostream>
#include <fstream>
#include <string.h>
#include <conio.h>
using namespace std;
class pass
{
public:
    char p[20];
    void password(int x)
    {
        if (x == 1234)
        {
            cout << "\nEnter password(less than 10 characters)";
            cin.ignore();
            cin.getline(p, 20);
            fstream wr;
            wr.open("pass.txt", ios::out);
            wr.write((char *)this, sizeof(pass));
            wr.close();
        }
        else
        {
            cout << "\nCode Error";
        }
    }
};
pass obj1;
class hotel
{
public:
    int room_no;
    char date[15];
    char date1[15];
    char name[30];
    char mob[15];
    char adr[15];
    char adress[50];

    void accept()
    {
        cin.ignore();
        cout << "\nEnter date ";
        cin.getline(date, 15);
        cout << "\nEnter full name ";
        cin.getline(name, 30);
        cout << "\nEnter mobile number ";
        cin >> mob;
        cin.ignore();
        cout << "\nEnter adhar card number ";
        cin.getline(adr, 15);
        cout << "\nEnter address ";
        cin.getline(adress, 50);
    }
    void display()
    {
        cout << "\nRoom number       " << room_no;
        cout << "\nName              " << name;
        cout << "\nMobile number     " << mob;
        cout << "\nAdhar card number " << adr;
        cout << "\nAddress           " << adress;
        cout << "\n----------------------------";
    }
};
hotel obj;
int check(int r)
{
    int flag = 1;
    fstream rd;
    rd.open("record.txt", ios::in);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(obj);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&obj, sizeof(obj));
        if (r == obj.room_no)
        {
            flag = 0;
            break;
        }
    }
    return flag;
}
void alotroom()
{
    int r, c;
    cout << "\nEnter room number ";
    cin >> r;
    c = check(r);
    if (c == 0)
    {
        cout << "\nROOM ALREADY BOOKED";
    }
    else
    {
        obj.room_no = r;
        obj.accept();
        fstream wr;
        wr.open("record.txt", ios::app);
        wr.write((char *)&obj, sizeof(obj));
    }
}
void roomstatus()
{
    char p1[20];
    fstream rdp;
    rdp.open("pass.txt", ios::in);
    rdp.read((char *)&obj1, sizeof(pass));
    cout << "\nEnter password ";
    for (int i = 0; i < strlen(obj1.p); i++)
    {
        p1[i] = getch();
        cout << "*";
    }
    p1[strlen(obj1.p)] = '\0';
    if (stricmp(p1, obj1.p) == 0)
    {
        fstream rd;
        rd.open("record.txt", ios::in);
        rd.seekg(0, ios::end);
        int n = rd.tellg();
        n = n / sizeof(obj);
        rd.seekg(0, ios::beg);
        for (int i = 1; i <= n; i++)
        {
            rd.read((char *)&obj, sizeof(obj));
            obj.display();
        }
    }
    else
    {
        cout << "\nPassword Mismatch";
    }
}
void rstatus()
{
    fstream rd;
    rd.open("record.txt", ios::in);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(obj);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&obj, sizeof(obj));
        cout << "\nRoom number       " << obj.room_no;
        cout << "\nName              " << obj.name;
        cout << "\nMobile number     " << obj.mob;
        cout << "\n----------------------------";
    }
}
void edit()
{
    int rno;
    cout << "\nEnter room number";
    cin >> rno;
    fstream wr, rd;
    rd.open("record.txt", ios::in);
    wr.open("tmp.txt", ios::out);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(obj);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&obj, sizeof(obj));
        if (obj.room_no == rno)
        {
            cout << "\nEnter new room number ";
            cin >> rno;
            obj.room_no = rno;
            obj.accept();
            wr.write((char *)&obj, sizeof(obj));
        }
        else
        {
            wr.write((char *)&obj, sizeof(obj));
        }
    }
    rd.close();
    wr.close();
    remove("record.txt");
    rename("tmp.txt", "record.txt");
}
void roominfo()
{
    int r;
    cout << "\nEnter room number";
    cin >> r;
    fstream rd;
    rd.open("record.txt", ios::in);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(obj);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&obj, sizeof(obj));
        if (r == obj.room_no)
        {
            rstatus();
        }
        else
        {
            cout << "\nSorry room empty";
        }
    }
}
void customerinfo()
{
    char na[30];
    cin.ignore();
    cout << "\nEnter name";
    cin.getline(na, 30);
    fstream rd;
    rd.open("record.txt", ios::in);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(obj);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&obj, sizeof(obj));
        if (stricmp(obj.name, na) == 0)
        {
            rstatus();
        }
        else
        {
            cout << "\nSorry customer details not found";
        }
    }
}
void leaveroom()
{
    int rno;
    cout << "\nEnter room number ";
    cin >> rno;
    fstream rd, wr, nwr;
    rd.open("record.txt", ios::in);
    wr.open("tmp.txt", ios::app);
    nwr.open("oldRecords.txt", ios::app);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(obj);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&obj, sizeof(obj));
        if (obj.room_no == rno)
        {

            cin.ignore();
            cout << "\nEnter checkout date ";
            cin.getline(obj.date1, 15);
            nwr.write((char *)&obj, sizeof(obj));
        }
        else
        {
            wr.write((char *)&obj, sizeof(obj));
        }
    }
    rd.close();
    wr.close();
    remove("record.txt");
    rename("tmp.txt", "record.txt");
}
void oldreco()
{
    fstream rd;
    rd.open("oldRecords.txt", ios::in);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(obj);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&obj, sizeof(obj));
        obj.display();
        cout << "\nCheckout date " << obj.date1;
    }
}
main()
{
    int e = 1, x;

    cout << "\t\t\t\t*******************************************\n";
    cout << "\t\t\t\t*******************************************\n";
    cout << "\t\t\t\t* *                                     * *\n";
    cout << "\t\t\t\t* *              Welcome to             * *\n";
    cout << "\t\t\t\t* *             Hotel Managment         * *\n";
    cout << "\t\t\t\t* *                System               * *\n";
    cout << "\t\t\t\t* *                                     * *\n";
    cout << "\t\t\t\t* *                                     * *\n";
    cout << "\t\t\t\t*******************************************\n";
    cout << "\t\t\t\t*******************************************\n";

    system("pause");
    system("cls");

    while (e != 0)
    {
        cout << "\n\t\t\t\t=========================================";
        cout << "\n\t\t\t\t|       HOTEL MANAGEMENT SYSTEM         |";
        cout << "\n\t\t\t\t=========================================";
        cout << "\n\t\t\t\t| 1. Book room                          |";
        cout << "\n\t\t\t\t| 2. Rooms status                       |";
        cout << "\n\t\t\t\t| 3. GET Room allotment details         |";
        cout << "\n\t\t\t\t| 4. View customer details              |";
        cout << "\n\t\t\t\t| 5. Edit the details                   |";
        cout << "\n\t\t\t\t| 6. Check Out                          |";
        cout << "\n\t\t\t\t| 7. View Bookings                      |";
        cout << "\n\t\t\t\t| 8. View  Record                       |";
        cout << "\n\t\t\t\t|9. Enter 9 to change password          |";
        cout << "\n\t\t\t\t| 9.Enter 0 to exit                     |";
        cout << "\n\t\t\t\t|_______________________________________|";
        cout << "\n\t\t\t\tSelect your choice no. for task           ";
        cin >> x;
        switch (x)
        {
        case 1:
        {
            alotroom();
            break;
        }
        case 2:
        {
            rstatus();
            break;
        }
        case 3:
        {
            roominfo();
            break;
        }
        case 4:
        {
            customerinfo();
            break;
        }
        case 5:
        {
            edit();
            break;
        }
        case 6:
        {
            leaveroom();
            break;
        }
        case 7:
        {
            roomstatus();
            break;
        }
        case 9:
        {
            int y;
            cout << "\nEnter passcode - ";
            cin >> y;
            obj1.password(y);
            break;
        }

        case 0:
        {
            e = 0;
            break;
        }
        }
    }
    system("cls");

    cout << "\t\t\t\t*******************************************\n";
    cout << "\t\t\t\t*******************************************\n";
    cout << "\t\t\t\t* *               LOGOUT                * *\n";
    cout << "\t\t\t\t* *              FROM THE               * *\n";
    cout << "\t\t\t\t* *        HOTEL MANAGMENT SYSTEM       * *\n";
    cout << "\t\t\t\t*******************************************\n";
    cout << "\t\t\t\t*******************************************\n";
    system("pause");
}
