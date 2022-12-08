const conversionForm = document.querySelector('#conversion_form');
const body = document.querySelector('#table_body');

// function numToConvert(conversionFormS)
// console.log(conversionForm)
conversionForm.addEventListener('submit', function (event) {
    event.preventDefault();
    body.innerHTML = "";
    let value = conversionForm.children[1].value;
    numToConvert(value)
    conversionForm.reset()
})

function numToConvert(value) {
    value = parseInt(value)
    let list = masterConvert(1,value,true)
    console.log(list)
    addRow(list[0],list[1],list[2])

    let index = 0
    while (list[1] != 1 && list[1] != 2 && list[1] != 3) {
        list = masterConvert(index,list[1])
        if (list[0] === 0 && list[1] === 1 || list[1] === 2) {
            addRow(list[0],list[1],list[2])
        } else {
            addRow(list[0],list[1],list[2])
        }
        index++;
    } 

    list = masterConvert(index,list[1])
    addRow(list[0],list[1],list[2])
}

function masterConvert(index,wholeNumber,isInit = false) {
    let binaryConversion = index % 2
    if (!isInit) {
        wholeNumber = wholeNumber % 2 === 0 ? wholeNumber / 2 : (wholeNumber + 3) / 2;
        // console.log(binaryConversion,wholeNumber)
        // if (binaryConversion === 0 && (wholeNumber === 1 || wholeNumber === 2)) {
        //     wholeNumber = 0;
        //     console.log("Test");
        // }
    }
    return [
        binaryConversion,
        wholeNumber,
        binaryConversion.toString().repeat(wholeNumber)
    ];

}
// 25 --> 14 --> 7 --> 5 --> 4 --> 2 --> 1
// 1  --> 0  --> 1 --> 0 --> 1 --> 0 --> 1
// if binaryConversion = 0, wholeNumber = 0

function addRow(binaryConversion,wholeNumber,tallyNotation) {
    body.innerHTML += `
    <tr>
        <td>${binaryConversion}</td>
        <td>${wholeNumber}</td>
        <td>${tallyNotation}</td>
    </tr>
    `
}
// If EVEN, (N/2) until reaching 3, 2 or 1

// If ODD, (N+3)/2 until reaching 3, 2 or 1