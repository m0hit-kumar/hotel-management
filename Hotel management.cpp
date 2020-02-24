#include<iostream.h>
#include<conio.h>
#include <fstream.h>
class customer{
	int id;
	char c_name,address;
	void customer_details(id,c_name,address)
	cout<<"enetr costomer id:";
	cin>>id;
    cout<<"enetr customer name:"
    cin>>c_name;
    cout<<"enetr the address of costomer";
    cin>>address;
               }
	    display()
	    { 
	    cout<<"id"<<id;
	    cout<<"customer name"<<c_name;
	    cout<<"addresss"<<address;
	    }
}
int main()
{ customer data;
	ofstream fout;
	filout.open("record.dat",ios::out);
	
	
	cout<<"select the operation:";
	cout<<"1 to see the records || 2 check in ||3 check out || 4 check for room available";    
    cout<<"5 enetr more record";
	switch(ans)
	{
		case 1: ifstream fin("record.dat",ios::in);
		        fin.seekg(0);
			break;
			
		case 2: data.display()
                         break;
		case 3: break;
		case 4:. break;
		case 5: data.customer_deatils() ;
		         break;
		default: break;
	}
	cout<<"enter the id";
	cin>>id ;
	cout>>"enter the name of customer";

	return 0;
}



//under construcion
