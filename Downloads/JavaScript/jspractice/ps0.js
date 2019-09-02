//local has the priority

var g = 'global';
(function () {
    var l = 'local';
    console.log(l);
}) ();

(function () {
    var g = 'local';
    console.log(g);
}) ();

//https://www.cnblogs.com/janneystory/p/5689747.html
//function scope
//it will find from up hierachy
var v = 11;
(function () {
    console.log(v);
    var v = 12;
    console.log(v);
}) ();

var b = 'Jim';
(function () {
    console.log(b);
})();

//from es6, let and const are blockScope
//whereas var is funcinal scope
(function avrtest() {
    var x = 1;
    if (true) {
        console.log(x);
        var x = 2;
        console.log(x);
    }
    console.log(x);
}) ();

(function lettest() {
    let x = 3;
    if (true) {
        let x = 4;
        console.log(x);
    }
    console.log(x);
}) ();

(function letprint() {
    let j = 5;
    for (let j = 0;j < 3;j++) {
        console.log(j);
    }
    console.log(j);
}) ();

(function varprint() {
    var i = 5;
    for (var i = 0;i < 3;i++) {
        console.log(i);
    }
    console.log(i);
}) ();
