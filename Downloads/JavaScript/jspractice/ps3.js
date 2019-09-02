//this

var obj = {
    a:'custom',
}
var a = 'global';
function whats() {
    return this.a;
}
 console.log(whats());
 var t = whats.call(obj);
 console.log(t);

 //this with bind
 const binder  = {
     x:55,
     getx:function () {
         return this.x;
     }
 }
 var unbound = binder.getx;
 console.log(unbound());

 var bound = unbound.bind(binder);
 console.log(bound());



