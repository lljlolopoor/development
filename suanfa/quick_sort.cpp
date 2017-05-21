#include <iostream>
using namespace std;

int partition(int A[], int low, int high)
{
    int key;
    key=A[low];
    while(low<high)
    {
        while(low<high && A[high]>key) high--;
        A[low]=A[high];
        while(low<high && A[low]<key) low++;
        A[high]=A[low];
    }
    A[low]=key;
    return low;
}

void quick_sort(int A[], int low, int high)
{
    int loc;
    if(low<high)
    {
        loc = partition(A, low, high);
        quick_sort(A, low, loc-1);
        quick_sort(A, loc+1, high);
    }
}

int main()
{
    int A[10]={5,1,2,6,3,9,8,4,7,10};
    for(int i=0;i<10;i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
    quick_sort(A,0,9);
    for(int i=0;i<10;i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
}
