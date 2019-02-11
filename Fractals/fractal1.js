var canvas = document.getElementById("canvas1");
var context = canvas.getContext("2d");

var CANVAS_SIZE = 500;
var max_iteration = 1000;

//Mandelbrot-Menge
function drawFractalPoint(Px,Py){
    //c = (x0 + y0i)
    var x0 = (2*Px)/CANVAS_SIZE-1.5;
    var y0 = (2*Py)/CANVAS_SIZE-1;

    // TODO
    var iteration = 1;
    // z = a + bi
    var a = 0;          //realPart(z)
    var b = 0;          //ImaginaryPart(z)
    var a_temp;
    while ((a*a + b*b < 4) && (iteration < max_iteration)) {
        a_temp = a*a - b*b + x0;    //i^2 = -1
        b = 2*a*b + y0;
        a = a_temp;             //update of z = z^2 + c
        iteration = iteration + 1;
    }
    
    color="rgb("+(10*iteration%256)+", "+(10*iteration%256)+", 250)"
    myPoint([Px,Py],color);
}

function drawAll() {
    var factor=2;   
     for(var i=0; i < (CANVAS_SIZE/factor);i++)
       for(var j=0; j < (CANVAS_SIZE/factor);j++)
           drawFractalPoint(factor*i,factor*j);
}


function myPoint(pos,color) {
    context.strokeStyle = color;
    context.beginPath();
    context.arc(pos[0],pos[1],1,0,2*Math.PI, true)
    context.closePath()
    context.stroke();
    context.fillStyle = color;
    context.fill();
}

drawAll();
