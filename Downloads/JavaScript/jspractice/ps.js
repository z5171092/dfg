function times(a, b) {
    return a*b;
}
var ji = times(14, 14);
console.log(ji);

var amount = 99;
if (amount === 100) {
    console.log('yes');
} else {
    console.log('no!');
}

var integer = 0;
for (var i = 0;i < 9;i++) {
    integer++;
    console.log(integer);
}

//This is object;
var worker = {
    name:'jack',
    age:15,
    job:'manong',
}
console.log(worker.age);

var array = ['hello',55,true];
for (var a = 0;a < 3;a++) {
    console.log(array[a]);
}

var wukong = '42';
var wujing = 42;
if (wukong === wujing) {
    console.log("wukong");
} 
if (wukong ===! wujing) {
    console.log('wujing');
}

//IIFE
(function preed(a) {
    var b = 2 + 1;
    console.log(b);
})();