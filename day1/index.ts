let input = `R2, L5, L4`;
let dir = ['N', 'E', 'S', 'W'];
let currDir = 0;
let currentLocation = {
    x: 0,
    y: 0
};

let structuredInput = input.split(', ');

_.each(structuredInput, (instruction: string) => {
    if (instruction.charAt(0) === 'R') {
        currDir = (currDir + 1) % 4;
    } else if (instruction.charAt(0) === 'L') {
        currDir = (currDir <= 0 ? 3 : currDir - 1);
    } else {
        throw '0: ' + instruction.charAt(0);
    }
    console.log(currDir);
    switch(currDir) {
        case 0: // N
            currentLocation.y += parseInt(instruction.slice(1), 10);
            break;
        case 1: // E
            currentLocation.x += parseInt(instruction.slice(1), 10);
            break;
        case 2: // S
            currentLocation.y -= parseInt(instruction.slice(1), 10);
            break;
        case 3: // W
            currentLocation.x -= parseInt(instruction.slice(1), 10);
            break;
        default:
            console.log('1: ' + currDir)
            throw '1: ' + currDir
    }
});

console.log(JSON.stringify(currentLocation));
