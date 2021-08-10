const getPermutations = str => {
    const arr = str.split('');
    const result = [];

    const swap = (swapArr, indexA, indexB) => {
        [swapArr[indexA], swapArr[indexB]] = [swapArr[indexB], swapArr[indexA]];
    };

    const generate = (n , heapArr) => {
        if (n === 1) {
            if (result.indexOf(heapArr.join('')) === -1) {
                result.push(heapArr.join(''));
            }            
            // console.log(result);
            return;
        }

        generate(n - 1, heapArr);

        for (let i = 0; i < n - 1; i++) {
            if (n % 2 === 0) {
                swap(heapArr, i, n - 1);
            } else {
                swap(heapArr, 0, n - 1);
            }

            generate(n - 1, heapArr);
        }
    }

    generate(arr.length, arr);
    return result;
}

let x = '166';
console.log(`Permutations of ${x} using Heap algo:\n${getPermutations(x)}`);