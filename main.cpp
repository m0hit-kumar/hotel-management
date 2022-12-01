#include <iostream>
#include <string>
#include <fstream>

using namespace std;

struct student
{

    int rollno;
    string department;
    int year;
    string guardian;
    string address;
    string mobile;
    string name;
};
// student stud;
class hostel
{
public:
    int room_no;
    string checkout;
    string vistors;
    int attendance;
    int allot_date;
    int payment_date;
    int payment;
    student stud;

    void vistors_record(){

    };

    void hostel_report()
    {
    }

    void data()
    {

        cout << "Enter roll no.:";
        cin >> stud.rollno;
        cout << "Name:";
        cin >> stud.name;
        cout << "Guardian";
        cin >> stud.guardian;
        cout << "Year";
        cin >> stud.year;
        cout << "Department:";
        cin >> stud.department;
        cout << "Address:";
        cin >> stud.address;
        cout << "Mobile:";
        cin >> stud.mobile;
        cout << "Payment:";
        cin >> payment;
        cout << "Room no";
        cin >> room_no;
        cout << "Vistor";
        cin >> vistors;
        cout << "Attendance";
        cin >> attendance;
        cout << "Allotment Date";
        cin >> allot_date;
        cout << "Payment Date";
        cin >> payment_date;
    }

    void display()
    {

        cout << "Roll no.:";
        cout << stud.rollno;
        cout << "Name:";
        cout << stud.name;
        cout << "Guardian";
        cout << stud.guardian;
        cout << "Year";
        cout << stud.year;
        cout << "Department:";
        cout << stud.department;
        cout << "Address:";
        cout << stud.address;
        cout << "Mobile:";
        cout << stud.mobile;
        cout << "Payment:";
        cout << payment;
        cout << "Room no";
        cout << room_no;
        cout << "Vistor";
        cout << vistors;
        cout << "Attendance";
        cout << attendance;
        cout << "Allotment Date";
        cout << allot_date;
        cout << "Payment Date";
        cout << payment_date;
        cout << "\n----------------------------";
    }
};
hostel host;
int check(int r)
{
    int flag = 1;
    fstream rd;
    rd.open("record.txt", ios::in);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(host);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&host, sizeof(host));
        if (r == host.room_no)
        {
            flag = 0;
            break;
        }
    }
    return flag;
}
void allot_room()
{

    host.data();
    fstream wr;
    wr.open("record.txt", ios::app);
    wr.write((char *)&host, sizeof(host));
}
void roomstatus()
{

    fstream rd;
    rd.open("record.txt", ios::in);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(host);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&host, sizeof(host));
        host.display();
    }
}
void rstatus()
{
    fstream rd;
    rd.open("record.txt", ios::in);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(host);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&host, sizeof(host));
        cout << "\nRoom number       " << host.room_no;
        cout << "\nName              " << host.stud.name;
        cout << "\nMobile number     " << host.stud.mobile;
        cout << "\n----------------------------";
    }
}
void vistorEntry()
{
    int rno;
    cout << "\nEnter Roll no number";
    cin >> rno;
    string vistor;
    fstream wr, rd;
    rd.open("record.txt", ios::in);
    wr.open("tmp.txt", ios::out);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(host);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&host, sizeof(host));
        if (host.stud.rollno == rno)
        {
            cout << "\nEnter vistor name   ";
            cin >> vistor;
            host.vistors = vistor;
            // host.accept();
            wr.write((char *)&host, sizeof(host));
        }
        else
        {
            wr.write((char *)&host, sizeof(host));
        }
    }
    rd.close();
    wr.close();
    remove("record.txt");
    rename("tmp.txt", "record.txt");
}
void changeRoomNo()
{
    int rno;
    cout << "\nEnter room number";
    cin >> rno;
    fstream wr, rd;
    rd.open("record.txt", ios::in);
    wr.open("tmp.txt", ios::out);
    rd.seekg(0, ios::end);
    int n = rd.tellg();
    n = n / sizeof(host);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&host, sizeof(host));
        if (host.room_no == rno)
        {
            cout << "\nEnter new room number ";
            cin >> rno;
            host.room_no = rno;
            host.data();
            wr.write((char *)&host, sizeof(host));
        }
        else
        {
            wr.write((char *)&host, sizeof(host));
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
    n = n / sizeof(host);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&host, sizeof(host));
        if (r == host.room_no)
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
    n = n / sizeof(host);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&host, sizeof(host));
        if (host.stud.name == "")
        {
            rstatus();
        }
        else
        {
            cout << "\nSorry Student details not found";
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
    n = n / sizeof(host);
    rd.seekg(0, ios::beg);
    for (int i = 1; i <= n; i++)
    {
        rd.read((char *)&host, sizeof(host));
        if (host.room_no == rno)
        {

            cin.ignore();
            cout << "\nEnter checkout date ";
            cin >> host.checkout;
            nwr.write((char *)&host, sizeof(host));
        }
        else
        {
            wr.write((char *)&host, sizeof(host));
        }
    }
    rd.close();
    wr.close();
    remove("record.txt");
    rename("tmp.txt", "record.txt");
}

int main()
{
    hostel h;
    system("cls");

    char q = 'a';
    int selection;
    while (q != 'q')
    {

        cout << "\n\t\t\t\t=========================================";
        cout << "\n\t\t\t\t|       HOSTEL ROOM ALLOT. SYSTEM       |";
        cout << "\n\t\t\t\t=========================================";
        cout << "\n\t\t\t\t| 1. Allot room                         |";
        cout << "\n\t\t\t\t| 2. Rooms status                       |";
        cout << "\n\t\t\t\t| 3. Allotment Room                     |";
        cout << "\n\t\t\t\t| 4. View customer details              |";
        cout << "\n\t\t\t\t| 5. Edit the details                   |";
        cout << "\n\t\t\t\t| 6. Check Out                          |";
        cout << "\n\t\t\t\t| 7. View Bookings                      |";
        cout << "\n\t\t\t\t| 8. View  Record                       |";
        cout << "\n\t\t\t\t| 9. Enter 9 to change password         |";
        cout << "\n\t\t\t\t| 10.Enter 0 to exit                    |";
        cout << "\n\t\t\t\t|_______________________________________|";
        cout << "\n\t\t\t\tSelect your choice no. for task           ";
        cin >> selection;
        switch (selection)
        {

        case 1:
        {
            h.vistors_record();
            break;
        }
        case 2:
        {
            h.hostel_report();
            break;
        }
        case 3:
        {
            allot_room();
            break;
        }

        default:
        {
            q = 'q';
            break;
        };
        }
    }
    return 0;
}