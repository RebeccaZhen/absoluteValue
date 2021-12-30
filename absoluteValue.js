function absoluteValue(input) {
	if (input >= 0) {
		return input;
	} else {
		return 0 - input;
	}
}

let Integer;
const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout
});

readline.question('Enter your integer: ', Integer => {
	console.log (`${absoluteValue(Integer)}`);
	readline.close();
});