/* Bubble Sort Example in Java */

import java.io.File;
import java.util.Arrays;


public class BubbleSortExample {
	public static void main(String[] args) {
		int[] myArray = {5, 8, 2, 10, 1};
		int tmp = 0;

		for (int i = 0; i < myArray.length; i++) {
			for (int j = 1; j < myArray.length - i; j++) {
				if (myArray[j-1] > myArray[j]) {
					tmp = myArray[j-1];
					myArray[j-1] = myArray[j];
					myArray[j] = tmp;
				}
			}
		}
		System.out.println(Arrays.toString(myArray));
	}
}
