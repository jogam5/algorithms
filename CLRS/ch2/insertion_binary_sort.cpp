#include <iostream>
#include <string>
#include <vector>
using namespace std;

int searchPosition(vector<int> array, int low, int high, int key);
vector<int> insertionSort(vector<int> array);

int main() {
  vector<int> v = {8, 3, 14, 5, 6, 7, 10, 100};
  vector<int> z = {3, 5, 7, 8, 10};

	v = insertionSort(v);
	for (int i = 0; i < v.size(); i++) {
		cout << v.at(i) << endl;
	}
}

/*
 * The goal of this modified insertion sort algorithm is to figure out if
 * using binary search could reduce the running time from O(N^2) to O(NLogN^2).
 *
 * As can be seen in the code, it's not possible to avoid the step where the
 * elements of the array or vector are moved from left to right (i.e. while loop).
 * Therefore the running time remains O(N^2) because in the worst case scenario
 * an element located in the end of the array will cause all the elements to 
 * slide one place to the right. For instance A = {32, 41, 42, 66, 1}. We are
 * able to reduce the number comparisons to find the proper position of the key
 * thanks to 'location' but the slide of the elements greater than the key towards
 * the end of the array is the step that causes the running time to be the same.
 */

vector<int> insertionSort(vector<int> array) {
	for(int i=1; i < array.size(); i++) {
		int key = array[i];
		int j = i - 1;

		// current location of key
		int location = searchPosition(array, 0, j, key);
		
		while ( j >= location) {
			// slide to the right
			array[j + 1] = array[j];
			j--;
		}

		array[location] = key;
	}
	return array;
}

/* 
 * Problem: Finding the index in the array where a given value (key) should fit
 * ---
 * Description: The algorithm is based on binary search. It recursively figures out
 * the position of the key by finding a midpoint to halve the number of elements in
 * the array. The crucial difference with respect to binary search is that instead
 * of returning -1 when a value is not present, it returns the expected index value even if
 * the value is not in the array.
 *
 * Running time: O(logN)
 */

int searchPosition(vector<int> array, int low, int high, int key) {
	int midpoint = (low + high)/2;

	if ( low > high ) {
		// Cases where key is out of bounds
		return low;
	}

	if (array[midpoint] == key) {
		// Base case
		return midpoint; 
	} else if ( array[midpoint] > key ) {
		// Recursive cases
			return searchPosition(array, low, midpoint-1, key);
	} else {
			return searchPosition(array, midpoint+1, high, key);
	}
}

