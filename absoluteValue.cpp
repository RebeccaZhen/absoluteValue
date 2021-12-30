#include <iostream>

int absoluteValue(int input) {
	if (input >= 0) {
		return input;
	} else {
		return 0 - input;
	}
}

int main() {
	std::cout << "Enter your integer: ";
	int Integer;
	std::cin >> Integer;
	std::cout << absoluteValue(Integer);
	return 0;
}

//comment