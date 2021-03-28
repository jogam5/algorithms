#include <iostream>
#include <string>
#include <vector>
using namespace std;

int binarySearch(vector<int> array, int low, int high, int key);

int main() {
  vector<int> v = {1, 3, 4, 5, 6, 7, 10, 100};
	int key = 7;
  cout << "The value " << 
					key << " is in the position: " << binarySearch(v, 0, v.size()-1, key) << endl;
	key = 1;
  cout << "The value " << 
					key << " is in the position: " << binarySearch(v, 0, v.size()-1, key) << endl;

	key = 100;
  cout << "The value " << 
					key << " is in the position: " << binarySearch(v, 0, v.size()-1, key) << endl;

	key = 2;
  cout << "The value " << 
					key << " is in the position: " << binarySearch(v, 0, v.size()-1, key) << endl;

	key = 8;
  cout << "The value " << 
					key << " is in the position: " << binarySearch(v, 0, v.size()-1, key) << endl;

	return 0; 
}


/*
 * Problem: Figuring out if a given value (key) is contained within a vector (i.e. array)
 * ---
 * Description: The algorithm works by computing the midpoint of the lowest and the highest value 
 * index from the vector. This midpoint value (i.e. A[midpoint]) is compared against the 'key'. The
 * base case happens when A[midpoint] is equal to the key, thus the value was found and the function
 * returns the vector's index where the value resides. The recursive cases occur when the key is
 * either greater or lower than A[midpoint]. If the index of 'low' is greater than 'high', the key
 * is not present in the vector and the program returns -1.
 *
 * Running time: O(logN).
 * After each comparison (i.e. A[midpoint] VS key) the number of elements in the vector is
 * halved (N/2^x). Therefore the worst case for N/2^x is when x is such that 2^x = N.
 *
*/
int binarySearch(vector<int> array, int low, int high, int key) {
	int midpoint = (low + high)/2;

	if ( low > high ) return -1;

	if (array[midpoint] == key) {
		// Base case
		return midpoint; 
	} else if ( array[midpoint] > key ) {
		// Recursive cases
			return binarySearch(array, low, midpoint-1, key);
	} else {
			return binarySearch(array, midpoint+1, high, key);
	}
}
