function mult(a, b) {
    return a + b;
}

var c = mult(1, 4);
console.log(c);

//template string
(function template() {
    var a = 1;
    var b = 2;
    console.log(`the sum of ${a} and ${b} is 3 rather than ${a - b}`);
}) ();


//!!!
//The most important thing is the arrow function!!!
//!!!
//this can change the bind of 'this'!!!
//the outcom is NaN as this points to global

const calender = {
    currentDay:6,
    nextDay: function () {
        setTimeout(function () {
            this.currentDay += 1;
            console.log(this.currentDay);
        });
    }
       
}

calender.nextDay();
//the issue can be fixed by adding a variable self

const calander = {
    currentDay: 6,
    nextDay: function () { 
        var self = this;
        setTimeout(function () {
            self.currentDay += 1;
            console.log(self.currentDay);
        })
    }
}
calander.nextDay();
//at last, there is the arrow funciton version

const canlander = {
    currentDay:6,
    nextDay: function () {
        setTimeout(() => {
            this.currentDay += 1;
            console.log(this.currentDay);
        })
    }
}
canlander.nextDay();

//only by calling the funcition can we know what 'this' is  
